from datetime import datetime
from typing import Optional

from beanie import Document, Indexed


class User(Document):
    full_name: str
    email: Indexed(str, unique=True)  # type: ignore[valid-type]
    password_hash: str
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Settings:
        name = "users"


