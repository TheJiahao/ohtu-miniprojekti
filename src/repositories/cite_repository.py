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
        """Palauttaa listan kaikista viitteistä"""
        ids = self.get_all_ids()
        types = self.get_all_types()
        fields = self.get_all_fields()
        authors = self.get_all_authors()

        all_cites = []
        for id in ids:
            cite = Cite(id, types[id], authors[id], fields[id])
            all_cites.append(cite)

        return all_cites

    def get_all_ids(self) -> list[str]:
        """Hakee tietokannasta viitteiden id:t"""
        ids = self._database.cursor.execute("SELECT id FROM Cites").fetchall()
        return [id[0] for id in ids]

    def get_all_types(self) -> dict[str, str]:
        """Hakee tietokannasta viitteen tyypit"""
        types = self._database.cursor.execute("SELECT id, type FROM Cites").fetchall()
        return dict(types)

    def get_all_authors(self) -> dict[str, list[str]]:
        """Hakee tietokannasta viitteen kirjailijat"""
        authors = {}
        for id in self.get_all_ids():
            authors_query = self._database.cursor.execute(
                "SELECT name FROM Authors WHERE cite_id = ?", (id,)
            )
            authors[id] = [author[0] for author in authors_query]

        return authors

    def get_all_fields(self) -> dict[str, dict[str, str]]:
        """Hakee tietokannasta viitteen tiedot"""
        fields = {}
        for id in self.get_all_ids():
            fields_query = self._database.cursor.execute(
                "SELECT name, content FROM Fields WHERE cite_id = ?", (id,)
            )
            fields[id] = dict(fields_query.fetchall())

        return fields

    def remove_all_cites(self) -> None:
        """Poistaa kaikki viitteet."""

        self._database.initialize()


cite_repository = CiteRepository()
