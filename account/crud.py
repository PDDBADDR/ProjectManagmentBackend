from typing import Optional

from sqlalchemy.orm import Session

from account.models import User
from account.schemas import UserCreateSchema, UserUpdateSchema
from core.crud import CRUDBase


class CRUDUser(CRUDBase[User, UserCreateSchema, UserUpdateSchema]):
    def get_by_username(self, db: Session, *, username: str) -> Optional[User]:
        return db.query(User).filter(User.username == username).first()


db_user = CRUDUser(User)
