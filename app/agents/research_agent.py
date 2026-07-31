from fastapi import UploadFile
from app.llm.openai_provider import MockProvider
from app.agents.planner import Planner

class ResearchAgent:
    def __init__(self):
        self.provider = MockProvider()
        self.planner = Planner()

    async def run(
        self,
        message: str,
        files: list[UploadFile] = [],
    ) -> str:

        plan = await self.planner.create_plan(
            message=message,
            has_files=len(files) > 0
        )

        context = await self._build_context(
            message, 
            files, 
            plan
        )

        print(context)

        answer = await self._generate_answer(context)

        print(answer)

        return answer

    async def _build_context(
        self,
        message: str,
        files: list[UploadFile],
        plan
    ) -> dict:

        return {
            "message": message,
            "files": files,
            "plan": plan,
        }

    async def _generate_answer(
        self,
        context: dict,
    ) -> str:
        return await self.provider.generate(
            prompt=context["message"],
        )