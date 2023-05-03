from prisma.models import Customer

Customer.create_partial("CustomerCreate", include={"name"})
