import pytest
from fastapi import UploadFile
from app.context.context_builder import ContextBuilder
from app.processors.processor_manager import ProcessorManager
from tests.conftest import test_files_dir

# 파일이 없는 context_builder 테스트
@pytest.mark.unit
@pytest.mark.anyio
async def test_context_builder_without_files():

    builder = ContextBuilder(
        ProcessorManager()
    )

    context = await builder.build(
        message="AI Agent란?",
        files=[],
        plan=None,
    )

    assert context["message"] == "AI Agent란?"
    assert context["documents"] == []
    assert context["plan"] is None


# pdf 파일 context_builder 테스트
@pytest.mark.unit
@pytest.mark.anyio
async def test_context_builder_with_pdf(test_files_dir):
    builder = ContextBuilder(
        ProcessorManager()
    )

    with open(
        test_files_dir / "sample.pdf",
        "rb"
    ) as f:
        upload_file = UploadFile(
            filename="sample.pdf",
            file=f,
        )

        context = await builder.build(
            message="논문 분석",
            files=[upload_file],
            plan={
                "task_type": "analyze_document"
            },
        )

    assert context["message"] == "논문 분석"
    assert len(context["documents"]) == 1
    assert context["plan"]["task_type"] == "analyze_document"

# 여러 파일 context_builder 테스트
@pytest.mark.unit
@pytest.mark.anyio
async def test_context_builder_multiple_files(test_files_dir):
    builder = ContextBuilder(
        ProcessorManager()
    )

    files = []

    with open(test_files_dir / "sample.pdf", "rb") as pdf:
        files.append(
            UploadFile(
                filename="sample.pdf",
                file=pdf,
            )
        )

    with open(test_files_dir / "sample.png", "rb") as image:
        files.append(
            UploadFile(
                filename="sample.png",
                file=image,
            )
        )

    context = await builder.build(
        message="논문과 이미지 분석",
        files=files,
        plan=None,
    )

    assert len(context["documents"]) == 2