from fastapi import APIRouter, HTTPException, status

from app.schemas.user import UserCreate, UserPublic, LoginRequest, TokenResponse
from app.services.user_service import create_user, authenticate_user


router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/register", response_model=UserPublic, status_code=status.HTTP_201_CREATED)
async def register(user_in: UserCreate) -> UserPublic:
    try:
        return await create_user(user_in)
    except ValueError as exc:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(exc)) from exc


@router.post("/login", response_model=TokenResponse)
async def login(credentials: LoginRequest) -> TokenResponse:
    try:
        return await authenticate_user(credentials)
    except ValueError as exc:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=str(exc)) from exc


