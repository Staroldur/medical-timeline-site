"""Synthetic mutations of public policy pages verify the publication checks fail closed."""
from contextlib import redirect_stdout
import io
import re
from datetime import date, timedelta
from pathlib import Path
import shutil
import tempfile
import unittest

import validate as site


class PublicationChecks(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name) / 'site'
        shutil.copytree(site.ROOT, self.root, ignore=shutil.ignore_patterns('.git', '.DS_Store', '__pycache__'))

    def run_check(self):
        with redirect_stdout(io.StringIO()):
            site.validate(self.root)

    def replace(self, name, old, new):
        path = self.root / name
        source = path.read_text()
        self.assertIn(old, source)
        path.write_text(source.replace(old, new, 1))

    def test_complete_site_passes(self):
        self.run_check()

    def test_draft_and_noindex_are_rejected_in_both_languages(self):
        for name in ['privacy.html', 'privacy-he.html']:
            original = (self.root / name).read_text()
            for marker in ['<p>Publication draft</p>', '<p>טיוטה</p>',
                           '<meta name="robots" content="noindex, nofollow">']:
                with self.subTest(name=name, marker=marker):
                    (self.root / name).write_text(original.replace('</head>', marker + '</head>'))
                    with self.assertRaises(AssertionError):
                        self.run_check()
            (self.root / name).write_text(original)

    def test_missing_or_mismatched_effective_date_is_rejected(self):
        original = (self.root / 'privacy-he.html').read_text()
        current = re.search(r'datetime="([^"]+)"', original)[1]
        different = (date.fromisoformat(current) + timedelta(days=1)).isoformat()
        for value in ['', 'not-a-date', different]:
            with self.subTest(value=value):
                (self.root / 'privacy-he.html').write_text(original.replace(f'datetime="{current}"', f'datetime="{value}"'))
                with self.assertRaises((AssertionError, ValueError)):
                    self.run_check()

    def test_missing_support_practices_are_rejected(self):
        self.replace('privacy.html', 'reasonably necessary', 'forever')
        with self.assertRaises(AssertionError):
            self.run_check()

    def test_robots_exclusion_is_rejected(self):
        path = self.root / 'robots.txt'
        path.write_text(path.read_text() + 'Disallow: /privacy.html\n')
        with self.assertRaises(AssertionError):
            self.run_check()

    def test_missing_policy_sitemap_entry_is_rejected(self):
        self.replace('sitemap.xml', '<url><loc>' + site.BASE + 'privacy-he.html</loc></url>', '')
        with self.assertRaises(AssertionError):
            self.run_check()


if __name__ == '__main__':
    unittest.main()
