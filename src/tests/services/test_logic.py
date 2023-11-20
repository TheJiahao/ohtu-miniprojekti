import unittest

from entities.cite import Cite


class TestCite(unittest.TestCase):
    def setUp(self):
        self.logic = Logic()

    def test_create_cite(self):
        create = self.logic.create_cite(self)
        self.assertEqual(create, "Cite added")