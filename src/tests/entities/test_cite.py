import unittest

from entities.cite import Cite


class TestCite(unittest.TestCase):
    def setUp(self):
        self.cite = Cite(
            "amazing article", "article", {"year": 3202, "author": "Someone"}
        )

    def test_cite_can_be_initialized(self):
        Cite("amazing article", "article", {"year": 3202, "author": "Someone"})

    def test_cite_str(self):
        self.assertEqual(
            str(self.cite), "amazing article - article - {'year': 3202, 'author': 'Someone'}"
        )
