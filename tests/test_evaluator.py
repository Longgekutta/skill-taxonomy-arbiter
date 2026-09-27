#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
tests/test_evaluator.py: Unit tests for skill-taxonomy-arbiter helper scripts.
"""
import unittest
import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(BASE_DIR, "scripts"))

from interactive_evaluator import evaluate_idea


class TestSkillEvaluator(unittest.TestCase):

    def test_evaluate_skill_concept(self):
        res = evaluate_idea("AI智能体提示词工作流与markdown操作规范SOP")
        self.assertEqual(res["archetype"], "skill")
        self.assertEqual(res["recommended_prefix"], "skill-")

    def test_evaluate_tool_concept(self):
        res = evaluate_idea("无状态一次性命令行装具，输入参数秒级退出，符合UCFS五动词")
        self.assertEqual(res["archetype"], "tool")
        self.assertEqual(res["recommended_prefix"], "tool-")


if __name__ == "__main__":
    unittest.main()
