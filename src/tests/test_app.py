import unittest

from ui.app import App
from services.logic import Logic


class StubIO:
    def __init__(self, inputs):
        self.inputs = inputs
        self.outputs = []

    def read(self):
        return self.inputs.pop(0)

    def write(self, text):
        self.outputs.append(text)


class TestApp(unittest.TestCase):
    def setUp(self):
        self.logic = Logic()

    def test_choose_action_palauttaa_valinnan_inttinä(self):
        io = StubIO(
            ["1", "Testi viitenimi", ["Matti", "Pekka"], "Testi otsikko", "1621"]
        )
        app = App(io, self.logic)
        self.assertEqual(app.choose_action(), 1)
