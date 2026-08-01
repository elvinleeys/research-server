import pytest
from fastapi import UploadFile
from app.processors.pdf_processor import PDFProcessor
from tests.conftest import test_files_dir


@pytest.mark.unit
@pytest.mark.anyio
async def test_pdf_processor(test_files_dir):
    processor = PDFProcessor()

    with open(
        test_files_dir / "sample.pdf",
        "rb"
    ) as f:
        upload_file = UploadFile(
            filename="sample.pdf",
            file=f,
        )


        result = await processor.process(
            upload_file
        )

    assert isinstance(result, str)
    assert len(result) > 0