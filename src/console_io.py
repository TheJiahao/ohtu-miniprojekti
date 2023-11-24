class ConsoleIO:
    """Luokka, joka vastaa konsoliin kirjoittamisesta ja lukemisesta."""

    def read(self) -> str:
        """Lukee konsolista merkkijonon.

        Returns:
            str: Konsolista luettu merkkijono.
        """

        return input()

    def write(self, text: str) -> None:
        """Kirjoittaa konsoliin merkkijonon.

        Args:
            text (str): Konsoliin kirjoitettava merkkijono.
        """

        print(text)
