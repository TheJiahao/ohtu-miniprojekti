from infrastructure.console_io import ConsoleIO
from services.logic import Logic
from ui.view import View


class RemoveCiteView(View):
    """Luokka, joka vastaa viitteiden poistonäkymästä."""

    def __init__(self, logic: Logic, io: ConsoleIO) -> None:
        super().__init__("Viitteiden poisto", "Viitteiden poisto", logic, io)

    def start(self) -> None:
        """Käynnistää poistonäkymän"""

        super().start()
        print("Placeholder")
