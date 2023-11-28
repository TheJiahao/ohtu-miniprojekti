import unittest

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
    pass
