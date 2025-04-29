# -*- coding: utf-8 -*-

"""代码文件模型定义"""

import os
from typing import List, Optional


class CodeFile:
    """代码文件模型"""

    def __init__(self, file_path: str, file_name: Optional[str] = None, file_content: Optional[str] = None):
        """初始化代码文件"""
        self.file_path = file_path
        self.file_name = file_name if file_name else os.path.basename(file_path)
        self.file_content = file_content
        self.issues = []

    def has_issues(self) -> bool:
        """检查是否有问题"""
        return len(self.issues) > 0

    def error_count(self) -> int:
        """获取错误数量"""
        return sum(1 for issue in self.issues if issue.severity == "error")

    def warning_count(self) -> int:
        """获取警告数量"""
        return sum(1 for issue in self.issues if issue.severity == "warning")

    def info_count(self) -> int:
        """获取提示数量"""
        return sum(1 for issue in self.issues if issue.severity == "info")

