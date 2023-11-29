import unittest
from unittest.mock import MagicMock

from services.logic import Logic
from ui.ui import UI


class StubIO:
    def __init__(self, inputs):
        self.inputs = inputs
        self.outputs = []

    def read(self):
        return self.inputs.pop(0)

    def write(self, text):
        self.outputs.append(text)


class TestUI(unittest.TestCase):
    def setUp(self):
        self.mock_logic = MagicMock()
        self.stub_io = StubIO(inputs=["lopeta"])
        self.ui = UI(self.mock_logic, self.stub_io)

    def test_ui_start(self):
        self.ui.start()
        self.assertTrue(any("lisää" in string for string in self.stub_io.outputs))
