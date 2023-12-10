import unittest
from unittest.mock import Mock

from entities.cite import Cite
from services.logic import Logic


class TestLogic(unittest.TestCase):
    def initialize_filter_service(self) -> Mock:
        filter_service = Mock()
        filter_service.filter_by_id.return_value = [self.id_test]
        filter_service.filter_by_name.return_value = [self.name_test]
        filter_service.filter_by_author.return_value = [self.author_test]

        return filter_service

    def initialize_cite_repository(self) -> Mock:
        cite_repository = Mock()
        cite_repository.get_all_cites.return_value = self.cites

        return cite_repository

    def setUp(self):
        self.id_test = Cite("id_test", "book", fields={"title": ""})
        self.name_test = Cite("title", "article", fields={"title": "title_test"})
        self.author_test = Cite(
            "author", "journal", ["author_test"], fields={"title": ""}
        )
        self.cites = [self.id_test, self.name_test, self.author_test]

        self.filter_service_mock = self.initialize_filter_service()
        self.cite_repository_mock = self.initialize_cite_repository()

        self.logic = Logic(self.cite_repository_mock, self.filter_service_mock)

    def test_create_cite(self):
        self.logic.create_cite("123", "book", [], {"year": 1900, "author": "Hello"})
        self.cite_repository_mock.add_cite.assert_called_once()

    def test_logic_get_all_cites(self):
        get_all = self.logic.get_all_cites()

        self.assertEqual(get_all, self.cites)

    def test_filter_cites_by_name(self):
        result = self.logic.filter_cites("Test", {"name"})

        self.assertEqual(len(result), 1)
        self.assertIn(self.name_test, result)

    def test_filter_cites_by_id(self):
        result = self.logic.filter_cites("Test", {"id"})

        self.assertEqual(len(result), 1)
        self.assertIn(self.id_test, result)

    def test_filter_cites_by_author(self):
        result = self.logic.filter_cites("Test", {"author"})

        self.assertEqual(len(result), 1)
        self.assertIn(self.author_test, result)

    def test_filter_cites_by_multiple_filters_and_multiple_hit(self):
        result = self.logic.filter_cites("Test", {"id", "name", "author"})

        self.assertEqual(len(result), 3)
        self.assertEqual(sorted(self.cites), sorted(result))

    def test_filter_cites_with_nonexistent_filter(self):
        result = self.logic.filter_cites("Test", set())
        self.assertEqual(len(result), 0)

    def test_remove_cite(self):
        self.logic.remove_cite("123")
        self.cite_repository_mock.remove_cite.assert_called()

    def test_remova_all_cites(self):
        self.logic.remove_all_cites()
        self.cite_repository_mock.remove_all_cites.assert_called()
