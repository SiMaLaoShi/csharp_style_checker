# -*- coding: utf-8 -*-

"""结构相关的规则实现"""

import re
from typing import List
from csharp_style_checker.rules.base_rule import BaseRule
from csharp_style_checker.models.code_issue import CodeIssue


class BraceOnNewLineRule(BaseRule):
    """检查花括号是否在新行"""

    def __init__(self):
        super().__init__(
            rule_id="CS0004",
            name="BraceOnNewLine",
            description="开括号应该放在新行上（Allman风格）",
            category="structure",
            severity="warning"
        )

    def analyze(self, lines: List[str], source_code: str, file_path: str) -> List[CodeIssue]:
        issues = []

        # 检查方法、类、命名空间等后面的花括号是否在同一行
        keywords = ["class", "namespace", "if", "for", "foreach", "while", "do", "switch", "try", "catch", "finally",
                    "using"]

        for i, line in enumerate(lines):
            line = line.strip()

            for keyword in keywords:
                # 匹配形如"keyword ... {"的模式
                if re.search(r'\b' + keyword + r'\b.*{.*$', line):
                    # 确保这不是多行语句的结束
                    if not line.startswith("{"):
                        issues.append(CodeIssue(
                            line=i + 1,
                            column=line.find('{') + 1,
                            message=f"'{keyword}' 的开括号应该放在新行",
                            rule_id=self.rule_id,
                            severity=self.severity,
                            file_path=file_path
                        ))

        return issues

