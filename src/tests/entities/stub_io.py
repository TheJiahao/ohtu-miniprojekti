from collections import deque


class StubIO:
    """Testauksessa käytettävä luokka, joka vastaa syötteistä ja tulostuksista."""

    def __init__(self) -> None:
        """Luokan konstruktori, joka alustaa syöte ja tulostus listat.

        Args:
            inputs (list): Syötteet
        """
        self.__inputs: deque = deque()
        self.outputs: list[str] = []

    def read(self) -> str:
        """Palauttaa ja poistaa syötelistasta ensimmäisen syötteen.

        Returns:
            str: Sovellukselle annettava syöte
        """
        return self.__inputs.popleft()

    def write(self, text: str, end: str = "") -> None:
        """Lisää tulostuslistaan merkkijonon.

        Args:
            text (str): Tulostukseen lisättävä merkkijono
        """
        self.outputs.append(str(text))

    def add_input(self, text: str) -> None:
        """Lisää syötelistan loppuun uuden syötten.

        Args:
            text (str): Lisättävä merkkijono
        """
        self.__inputs.append(text)
