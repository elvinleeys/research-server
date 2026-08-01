from fastapi import UploadFile
from app.llm.openai_provider import MockProvider
from app.agents.planner import Planner
from app.processors.processor_manager import ProcessorManager
from app.context.context_builder import ContextBuilder



class ResearchAgent:
    def __init__(self):
        self.provider = MockProvider()
        self.planner = Planner()
        self.processor_manager = ProcessorManager()
        self.context_builder = ContextBuilder(
            self.processor_manager
        )


    async def run(
        self,
        message: str,
        files: list[UploadFile] = [],
    ) -> str:
        plan = await self.planner.create_plan(
            message=message,
            has_files=len(files) > 0,
        )

        context = await self.context_builder.build(
            message=message,
            files=files,
            plan=plan,
        )

        return await self._generate_answer(
            context
        )


    async def _generate_answer(
        self,
        context: dict,
    ) -> str:
        return await self.provider.generate(
            prompt=context["message"],
            context=context,
        )