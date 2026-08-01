import pytest
from tests.conftest import client, test_files_dir

# 메시지만 전송했을 경우
@pytest.mark.integration
def test_chat_message_only(client):
    response = client.post(
        "/chat/",
        data={"message": "AI Agent란 무엇인가?"}
    )

    assert response.status_code == 200
    assert response.json()["answer"] == "LLM 응답: AI Agent란 무엇인가?"


# 파일 하나만 전송했을 경우
@pytest.mark.integration
def test_chat_pdf(client, test_files_dir):
    file_path = test_files_dir / "sample.pdf"

    with open(file_path, "rb") as f:
        response = client.post(
            "/chat/",
            data={
                "message": "요약해줘"
            },
            files={
                "files": (
                    "sample.pdf",
                    f,
                    "application/pdf"
                )
            }
        )

    assert response.status_code == 200

    body = response.json()

    assert body["answer"] == "LLM 응답: 요약해줘"


# 여러 파일을 전송했을 경우
@pytest.mark.integration
def test_chat_multiple_files(client, test_files_dir):
    pdf_path = test_files_dir / "sample.pdf"
    image_path = test_files_dir / "sample.png"

    with open(pdf_path, "rb") as pdf, open(image_path, "rb") as image:

        response = client.post(
            "/chat/",
            data={
                "message": "파일 분석"
            },
            files=[
                (
                    "files",
                    (
                        "sample.pdf",
                        pdf,
                        "application/pdf"
                    )
                ),
                (
                    "files",
                    (
                        "sample.png",
                        image,
                        "image/png"
                    )
                ),
            ],
        )


    assert response.status_code == 200