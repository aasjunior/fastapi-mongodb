from app.models import models, database, schemas
from bson.objectid import ObjectId

def create_item(item: schemas.ItemSchema):
    item_dict = item.dict()
    result = database.collection.insert_one(item_dict)
    if result:
        item_dict["_id"] = str(result.inserted_id)  # Converta o ObjectId para uma string
        return item_dict
    else:
        return None

def read_items():
    items = list(database.collection.find())
    for item in items:
        item["_id"] = str(item["_id"])
    return items

def read_item(item_id: str):
    item_id_obj = ObjectId(item_id)
    item = database.collection.find_one({"_id": item_id_obj})
    if item:
        item["_id"] = str(item["_id"])
        return item
    else:
        return None

def update_item(item_id: str, item: schemas.ItemSchema):
    item_dict = item.dict()
    item_id_obj = ObjectId(item_id)
    result = database.collection.update_one({"_id": item_id_obj}, {"$set": item_dict})
    if result.matched_count:
        item_dict["_id"] = item_id
        return item_dict
    else:
        return None


def delete_item(item_id: str):
    item_id_obj = ObjectId(item_id)
    result = database.collection.delete_one({"_id": item_id_obj})
    if result:
        return True
    else:
        return False