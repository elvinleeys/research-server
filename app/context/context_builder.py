from fastapi import UploadFile
from app.processors.processor_manager import ProcessorManager
from app.schemas.plan import Plan


class ContextBuilder:
    def __init__(
        self,
        processor_manager: ProcessorManager,
    ):
        self.processor_manager = processor_manager


    async def build(
        self,
        message: str,
        files: list[UploadFile],
        plan: Plan,
    ) -> dict:
        documents = []

        for file in files:
            content = await self.processor_manager.process(
                file
            )

            documents.append(
                {
                    "filename": file.filename,
                    "content": content,
                }
            )

        return {
            "message": message,
            "documents": documents,
            "plan": plan,
        }