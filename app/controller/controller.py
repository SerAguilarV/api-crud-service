from fastapi import APIRouter
from fastapi.responses import JSONResponse
from typing import Union, Optional

from app.models.telefonos import TelefonosEntity, Telefonos, UpdateTelefonos
from app.service.telefonos_service import TelefonosService

router = APIRouter()
telefonos_service = TelefonosService()


@router.get("/telefonos", response_model=Optional[TelefonosEntity])
async def get_telefono(telefono: Union[int, None] = None, id: Union[str, None] = None):
    if telefono is not None and id is not None:
        return JSONResponse(status_code=400, content={"result": False, "error": "Envia solo un parametro"})
    elif telefono is not None:
        return await telefonos_service.get_telefono_by_telefono(telefono)
    elif id is not None:
        return await telefonos_service.get_telefono_by_id(id)
    return JSONResponse(status_code=400, content={"result": False, "error": "Añade un pametro id o telefono"})


@router.post("/telefonos", response_model=Optional[TelefonosEntity])
async def create_telefonos(telefono: Telefonos):
    telefono = await telefonos_service.insert_telefono(telefono)
    if telefono is None:
        return JSONResponse(status_code=400, content={"result": False, "error": "Telefono ya existente"})
    return telefono


@router.delete("/telefonos")
async def delete_state(telefono:int):
    telefono = await telefonos_service.delete_by_telefono(telefono)
    if telefono is None:
        return JSONResponse(status_code=404, content={"result": False, "error": "Telefono no existe"})
    return JSONResponse(status_code=200, content={"result": True})


@router.put("/telefonos")
async def update_state(telefono:UpdateTelefonos):
    telefono = await telefonos_service.update_by_telefono(telefono)
    if telefono is None:
        return JSONResponse(status_code=404, content={"result": False, "error": "Telefono no existe"})
    return JSONResponse(status_code=200, content={"result": True})
