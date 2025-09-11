from datetime import datetime, timezone
from typing import Any, Dict, Optional

from pymongo.errors import DuplicateKeyError

from app.models.user import User
from app.schemas.user import UserCreate, UserPublic
from app.utils.security import hash_password
from app.utils.security import verify_password
from app.utils.jwt import create_access_token
from app.schemas.user import LoginRequest, TokenResponse


async def create_user(user_in: UserCreate) -> UserPublic:
    now = datetime.now(timezone.utc)
    user = User(
        full_name=user_in.full_name.strip(),
        email=user_in.email.lower(),
        password_hash=hash_password(user_in.password),
        created_at=now,
        updated_at=None,
    )

    try:
        await user.insert()
    except Exception as exc:  # noqa: BLE001
        # Beanie propagates DuplicateKeyError on unique index violations
        if isinstance(exc, DuplicateKeyError) or "duplicate key" in str(exc).lower():
            raise ValueError("Email already registered") from exc
        raise

    return UserPublic(
        id=str(user.id),
        full_name=user.full_name,
        email=user.email,
        created_at=user.created_at,
        updated_at=user.updated_at,
    )


async def authenticate_user(credentials: LoginRequest) -> TokenResponse:
    user = await User.find_one(User.email == credentials.email.lower())
    if not user:
        raise ValueError("Invalid email or password")
    if not verify_password(credentials.password, user.password_hash):
        raise ValueError("Invalid email or password")

    token = create_access_token(subject=str(user.id))
    return TokenResponse(
        access_token=token,
        user=UserPublic(
            id=str(user.id),
            full_name=user.full_name,
            email=user.email,
            created_at=user.created_at,
            updated_at=user.updated_at,
        ),
    )


