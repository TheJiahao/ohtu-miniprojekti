from entities.cite import Cite
from infrastructure.database import database


class CiteRepository:  # pylint: disable=too-few-public-methods
    """Luokka vastaa Cite olion toimenpiteistä"""

    def __init__(self, db=database) -> None:
        """Luokan konstruktori

        Args:
            db (SQLiteDB, optional): SQLiteDB olio, oletuksena database.py:n sisällä luotu
        """

        self.db = db

    def add_cite(self, cite: Cite) -> None:
        """Kutsuu tietokannan add_cite() funktiota

        Args:
            cite (Cite): Cite olio
        """

        self.db.add_cite(cite)

    # def get_all_cites(self) -> list[Cite]:
    #     return self.db.get_all_cites()
    #     pass

    def get_cites(self):
        cites = self.db.get_cites()
        return cites


# muissa moduuleissa käytettävä olio
cite_repository = CiteRepository()
