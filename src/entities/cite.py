class Cite:
    """Luokka, joka kuvaa viitettä.

    Attributes:
        name (str): Viitteen nimi.
        type (str): Viitteen tyyppi.
        fields (dict): Viitteen kentät.
    """

    def __init__(self, name: str, type: str, fields: dict) -> None:
        """Luokan konstruktori

        Args:
            name (str): nimi
            type (str): Viitteen tyyppi.
            fields (dict): Viitteen kentät.
        """

        self.name: str = name
        self.type: str = type
        self.fields: dict = fields
