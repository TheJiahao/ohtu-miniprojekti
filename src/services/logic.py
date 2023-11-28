from entities.cite import Cite
from repositories.cite_repository import cite_repository
from services.filter_service import FilterService


class Logic:
    """Sovelluslogiikasta vastaava luokka."""

    def __init__(self, repository=cite_repository, filter_service=FilterService()):
        """Luokan konstruktori

        Args:
            repository (CiteRepository, optional): CiteRepository olio,
            oletuksena cite_repository.py:n sisällä luotu
        """

        self.repository = repository
        self.__filter_service = filter_service

    def filter_cites(self, search: str, filters: set[str]) -> list[Cite]:
        """Hakee hakusanan ja tyypin mukaiset viitteet

        Args:
            search (str): hakusana
            filters (set[str]): setti filtereitä, esim. nimi, vuosi, kirjoittajat

        Returns:
            list[Cite]: lista Cite olioita
        """
        cites = []

        if "name" in filters:
            cites.append(self.__filter_service.filter_by_name(search))

        return cites

    def create_cite(self, id: str, type: str, authors: list[str], fields: dict):
        """Lisää uuden viitteen.

        Args:
            id (str): Viitteen tunnus.
            type (str): Viitteen tyyppi.
            authors (list[str]): Viitteen tekijät.
            fields (dict): Vitteen kentät.

        """

        cite = Cite(id, type, authors, fields)
        self.repository.add_cite(cite)

    def get_all_cites(self) -> list[Cite]:
        """Palauttaa kaikki viitteet.

        Returns:
            list[Cite]: Lista, joka sisältää kaikki viitteet.
        """

        cites = self.repository.get_all_cites()
        return cites
