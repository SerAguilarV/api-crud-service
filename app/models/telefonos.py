from pydantic import BaseModel, validator, Field
from datetime import datetime
from bson.objectid import ObjectId
from typing import Optional

from app.models.utils import PyObjectId


class UpdateTelefonos(BaseModel):
    nombre: Optional[str]
    apellido_materno: Optional[str]
    apellido_paterno: Optional[str]
    telefono: int
    status: Optional[str]
    descripcion: Optional[str]


class Telefonos(BaseModel):
    nombre: str
    apellido_materno: str
    apellido_paterno: str
    telefono: int
    status: str
    descripcion: str
    cliente: str

    @validator('telefono')
    def check_length_telefono(cls, v):
        assert len(str(v)) == 10, "longitud de telefono incorrecta"
        return v


class TelefonosCreate(Telefonos):

    created_at: Optional[datetime]

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}


class TelefonosEntity(TelefonosCreate):

    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}


