class Cite: # pylint: disable=too-few-public-methods
    """Luokka, joka kuvaa viitettä.

    Attributes:
        name (str): Viitteen nimi.
        entry_type (str): Viitteen tyyppi.
        fields (dict): Viitteen kentät.
    """

    def __init__(self, name: str, entry_type: str, fields: dict) -> None:
        """Luokan konstruktori

        Args:
            name (str): nimi.
            entry_type (str): Viitteen tyyppi.
            fields (dict): Viitteen kentät.
        """

        self.name: str = name
        self.entry_type: str = entry_type
        self.fields: dict = fields

    def __str__(self) -> str:
        """Palauttaa luokan merkkijonona

        Returns:
            str: Luokka merkkijonona.
        """

        return f"{self.name} - {self.entry_type} - {self.fields}"
