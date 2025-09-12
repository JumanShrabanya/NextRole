from contextlib import asynccontextmanager

from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.db.dbconnect import close_client, connect_and_ping, get_database
from app.routes.auth import router as auth_router
from app.routes.career import router as career_router
from beanie import init_beanie
from app.models.user import User

@asynccontextmanager
async def lifespan(app: FastAPI):
    try:
        await connect_and_ping()
        db = get_database()
        await init_beanie(database=db, document_models=[User])
    except Exception as e:
        print(f"❌ MongoDB connection failed during startup: {e}")
        # Optionally: log or raise depending on how critical DB is
    try:
        yield
    finally:
        await close_client()


app = FastAPI(lifespan=lifespan)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Next.js dev server
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router)
app.include_router(career_router)

@app.get("/")
def read_root():
    return {"message": "Hello from FastAPI!"}

@app.get("/hello")
def say_hello():
    return {"message": "Connection apis working ✅"}


@app.get("/health")
async def health():
    try:
        db = get_database()
        await db.command("ping")
        return {"status": "ok"}
    except Exception as exc:  # noqa: BLE001
        return {"status": "error", "detail": str(exc)}
