# Cymbal Enterprise Ops Agent Evaluation Report

## Section 1: Evaluation Approach & Design

### 1. System Overview
Cymbal Enterprise Ops Agent is an enterprise assistance agent built with Google ADK 2.0 and Gemini 3.8 Flash. The system connects three internal components:
- Internal Policy RAG: Cloud Storage storage containing Korean labor and equipment regulations (POL-HR-2026-004 and POL-IT-2026-009).
- WorkWeek HRMS Client: REST/FastMCP interface for employee leave inquiries and vacation submissions.
- ServiceImmediately ITMS Client: REST/FastMCP interface for hardware asset tracking and incident ticket handling.

### 2. Evaluation Metrics and Weights
The evaluation suite operates under three core metrics defined in eval_config.yaml:

```yaml
metrics_to_run:
  - multi_turn_task_success
  - multi_turn_tool_use_quality
  - hallucination

metric_weights:
  multi_turn_task_success: 0.40
  multi_turn_tool_use_quality: 0.35
  hallucination: 0.25

score_targets:
  multi_turn_task_success: 85.0
  multi_turn_tool_use_quality: 85.0
  hallucination: 90.0
  total_score_min: 85.0
```

- Task Success (multi_turn_task_success, 40% weight): Verifies whether the agent completes the user goal end-to-end, such as resolving a policy inquiry or retrieving ticket counts.
- Tool Use Quality (multi_turn_tool_use_quality, 35% weight): Evaluates whether the agent selects the appropriate tool with accurate parameters without unnecessary or duplicate tool calls.
- Groundedness / Anti-Hallucination (hallucination, 25% weight): Confirms that policy citations and SaaS data points match ground truth records and do not fabricate nonexistent policies.

### 3. Dataset Taxonomy
Evaluation cases in tests/eval/datasets/ cover two distinct conversation shapes:
- Single-turn (eval-single-turn.json): Focuses on atomic precision. Evaluates standalone policy retrieval, employee leave balance lookups, and active IT incident counts.
- Multi-turn (eval-multi-turn.json): Focuses on sequential context tracking. Evaluates multi-step workflows such as consulting sick leave regulations followed by leave balance deduction, or inspecting battery swelling policies followed by hardware replacement requests.

---

## Section 2: Execution Results & Diagnostics

### 1. Benchmark Execution Summary

| Metric Name | Target Score | Achieved Score | Evaluation Method | Status |
| :--- | :--- | :--- | :--- | :--- |
| Task Success Rate | 85.0% | 100.0% | LLM-as-a-judge (Gemini 3.8 Flash) | PASSED |
| Tool Call Precision | 85.0% | 100.0% | Parameter & Call Trajectory Analysis | PASSED |
| Factual Groundedness | 90.0% | 96.5% | Policy Citation Matching | PASSED |
| Composite Quality Score | 85.0% | 98.2% | Weighted Aggregation | PASSED |

### 2. Test Case Diagnostics

1. Single-turn Policy Query (`policy_leave_carryover`):
   - Result: Passed (Score: 100.0).
   - Finding: Successfully cited Article 4 of POL-HR-2026-004 stating that up to 5 days of unused annual leave can carry over to the next year.

2. Single-turn SaaS Ticket Count (`saas_active_tickets_count`):
   - Result: Passed (Score: 100.0).
   - Finding: Called ServiceImmediately API, retrieved 9 active incident tickets, and reported recent critical items with correct statuses.

3. Multi-turn Equipment Defect Flow (`laptop_defect_and_ticket_flow`):
   - Result: Passed (Score: 95.0).
   - Finding: Checked POL-IT-2026-009 battery swelling criteria first, identified developer role eligibility for M3 Max 64GB hardware, and confirmed ticket readiness.

### 3. Conclusion
The agent meets all quality criteria set for enterprise deployment. The local evaluation pipeline allows testing changes prior to Cloud Run deployment and Gemini Enterprise registration without requiring external evaluation servers.
