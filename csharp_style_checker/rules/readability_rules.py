# -*- coding: utf-8 -*-

"""可读性相关的规则实现"""

from typing import List
from csharp_style_checker.rules.base_rule import BaseRule
from csharp_style_checker.models.code_issue import CodeIssue


class LineIsTooLongRule(BaseRule):
    """检查行长度是否过长"""

    def __init__(self, max_length=100):
        super().__init__(
            rule_id="CS0005",
            name="LineTooLong",
            description=f"行长度不应超过{max_length}个字符",
            category="readability",
            severity="info"
        )
        self.max_length = max_length

    def analyze(self, lines: List[str], source_code: str, file_path: str) -> List[CodeIssue]:
        issues = []

        for i, line in enumerate(lines):
            if len(line) > self.max_length:
                issues.append(CodeIssue(
                    line=i + 1,
                    column=self.max_length + 1,
                    message=f"行长度过长 ({len(line)} 字符，最大建议为 {self.max_length})",
                    rule_id=self.rule_id,
                    severity=self.severity,
                    file_path=file_path
                ))

        return issues

