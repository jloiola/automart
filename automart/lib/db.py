from peewee import Model, SqliteDatabase
from pathlib import Path

root_dir = Path().parent.parent
db_dir = root_dir / "data" / "automart.db"
db = SqliteDatabase(db_dir)
