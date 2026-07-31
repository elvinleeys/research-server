from fastapi import UploadFile
from app.llm.openai_provider import MockProvider

class ResearchAgent:
    def __init__(self):
        self.provider = MockProvider()

    async def run(
        self,
        message: str,
        files: list[UploadFile] = [],
    ) -> str:

        context = await self._build_context(message, files)

        print(context)

        answer = await self._generate_answer(context)

        print(answer)

        return answer

    async def _build_context(
        self,
        message: str,
        files: list[UploadFile],
    ) -> dict:

        return {
            "message": message,
            "files": files,
        }

    async def _generate_answer(
        self,
        context: dict,
    ) -> str:
        return await self.provider.generate(
            prompt=context["message"],
        )