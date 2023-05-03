from typing import Type
from datetime import datetime
from tortoise.models import Model
from tortoise.fields import IntField, CharField, DatetimeField
from tortoise.signals import pre_save


class User(Model):
    id = IntField(pk=True)
    username = CharField(max_length=20, unique=True)
    name = CharField(max_length=50, null=True)
    family_name = CharField(max_length=50, null=True)
    category = CharField(max_length=30, default="misc")
    password_hash = CharField(max_length=128, null=True)
    created_at = DatetimeField(auto_now_add=True)
    modified_at = DatetimeField(auto_now=True)

    class PydanticMeta:
        exclude = ("password_hash",)


@pre_save(User)
async def signal_pre_save(
    sender: "Type[User]", instance: User, using_db, update_fields
) -> None:
    print(sender.modified_at, instance.modified_at, using_db, update_fields)
