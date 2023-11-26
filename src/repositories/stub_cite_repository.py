from entities.cite import Cite
from infrastructure.database import Database
from infrastructure.database import database as default_database


class StubCiteRepository:
    """Testausta varten luokka, joka vastaa Cite olion tallennuksesta"""

    def __init__(self, cites: list, database: Database = default_database) -> None:
        """Luokan konstruktori

        Args:
            cites (list): syötetty lista viitteitä, eli Cites olioita
            database (Database, optional): tietokanta
        """

        self._database: Database = database
        self.cites = cites

    def get_all_cites(self) -> list[Cite]:
        """Hakee kaikki viitteet, tässä testiluokassa annettu jo parametrina

        Returns:
            list[Cite]: lista Cite olioita
        """
        return self.cites
