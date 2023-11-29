from entities.cite import Cite
from repositories.cite_repository import cite_repository


class FilterService:
    """Luokka vastaa viitteiden filtteröinnistä"""

    def __init__(self, repository=cite_repository) -> None:
        self.repository = repository

    # Vähän epävarma onko toi palautusmuoto list[Cite]
    # mutta tehkää niinkun parhaaks näätte :)

    def filter_by_name(self, name: str) -> list[Cite]:
        """Hakee viitteet annetun hakusanan perusteella

        Args:
            name (str): viitteen nimen hakusana

        Returns:
            list[Cite]: lista viiteolioita, jotka sopivat hakusanaan
        """
        cites = self.repository.get_all_cites()
        filtered_cites = [
            cite for cite in cites if name.lower() in cite.fields["title"].lower()
        ]
        return filtered_cites

    def filter_by_author(self, author: str) -> list[Cite]:
        """Hakee viitteet annetun tekijän perusteella

        Args:
            author (str): viitteen tekijä hakusana

        Returns:
            list[Cite]: lista viiteolioita, jotka sopivat hakusanaan
        """
        cites = self.repository.get_all_cites()
        if author == "":
            return cites

        filtered_cites = [
            cite
            for cite in cites
            if author.lower() in [c.lower() for c in cite.authors]
        ]
        return filtered_cites
    
    def filter_by_id(self, id) -> list[Cite]:
        """Hakee viitteet annetun ID:n perusteella

        Args:
            id (int): viitteen id, jolla ne haetaan

        Returns:
            list[Cite]: lista viiteolioita, jotka sopivat hakusanaan
        """

        cites = self.repository.get_all_cites()
        if id < 1:
            return cites
        filtered_cites = [
            cite for cite in cites
            if id in [id for id in cite.id]
        ]
        return filtered_cites
        

    # def filter_by_tag(tag: str) -> list[Cite]:
    #     pass
