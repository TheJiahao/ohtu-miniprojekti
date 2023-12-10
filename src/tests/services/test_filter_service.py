import unittest

from entities.cite import Cite
from services.filter_service import FilterService
from tests.stubs.stub_cite_repository import StubCiteRepository


class TestFilterService(unittest.TestCase):
    def setUp(self) -> None:
        self.cites = [
            Cite(
                "1", "book", ["Author1", "Author2"], {"title": "Testi1", "year": 1234}
            ),
            Cite("Kokeilu2", "article", ["Pekka"], {"title": "123tes12", "year": 1000}),
            Cite(
                "3",
                "book",
                ["Author", "Author2", "Mikko"],
                {"title": "Moiit", "year": 1234},
            ),
        ]
        self.cite_repository = StubCiteRepository(self.cites)
        self.filter_service = FilterService(self.cite_repository)

    def test_init(self):
        self.assertIsNotNone(self.filter_service)

    def test_title_filter_returns_filtered_titles(self):
        self.assertEqual(
            self.filter_service.filter_by_title("Tes"), [self.cites[0], self.cites[1]]
        )

    def test_title_filter_returns_all_titles_with_empty_search(self):
        self.assertEqual(self.filter_service.filter_by_title(""), self.cites)

    def test_title_filter_returns_empty_list_when_no_matches(self):
        self.assertEqual(self.filter_service.filter_by_title("Ei löydy"), [])

    def test_author_filter_returns_filtered_cites(self):
        self.assertEqual(
            self.filter_service.filter_by_author("author2"),
            [self.cites[0], self.cites[2]],
        )

    def test_author_filter_substring_returns_filtered_cites(self):
        self.assertEqual(
            self.filter_service.filter_by_author("r2"), [self.cites[0], self.cites[2]]
        )

    def test_author_filter_returns_all_cites_with_empty_search(self):
        self.assertEqual(self.filter_service.filter_by_author(""), self.cites)

    def test_author_filter_returns_empty_list_when_no_matches(self):
        self.assertEqual(self.filter_service.filter_by_author("Ei löydy"), [])

    def test_id_filter_returns_filtered_cites(self):
        self.assertEqual(self.filter_service.filter_by_id("1"), [self.cites[0]])

    def test_id_filter_returns_empty_list_when_no_matches(self):
        self.assertEqual(self.filter_service.filter_by_id("Ei löydy"), [])

    def test_id_filter_substring_returns_filtered_cites(self):
        self.assertEqual(self.filter_service.filter_by_id("Kokei"), [self.cites[1]])
