from fastapi import APIRouter, Form, File, UploadFile
from app.schemas.chat import ChatResponse
from app.services.chat_service import generate_response


router = APIRouter(
    prefix="/chat",
    tags=["chat"]
)


@router.post("/")
async def chat(
    message: str = Form(...),
    files: list[UploadFile] | None = File(default=None),
):
    answer = await generate_response(
        message=message,
        files=files,
    )

    return ChatResponse(answer=answer)