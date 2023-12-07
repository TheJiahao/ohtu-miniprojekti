import toml


class Cite:  # pylint: disable=too-few-public-methods
    """Luokka, joka kuvaa viitettä.

    Attributes:
        id (str): Viitteen tunnus.
        type (str): Viitteen tyyppi.
        authors: (list[str]): Viitteen tekijät.
        fields (dict): Viitteen kentät.
    """

    def __init__(
        self,
        id: str,
        type: str,
        authors: list[str] | None = None,
        fields: dict | None = None,
    ) -> None:
        """Luokan konstruktori

        Args:
            id (str): Viitteen tunnus.
            type (str): Viitteen tyyppi.
            authors: (list[str] | None): Viitteen tekijät.
            fields (dict | None): Viitteen kentät.
        """

        self.id: str = id
        self.type: str = type
        self.authors: list[str] = authors or []
        self.fields: dict = fields or {}

    def __str__(self) -> str:
        """Palauttaa viitteet toml muotoisena merkkijonona

        Returns:
            str: viitteen tiedot toml muodossa
        """

        toml_dict = {
            "Id": self.id,
            "Tyyppi": self.type,
            "Kirjoittajat": ", ".join(self.authors),
            **self.fields,
        }

        return toml.dumps(toml_dict)

    def __lt__(self, other: "Cite") -> bool:
        return self.id < other.id

    def __le__(self, other: "Cite") -> bool:
        return self < other or self == other

    def __eq__(self, other: "Cite") -> bool:
        return self.id == other.id

    def __ne__(self, other: "Cite") -> bool:
        return not self == other

    def __gt__(self, other: "Cite") -> bool:
        return self.id > other.id

    def __ge__(self, other: "Cite") -> bool:
        return self > other or self == other
