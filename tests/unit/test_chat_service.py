from unittest.mock import AsyncMock, patch
import pytest
from app.services.chat_service import generate_response

@pytest.mark.unit
@pytest.mark.anyio
async def test_generate_response_calls_agent():
    with patch(
        "app.services.chat_service.agent.run",
        new_callable=AsyncMock
    ) as mock_run:
        mock_run.return_value = "테스트 응답"

        result = await generate_response(
            message="hello"
        )

        mock_run.assert_called_once()

        assert result == "테스트 응답"