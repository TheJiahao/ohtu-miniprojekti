import os
import pytest
from infrastructure.database import SQLiteDB
from entities.cite import Cite


@pytest.fixture
def test_db():
    db = SQLiteDB("test.db")
    yield db

    db.connection.close()
    os.remove("test.db")


def test_file_gets_created(test_db):
    assert os.path.exists("test.db")


def test_db_init_connection(test_db):
    assert test_db.connection is not None


def test_db_init_create_table(test_db):
    cursor = test_db.connection.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='cites'")
    table = cursor.fetchone()
    cursor.close()

    assert table is not None


def test_db_add_cite(test_db):
    cite = Cite("testiA", "testiB", "testiC")
    test_db.add_cite(cite)
    cursor = test_db.connection.cursor()

    cursor.execute("SELECT * FROM cites WHERE name = ?", (cite.name,))
    result = cursor.fetchone()
    cursor.close()

    assert result is not None
    assert result[1] == cite.name
