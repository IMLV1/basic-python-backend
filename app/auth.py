import jwt
from datetime import datetime, timedelta
from .config import JWT_SECRET

ALGORITHM = "HS256"

def create_access_token(user_id: int):
    payload = {"sub": str(user_id), "exp": datetime.utcnow() + timedelta(hours=1)}
    return jwt.encode(payload, JWT_SECRET, algorithm=ALGORITHM)
