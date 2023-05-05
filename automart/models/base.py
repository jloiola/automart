from peewee import Model, AutoField
from automart.lib.db import db


class BaseModel(Model):
    id = AutoField()

    class Meta:
        database = db
        legacy_table_names = False
