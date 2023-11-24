from entities.cite import Cite
from infrastructure.database import Database
from infrastructure.database import database as default_database


class CiteRepository:
    """Luokka, joka vastaa Cite olion tallennuksesta"""

    def __init__(self, database=default_database) -> None:
        """Luokan konstruktori

        Args:
            db (SQLiteDB, optional): SQLiteDB olio, oletuksena database.py:n sisällä luotu
        """

        self._database: Database = database

    def add_cite(self, cite: Cite) -> None:
        """Kutsuu tietokannan add_cite() funktiota

        Args:
            cite (Cite): Cite olio
        """

        self._database.cursor.execute(
            """
            INSERT INTO Cites (id, type) VALUES (?, ?)
            """,
            (cite.id, cite.type),
        )

        for name, content in cite.fields:
            self._database.cursor.execute(
                """
                INSERT INTO Fields (cite_id, name, content) VALUES (?, ?, ?)
                """,
                (cite.id, name, content),
            )

        self._database.connection.commit()

    # def get_all_cites(self) -> list[Cite]:
    #     return self.db.get_all_cites()
    #     pass

    def get_cites(self):
        pass

    def remove_all_cites(self) -> None:
        """Poistaa kaikki viitteet."""

        self._database.initialize()


cite_repository = CiteRepository()
