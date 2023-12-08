from infrastructure.console_io import ConsoleIO
from services.logic import Logic
from ui.view import View


class FilterCiteView(View):
    """Luokka, joka vastaa viitteiden hakunäkymästä."""

    def __init__(self, logic: Logic, io: ConsoleIO) -> None:
        self._filtertypes: dict[int, str] = {
            "nimi": "name",
            "kirjailija": "author",
            "id": "id",
        }

        help_message = "\n".join(
            ["nimi: nimi", "kirjailija: kirjailija", "id: id", "Syötä hakutyyppi: "]
        )

        super().__init__("Viitteiden haku", help_message, logic, io)

    def start(self) -> None:
        """Käynnistää hakunäkymän"""

        super().start()

        try:
            type = self._filtertypes[self._io.read()]
        except (ValueError, KeyError):
            self._io.write("virheellinen syöte")
            return

        match type:
            case "name":
                search = self._ask_string("Hae nimellä: ")
            case "author":
                search = self._ask_string("Hae kirjoittajalla: ")
            case "id":
                search = self._ask_string("Hae id:llä: ")

        filters = {type}

        super().show_cites(self._logic.filter_cites(search, filters))
