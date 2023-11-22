import unittest
from services.logic import Logic
from unittest.mock import Mock


class TestCite(unittest.TestCase):
    def setUp(self):
        self.repository_mock = Mock()
        self.logic = Logic(self.repository_mock)

    def test_create_cite(self):
        self.repository_mock.add_cite()
        create = self.logic.create_cite("book", 123, {"year": 1900, "author": "Hello"})
        self.assertEqual(create, "Cite added")

    def test_create_cite_error(self):
        self.repository_mock.add_cite.side_effect = Exception()
        create = self.logic.create_cite("book", 123, {"year": 1900, "author": "Hello"})
        self.assertEqual(create, "Error")