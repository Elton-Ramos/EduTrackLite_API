from pydantic import BaseModel

class UserCreate(BaseModel):
    name: str
    email: str
    is_active: bool = True

class UserUpdate(BaseModel):
    name: str | None = None
    email: str | None = None
    is_active: bool | None = None

class User(UserCreate):
    id: int

    class Config:
        orm_mode = True