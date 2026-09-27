#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
scripts/interactive_evaluator.py: Auxiliary evaluation script for skill-taxonomy-arbiter.
Provides a structured questionnaire or passes natural language ideas to the underlying arbiter.
"""
import sys
import os
import subprocess
import json

ARBITER_CLI = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), "tool-taxonomy-arbiter", "main.py")


def evaluate_idea(idea_text: str) -> dict:
    if not os.path.exists(ARBITER_CLI):
        raise FileNotFoundError(f"Underlying arbiter CLI not found: {ARBITER_CLI}")

    cmd = [sys.executable, ARBITER_CLI, "run", "--idea", idea_text, "--json"]
    proc = subprocess.run(cmd, capture_output=True, text=True, check=True)
    return json.loads(proc.stdout)


def evaluate_path(target_path: str) -> dict:
    if not os.path.exists(ARBITER_CLI):
        raise FileNotFoundError(f"Underlying arbiter CLI not found: {ARBITER_CLI}")

    cmd = [sys.executable, ARBITER_CLI, "run", "--path", target_path, "--json"]
    proc = subprocess.run(cmd, capture_output=True, text=True, check=True)
    return json.loads(proc.stdout)


def interactive_questionnaire():
    print("=" * 60)
    print(" 🎯 软件架构形态 5 项核心自问测试 (Interactive Questionnaire)")
    print("=" * 60)
    q1 = input("1. 该构思是否需要后台长驻守护进程并监听网络端口 (HTTP/WS)? [y/N]: ").strip().lower() == "y"
    q2 = input("2. 是否属于 Model Context Protocol (MCP) 标准工具暴露? [y/N]: ").strip().lower() == "y"
    q3 = input("3. 核心载体是 AI Agent 的认知提示词流程 (SOP)，还是二进制机器代码? [sop/code]: ").strip().lower()
    q4 = input("4. 是否属于绝对负向安全红线或合规验收契约 (Rule/Spec)? [rule/spec/none]: ").strip().lower()
    q5 = input("5. 是否包含独立的前端 GUI、移动端 APK 或端到端业务机器人? [y/N]: ").strip().lower() == "y"

    parts = []
    if q1: parts.append("常驻后台守护进程并监听端口")
    else: parts.append("极速一次性命令行装具，退出后不留常驻进程")

    if q2: parts.append("实现Model Context Protocol标准协议")
    if q3 == "sop": parts.append("AI智能体SOP认知提示词工作流与markdown规范")
    else: parts.append("原生编译解释机器代码与算法实现")

    if q4 == "rule": parts.append("负向行为红线与边界拦截防御规则")
    elif q4 == "spec": parts.append("刚性规范标准与验收神谕RFC契约")

    if q5: parts.append("包含端到端GUI客户端或移动APK应用")

    combined = "，".join(parts)
    print(f"\n[*] 组装评估向量描述: {combined}\n")
    res = evaluate_idea(combined)
    print(json.dumps(res, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    if len(sys.argv) > 1:
        arg = sys.argv[1]
        if os.path.exists(arg):
            print(json.dumps(evaluate_path(arg), ensure_ascii=False, indent=2))
        else:
            print(json.dumps(evaluate_idea(" ".join(sys.argv[1:])), ensure_ascii=False, indent=2))
    else:
        interactive_questionnaire()
