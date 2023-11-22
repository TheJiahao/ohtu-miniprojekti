import unittest
from unittest.mock import MagicMock
from repositories.cite_repository import CiteRepository
from entities.cite import Cite


class TestCiteRepository(unittest.TestCase):
    def setUp(self):
        self.mock_db = MagicMock()
        self.repository = CiteRepository(db=self.mock_db)

    def test_init(self):
        assert self.repository.db is not None

    def test_add_cite(self):
        cite = Cite("repo_add_cite", "testiB", "testiC")
        self.repository.add_cite(cite)

        self.mock_db.add_cite.assert_called_once_with(cite)
