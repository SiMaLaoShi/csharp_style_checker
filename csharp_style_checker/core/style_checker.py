# -*- coding: utf-8 -*-

"""C# 代码风格检查器核心实现"""

import os
from typing import List

from csharp_style_checker.models.code_file import CodeFile
from csharp_style_checker.models.check_result import CheckResult
from csharp_style_checker.models.code_issue import CodeIssue
from csharp_style_checker.rules.naming_rules import (
    ClassNamePascalCaseRule,
    PrivateFieldUnderscoreRule,
    MethodNamePascalCaseRule, ConstantNameAllCapsRule, InterfaceNamingRule, StructNamingRule, StaticFieldNamingRule,
    CollectionPluralNamingRule
)
from csharp_style_checker.rules.structure_rules import BraceOnNewLineRule
from csharp_style_checker.rules.readability_rules import LineIsTooLongRule


class StyleChecker:
    """C# 代码风格检查器"""

    def __init__(self):
        """初始化检查器"""
        self.rules = [
            ClassNamePascalCaseRule(),
            PrivateFieldUnderscoreRule(),
            MethodNamePascalCaseRule(),
            BraceOnNewLineRule(),
            LineIsTooLongRule(200),
            ConstantNameAllCapsRule(),
            InterfaceNamingRule(),
            StructNamingRule(),
            StaticFieldNamingRule(),
            CollectionPluralNamingRule(),
        ]
        self.file_extensions = ['.cs']

    def check_directory(self, directory_path: str) -> CheckResult:
        """检查目录下的所有C#文件"""
        if not os.path.exists(directory_path):
            raise FileNotFoundError(f"目录不存在: {directory_path}")

        # 查找所有C#文件
        file_paths = []
        for root, _, files in os.walk(directory_path):
            for file in files:
                if any(file.endswith(ext) for ext in self.file_extensions):
                    file_paths.append(os.path.join(root, file))

        return self.check_files(file_paths)

    def check_files(self, file_paths: List[str]) -> CheckResult:
        """检查指定的C#文件列表"""
        result = CheckResult()
        result.total_files = len(file_paths)

        for file_path in file_paths:
            try:
                file_result = self.check_file(file_path)
                result.code_files.append(file_result)
                result.total_issues += len(file_result.issues)

                # 更新问题统计
                result.error_count += file_result.error_count()
                result.warning_count += file_result.warning_count()
                result.info_count += file_result.info_count()

            except Exception as e:
                print(f"检查文件出错: {file_path}, 错误: {str(e)}")

                # 记录解析失败的文件
                error_file = CodeFile(
                    file_path=file_path,
                    file_name=os.path.basename(file_path)
                )
                error_file.issues = [
                    CodeIssue(
                        line=0,
                        column=0,
                        message=f"文件解析失败: {str(e)}",
                        rule_id="PARSE_ERROR",
                        severity="error"
                    )
                ]

                result.code_files.append(error_file)
                result.total_issues += 1
                result.error_count += 1

        return result

    def check_file(self, file_path: str) -> CodeFile:
        """检查单个C#文件"""
        with open(file_path, 'r', encoding='utf-8') as f:
            code = f.read()

        code_file = CodeFile(
            file_path=file_path,
            file_name=os.path.basename(file_path),
            file_content=code
        )

        try:
            # 将代码拆分为行
            lines = code.splitlines()

            # 应用每条规则
            for rule in self.rules:
                if rule.is_enabled:
                    rule_issues = rule.analyze(lines, code, file_path)
                    code_file.issues.extend(rule_issues)

        except Exception as e:
            # 捕获处理错误
            code_file.issues = [
                CodeIssue(
                    line=0,
                    column=0,
                    message=f"分析错误: {str(e)}",
                    rule_id="ANALYSIS_ERROR",
                    severity="error"
                )
            ]

        return code_file

