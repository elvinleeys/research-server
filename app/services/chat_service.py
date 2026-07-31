from fastapi import UploadFile
from app.agents.research_agent import ResearchAgent

agent = ResearchAgent()

async def generate_response(
    message: str,
    files: list[UploadFile] = [],
) -> str:
    return await agent.run(
        message=message,
        files=files,
    )