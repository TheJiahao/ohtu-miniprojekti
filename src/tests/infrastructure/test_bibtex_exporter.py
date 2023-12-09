import os
import unittest

from config import DATA_DIRECTORY
from entities.cite import Cite
from infrastructure.bibtex_exporter import BibtexExporter


class TestBibtexExporter(unittest.TestCase):
    def setUp(self):
        self.exporter = BibtexExporter()
        self.path = os.path.join(DATA_DIRECTORY, "test", "test_file.bib")

        try:
            os.remove(self.path)
        except OSError:
            pass

        self.acm_comminication = Cite(
            "weiser1993some",
            "article",
            ["Weiser Mark"],
            {
                "journal": "Communications of the ACM",
                "volume": "36",
                "year": "1993",
                "publisher": "ACM New York, NY, USA",
            },
        )

        self.generalized_integral = Cite(
            "mcleod1980generalized",
            "book",
            ["McLeod Robert M"],
            {
                "title": "The generalized Riemann integral",
                "volume": "20",
                "year": "1980",
                "publisher": "American Mathematical Soc.",
            },
        )

        self.relativity_theory = Cite(
            "einstein1922general",
            "incollection",
            ["Albert Einstein"],
            {
                "title": "The general theory of relativity",
                "booktitle": "The Meaning of Relativity",
                "pages": "54--75",
                "year": "1922",
                "publisher": "Springer",
            },
        )

        self.new_general_relativity = Cite(
            "hayashi1979new",
            "article",
            ["Hayashi Kenji", "Shirafuji Takeshi"],
            {
                "title": "New general relativity",
                "journal": "Physical Review D",
                "volume": "19",
                "number": "12",
                "pages": "3524",
                "year": "1979",
                "publisher": "APS",
            },
        )

        self.cites = [
            self.acm_comminication,
            self.generalized_integral,
            self.relativity_theory,
            self.new_general_relativity,
        ]

    def test_dump_empty_list(self):
        result = self.exporter._BibtexExporter__dump_list([])

        self.assertEqual(result, "{}")

    def test_dump_list(self):
        data = ["Alan Turing", "Newton Isaac", "Albert Einstein"]

        result = self.exporter._BibtexExporter__dump_list(data)

        self.assertEqual(result, "{Alan Turing and Newton Isaac and Albert Einstein}")

    def test_dump_string(self):
        data = "One line of something"

        self.assertEqual(
            self.exporter._BibtexExporter__dump_string(data), "{One line of something}"
        )

    def test_dump_empty_string(self):
        self.assertEqual(self.exporter._BibtexExporter__dump_string(""), "{}")

    def test_dump_cite(self):
        expected = """@article{weiser1993some,
author = {Weiser Mark},
journal = {Communications of the ACM},
publisher = {ACM New York, NY, USA},
volume = {36},
year = {1993},
}"""

        result = self.exporter._BibtexExporter__dump_cite(self.acm_comminication)

        self.assertEqual(result, expected)

    def test_dump(self):
        expected = ",\n".join(
            [
                self.exporter._BibtexExporter__dump_cite(self.relativity_theory),
                self.exporter._BibtexExporter__dump_cite(self.new_general_relativity),
                self.exporter._BibtexExporter__dump_cite(self.generalized_integral),
                self.exporter._BibtexExporter__dump_cite(self.acm_comminication),
            ]
        )

        result = self.exporter._BibtexExporter__dump(self.cites)

        self.assertEqual(result, expected)

    def test_export_adds_file_extension(self):
        file_basename = os.path.splitext(self.path)[0]

        try:
            os.remove(file_basename)
        except FileNotFoundError:
            pass

        self.exporter.export(file_basename, self.cites)

        self.assertNotEqual(os.path.getsize(self.path), 0)
        self.assertFalse(os.path.exists(file_basename))

    def test_export_empty_list_writes_nothing(self):
        self.exporter.export(self.path, [])
        self.assertEqual(os.path.getsize(self.path), 0)

    def test_export(self):
        self.exporter.export(self.path, self.cites)
        data = ""

        with open(self.path, mode="r", encoding="utf-8") as file:
            data = file.read()

        self.assertEqual(data, self.exporter._BibtexExporter__dump(self.cites))
