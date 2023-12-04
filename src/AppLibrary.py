# pylint: skip-file

from repositories.cite_repository import CiteRepository
from services.logic import Logic
from tests.entities.stub_io import StubIO
from ui.ui import UI


class AppLibrary:
    def __init__(self):
        self.cite_repo = CiteRepository()
        self.io = StubIO()
        self.logic = Logic(self.cite_repository)
        self.app = UI(self.logic, self.io)

    def start_app(self):
        self.app.start()

    def input(self, text):
        self.io.add_input(str(text))

    def empty_db(self):
        self.cite_repo.remove_all_cites()

    def output_should_contain(self, value: str):
        outputs = self.io.outputs

        for line in outputs:
            if value in line:
                return

        raise AssertionError(f"Output {value} is not in {str(outputs)}")

    def output_should_not_contain(self, value: str):
        outputs = self.io.outputs

        for line in outputs:
            if value in line:
                raise AssertionError(f"Output should not contain {value}")
