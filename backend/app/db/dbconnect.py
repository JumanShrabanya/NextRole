from typing import Optional

import motor.motor_asyncio

from app.core.settings import settings


_client: Optional[motor.motor_asyncio.AsyncIOMotorClient] = None


def get_client() -> motor.motor_asyncio.AsyncIOMotorClient:
    global _client
    if _client is None:
        if not settings.mongo_uri:
            raise RuntimeError("MONGO_URI is not configured")
        _client = motor.motor_asyncio.AsyncIOMotorClient(settings.mongo_uri)
    return _client


def get_database():
    return get_client()[settings.database_name]


async def connect_and_ping() -> None:
    client = get_client()
    await client.admin.command("ping")


async def close_client() -> None:
    global _client
    if _client is not None:
        _client.close()
        _client = None
