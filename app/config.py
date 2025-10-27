import os
from dotenv import load_dotenv

load_dotenv()  # โหลดค่าจาก .env

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./test.db")
JWT_SECRET = os.getenv("JWT_SECRET", "secret")
