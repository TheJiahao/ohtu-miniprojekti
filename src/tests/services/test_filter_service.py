import unittest

from services.filter_service import FilterService
from repositories.stub_cite_repository import StubCiteRepository
from entities.cite import Cite


class TestFilterService(unittest.TestCase):
    def setUp(self) -> None:
        self.cites = [Cite(1, "book", ["Author1", "Author2"], {'title': 'Testi1', 'year': 1234}),
                     Cite(2, "article", ["Pekka"], {'title': '123tes12', 'year': 1000}),
                     Cite(3, "book", ["Author", "Author2", "Mikko"], {'title': 'Moiit', 'year': 1234})]
        self.cite_repository = StubCiteRepository(self.cites)
        self.filter_service = FilterService(self.cite_repository)

    def test_init(self):
        self.assertIsNotNone(self.filter_service)

    def test_name_filter_returns_filtered_names(self):
        self.assertEqual(self.filter_service.filter_by_name("Tes"), [self.cites[0], self.cites[1]])
    
    def test_name_filter_returns_all_names_with_empty_search(self):
        self.assertEqual(self.filter_service.filter_by_name(""), self.cites)
    
    def test_name_filter_returns_empty_list_when_no_matches(self):
        self.assertEqual(self.filter_service.filter_by_name("Ei löydy"), [])
    
