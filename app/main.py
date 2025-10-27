from fastapi import FastAPI
from app.routers import users, auth

app = FastAPI(title="Company User System")

app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(users.router, prefix="/users", tags=["users"])
