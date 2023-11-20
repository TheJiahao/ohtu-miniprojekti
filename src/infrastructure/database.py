import sqlite3


class SQLiteDB:
    """Luokka vastaa yhteydestä tietokantaan"""

    def __init__(self, db_path: str) -> None:
        """Luokan konstruktori

        Args:
            db_path (str): Tietokannan sijainti.
        """
        self.connection = sqlite3.connect(db_path)
        self.create_table()

    def create_table(self) -> None:
        """Luo tietokantaan taulun, jos sitä ei ole olemassa"""

        cursor = self.connection.cursor()
        sql = """
            CREATE TABLE IF NOT EXISTS cites (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                type TEXT,
                fields TEXT
            )
        """

        cursor.execute(sql)
        self.connection.commit()
        cursor.close()

    def add_cite(self, cite) -> None:
        """Lisää lähteen tietokantaan

        Args:
            cite (Cite): Lähde olio.
        """
        cursor = self.connection.cursor()
        cursor.execute(
            "INSERT INTO cites (name, entry_type, fields) VALUES (?, ?, ?)",
            cite.name,
            cite.entry_type,
            cite.fields,
        )
        self.connection.commit()
        cursor.close()


database = SQLiteDB("data/citations.db")
