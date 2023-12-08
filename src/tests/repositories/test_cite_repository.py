import unittest

from entities.cite import Cite
from infrastructure.database import database
from repositories.cite_repository import CiteRepository


class TestCiteRepository(unittest.TestCase):
    def setUp(self):
        self.repository = CiteRepository(database)
        self.repository.remove_all_cites()

    def test_add_cite_without_fields_or_authors(self):
        self.repository.add_cite(Cite("amazingBook", "book", [], {}))

        cite_data = database.cursor.execute("SELECT * FROM Cites").fetchall()
        authors = database.cursor.execute("SELECT * FROM Authors").fetchall()
        fields = database.cursor.execute("SELECT * FROM Fields").fetchall()

        self.assertEqual(cite_data[0]["id"], "amazingBook")
        self.assertEqual(len(fields), 0)

    def test_add_cite_with_multiple_fields(self):
        self.repository.add_cite(
            Cite("amazingBook", "book", [], {"year": 3202, "title": "An amazing book"})
        )

        fields = database.cursor.execute("SELECT * FROM Fields").fetchall()

        self.assertEqual(len(fields), 2)
        self.assertNotEqual(fields[0], fields[1])

        self.assertIn(
            (fields[0]["name"], fields[0]["content"]),
            [("year", "3202"), ("title", "An amazing book")],
        )
        self.assertIn(
            (fields[1]["name"], fields[1]["content"]),
            [("year", "3202"), ("title", "An amazing book")],
        )

    def test_add_cite_with_fields_adds_correct_cite_id(self):
        self.repository.add_cite(
            Cite("amazingBook", "book", [], {"title": "An amazing book"})
        )

        fields = database.cursor.execute("SELECT * FROM Fields").fetchall()

        self.assertEqual(len(fields), 1)
        self.assertEqual(fields[0]["cite_id"], "amazingBook")

    def test_add_cite_with_authors_adds_correct_cite_id(self):
        self.repository.add_cite(Cite("amazingBook", "book", ["alice", "bob"], {}))

        authors = database.cursor.execute("SELECT * FROM Authors").fetchall()

        self.assertEqual(authors[0]["cite_id"], "amazingBook")

    def test_add_cite_with_multiple_authors(self):
        self.repository.add_cite(Cite("amazingBook", "book", ["Alice", "Bob"], {}))

        authors = database.cursor.execute("SELECT * FROM Authors").fetchall()

        self.assertEqual(len(authors), 2)
        self.assertNotEqual(authors[0], authors[1])

        self.assertIn(authors[0]["name"], ("Alice", "Bob"))
        self.assertIn(authors[1]["name"], ("Alice", "Bob"))

    def test_add_cite_adds_correct_id_and_type(self):
        self.repository.add_cite(
            Cite(
                "amazingBook",
                "book",
                ["Alice", "Bob"],
                {"year": 3202, "title": "An amazing book"},
            )
        )

        cites = database.cursor.execute("SELECT * FROM Cites").fetchall()

        self.assertEqual(len(cites), 1)
        self.assertEqual(cites[0]["id"], "amazingBook")
        self.assertEqual(cites[0]["type"], "book")

    def test_get_all_ids(self):
        self.repository.add_cite(Cite("idtest1", "book", ["Alice1", "Bob1"], {}))
        self.repository.add_cite(
            Cite("idtest2", "article", ["AnemicAlice", "BetterBob"], {})
        )

        expected_ids = ["idtest1", "idtest2"]
        ids = self.repository.get_all_ids()

        self.assertEqual(ids, expected_ids)

    def test_get_all_types(self):
        self.repository.add_cite(Cite("typetest1", "book", ["Alice1", "Bob1"], {}))
        self.repository.add_cite(
            Cite("typetest2", "article", ["AnotherAlice", "BusyBob"], {})
        )
        self.repository.add_cite(
            Cite("typetest3", "journal", ["AnemicAlice", "BetterBob"], {})
        )

        expected_types = {
            "typetest1": "book",
            "typetest2": "article",
            "typetest3": "journal",
        }
        types = self.repository.get_all_types()

        self.assertEqual(types, expected_types)

    def test_get_all_authors(self):
        self.repository.add_cite(Cite("authortest1", "book", ["Alice1", "Bob1"], {}))
        self.repository.add_cite(Cite("authortest2", "article", ["AnotherAlice"], {}))

        expected_authors = {
            "authortest1": ["Alice1", "Bob1"],
            "authortest2": ["AnotherAlice"],
        }
        authors = self.repository.get_all_authors()

        self.assertEqual(authors, expected_authors)

    def test_get_all_fields(self):
        self.repository.add_cite(
            Cite(
                "fieldtest1",
                "book",
                ["Alice1", "Bob1"],
                {"field1": "value1", "field2": "value2"},
            )
        )
        self.repository.add_cite(
            Cite(
                "fieldtest2",
                "article",
                ["AnotherAlice"],
                {"field3": "value3", "field4": "value4"},
            )
        )

        expected_fields = {
            "fieldtest1": {"field1": "value1", "field2": "value2"},
            "fieldtest2": {"field3": "value3", "field4": "value4"},
        }
        fields = self.repository.get_all_fields()

        self.assertEqual(fields, expected_fields)

    def test_get_all_cite(self):
        self.repository.add_cite(
            Cite(
                "fieldtest1",
                "book",
                ["Alice1", "Bob1"],
                {"field1": "value1", "field2": "value2"},
            )
        )
        self.repository.add_cite(
            Cite(
                "fieldtest2",
                "article",
                ["AnotherAlice"],
                {"field3": "value3", "field4": "value4"},
            )
        )

        expected_cites = [
            Cite(
                "fieldtest1",
                "book",
                ["Alice1", "Bob1"],
                {"field1": "value1", "field2": "value2"},
            ),
            Cite(
                "fieldtest2",
                "article",
                ["AnotherAlice"],
                {"field3": "value3", "field4": "value4"},
            ),
        ]
        cites = self.repository.get_all_cites()

        for cite, expected_cite in zip(cites, expected_cites):
            self.assertEqual(cite.id, expected_cite.id)
            self.assertEqual(cite.type, expected_cite.type)
            self.assertEqual(cite.authors, expected_cite.authors)
            self.assertEqual(cite.fields, expected_cite.fields)

    def test_remove_cite(self):
        self.repository.add_cite(
            Cite("amazingBook", "book", ["Ama Zing"], {"title": "An amazing book"})
        )
        self.repository.remove_cite("amazingBook")

        cite_data = database.cursor.execute("SELECT * FROM Cites").fetchall()
        authors = database.cursor.execute("SELECT * FROM Authors").fetchall()
        fields = database.cursor.execute("SELECT * FROM Fields").fetchall()

        self.assertEqual(len(cite_data), 0)
        self.assertEqual(len(authors), 0)
        self.assertEqual(len(fields), 0)

    def test_remove_cite_only_removes_one_cite(self):
        self.repository.add_cite(
            Cite("amazingBook", "book", ["Ama Zing"], {"title": "An amazing book"})
        )
        self.repository.add_cite(
            Cite("goodBook", "book", ["Good Book"], {"title": "A good book"})
        )
        self.repository.remove_cite("amazingBook")

        cite_data = database.cursor.execute("SELECT * FROM Cites").fetchall()
        authors = database.cursor.execute("SELECT * FROM Authors").fetchall()
        fields = database.cursor.execute("SELECT * FROM Fields").fetchall()

        self.assertEqual(len(cite_data), 1)
        self.assertEqual(len(authors), 1)
        self.assertEqual(len(fields), 1)

    def test_remove_all_cites(self):
        self.repository.add_cite(
            Cite("amazingBook", "book", ["Ama Zing"], {"title": "An amazing book"})
        )
        self.repository.add_cite(
            Cite("goodBook", "book", ["Good Book"], {"title": "A good book"})
        )
        self.repository.remove_cite("amazingBook")

        self.repository.remove_all_cites()

        cite_data = database.cursor.execute("SELECT * FROM Cites").fetchall()
        authors = database.cursor.execute("SELECT * FROM Authors").fetchall()
        fields = database.cursor.execute("SELECT * FROM Fields").fetchall()

        self.assertEqual(len(cite_data), 0)
        self.assertEqual(len(authors), 0)
        self.assertEqual(len(fields), 0)
