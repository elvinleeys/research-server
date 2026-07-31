from app.schemas.plan import Plan

class Planner:
    async def create_plan(
        self,
        message: str,
        has_files: bool = False,
    ) -> Plan:
        if has_files:
            return Plan(
                task_type="analyze_document",
                steps=[
                    "파일 내용 추출",
                    "문서 분석",
                    "답변 생성"
                ]
            )

        if "요약" in message:
            return Plan(
                task_type="summarize",
                steps=[
                    "내용 분석",
                    "핵심 정보 추출",
                    "요약 생성"
                ]
            )

        return Plan(
            task_type="general",
            steps=[
                "사용자 질문 분석",
                "답변 생성"
            ]
        )