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
        accepted_types = ["book", "article", "journal"]
        for a_type in accepted_types:
            if a_type == type:
                id = self._ask_string("Syötä viitteen id: ")

                authors = [
                    author.strip()
                    for author in self._ask_string(
                        "Syötä tekijät (authors), erota pilkulla: "
                    ).split(",")
                ]
                fields["title"] = self._ask_string("Syötä otsikko (title): ")
                fields["year"] = self._ask_string("Syötä vuosi (year): ")

                try:
                    self._logic.create_cite(id, type, authors, fields)
                    self._io.write("Viite lisätty.\n")
                    return

                except sqlite3.IntegrityError:
                    self._io.write("Viitteen lisäys epäonnistui.\n")
        self._io.write("Virheellinen syöte. Sallitut syötteet: book, article, journal")
