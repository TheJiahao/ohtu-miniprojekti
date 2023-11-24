# from entities.cite import Cite
from repositories.cite_repository import cite_repository


class FilterService:
    """Luokka vastaa viitteiden filtteröinnistä"""

    def __init__(self, repository=cite_repository) -> None:
        self.repository = repository

    # Vähän epävarma onko toi palautusmuoto list[Cite]
    # mutta tehkää niinkun parhaaks näätte :)

    # def filter_by_name(name: str) -> list[Cite]:
    #     pass

    # def filter_by_author(author: str) -> list[Cite]:
    #     pass

    # def filter_by_tag(tag: str) -> list[Cite]:
    #     pass
