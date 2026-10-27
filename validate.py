#!/usr/bin/env python3
"""Buildless source checks; browser layout and legal approval are separate checks."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit
import re
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parent
BASE = 'https://staroldur.github.io/medical-timeline-site/'
PAGES = ['index.html', 'he.html', 'support.html', 'support-he.html', 'privacy.html', 'privacy-he.html']
VOID = {'area', 'base', 'br', 'col', 'embed', 'hr', 'img', 'input', 'link', 'meta', 'param', 'source', 'track', 'wbr'}

class Page(HTMLParser):
    def __init__(self, name):
        super().__init__(convert_charrefs=True)
        self.name = name
        self.ids = set()
        self.links = []
        self.stack = []
        self.h1s = 0
        self.canonical = None
        self.alternates = {}
        self.lang = None

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        assert tag not in {'script', 'iframe', 'form'}, (self.name, tag)
        if tag not in VOID:
            self.stack.append(tag)
        if tag == 'html':
            self.lang = attrs.get('lang')
            assert attrs.get('dir') == ('rtl' if self.lang == 'he' else 'ltr')
        if tag == 'h1':
            self.h1s += 1
        if 'id' in attrs:
            assert attrs['id'] not in self.ids, (self.name, 'duplicate ID')
            self.ids.add(attrs['id'])
        if tag == 'img':
            assert 'alt' in attrs and 'width' in attrs and 'height' in attrs
        if tag == 'link' and attrs.get('rel') == 'canonical':
            self.canonical = attrs['href']
        if tag == 'link' and attrs.get('rel') == 'alternate':
            self.alternates[attrs['hreflang']] = attrs['href']
        for key in ['src', 'href']:
            if key in attrs:
                self.links.append(attrs[key])
        if 'src' in attrs:
            assert not urlsplit(attrs['src']).scheme, 'Remote resource'

    def handle_endtag(self, tag):
        assert self.stack and self.stack.pop() == tag, (self.name, 'unbalanced HTML', tag)

parsed = {}
for name in PAGES:
    page = Page(name)
    source = (ROOT / name).read_text()
    assert '<title>' in source and 'name="description"' in source
    assert '[OWNER' not in source and '[להשלמה' not in source
    page.feed(source)
    assert not page.stack and page.h1s == 1 and 'main' in page.ids
    assert page.canonical == BASE + name
    assert set(page.alternates) == {'en', 'he', 'x-default'}
    parsed[name] = page
for name, page in parsed.items():
    for link in page.links:
        uri = urlsplit(link)
        if uri.scheme:
            assert uri.scheme in {'https', 'mailto'}, (name, link)
            continue
        target = uri.path or name
        assert (ROOT / target).is_file(), (name, link)
        if uri.fragment:
            assert uri.fragment in parsed[target].ids, (name, link)
css = (ROOT / 'styles.css').read_text()
assert 'prefers-reduced-motion' in css and '@media print' in css and ':focus-visible' in css
assert '@import' not in css
for asset in re.findall(r'url\([\'"]?([^\)\'\"]+)', css):
    assert (ROOT / asset).is_file(), asset
urls = [e.text for e in ET.parse(ROOT / 'sitemap.xml').getroot().iter() if e.tag.endswith('loc')]
assert all(url.startswith(BASE) and (ROOT / url.removeprefix(BASE)).is_file() for url in urls)
print('PASS: 6 balanced HTML pages; local links/fragments/assets; direction, titles, canonical/alternate URLs; no scripts/forms/remote assets; CSS safety hooks; sitemap.')
print('This is a source integrity check, not a W3C conformance certificate or legal approval.')
