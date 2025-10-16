from pydantic import BaseModel
import os
from dotenv import load_dotenv


load_dotenv()


class MongoSettings(BaseModel):
    mongo_uri: str = os.getenv("MONGO_URI", "")
    database_name: str = os.getenv("MONGO_DB", "NextRole")


class JwtSettings(BaseModel):
    secret_key: str = os.getenv("JWT_SECRET", "change-me")
    algorithm: str = os.getenv("JWT_ALG", "HS256")
    access_token_expires_minutes: int = int(os.getenv("JWT_ACCESS_MIN", "60"))


class GeminiSettings(BaseModel):
    api_key: str = os.getenv("GEMINI_API_KEY", "")
    model: str = os.getenv("GEMINI_MODEL", "gemini-2.5-flash-lite")


settings = MongoSettings()
jwt_settings = JwtSettings()
gemini_settings = GeminiSettings()


