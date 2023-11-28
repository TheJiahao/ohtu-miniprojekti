from infrastructure.console_io import ConsoleIO
from services.logic import Logic
from ui.add_cite_view import AddCiteView
from ui.view import View


class UI(View):
    """Luokka, joka vastaa käyttöliittymästä."""

    def __init__(
        self, logic: Logic, io: ConsoleIO, views: dict[str, View] | None = None
    ) -> None:
        add_cite_view = AddCiteView(logic, io)

        self.__views: dict[str, View] = views or {"lisää": add_cite_view}

        help_message = "\n".join(
            [f"{command}: {view.description}" for command, view in self.__views.items()]
        )

        help_message += "\nlopeta: Lopeta"

        super().__init__("Sovelluksen päänäkymä", help_message, logic, io)

    def start(self):
        """Käynnistää sovelluksen."""
        while True:
            self._show_help()

            try:
                choice = self._io.read()

                if choice == "lopeta":
                    break

                self.__views[choice].start()

            except (ValueError, KeyError):
                self._io.write("Toimintoa ei olemassa tai ei toteutettu vielä.")

    def get_cites(self):
        """palauttaa kaikki viitteet

        Returns:
            list: kaikki citet omissa listoissaan
        """
        cites = self._logic.get_all_cites()
        return cites
