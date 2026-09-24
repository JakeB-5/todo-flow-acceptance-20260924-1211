import unittest

from greeting import greet


class GreetTests(unittest.TestCase):
    def test_trim(self):
        self.assertEqual(greet(" Ada "), "Hello, Ada")

    def test_empty_whitespace_only(self):
        self.assertEqual(greet("  "), "Hello, world")

    def test_empty_string(self):
        self.assertEqual(greet(""), "Hello, world")

    def test_trims_tabs_and_newlines(self):
        self.assertEqual(greet("\tAda\n"), "Hello, Ada")

    def test_plain_name_unchanged(self):
        self.assertEqual(greet("Ada"), "Hello, Ada")


if __name__ == "__main__":
    unittest.main()
