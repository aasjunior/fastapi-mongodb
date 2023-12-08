from pydantic import BaseModel

class ItemSchema(BaseModel):
    name: str
    value: str

class UserSchema(BaseModel):
    username: str
    password: str