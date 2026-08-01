from io import BytesIO

from docx import Document
from fastapi import UploadFile

from app.processors.base_processor import BaseProcessor


class DocxProcessor(BaseProcessor):

    def supports(
        self,
        file: UploadFile
    ) -> bool:
        return (
            file.content_type
            == "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
        )


    async def process(
        self,
        file: UploadFile
    ) -> str:
        contents = await file.read()

        document = Document(
            BytesIO(contents)
        )

        paragraphs = [
            paragraph.text
            for paragraph in document.paragraphs
            if paragraph.text.strip()
        ]

        await file.seek(0)

        return "\n".join(paragraphs)