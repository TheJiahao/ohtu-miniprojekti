import unittest

from infrastructure.bibtex_exporter import BibtexExporter
from entities.cite import Cite


class TestBibtexExporter(unittest.TestCase):
    def test_dump_empty_list(self):
        result = BibtexExporter.dump_list([])

        self.assertEqual(result, "{}")

    def test_dump_list(self):
        data = ["Alan Turing", "Newton Isaac", "Albert Einstein"]

        result = BibtexExporter.dump_list(data)

        self.assertEqual(result, "{Alan Turing and Newton Isaac and Albert Einstein}")
