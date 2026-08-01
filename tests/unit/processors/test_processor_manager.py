import pytest
from fastapi import UploadFile
from tests.conftest import test_files_dir
from app.processors.processor_manager import ProcessorManager

@pytest.mark.unit
@pytest.mark.anyio
async def test_processor_manager_pdf(test_files_dir):
    manager = ProcessorManager()

    with open(
        test_files_dir / "sample.pdf",
        "rb"
    ) as f:
        file = UploadFile(
            filename="sample.pdf",
            file=f,
            headers={
                "content-type": "application/pdf"
            }
        )

        result = await manager.process(file)

    assert isinstance(result, str)