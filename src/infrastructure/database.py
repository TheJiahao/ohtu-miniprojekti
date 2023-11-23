import os
from sqlite3 import Connection, Cursor, Row, connect

from config import DATABASE_FILE_PATH


class Database:
    """Luokka, joka vastaa tietokantayhteydestä ja tietokannan alustuksesta."""

    def __init__(self) -> None:
        """Luokan konstruktori."""
        self.connection: Connection = connect(DATABASE_FILE_PATH)
        self.connection.row_factory = Row
        self.cursor: Cursor = self.connection.cursor()

        if os.path.getsize(DATABASE_FILE_PATH) == 0:
            self.initialize()

    def create_tables(self) -> None:
        """Luo tietokantaan taulun, jos sitä ei ole olemassa"""

        self.cursor.execute(
            """
            CREATE TABLE Cites (
            id TEXT PRIMARY KEY,
            type TEXT
            )
            """
        )

        self.cursor.execute(
            """
            CREATE TABLE Fields (
                cite_id TEXT REFERENCES Cites,
                name TEXT,
                content TEXT
            )
            """
        )

        self.connection.commit()

    def drop_tables(self) -> None:
        self.cursor.execute(
            """
            DROP TABLE IF EXISTS Cites
            """
        )

        self.cursor.execute(
            """
            DROP TABLE IF EXISTS Fields
            """
        )

        self.connection.commit()

    def initialize(self) -> None:
        self.drop_tables()
        self.create_tables()


database = Database()
