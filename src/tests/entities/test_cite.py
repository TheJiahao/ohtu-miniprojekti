
from entities.cite import Cite

import unittest


class TestCite(unittest.TestCase):
    def test_cite_can_be_initialized(self):
        Cite("amazing article", "article", {"year": 3202, "author": "Someone"})
