from abc import ABC, abstractmethod
from fastapi import UploadFile


class BaseProcessor(ABC):
    """모든 파일 Processor의 공통 인터페이스"""

    @abstractmethod
    def supports(self, file: UploadFile) -> bool:
        """현재 Processor가 해당 파일을 처리할 수 있는지 판단"""
        pass

    @abstractmethod
    async def process(self, file: UploadFile) -> str:
        """파일을 읽어 LLM이 사용할 텍스트로 변환"""
        pass