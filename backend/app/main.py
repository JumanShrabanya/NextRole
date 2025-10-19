import os
from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware

from app.db.dbconnect import close_client, connect_and_ping, get_database
from app.routes.auth import router as auth_router
from app.routes.career import router as career_router
from beanie import init_beanie
from app.models.user import User

app = FastAPI()

# CORS setup
origins = ["http://localhost:3000"]
frontend_origin = os.getenv("FRONTEND_ORIGIN")
if frontend_origin:
    origins.append(frontend_origin)

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router)
app.include_router(career_router)

# Initialize Beanie/MongoDB for each request if not initialized
async def get_initialized_db():
    db = get_database()
    # You may wish to set a global flag after first init in production
    try:
        await init_beanie(database=db, document_models=[User])
    except Exception as e:
        # Avoid repeating initialization or handle as needed
        pass
    return db

@app.get("/")
async def read_root():
    return {"message": "Hello from FastAPI!"}

@app.get("/hello")
async def say_hello():
    return {"message": "Connection apis working ✅"}

@app.get("/health")
async def health(db=Depends(get_initialized_db)):
    try:
        await db.command("ping")
        return {"status": "ok"}
    except Exception as exc:
        return {"status": "error", "detail": str(exc)}
