import unittest
from services.logic import Logic
from entities.cite import Cite


class TestCite(unittest.TestCase):
    def setUp(self):
        self.logic = Logic()

    def test_create_cite(self):
        create = self.logic.create_cite(
            "book", "Test", {"name": "Test1", "author": "Test Test", "year": 1900}
        )
        self.assertEqual(create, "Cite added")

    def test_get_cites(self):
        self.logic.create_cite(
            "book", "Test", {"name": "Test1", "author": "Test Test", "year": 1900}
        )

        cites = self.logic.get_cites()
        self.assertEqual(cites, ('book',))
