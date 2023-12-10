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
        self._logic.export("export/cites", "bibtex", self._logic.get_all_cites())
