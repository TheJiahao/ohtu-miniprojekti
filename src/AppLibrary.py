# pylint: skip-file

from tests.entities.stub_io import StubIO
from repositories.cite_repository import CiteRepository
from services.logic import Logic
from ui.ui import UI


class AppLibrary:
    def __init__(self):
        self.cite_repository = CiteRepository()
        self.io = StubIO()
        self.logic = Logic(self.cite_repository)
        self.app = UI(self.logic, self.io)

    def start_app(self):
        self.app.start()

    def input(self, text):
        self.io.add_input(str(text))

    def empty_db(self):
        self.cite_repository.remove_all_cites()

    def output_contains(self, value):
        outputs = self.io.outputs

        if not value in outputs:
            raise AssertionError(f"Output {value} is not in {str(outputs)}")
