# -*- coding: utf-8 -*-

"""代码问题模型定义"""

class CodeIssue:
    """代码问题模型"""

    def __init__(self, line=0, column=0, message="", rule_id="", severity="info", file_path=None):
        """初始化代码问题"""
        self.line = line
        self.column = column
        self.message = message
        self.rule_id = rule_id
        self.severity = severity
        self.file_path = file_path

