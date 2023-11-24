import unittest

from entities.cite import Cite
from infrastructure.database import database
from repositories.cite_repository import CiteRepository


class TestCiteRepository(unittest.TestCase):
    def setUp(self):
        self.repository = CiteRepository(database)
        self.repository.remove_all_cites()

    def test_add_cite_without_fields(self):
        self.repository.add_cite(Cite("Amazing book", "book", {}))

        data = database.cursor.execute("SELECT * FROM Cites").fetchall()
