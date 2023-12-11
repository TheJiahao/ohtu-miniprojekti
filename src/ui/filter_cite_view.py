from infrastructure.console_io import ConsoleIO
from services.logic import Logic
from ui.view import View


class FilterCiteView(View):
    """Luokka, joka vastaa viitteiden hakunäkymästä."""

    def __init__(self, logic: Logic, io: ConsoleIO) -> None:
        self.__filter_types: dict[str, str] = {
            "otsikko": "title",
            "tekijä": "author",
            "id": "id",
        }

        help_message = ["Tällä hetkellä tuetut hakutyypit"]
        help_message.extend(
            [
                f"{name}: {translation}"
                for name, translation in self.__filter_types.items()
            ]
        )

        help_message = "\n".join(help_message)

        super().__init__("Viitteiden haku", help_message, logic, io)

    def start(self) -> None:
        """Käynnistää hakunäkymän"""

        super().start()

        keyword = ""
        help_messages = {
            "title": "Hae otsikolla: ",
            "author": "Hae kirjoittajalla: ",
            "id": "Hae id:llä: ",
        }

        try:
            type = self._ask_string("Syötä hakutyyppi: ")
            type = self.__filter_types[type]

            keyword = self._ask_string(help_messages[type])

        except KeyError:
            self._io.write("Virheellinen syöte")
            return

        filters = {type}

        self.show_cites(self._logic.filter_cites(keyword, filters))
