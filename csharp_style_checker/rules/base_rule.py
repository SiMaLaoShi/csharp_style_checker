# -*- coding: utf-8 -*-

"""规则基类定义"""

from typing import List
from csharp_style_checker.models.code_issue import CodeIssue


class BaseRule:
    """规则基类"""

    def __init__(self, rule_id, name, description, category, severity):
        self.rule_id = rule_id
        self.name = name
        self.description = description
        self.category = category
        self.severity = severity
        self.is_enabled = True

    def analyze(self, lines: List[str], source_code: str, file_path: str) -> List[CodeIssue]:
        """分析代码并返回问题列表"""
        return []

