"""Verify the demo's required Welcome content using only the standard library."""

from pathlib import Path
import re
import unittest


class DemoContentTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.html = Path(__file__).with_name("index.html").read_text(encoding="utf-8")

    def test_welcome_button(self):
        self.assertRegex(
            self.html,
            re.compile(r"<button\b[^>]*>\s*Welcome\s*</button\s*>", re.IGNORECASE),
        )

    def test_welcome_message(self):
        self.assertIn("Welcome to the lab!", self.html)


if __name__ == "__main__":
    unittest.main()
