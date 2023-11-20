from entities.cite import Cite
from infrastructure.database import database


class CiteRepository: # pylint: disable=too-few-public-methods
    def __init__(self, db=database) -> None:
        self.db = db

    def add_cite(self, cite: Cite) -> None:
        self.db.add_cite(cite)

    # def get_all_cites(self) -> list[Cite]:
    #     return self.db.get_all_cites()
    #     pass


cite_repository = CiteRepository()
