# 행사 전 점검 (강사용)

행사 1~2일 전에 실행합니다. 버전은 다음과 같이 고정되어 있습니다.

| 경로 | 고정 방식 | 설치되는 google-adk |
|:---|:---|:---|
| 실습 1 기본 경로 | 실습 1 Task 1 1단계에서 `google-agents-cli==1.8.0` 설치. 이 버전의 `agents-cli create`가 만드는 `uv.lock`이 버전을 고정 | 2.9.2 |
| 실습 2 5.3 이후 | `rm -f uv.lock` 대신 `uv lock`으로 다시 잠가 기존 버전 유지 | 2.9.2 |
| 완성본 zip (체크포인트) | `pyproject.toml`의 범위 `>=2.9.2,<=2.11.0`. lock 파일 없음 | 범위 안에서 해석 (2026-10-02 확인: 실습 1 zip 2.9.2, 실습 2 zip 2.11.0) |

2.9.2와 2.11.0은 2026-10-02에 실습 1 흐름으로 확인한 버전입니다. 버전이 고정되어 있어도 모델, API, Mock SaaS는 바뀔 수 있으므로, 고정한 버전으로 실습 1의 핵심 흐름이 그대로 동작하는지 15분 안에 확인합니다.

## 준비

- 실습 환경과 같은 Debian 12 VM 1대 (gcloud 로그인, ADC 설정, 실습 1 시작 준비의 API 활성화 완료)
- Mock SaaS 포털에서 발급한 MCP 토큰 1개

## 절차

1. 실습 1 Task 1 1단계 블록을 그대로 실행하고 `agents-cli --version`을 확인합니다.
2. Task 4 1단계 명령으로 토큰을 `~/lab.env`에 저장합니다.
3. 완성본으로 프로젝트를 만들고 통합 테스트를 실행합니다.

```bash
cd ~
curl -fsSL https://raw.githubusercontent.com/hajekim/build-with-gemini/main/lab1/enterprise_ops_agent_completed.zip -o eoa.zip
unzip -oq eoa.zip && cd enterprise-ops-agent && agents-cli install
source ~/lab.env
uv run python3 -c "import importlib.metadata as m; print('google-adk', m.version('google-adk'))"
uv run python3 tests/test_scenarios.py
```

4. 실습 1 Task 5 4단계의 `agents-cli run` 질의를 실행합니다.
5. 실습 1 Task 5 8단계대로 `agents-cli playground --port 8085`를 실행하고 시나리오 2를 보냅니다. VM에 브라우저가 없으면 Cloudtop에서 IAP 터널로 엽니다.

```bash
gcloud compute ssh <VM> --zone <ZONE> --tunnel-through-iap -- -N -L 8085:localhost:8085
```

## 통과 기준

| 항목 | 기준 |
|:---|:---|
| 설치 | `agents-cli, version ...` 출력, `ERROR` 줄 없음 |
| 통합 테스트 | `ALL 5 TEST SCENARIOS PASSED` |
| `agents-cli run` | `transfer_to_agent`에 이어 `search_company_policy` 호출, 규정 조항 포함 답변 |
| playground | 터미널 텔레메트리 질문 후 기동, 화면에 Events/Traces와 Type a message..., 이벤트 순서 `search_company_policy`가 `list_tickets`, `create_ticket`보다 먼저 |

## 실패하면

- 기록할 것: `google-adk` 버전, 실패한 항목, 오류 전문
- 화면 이름만 달라졌으면 실습 1 Task 5 8단계 문구와 스크린샷을 고칩니다.
- 테스트나 실행이 실패하면 원인이 버전인지 먼저 확인합니다. 버전을 바꿔야 하면 세 곳을 함께 고칩니다: 실습 1 Task 1 1단계 pip 줄(`google-agents-cli`, `google-adk`), 완성본 zip 두 개의 `pyproject.toml` 범위, 이 문서의 표. agents-cli를 올리면 새 버전이 만드는 `uv.lock`의 google-adk 버전을 확인합니다.

## 기록

| 날짜 | google-adk | agents-cli | 결과 |
|:---|:---|:---|:---|
| 2026-10-02 | 2.9.2, 2.11.0 | 1.8.0 | 통과 (두 버전 모두 playground 화면과 호출 순서 동일) |

## 콘솔에서 사람이 확인할 항목

2026-10-02 VM 점검(agy CLI, 헤드리스)에서 확인하지 못한 단계입니다. 행사 전에 콘솔과 브라우저로 한 번 따라 해 봅니다.

- 실습 1 시작 준비의 Antigravity 2.0 앱 경로, 원격 브라우저
- 실습 2 2.5 GE 앱 만들기, 라이선스 할당, 웹 앱 URL
- 실습 2 3.2 `/skills` 화면
- 실습 2 9.2 등록 성공, 9.3 Preview, 9.4/9.5 GE 웹 앱 대화

실습 2 4.4, 5.7, 9.2의 좁힌 프롬프트는 같은 날 각 1회씩 측정했습니다(지정 명령만 실행, 실패 시 멈춤 확인). 5.7은 첫 배포가 아니라 같은 엔진 재배포로 측정했습니다. 모델이나 agy 버전이 바뀌면 다시 확인합니다.
