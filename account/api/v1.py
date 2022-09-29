from datetime import timedelta

from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from starlette import status

from core.dependencies import get_db
from settings import ACCESS_TOKEN_EXPIRE_MINUTES

from ..crud import db_user
from ..schemas import UserCreateSchema
from ..utils import authenticate, create_access_token, hash_password

router = APIRouter(
    prefix="/account",
    tags=["account"],
)


@router.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = authenticate(db, username=form_data.username, password=form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    acces_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username},
        expires_delta=acces_token_expires,
    )
    return {"username": user.username, "access_token": access_token, "token_type": "bearer"}


@router.post("/register")
def register(*, db: Session = Depends(get_db), user_in: UserCreateSchema):
    user = db_user.get_by_username(db, username=user_in.username)
    if user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="The user with this username already exists."
        )
    user_in.password = hash_password(user_in.password)
    user = db_user.create(db, obj_in=user_in)
    return user
