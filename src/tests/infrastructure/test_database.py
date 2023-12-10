import unittest
from unittest.mock import patch

from config import DATABASE_FILE_PATH
from infrastructure.database import Database, database


class TestDatabase(unittest.TestCase):
    def setUp(self) -> None:
        self.connection = database.connection
        self.cursor = database.cursor

        return database.drop_tables()

    def test_create_tables(self):
        database.create_tables()

        rows = self.cursor.execute(
            """
            SELECT name
            FROM sqlite_master
            WHERE type="table"
            """
        ).fetchall()

        tables = {row["name"] for row in rows}

        self.assertEqual(tables, {"Cites", "Authors", "Fields"})

    def test_drop_tables(self):
        self.cursor.execute("CREATE TABLE Cites (test TEXT PRIMARY KEY)")
        self.cursor.execute("CREATE TABLE Fields (test TEXT PRIMARY KEY)")
        self.cursor.execute("CREATE TABLE Authors (test TEXT PRIMARY KEY)")

        database.drop_tables()

        rows = self.cursor.execute(
            """
            SELECT name
            FROM sqlite_master
            WHERE type="table"
            """
        ).fetchall()

        self.assertEqual(len(rows), 0)

    def test_initialize_database(self):
        database.initialize()

        rows = self.cursor.execute(
            """
            SELECT name
            FROM sqlite_master
            WHERE type="table"
            """
        ).fetchall()

        tables = {row["name"] for row in rows}

        self.assertEqual(tables, {"Cites", "Authors", "Fields"})

    @patch.object(Database, "initialize")
    def test_initialize_getsize_zero(self, mock_initialize):
        open(DATABASE_FILE_PATH, "w").close()
        db = Database()

        mock_initialize.assert_called_once()
