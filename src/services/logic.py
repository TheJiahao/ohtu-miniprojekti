from entities.cite import Cite
from repositories.cite_repository import cite_repository


class Logic:
    """Sovelluslogiikasta vastaava luokka."""

    def __init__(self, repository=cite_repository):
        """Luokan konstruktori

        Args:
            repository (CiteRepository, optional): CiteRepository olio, oletuksena cite_repository.py:n sisällä luotu
        """

        self.repository = repository

    def create_cite(self, type: str, name: str, fields: dict):
        """Lisää uuden viitteen.

        Args:
            type (str): Viitteen tyyppi
            name (str): Viitteen nimi
            fields (dict): Vitteen kentät

        Returns:
            str: "Cite added" tai "Error"
        """

        cite = Cite(name, type, fields)

        try:
            self.repository.add_cite(cite)
            return "Cite added"
        except Exception:
            return "Error"
