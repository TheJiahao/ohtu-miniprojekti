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
