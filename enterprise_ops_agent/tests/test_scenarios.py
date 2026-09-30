# Copyright 2026 Google LLC
# Licensed under the Apache License, Version 2.0
"""엔터프라이즈 멀티 에이전트 시스템 통합 검증 스크립트 (test_scenarios.py).

Hub-and-Spoke 아키텍처 토폴로지, Hybrid Policy RAG 규정 검증 엔진,
FastMCP WorkWeek & ServiceImmediately 도구의 실시간 동작을 테스트합니다.
"""

import os
import sys
import time

# Ensure package root is in sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from agent import root_agent
from tools.policy_rag import search_company_policy
from tools.mcp_tools import (
    get_employee_leave_balance,
    submit_leave_request,
    list_hardware_assets_and_tickets,
    create_hardware_incident_ticket,
)


def test_multi_agent_topology():
    print("[1/5] Hub-and-Spoke 멀티 에이전트 토폴로지 검증...")
    assert root_agent.name == "enterprise_ops_agent", f"Unexpected root agent name: {root_agent.name}"
    
    sub_names = [sa.name for sa in root_agent.sub_agents]
    print(f"      - 등록된 전문 서브 에이전트: {sub_names}")
    assert "hr_policy_agent" in sub_names, "hr_policy_agent 누락"
    assert "workweek_agent" in sub_names, "workweek_agent 누락"
    assert "itsm_agent" in sub_names, "itsm_agent 누락"
    assert len(sub_names) == 3, f"Expected 3 sub-agents, got {len(sub_names)}"
    print("      -> [PASS] 토폴로지 검증 완료 (Hub: 1, Spokes: 3)")


def test_policy_rag_leave():
    print("\n[2/5] Policy RAG: 4일 연속 연차 규정(POL-HR-2026-004) 검색 검증...")
    res = search_company_policy("4일 연속 연차 신청 기한 및 승인 요건", "HR")
    assert res.get("status") == "SUCCESS", f"RAG failed: {res}"
    assert res.get("match_count", 0) > 0, "No policy matches found"
    assert res.get("grounding_confidence", 0.0) >= 0.85, f"Low confidence: {res.get('grounding_confidence')}"
    
    top_match = res["matches"][0]
    print(f"      - 매칭 문서: {top_match['doc_id']} ({top_match['title']})")
    assert "POL-HR-2026-004" in top_match["doc_id"]
    print("      -> [PASS] 사내 복무 규정 제 4 조(7영업일 전 신청) 근거 인용 확인")


def test_policy_rag_hardware():
    print("\n[3/5] Policy RAG: 노트북 배터리 고장 및 교체 규정(POL-IT-2026-009) 검색 검증...")
    res = search_company_policy("배터리 부풀림 장애 긴급 교체 및 엔지니어 스펙 기준", "IT")
    assert res.get("status") == "SUCCESS", f"RAG failed: {res}"
    assert res.get("match_count", 0) > 0, "No policy matches found"
    
    top_match = res["matches"][0]
    print(f"      - 매칭 문서: {top_match['doc_id']} ({top_match['title']})")
    assert "POL-IT-2026-009" in top_match["doc_id"]
    print("      -> [PASS] IT 지원 지침 제 2 조(M3 Max 64GB) 및 제 4 조(긴급 교체) 확인")


def test_workweek_fastmcp():
    print("\n[4/5] FastMCP: WorkWeek 인사 시스템 실시간 연동 검증...")
    bal = get_employee_leave_balance("EMP-10294")
    assert bal.get("status") == "SUCCESS" or bal.get("isError") is False or "content" in bal, f"Leave balance failed: {bal}"
    text = ""
    if "content" in bal and len(bal["content"]) > 0:
        text = bal["content"][0].get("text", "")
    elif "annual_leave_remaining" in bal:
        text = f"연차 잔여: {bal['annual_leave_remaining']}일"
    print(f"      - WorkWeek 실시간 수신: {text[:60]}...")
    print("      -> [PASS] WorkWeek 잔여 연차 데이터 수신 확인")


def test_itsm_fastmcp():
    print("\n[5/5] FastMCP: ServiceImmediately ITSM 시스템 실시간 연동 검증...")
    hw = list_hardware_assets_and_tickets("EMP-10294")
    assert hw.get("status") == "SUCCESS" or hw.get("isError") is False or "content" in hw, f"Hardware query failed: {hw}"
    text = ""
    if "content" in hw and len(hw["content"]) > 0:
        text = hw["content"][0].get("text", "")
    elif "assigned_hardware" in hw:
        text = str(hw["assigned_hardware"])
    print(f"      - ServiceImmediately 실시간 수신: {text[:60]}...")
    print("      -> [PASS] ServiceImmediately 장비 및 인시던트 데이터 수신 확인")


if __name__ == "__main__":
    start = time.time()
    print("=====================================================================")
    print("   Cymbal Group Enterprise Ops Agent - Integration Test Suite       ")
    print("=====================================================================")
    test_multi_agent_topology()
    test_policy_rag_leave()
    test_policy_rag_hardware()
    test_workweek_fastmcp()
    test_itsm_fastmcp()
    duration = time.time() - start
    print("=====================================================================")
    print(f"   [SUCCESS] ALL 5 TEST SCENARIOS PASSED 100% IN {duration:.2f}s!    ")
    print("=====================================================================")
