from entities.cite import Cite
from repositories.cite_repository import cite_repository


class Logic:
    """Sovelluslogiikasta vastaava luokka."""

    def __init__(self, repository=cite_repository):
        """Luokan konstruktori

        Args:
            repository (CiteRepository, optional): CiteRepository olio,
            oletuksena cite_repository.py:n sisällä luotu
        """

        self.repository = repository

    def create_cite(self, id: str, type: str, authors: list[str], fields: dict):
        """Lisää uuden viitteen.

        Args:
            id (str): Viitteen tunnus.
            type (str): Viitteen tyyppi.
            authors (list[str]): Viitteen tekijät.
            fields (dict): Vitteen kentät.

        Returns:
            str: "Cite added" tai "Error"
        """

        cite = Cite(id, type, authors, fields)
        self.repository.add_cite(cite)
        return "Cite added"

    def get_all_cites(self):
        cites = self.repository.get_cites()
        print(cites)
        return cites
