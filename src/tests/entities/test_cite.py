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
            {"year": 3202, "title": "Someone"},
        )

        self.assertEqual(
            str(cite),
            'Id = "amazing article"'
            '\nTyyppi = "article"'
            '\nKirjoittajat = "Alice, Bob"'
            ""
            '\n\n["Kentät"]'
            "\nyear = 3202"
            '\ntitle = "Someone"\n',
        )
