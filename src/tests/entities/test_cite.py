import unittest

from entities.cite import Cite


class TestCite(unittest.TestCase):
    def test_cite_can_be_initialized(self):
        Cite(
            "amazing article",
            "article",
            ["Alice", "Bob"],
            {"year": 3202, "author": "Someone"},
        )

    def test_cite_str(self):
        cite = Cite(
            "amazing article",
            "article",
            ["Alice", "Bob"],
            {"year": 3202, "author": "Someone"},
        )

        self.assertEqual(
            str(cite),
            "amazing article - article - ['Alice', 'Bob'] - {'year': 3202, 'author': 'Someone'}",
        )
