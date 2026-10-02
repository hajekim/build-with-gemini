# Build with Gemini Track 3: AI 엔지니어링 핸즈온

Build with Gemini 행사 Track 3 실습 가이드와 자산을 모아 둔 저장소입니다.

참가자는 Antigravity 2.0(데스크톱 앱 또는 agy CLI)에게 설계서(SDD)를 바탕으로 프롬프트를 주며, ADK 멀티 에이전트를 만듭니다. 이 에이전트는 사내 규정 RAG와 Mock SaaS MCP 도구를 씁니다. 실습 2에서는 이 에이전트를 평가하고 보안 설정을 더해 Agent Runtime에 배포한 뒤 Gemini Enterprise에 등록합니다.

## 가이드 웹사이트

- [build.geap.dev](https://build.geap.dev/) (GitHub Pages)
- [Cloud Run 미러](https://build-with-gemini-guide-dri5akvbzq-du.a.run.app/)

웹사이트에서 실습 1, 실습 2, 설계서(SDD), Mock SaaS 명세를 탭으로 볼 수 있습니다. 코드 블록마다 실행 위치가 표시됩니다. `bash` 블록은 터미널 창에서 실행하고, `prompt` 블록은 에이전트 창(Antigravity 앱 또는 agy CLI)에 붙여 넣습니다.

## 실습 구성

| 실습 | 내용 | 시간 |
|:---|:---|:---|
| [실습 1](lab1/INSTRUCTION.md) | 개발 환경과 agents-cli 프로젝트 준비, ADK Orchestrator-Worker 구조, Vertex AI Search 기반 규정 RAG, Mock SaaS MCP 연동, 시나리오 테스트와 4-Tier evalset. 선택 과제로 A2A 로컬 검증 | 90분 (선택 과제 +15분) |
| [실습 2](lab2/INSTRUCTION.md) | agents-cli eval 평가와 개선, Secret Manager와 Agent Identity로 Agent Runtime 배포, Agent Registry 등록, Agent Gateway 접근 정책으로 위험 도구 차단, Model Armor, Gemini Enterprise 등록과 Preview 테스트 | 약 110~120분 |

실습 1을 끝내지 못했어도 완성본을 받아 실습 2를 진행할 수 있습니다(실습 2의 2.2절).

## 저장소 구조

```
build-with-gemini/
├── index.html                   # 가이드 웹사이트 (마크다운 문서를 탭과 단계로 렌더링)
├── CNAME                        # GitHub Pages 도메인 (build.geap.dev)
├── docs/
│   ├── SDD.md                   # 에이전트 설계서
│   ├── MOCK_SAAS.md             # Mock SaaS 웹 포털과 MCP 도구 명세
│   └── policies/                # 규정 PDF (POL-HR-2026-004 연차, POL-IT-2026-009 IT 자산)
├── lab1/
│   ├── INSTRUCTION.md           # 실습 1 가이드
│   ├── enterprise_ops_agent_completed.zip   # 실습 1 완성본
│   └── images/
└── lab2/
    ├── INSTRUCTION.md           # 실습 2 가이드
    ├── enterprise_ops_agent_lab2_completed.zip   # 실습 2 완성본
    ├── registry/                # Agent Registry 도구 명세 (위험도 주석 포함)
    └── images/                  # Gemini Enterprise 설정과 테스트 화면
```

## 실습용 Mock SaaS

인사 시스템 WorkWeek와 IT 서비스 관리 시스템 ServiceImmediately를 흉내 낸 서비스입니다. 웹 포털에서 개인 MCP 토큰을 발급받아 씁니다. 자세한 도구 목록과 데이터는 [docs/MOCK_SAAS.md](docs/MOCK_SAAS.md)에 있습니다.

- 웹 포털: https://korean-mock-saas-dri5akvbzq-du.a.run.app/
- WorkWeek MCP: `https://korean-mock-saas-dri5akvbzq-du.a.run.app/work-week/mcp`
- ServiceImmediately MCP: `https://korean-mock-saas-dri5akvbzq-du.a.run.app/service-immediately/mcp`
