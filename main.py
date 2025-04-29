#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
C# 代码风格检查工具
直接读取指定的C#文件或目录，检查代码风格问题并生成HTML报告
"""

import os
import sys
from csharp_style_checker.core.style_checker import StyleChecker
from csharp_style_checker.reporters.html_reporter import HtmlReporter


def main():
    """主程序入口"""
    if len(sys.argv) < 2:
        print("用法: python main.py <文件或目录路径> [输出报告路径]")
        return 1

    path = sys.argv[1]
    output = sys.argv[2] if len(sys.argv) > 2 else "csharp_style_report.html"
    try:
        # 初始化检查器
        checker = StyleChecker()

        # 执行检查
        if os.path.isfile(path):
            print(f"正在检查文件: {path}")
            result = checker.check_files([path])
        else:
            print(f"正在检查目录: {path}")
            result = checker.check_directory(path)

        # 生成报告
        reporter = HtmlReporter()
        reporter.generate_report(result, output)

        # 输出摘要
        print("\n检查摘要:")
        print(f"检查完成! 共检查 {result.total_files} 个文件，发现 {result.total_issues} 个问题.")
        print(f"错误: {result.error_count}, 警告: {result.warning_count}, 提示: {result.info_count}")
        print(f"HTML报告已生成: {os.path.abspath(output)}")

        return 0
    except Exception as e:
        print(f"错误: {str(e)}")
        return 1


if __name__ == "__main__":
    sys.exit(main())

