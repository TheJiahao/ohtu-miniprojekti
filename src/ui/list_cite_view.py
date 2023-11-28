from infrastructure.console_io import ConsoleIO
from services.logic import Logic
from ui.view import View


class ListCiteView(View):
    """Luokka, joka vastaa viitteiden listausnäkymästä."""

    def __init__(self, logic: Logic, io: ConsoleIO) -> None:
        super().__init__("Viitteiden listaus", "Viitteiden listaus", logic, io)

    def start(self) -> None:
        """Listaa kaikki viitteet."""

        super().start()
        super().show_cites(self._logic.get_all_cites())
