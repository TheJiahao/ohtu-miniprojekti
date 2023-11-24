import unittest

from services.filter_service import FilterService


class TestFilterService(unittest.TestCase):
    def setUp(self) -> None:
        self.filter_service = FilterService()

    def test_init(self):
        self.assertIsNotNone(self.filter_service)
