from fastapi import APIRouter, Depends, HTTPException, status
from app.services import services
from app.models import schemas
from . import auth

router = APIRouter()

@router.post("/items/")
async def create_item(item: schemas.ItemSchema, current_user: str = Depends(auth.get_current_user)):
    item_dict = services.create_item(item)
    if item_dict:
        return item_dict
    else:
        raise HTTPException(status_code=400, detail="Item not created")

@router.get("/items/")
async def read_items(current_user: str = Depends(auth.get_current_user)):
    items = services.read_items()
    return items

@router.put("/items/{item_id}")
async def update_item(item_id: str, item: schemas.ItemSchema, current_user: str = Depends(auth.get_current_user)):
    item_dict = services.update_item(item_id, item)
    if item_dict:
        return item_dict
    else:
        raise HTTPException(status_code=400, detail="Item not updated")

@router.delete("/items/{item_id}")
async def delete_item(item_id: str, current_user: str = Depends(auth.get_current_user)):
    result = services.delete_item(item_id)
    if result:
        return {"message": "Item deleted"}
    else:
        raise HTTPException(status_code=400, detail="Item not deleted")