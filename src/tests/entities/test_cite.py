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
            "\nyear = 3202"
            '\ntitle = "Someone"\n',
        )

    def test_compare_lt(self):
        self.assertTrue(Cite("aa", "book") < Cite("ab", "book"))

    def test_compare_eq(self):
        self.assertTrue(Cite("abc", "book") == Cite("abc", "article"))

    def test_compare_ne(self):
        self.assertTrue(Cite("xxxxx", "book") != Cite("yyyy", "book"))

    def test_compare_gt(self):
        self.assertTrue(Cite("xyz", "book") > Cite("abc", "book"))

    def test_compare_le(self):
        self.assertTrue(Cite("aa", "book") <= Cite("ab", "book"))
        self.assertTrue(Cite("abc", "book") <= Cite("abc", "article"))

    def test_compare_ge(self):
        self.assertTrue(Cite("xyz", "book") >= Cite("abc", "book"))
        self.assertTrue(Cite("abc", "book") >= Cite("abc", "article"))
