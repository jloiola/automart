from tortoise.models import Model as DbModel
from tortoise.fields import (
    IntField,
    CharField,
    DatetimeField,
    ForeignKeyField,
    ForeignKeyRelation,
)

# Database models/entities


class Customer(DbModel):
    id = IntField(pk=True)
    first_name = CharField(max_length=50, null=True)
    last_name = CharField(max_length=50, null=True)
    created_at = DatetimeField(auto_now_add=True)
    modified_at = DatetimeField(auto_now=True)


class Make(DbModel):
    id = IntField(pk=True)
    name = CharField(max_length=100, null=True)


class Model(DbModel):
    id = IntField(pk=True)
    make: ForeignKeyRelation["Make"] = ForeignKeyField(
        "models.Make", related_name="make"
    )
    name = CharField(max_length=100, null=True)
