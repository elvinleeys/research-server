from fastapi import UploadFile
from app.processors.base_processor import BaseProcessor
from app.processors.pdf_processor import PDFProcessor
from app.processors.image_processor import ImageProcessor
from app.processors.docx_processor import DocxProcessor

class ProcessorManager:
    def __init__(self):
        self.processors: list[BaseProcessor] = [
            PDFProcessor(),
            ImageProcessor(),
            DocxProcessor(),
        ]

    async def process(
        self,
        file: UploadFile
    ) -> str:
        for processor in self.processors:
            if processor.supports(file):
                return await processor.process(file)

        raise ValueError(
            f"지원하지 않는 파일 타입입니다: {file.content_type}"
        )