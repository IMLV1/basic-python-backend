from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app import crud, schemas, dependencies

router = APIRouter()

@router.post("/", response_model=schemas.UserOut)
def create_user(user: schemas.UserCreate, db: Session = Depends(dependencies.get_db)):
    return crud.create_user(db, user)
