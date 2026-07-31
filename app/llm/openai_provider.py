from app.llm.provider import LLMProvider

class MockProvider(LLMProvider):

    async def generate(
        self,
        prompt: str,
        context: str | None = None,
    ) -> str:
        return f"LLM 응답: {prompt}"