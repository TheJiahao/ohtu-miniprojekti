from typing import Callable

from entities.cite import Cite
from repositories.cite_repository import CiteRepository, cite_repository
from services.filter_service import FilterService


class Logic:
    """Sovelluslogiikasta vastaava luokka."""

    def __init__(self, repository=cite_repository, filter_service=FilterService()):
        """Luokan konstruktori

        Args:
            repository (CiteRepository, optional): CiteRepository olio,
            oletuksena cite_repository.py:n sisällä luotu
        """

        self.repository: CiteRepository = repository
        self.__filters: dict[str, Callable] = {
            "id": filter_service.filter_by_id,
            "name": filter_service.filter_by_name,
            "author": filter_service.filter_by_author,
        }

    def filter_cites(self, search: str, filters: set[str]) -> list[Cite]:
        """Hakee hakusanan ja tyypin mukaiset viitteet

        Args:
            search (str): hakusana
            filters (set[str]): setti filtereitä, esim. nimi, vuosi, kirjoittajat

        Returns:
            list[Cite]: lista Cite olioita
        """

        result = set()

        for filter in filters:
            result = result | set(self.__filters[filter](search))

        return list(result)

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
