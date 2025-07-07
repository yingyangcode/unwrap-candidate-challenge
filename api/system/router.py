from fastapi import APIRouter
from api.system.schemas import ResetResponseSchema
from app.system.service import SystemService
from app.storage.memory_store import memory_store

router = APIRouter(tags=["system"])


@router.post("/reset", response_model=ResetResponseSchema)
def reset_system():
    system_service = SystemService(memory_store)
    result = system_service.reset_system()
    return ResetResponseSchema(message=result["message"])