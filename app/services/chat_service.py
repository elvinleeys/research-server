from fastapi import UploadFile

async def generate_response(
    message: str,
    files: list[UploadFile] | None = None,
):
    if files:
        for file in files:
            print(file.filename)

    return f"입력받은 메시지: {message}"