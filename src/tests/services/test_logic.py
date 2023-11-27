import unittest
from unittest.mock import Mock

from services.logic import Logic
from entities.cite import Cite


class TestCite(unittest.TestCase):
    def setUp(self):
        self.repository_mock = Mock()
        self.filter_service_mock = Mock()
        self.logic = Logic(self.repository_mock, self.filter_service_mock)
        self.cites = [Cite(1, "book", ["Author1", "Author2"], {'title': 'Testi1', 'year': 1234}),
                     Cite(2, "article", ["Pekka"], {'title': '123tes12', 'year': 1000}),
                     Cite(3, "book", ["Author", "Author2", "Mikko"], {'title': 'Moiit', 'year': 1234})]

    def test_create_cite(self):
        create = self.logic.create_cite(
            "123", "book", [], {"year": 1900, "author": "Hello"}
        )
        self.assertEqual(create, "Cite added")

    def test_logic_get_all_cites(self):
        self.repository_mock.get_cites.return_value = "cites"
        get_all = self.logic.get_all_cites()
        self.assertEqual(get_all, "cites")

    def test_filter_cites_calls_filter_by_name_when_name_searched(self):
        self.logic.filter_cites("Tes", {"name"})
        self.filter_service_mock.filter_by_name.assert_called()
    
    def test_filter_cites_doesnt_call_filter_by_name_when_not_search(self):
        self.logic.filter_cites("Tes", {"authors"})
        self.filter_service_mock.filter_by_name.assert_not_called()