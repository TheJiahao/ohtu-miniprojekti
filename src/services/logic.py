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
            List[Cite]: lista Cite olioita
        """
        if not filters:
            return []

        if "name" in filters:
            return self.__filter_service.filter_by_name(search)
        elif "author" in filters:
            return self.__filter_service.filter_by_author(search)
        elif "tag" in filters:
            return self.__filter_service.filter_by_id(search)
        elif "id" in filters:
            return self.__filter_service.filter_by_id(search)

        return []

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

    def remove_cite(self, id: str) -> None:
        """Poistaa tietokannasta viitteen, jolla on annettu id.

        Args:
            id (str): Poistettavan viitteen id
        """

        self.repository.remove_cite(id)

    def remove_all_cites(self) -> None:
        """Poistaa kaikki viitteet"""

        self.repository.remove_all_cites()
