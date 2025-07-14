import os

class Config:
    MONGO_URI = os.environ.get("MONGO_URI")
    SECRET_KEY = os.environ.get("SECRET_KEY", "dev")  # Optional, but good practice

