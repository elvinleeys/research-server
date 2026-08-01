from io import BytesIO

from PIL import Image
from fastapi import UploadFile

from app.processors.base_processor import BaseProcessor


class ImageProcessor(BaseProcessor):

    def supports(
        self,
        file: UploadFile
    ) -> bool:

        return (
            file.content_type is not None
            and file.content_type.startswith("image/")
        )


    async def process(
        self,
        file: UploadFile
    ) -> str:

        contents = await file.read()

        image = Image.open(
            BytesIO(contents)
        )


        await file.seek(0)


        return f"""
            이미지 파일 정보

            파일명: {file.filename}
            타입: {file.content_type}
            크기: {image.width}x{image.height}
            색상 모드: {image.mode}
        """