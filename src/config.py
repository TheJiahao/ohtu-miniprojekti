import os
from pathlib import Path

from dotenv import load_dotenv, find_dotenv

try:
    load_dotenv(find_dotenv())
except FileNotFoundError:
    pass

DATA_DIRECTORY = Path(__file__).parents[1] / "data"
DATABASE_FILENAME = os.getenv("DATABASE_FILENAME") or "database.db"
DATABASE_FILE_PATH = DATA_DIRECTORY / DATABASE_FILENAME
