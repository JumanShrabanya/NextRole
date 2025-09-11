from datetime import datetime, timedelta, timezone
from typing import Any, Dict

from jose import jwt

from app.core.settings import jwt_settings


def create_access_token(subject: str, extra: Dict[str, Any] | None = None) -> str:
    now = datetime.now(timezone.utc)
    to_encode: Dict[str, Any] = {"sub": subject, "iat": int(now.timestamp())}
    if extra:
        to_encode.update(extra)
    expire = now + timedelta(minutes=jwt_settings.access_token_expires_minutes)
    to_encode["exp"] = expire
    return jwt.encode(to_encode, jwt_settings.secret_key, algorithm=jwt_settings.algorithm)


