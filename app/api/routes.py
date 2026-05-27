from fastapi import APIRouter, HTTPException
from app.schemas.llm_schema import LLMRequest, LLMResponse

from app.core.enums import TaskType
from app.services.task_service import TaskService

router = APIRouter()


@router.post("/chat", response_model = LLMResponse)
def chat(request: LLMRequest):
    try:
        request.task == TaskType.CHAT
        return TaskService.execute(request)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
