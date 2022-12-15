from datetime import datetime

from bson import ObjectId

from app.config.mongo import mongo_client
from app.models.telefonos import Telefonos, TelefonosCreate, UpdateTelefonos


class TelefonosService:

    def __init__(self):
        db = mongo_client()
        self.mongo = db["telefonos"]

    async def get_telefono_by_telefono(self, telefono):
        return await self.mongo.find_one({"telefono": telefono})

    async def get_telefono_by_id(self, id):
        return await self.mongo.find_one({"_id": ObjectId(id)})

    async def insert_telefono(self, telefono: Telefonos):
        if await self.get_telefono_by_telefono(telefono.telefono) is not None:
            return None
        telefono_entity = TelefonosCreate.parse_obj(dict(telefono))
        telefono_entity.created_at = datetime.now()
        id_insertado = await self.mongo.insert_one(telefono_entity.__dict__)
        return await self.get_telefono_by_id(id_insertado.inserted_id)

    async def delete_by_telefono(self, telefono):
        if await self.get_telefono_by_telefono(telefono) is None:
            return None
        return await self.mongo.delete_one({"telefono": telefono})

    async def update_by_telefono(self, telefono: UpdateTelefonos):
        telefono_for_update = await self.get_telefono_by_telefono(telefono.telefono)
        if telefono_for_update is None:
            return None
        data_to_update = {k: v for k, v in telefono.__dict__.items() if v is not None}
        return await self.mongo.update_one({"telefono": telefono.telefono}, {"$set": data_to_update})
