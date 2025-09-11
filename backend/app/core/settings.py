from pydantic import BaseModel
import os
from dotenv import load_dotenv


load_dotenv()


class MongoSettings(BaseModel):
    mongo_uri: str = os.getenv("MONGO_URI", "")
    database_name: str = os.getenv("MONGO_DB", "NextRole")


settings = MongoSettings()


