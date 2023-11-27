from infrastructure.console_io import ConsoleIO
from services.logic import Logic
from ui.view import View


class AddCiteView(View):
    """Luokka, joka vastaa viitteen lisäysnäkymästä."""

    def __init__(self, logic: Logic, io: ConsoleIO) -> None:
        help_message = """
        Valitse viitetyyppi:
        1: kirja (book)
        2: artikkeli (article)
        """

        super().__init__("Viitteen lisäys", help_message, logic, io)

    def start(self) -> None:
        """Käynnistää viitteen lisäysnäkymän."""
        super().start()

        fields = {}

        print("\nValitse viitetyyppi:\n")
        print("1: kirja (book)")
        print("2: artikkeli (article)\n")
        type = int(self._io.read())

        print("\nSyötä viitteen nimi: \n")
        id = str(self._io.read())

        # Seuraavaksi tulisi tyypistä riippuen eri kenttien kyselyitä

        print("\nSyötä kirjailijat (authors), erota pilkulla: \n")
        authors = (self._io.read()).split(", ")

        print("\nSyötä otsikko (title): \n")
        fields["title"] = str(self._io.read())

        print("\nSyötä vuosi (year): \n")
        fields["year"] = int(self._io.read())

        self._logic.create_cite(id, type, authors, fields)


view = AddCiteView(Logic(), ConsoleIO())
view.start()
