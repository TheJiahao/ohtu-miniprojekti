import unittest
from unittest.mock import Mock

from config import DATA_DIRECTORY
from entities.cite import Cite
from services.export_service import ExportService


class TestExportService(unittest.TestCase):
    def setUp(self):
        self.exporters = {"bibtex": Mock(), "json": Mock(), "toml": Mock()}
        self.export_service = ExportService(self.exporters)
        self.path = DATA_DIRECTORY / "test" / "exported_file"
        self.cites = [Cite("cite1", "book"), Cite("cite2", "article")]

    def test_export_with_unsupported_format_raises_exception(self):
        with self.assertRaises(ValueError):
            self.export_service.export(self.path, "yaml", self.cites)

    def test_export_with_valid_path_and_format(self):
        self.export_service.export(self.path, "bibtex", self.cites)

    def test_export_calls_export_method_of_exporter(self):
        self.export_service.export(self.path, "bibtex", self.cites)

        self.exporters["bibtex"].export.assert_called_once_with(self.path, self.cites)
