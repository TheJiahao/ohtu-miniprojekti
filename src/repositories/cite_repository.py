from entities.cite import Cite
from infrastructure.database import Database
from infrastructure.database import database as default_database


class CiteRepository:
    """Luokka, joka vastaa Cite olion tallennuksesta"""

    def __init__(self, database: Database = default_database) -> None:
        """Luokan konstruktori

        Args:
            database (Database, optional): Tietokantayhteydestä vastaava olio.
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

        for name in cite.authors:
            self._database.cursor.execute(
                """
                INSERT INTO Authors (cite_id, name) VALUES (?, ?)
                """,
                (cite.id, name),
            )

        for name, content in cite.fields.items():
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

    def remove_all_cites(self) -> None:
        """Poistaa kaikki viitteet."""

        self._database.initialize()


cite_repository = CiteRepository()
