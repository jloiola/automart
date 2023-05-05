from automart.lib.db import db
from automart.models import *


def setup_db():
    db.connect()

    with db.atomic():
        db.create_tables([Customer, VehicleMake, VehicleModel])

        with open("./data/seed_data.sql") as file:
            lines = file.readlines()

        for line in lines:
            db.execute_sql(line)


if __name__ == "__main__":
    setup_db()
