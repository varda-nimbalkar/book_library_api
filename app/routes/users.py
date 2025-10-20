
from fastapi import APIRouter , Depends ,HTTPException
from sqlalchemy.orm import Session
from app import schemas , crud , database

router=APIRouter(prefix="/users",tags=["Users"])

def get_db():
    db=database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/register", response_model =schemas.UserOut)
def register_user(user:schemas.UserCreate,db:Session=Depends(get_db)):
    created_user = crud.create_user(db,user)
    if not created_user:
        raise HTTPException(status_code=400,detail="Email already registered")
    return created_user