import fitz
from fastapi import UploadFile
from app.processors.base_processor import BaseProcessor


class PDFProcessor(BaseProcessor):
    def supports(self, file: UploadFile) -> bool:
        return (
            file.content_type == "application/pdf"
            or file.filename.endswith(".pdf")
        )

    async def process(self, file: UploadFile) -> str:
        pdf_bytes = await file.read()

        doc = fitz.open(
            stream=pdf_bytes,
            filetype="pdf"
        )

        texts = []

        for page in doc:
            texts.append(page.get_text())

        doc.close()

        await file.seek(0) # 이후 다시 사용할 수 있도록 포인터 복원

        return "\n".join(texts)
    