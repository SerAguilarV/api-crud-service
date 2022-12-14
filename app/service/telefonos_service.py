from datetime import datetime

from bson import ObjectId

from app.config.mongo import mongo_client
from app.models.telefonos import Telefonos, TelefonosCreate


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
