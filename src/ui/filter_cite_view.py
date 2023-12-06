from infrastructure.console_io import ConsoleIO
from services.logic import Logic
from ui.view import View


class FilterCiteView(View):
    """Luokka, joka vastaa viitteiden hakunäkymästä."""

    def __init__(self, logic: Logic, io: ConsoleIO) -> None:
        self._filtertypes: dict[int, str] = {1: "name", 2: "author", 3: "id"}

        help_message = "\n".join(
            ["1: nimi", "2: kirjailija", "3: id", "Syötä hakutyyppi: "]
        )

        super().__init__("Viitteiden haku", help_message, logic, io)

    def start(self) -> None:
        """Käynnistää hakunäkymän"""

        super().start()

        type = self._filtertypes[int(self._io.read())]

        match type:
            case "name":
                search = self._ask_string("Hae nimellä: ")
            case "author":
                search = self._ask_string("Hae kirjoittajalla: ")
            case "id":
                search = self._ask_string("Hae id:llä: ")

        filters = {type}

        super().show_cites(self._logic.filter_cites(search, filters))
