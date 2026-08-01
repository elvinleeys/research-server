import pytest
from fastapi import UploadFile
from tests.conftest import test_files_dir
from app.processors.docx_processor import DocxProcessor

@pytest.mark.unit
@pytest.mark.anyio
async def test_docx_processor(test_files_dir):
    processor = DocxProcessor()

    with open(
        test_files_dir / "sample.docx",
        "rb"
    ) as f:
        upload_file = UploadFile(
            filename="sample.docx",
            file=f,
        )

        result = await processor.process(
            upload_file
        )

    assert isinstance(result, str)
    assert len(result) > 0