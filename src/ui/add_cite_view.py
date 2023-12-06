import sqlite3
from infrastructure.console_io import ConsoleIO
from services.logic import Logic
from ui.view import View


class AddCiteView(View):
    """Luokka, joka vastaa viitteen lisäysnäkymästä."""

    def __init__(self, logic: Logic, io: ConsoleIO) -> None:
        self._supported_types: dict[str, str] = {
            "book": "kirja",
            "article": "artikkeli",
            "journal": "julkaisu",
        }

        messages = ["Tällä hetkellä tuetut viitetyypit"]
        messages.extend(
            [
                f"{name}: {translation}"
                for name, translation in self._supported_types.items()
            ]
        )

        help_message = "\n".join(messages)

        super().__init__("Viitteen lisäys", help_message, logic, io)

    def start(self) -> None:
        """Käynnistää viitteen lisäysnäkymän."""

        fields = {}

        super().start()

        type = self._ask_string("Syötä viitteen tyyppi: ")
        id = self._ask_string("Syötä viitteen nimi: ")

        # Seuraavaksi tulisi tyypistä riippuen eri kenttien kyselyitä

        authors = self._ask_string(
            "Syötä kirjailijat (authors), erota pilkulla: "
        ).split(", ")
        fields["title"] = self._ask_string("Syötä otsikko (title): ")
        fields["year"] = self._ask_string("Syötä vuosi (year): ")

        try:
            self._logic.create_cite(id, type, authors, fields)
            self._io.write("Viite lisätty.\n")

        except sqlite3.IntegrityError:
            self._io.write("Viitteen lisäys epäonnistui.\n")
