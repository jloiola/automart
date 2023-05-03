from prisma import Prisma
from prisma.models import Customer

db = Prisma()


def get_db():
    return db


Customer.create_partial("CustomerCreate", include={"name"})
