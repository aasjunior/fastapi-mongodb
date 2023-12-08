from app.models import models, database, schemas

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
        item["_id"] = str(item["_id"])  # Converta o ObjectId para uma string
    return items

def update_item(item_id: str, item: schemas.ItemSchema):
    item_dict = item.dict()
    result = database.collection.update_one({"_id": item_id}, {"$set": item_dict})
    if result:
        item_dict["_id"] = str(item_id)  # Converta o ObjectId para uma string
        return item_dict
    else:
        return Non

def delete_item(item_id: str):
    result = database.collection.delete_one({"_id": item_id})
    if result:
        return True
    else:
        return False