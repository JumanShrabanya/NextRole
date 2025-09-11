from fastapi import APIRouter, HTTPException, status

from app.schemas.user import UserCreate, UserPublic
from app.services.user_service import create_user


router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/register", response_model=UserPublic, status_code=status.HTTP_201_CREATED)
async def register(user_in: UserCreate) -> UserPublic:
    try:
        return await create_user(user_in)
    except ValueError as exc:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(exc)) from exc


