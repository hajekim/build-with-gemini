# Build with Gemini: AI Advanced 핸즈온 워크숍

본 저장소는 **Build with Gemini** 이벤트의 실습 참가자(150명)를 위한 공식 핸즈온 가이드 및 에셋 저장소입니다.

**Google Antigravity 2.0**(`agy`)과 **Google Agent Development Kit 2.0**(`google-adk`), **Model Context Protocol(FastMCP)**, **사내 규정 RAG**를 결합하여 실제 엔터프라이즈 환경에서 동작하는 멀티 툴 AI 에이전트를 구축합니다.

---

## 🌐 공식 핸즈온 가이드 웹사이트 (Cloud Run)

실습생들은 브라우저에서 아래 Cloud Run 전용 웹사이트를 열어 Qwiklabs 환경 접속부터 단계별 가이드, 원클릭 프롬프트 복사 기능을 활용할 수 있습니다.

🚀 **[공식 핸즈온 가이드 웹사이트 열기 (Google Cloud Run)](https://build-with-gemini-guide-330751298968.asia-northeast3.run.app/)**  
*(도메인 주소: [build.geap.dev](https://build.geap.dev/))*

---

## ⚡ 빠른 시작 (Quick Start)

실습 가상 머신(VM) 또는 터미널 환경에서 아래 명령어를 실행하여 실습 에셋을 즉시 워크스페이스에 복제합니다:

```bash
git clone https://github.com/hajekim/build-with-gemini.git
cd build-with-gemini
```

---

## 📂 저장소 구조 (Repository Structure)

```
build-with-gemini/
├── README.md                      # 워크숍 개요 및 웹사이트 안내
├── index.html                     # 웹 기반 인터랙티브 실습 가이드 (GitHub Pages)
├── docs/
│   ├── SDD.md                     # 소프트웨어 설계서 (아키텍처, RAG 규격, FastMCP API 명세)
│   └── policies/                  # 사내 규정 원본 PDF 문서
│       ├── leave_policy_2026.pdf           # 사내 복무 규정: 연차 및 병가 운영 지침 (POL-HR-2026-004)
│       └── it_hardware_guidelines.pdf     # 사내 IT 자산 운용 지침: PC 및 하드웨어 지원 (POL-IT-2026-009)
└── lab1/
    ├── README.md                  # 실습 1 상세 가이드 (INSTRUCTION)
    └── images/                    # 실습 설명용 고해상도 스크린샷 에셋
        ├── agent_architecture.png          # ADK 2.0 엔터프라이즈 에이전트 구성도
        ├── agy_terminal_session.png        # Antigravity CLI (agy) 실행 화면
        ├── mock_saas_workweek.png          # WorkWeek HRMS 웹 대시보드
        ├── mock_saas_mcp_modal.png         # 개인 MCP 토큰 발급 팝업
        ├── mock_saas_serviceimmediately.png # ServiceImmediately ITMS 대시보드
        ├── scenario_leave_result.png       # 시나리오 1: 4일 연속 연차 검증 결과
        └── scenario_hardware_result.png    # 시나리오 2: 긴급 노트북 교체 검증 결과
```

---

## 🧭 실습 커리큘럼 (Curriculum)

| 실습 | 제목 | 주요 실습 내용 | 가이드 링크 |
|:---|:---|:---|:---|
| **실습 1** | Antigravity 2.0 및 ADK 2.0 기반 엔터프라이즈 멀티 툴 AI 에이전트 구축 | `docs/SDD.md` 기반 프롬프트 주도 개발, `agents-cli` 설정, ADK 2.0 에이전트 뼈대 생성, 사내 규정 PDF RAG 도구 연동, Korean Mock SaaS FastMCP 연동 및 오케스트레이션 검증 | [실습 1 가이드](./lab1/README.md) |
| **실습 2** | (예정) 엔터프라이즈 보안 강화 및 Gemini Enterprise A2A 배포 | Model Garden 보안 가드레일, Agent Gateway 연동, Zero-Trust 보안 및 Gemini Enterprise 배포용 A2A(Agent-to-Agent) 구성 | 추후 공개 예정 |

---

## 🔗 실습용 외부 서비스

- **한국형 Mock SaaS 웹 포털**: https://korean-mock-saas-330751298968.asia-northeast3.run.app/
- **WorkWeek HRMS FastMCP 엔드포인트**: `https://korean-mock-saas-330751298968.asia-northeast3.run.app/work-week/mcp`
- **ServiceImmediately ITMS FastMCP 엔드포인트**: `https://korean-mock-saas-330751298968.asia-northeast3.run.app/service-immediately/mcp`
