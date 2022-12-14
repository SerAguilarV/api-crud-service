from motor import motor_asyncio
from app.config import secrets

env = secrets.Settings()


def mongo_client():
    client = motor_asyncio.AsyncIOMotorClient(env.MONGO_URI)
    return client[env.DATABASE]
