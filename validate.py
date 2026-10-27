#!/usr/bin/env python3
"""Buildless source checks; browser layout and legal approval are separate checks."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit
import re
from datetime import date
from fnmatch import fnmatchcase
from urllib.robotparser import RobotFileParser
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
        self.text = []
        self.times = []
        self.robots = []
        self.headings = 0

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        assert tag not in {'script', 'iframe', 'form'}, (self.name, tag)
        if tag not in VOID:
            self.stack.append(tag)
        if tag == 'html':
            self.lang = attrs.get('lang')
            assert attrs.get('dir') == ('rtl' if self.lang == 'he' else 'ltr')
        if tag == 'meta' and attrs.get('name', '').lower() == 'robots':
            self.robots.append(attrs.get('content', '').lower())
        if tag == 'time':
            self.times.append(attrs.get('datetime', ''))
        if tag == 'h2':
            self.headings += 1
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

    def handle_data(self, data):
        self.text.append(data)

    def handle_endtag(self, tag):
        assert self.stack and self.stack.pop() == tag, (self.name, 'unbalanced HTML', tag)

def check_final_policy(page, source):
    """Catch editorial-draft regressions and loss of important disclosure sections."""
    assert not re.search(r'draft|not yet effective|awaiting|OWNER INPUT|טיוט|טרם נכנס|להשלמה',
                         source, re.I), (page.name, 'Unresolved policy text')
    assert not any(re.search(r'noindex|nofollow|none', rule) for rule in page.robots), (page.name, 'Policy indexing blocked')
    assert len(page.times) == 1, (page.name, 'One explicit effective date required')
    effective = date.fromisoformat(page.times[0])
    assert page.headings >= 12, (page.name, 'Full policy sections required')
    text = ' '.join(''.join(page.text).split())
    if page.lang == 'he':
        months = ['ינואר', 'פברואר', 'מרץ', 'אפריל', 'מאי', 'יוני',
                  'יולי', 'אוגוסט', 'ספטמבר', 'אוקטובר', 'נובמבר', 'דצמבר']
        visible_date = f'{effective.day} ב{months[effective.month - 1]} {effective.year}'
    else:
        visible_date = effective.strftime('%B') + f' {effective.day}, {effective.year}'
    assert visible_date in text, (page.name, 'Visible effective date differs from datetime')
    for value in ['Stas Stern', 'staroldur@gmail.com', 'Google', 'Gmail', 'GitHub', 'Apple']:
        assert value in text, (page.name, 'Missing operator/provider disclosure', value)
    required = (['Support and privacy contact', 'Effective date', 'reasonably necessary',
                 'reasonable verification', 'Local medical data:', 'Support correspondence:',
                 'Permissions and external records', 'replaces all current',
                 'cannot recover', 'not password-encrypted'] if page.lang == 'en' else
                ['תמיכה ופרטיות', 'תאריך תחילה', 'נחוץ באופן סביר', 'באמצעים סבירים',
                 'מידע רפואי מקומי:', 'התכתבות עם התמיכה:', 'הרשאות ורשומות בשירותים חיצוניים',
                 'מחליף את כל', 'אינו יכול לשחזר', 'אינה מצפינה'])
    for value in required:
        assert value in text, (page.name, 'Missing substantive disclosure', value)
    other = 'privacy.html' if page.lang == 'he' else 'privacy-he.html'
    assert other in page.links, (page.name, 'Missing full equivalent language policy')
    assert 'mailto:staroldur@gmail.com' in page.links
    return page.times[0]


def check_indexing(root):
    urls = [e.text for e in ET.parse(root / 'sitemap.xml').getroot().iter() if e.tag.endswith('loc')]
    assert set(urls) == {BASE + name for name in PAGES}, 'Sitemap must include all six pages'
    robot_lines = (root / 'robots.txt').read_text().splitlines()
    for line in robot_lines:
        key, separator, value = line.partition(':')
        value = value.split('#', 1)[0].strip()
        if separator and key.strip().lower() == 'disallow' and value:
            assert not any(fnmatchcase('/' + name, value + '*') for name in
                           ['privacy.html', 'privacy-he.html']), 'Privacy exclusion in robots.txt'
    robots = RobotFileParser()
    robots.parse(robot_lines)
    for name in ['privacy.html', 'privacy-he.html']:
        assert robots.can_fetch('*', BASE + name), (name, 'robots.txt blocks policy')


def validate(root=ROOT):
    parsed = {}
    dates = []
    for name in PAGES:
        page = Page(name)
        source = (root / name).read_text()
        assert '<title>' in source and 'name="description"' in source
        assert not re.search(r'draft|טיוט', source, re.I), (name, 'Stale draft reference')
        assert '[OWNER' not in source and '[להשלמה' not in source
        page.feed(source)
        assert not page.stack and page.h1s == 1 and 'main' in page.ids
        assert page.canonical == BASE + name
        assert set(page.alternates) == {'en', 'he', 'x-default'}
        if name.startswith('privacy'):
            dates.append(check_final_policy(page, source))
        parsed[name] = page
    assert len(set(dates)) == 1, 'Effective dates differ between languages'
    for name, page in parsed.items():
        for link in page.links:
            uri = urlsplit(link)
            if uri.scheme:
                assert uri.scheme in {'https', 'mailto'}, (name, link)
                continue
            target = uri.path or name
            assert (root / target).is_file(), (name, link)
            if uri.fragment:
                assert uri.fragment in parsed[target].ids, (name, link)
    css = (root / 'styles.css').read_text()
    assert 'prefers-reduced-motion' in css and '@media print' in css and ':focus-visible' in css
    assert '@import' not in css
    for asset in re.findall(r"url\(['\"]?([^\)'\"]+)", css):
        assert not urlsplit(asset).scheme and (root / asset).is_file(), asset
    check_indexing(root)
    print('PASS: six complete linked pages; final-policy text, matching effective dates, operator/providers, indexing and sitemap; local assets and HTML structure.')
    print('Source checks do not establish owner approval, actual publication date, legal compliance or full W3C conformance.')


if __name__ == '__main__':
    validate()
