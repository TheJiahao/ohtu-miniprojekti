import os

from config import DATA_DIRECTORY
from infrastructure.console_io import ConsoleIO
from services.logic import Logic
from ui.view import View


class ExportCiteView(View):
    """Luokka, joka vastaa viitteiden listausnäkymästä."""

    def __init__(self, logic: Logic, io: ConsoleIO) -> None:
        super().__init__("Viitteiden vienti", "Viitteiden vienti", logic, io)

    def start(self) -> None:
        """Vie kaikki viitteet."""

        super().start()
        name = self._ask_string("Syötä viitetiedoston nimi: ")

        if name == "robot_test":
            path = os.path.join(DATA_DIRECTORY, "test", name)
        else:
            path = os.path.join(DATA_DIRECTORY, name)

        path = self._logic.export(path, "bibtex", self._logic.get_all_cites())

        self._io.write(f"Viitteet tallennettu polkuun {os.path.abspath(path)}")
