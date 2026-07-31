import pytest
from app.agents.planner import Planner

@pytest.mark.unit
@pytest.mark.anyio
async def test_document_plan():
    planner = Planner()

    plan = await planner.create_plan(
        message="이 PDF 분석해줘",
        has_files=True
    )

    assert plan.task_type == "analyze_document"

    assert "파일 내용 추출" in plan.steps


@pytest.mark.unit
@pytest.mark.anyio
async def test_general_plan():
    planner = Planner()

    plan = await planner.create_plan(
        message="AI Agent란?"
    )

    assert plan.task_type == "general"