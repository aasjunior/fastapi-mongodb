from fastapi import FastAPI, Depends
from app.controllers import routes, auth
from app.models import schemas
from motor.motor_asyncio import AsyncIOMotorClient

from app.settings import settings  # Importe as configurações corretamente

app = FastAPI()

async def check_db_connection():
    client = AsyncIOMotorClient(settings.MONGODB_URL)
    try:
        db_list = await client.list_database_names()
        if settings.DB_NAME not in db_list:
            await client[settings.DB_NAME].command({"create": settings.DB_NAME})
    finally:
        client.close()

@app.on_event("startup")
async def startup_db_client():
    await check_db_connection()

app.include_router(routes.router)

@app.post("/login")
def login(user: schemas.UserSchema):
    return auth.authenticate_user(user.username, user.password)

@app.get("/users/me")
async def read_users_me(current_user: str = Depends(auth.get_current_user)):
    return {"username": current_user}
