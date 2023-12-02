from infrastructure.console_io import ConsoleIO
from services.logic import Logic
from ui.view import View


class RemoveCiteView(View):
    """Luokka, joka vastaa viitteiden poistonäkymästä."""

    def __init__(self, logic: Logic, io: ConsoleIO) -> None:
        self._choices: dict[int, str] = {1: "id", 2: "all"}

        help_message = "\n".join(["Valitse poistotapa:", "1: id", "2: kaikki"])

        super().__init__("Viitteiden poisto", help_message, logic, io)

    def start(self) -> None:
        """Käynnistää poistonäkymän"""

        super().start()

        type = self._choices[int(self._io.read())]

        match type:
            case "id":
                self._io.write("Syötä viitteen id: \n")
            case "all":
                self._io.write('Vahvista poisto kirjoittamalla "vahvista": \n')
                if str(self._io.read()) == "vahvista":
                    self._logic.remove_all_cites()
                else:
                    print("Viitteitä ei poistettu")
                    return

        to_be_removed = str(self._io.read())

        self._logic.remove_cite(to_be_removed)
