import pytest
from fastapi import UploadFile
from tests.conftest import test_files_dir
from app.processors.image_processor import ImageProcessor

@pytest.mark.unit
@pytest.mark.anyio
async def test_image_processor(test_files_dir):
    processor = ImageProcessor()

    with open(
        test_files_dir / "sample.png",
        "rb"
    ) as f:
        upload_file = UploadFile(
            filename="sample.png",
            file=f,
        )

        result = await processor.process(
            upload_file
        )

    assert isinstance(result, str)
    assert "sample.png" in result