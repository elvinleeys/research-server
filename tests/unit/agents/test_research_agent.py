import pytest
from app.agents.research_agent import ResearchAgent

@pytest.mark.unit
@pytest.mark.anyio
async def test_research_agent_message_only():

    agent = ResearchAgent()

    result = await agent.run(
        message="AI Agent란?"
    )

    assert result == "LLM 응답: AI Agent란?"


@pytest.mark.unit
@pytest.mark.anyio
async def test_research_agent_with_files():

    agent = ResearchAgent()

    result = await agent.run(
        message="파일 분석해줘",
        files=[],
    )

    assert result == "LLM 응답: 파일 분석해줘"