import unittest
from unittest.mock import Mock

from services.logic import Logic


class TestCite(unittest.TestCase):
    def setUp(self):
        self.repository_mock = Mock()
        self.logic = Logic(self.repository_mock)

    def test_create_cite(self):
        create = self.logic.create_cite(
            "123", "book", [], {"year": 1900, "author": "Hello"}
        )
        self.assertEqual(create, "Cite added")

    def test_logic_get_all_cites(self):
        self.repository_mock.get_cites.return_value = "cites"
        get_all = self.logic.get_all_cites()
        self.assertEqual(get_all, "cites")
