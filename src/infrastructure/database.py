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
                entry_type TEXT,
                fields TEXT
            )
        """

        cursor.execute(sql)
        self.connection.commit()
        cursor.close()

    def add_cite(self, cite) -> None:
        """Lisää lähteen tietokantaan

        Args:
            cite (Cite): Lähde oliona.
        """

        cursor = self.connection.cursor()
        sql = "INSERT INTO cites (name, entry_type, fields) VALUES (?, ?, ?)"
        data = (cite.name, cite.entry_type, str(cite.fields))

        cursor.execute(sql, data)
        self.connection.commit()
        cursor.close()

    # def get_all_cites(self) -> list:
    #     pass

    def get_cites(self):
        """Hakee kaikki tietokannassa olevat viitteet"""
        cursor = self.connection.cursor()
        sql = "SELECT name FROM cites"
        cites = cursor.execute(sql).fetchall()
        cursor.close()
        return cites


database = SQLiteDB("data/citations.db")
