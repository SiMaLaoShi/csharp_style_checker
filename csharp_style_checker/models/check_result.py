# -*- coding: utf-8 -*-

"""检查结果模型定义"""

import time


class CheckResult:
    """检查结果模型"""

    def __init__(self):
        """初始化检查结果"""
        self.checked_at = time.time()
        self.total_files = 0
        self.total_issues = 0
        self.error_count = 0
        self.warning_count = 0
        self.info_count = 0
        self.code_files = []

