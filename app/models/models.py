from pydantic import BaseModel

class Item(BaseModel):
    name: str
    value: str

class User(BaseModel):
    username: str
    password: str