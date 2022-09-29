from typing import Optional

from pydantic import BaseModel


class UserBaseSchema(BaseModel):
    email: str


class UserCreateSchema(UserBaseSchema):
    username: str
    password: str


class UserUpdateSchema(UserBaseSchema):
    is_active: bool


class UserSchema(UserBaseSchema):
    id: int
    username: str
    is_active: bool

    class Config:
        orm_mode = True


class TokenSchema(BaseModel):
    access_token: str
    token_type: str


class TokenDataSchema(BaseModel):
    username: Optional[str] = None
