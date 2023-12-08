from infrastructure.console_io import ConsoleIO
from services.logic import Logic
from ui.view import View


class RemoveCiteView(View):
    """Luokka, joka vastaa viitteiden poistonäkymästä."""

    def __init__(self, logic: Logic, io: ConsoleIO) -> None:
        self._choices: dict[str, str] = {"id": "id", "kaikki": "all"}

        help_message = "\n".join(["id: id", "kaikki: kaikki", "Syötä poistotapa:"])

        super().__init__("Viitteiden poisto", help_message, logic, io)

    def start(self) -> None:
        """Käynnistää poistonäkymän"""

        super().start()
        
        try:
            type = self._choices[self._io.read()]
        except (ValueError, KeyError):
            self._io.write("virheellinen syöte")
            return

        match type:
            case "id":
                choice = self._ask_string("Syötä viitteen id: ")
            case "all":
                choice = self._ask_string('Vahvista poisto kirjoittamalla "vahvista": ')
                if choice == "vahvista":
                    self._logic.remove_all_cites()
                else:
                    print("Viitteitä ei poistettu")
                    return

        self._logic.remove_cite(choice)
