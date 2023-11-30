from infrastructure.console_io import ConsoleIO
from services.logic import Logic
from ui.view import View


class AddCiteView(View):
    """Luokka, joka vastaa viitteen lisäysnäkymästä."""

    def __init__(self, logic: Logic, io: ConsoleIO) -> None:
        self._types: dict[int, str] = {1: "book", 2: "article", 3: "journal"}

        help_message = "\n".join(
            [
                "Valitse viitetyyppi:",
                "1: kirja (book)",
                "2: artikkeli (article)",
                "3: julkaisu (journal)"
            ]
        )

        super().__init__("Viitteen lisäys", help_message, logic, io)

    def start(self) -> None:
        """Käynnistää viitteen lisäysnäkymän."""

        fields = {}

        super().start()

        type = self._types[int(self._io.read())]

        self._io.write("Syötä viitteen nimi: \n")
        id = str(self._io.read())

        # Seuraavaksi tulisi tyypistä riippuen eri kenttien kyselyitä

        self._io.write("Syötä kirjailijat (authors), erota pilkulla: \n")
        authors = (self._io.read()).split(", ")

        self._io.write("Syötä otsikko (title): \n")
        fields["title"] = self._io.read()

        self._io.write("Syötä vuosi (year): \n")
        fields["year"] = self._io.read()

        self._logic.create_cite(id, type, authors, fields)
