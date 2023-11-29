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

    def get_all_cites(self) -> list[Cite]:
        """Hakee tietokannasta kaikki viitteet."""
        cites = self._database.cursor.execute("SELECT id, type FROM Cites").fetchall()

        all_cites = []
        for id, type in cites:
            authors_query = self._database.cursor.execute(
                "SELECT name FROM Authors WHERE cite_id = ?", (id,)
            )
            authors = [author[0] for author in authors_query.fetchall()]

            fields_query = self._database.cursor.execute(
                "SELECT name, content FROM Fields WHERE cite_id = ?", (id,)
            )
            fields = {name: content for name, content in fields_query.fetchall()}

            cite = Cite(id, type, authors, fields)
            all_cites.append(cite)

        return all_cites

    def remove_all_cites(self) -> None:
        """Poistaa kaikki viitteet."""

        self._database.initialize()


cite_repository = CiteRepository()
