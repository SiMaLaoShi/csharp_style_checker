# -*- coding: utf-8 -*-

"""HTML报告生成器"""

import time
import os
from csharp_style_checker.models.check_result import CheckResult


class HtmlReporter:
    """HTML报告生成器"""

    def generate_report(self, result: CheckResult, output_path: str):
        """生成HTML报告"""
        html = self._get_html_template()

        # 基本信息
        report_date = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(result.checked_at))
        html = html.replace('{{REPORT_DATE}}', report_date)
        html = html.replace('{{TOTAL_FILES}}', str(result.total_files))
        html = html.replace('{{TOTAL_ISSUES}}', str(result.total_issues))
        html = html.replace('{{ERROR_COUNT}}', str(result.error_count))
        html = html.replace('{{WARNING_COUNT}}', str(result.warning_count))
        html = html.replace('{{INFO_COUNT}}', str(result.info_count))

        # 生成文件摘要表格
        file_summary = []
        for code_file in sorted(result.code_files, key=lambda f: len(f.issues), reverse=True):
            error_count = code_file.error_count()
            warning_count = code_file.warning_count()
            info_count = code_file.info_count()

            if error_count > 0:
                row_class = "error-row"
            elif warning_count > 0:
                row_class = "warning-row"
            elif info_count > 0:
                row_class = "info-row"
            else:
                row_class = "clean-row"

            file_hash = hash(code_file.file_path)

            file_summary.append(f'<tr class="{row_class}">')
            file_summary.append(f'  <td><a href="#file-{file_hash}">{code_file.file_name}</a></td>')
            file_summary.append(f'  <td>{len(code_file.issues)}</td>')
            file_summary.append(f'  <td>{error_count}</td>')
            file_summary.append(f'  <td>{warning_count}</td>')
            file_summary.append(f'  <td>{info_count}</td>')
            file_summary.append('</tr>')

        html = html.replace('{{FILE_SUMMARY}}', '\n'.join(file_summary))

        # 生成详细问题列表
        issue_details = []
        for code_file in result.code_files:
            if not code_file.issues:
                continue

            file_hash = hash(code_file.file_path)

            issue_details.append(f'<div class="file-section" id="file-{file_hash}">')
            issue_details.append(f'  <h3>{code_file.file_name}</h3>')
            issue_details.append(f'  <div class="file-path">{code_file.file_path}</div>')

            # 添加问题表格
            if code_file.issues:
                issue_details.append('  <table class="issues-table">')
                issue_details.append('    <tr><th>行</th><th>列</th><th>规则</th><th>严重性</th><th>消息</th></tr>')

                for issue in sorted(code_file.issues, key=lambda i: (i.line, i.column)):
                    severity_class = issue.severity.lower()
                    issue_details.append(f'    <tr class="{severity_class}-row">')
                    issue_details.append(f'      <td>{issue.line}</td>')
                    issue_details.append(f'      <td>{issue.column}</td>')
                    issue_details.append(f'      <td>{issue.rule_id}</td>')
                    issue_details.append(f'      <td>{issue.severity}</td>')
                    issue_details.append(f'      <td>{issue.message}</td>')
                    issue_details.append('    </tr>')

                issue_details.append('  </table>')

            # 添加代码预览
            if code_file.file_content:
                issue_details.append('  <div class="code-preview">')
                issue_details.append('    <h4>代码预览</h4>')
                issue_details.append('    <pre><code class="csharp">')

                # 处理代码，添加行号
                lines = code_file.file_content.splitlines()
                for i, line in enumerate(lines):
                    line_number = i + 1
                    line_content = self._html_escape(line)

                    # 标记有问题的行
                    issues_on_line = [i for i in code_file.issues if i.line == line_number]
                    if issues_on_line:
                        min_severity = min([i.severity for i in issues_on_line],
                                          key=lambda s: {"info": 2, "warning": 1, "error": 0}[s])
                        line_class = f"line-{min_severity}"
                    else:
                        line_class = ""

                    issue_details.append(
                        f'<span class="line-number">{line_number}</span><span class="{line_class}">{line_content}</span>')

                issue_details.append('    </code></pre>')
                issue_details.append('  </div>')

            issue_details.append('</div>')

        html = html.replace('{{ISSUE_DETAILS}}', '\n'.join(issue_details))

        # 写入文件
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(html)

        print(f"HTML报告已生成: {output_path}")

    def _html_escape(self, text):
        """转义HTML特殊字符"""
        return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;").replace("'",
                                                                                                                 "&#39;")

    def _get_html_template(self):
        """获取HTML模板"""
        # HTML模板太长，这里省略，使用原脚本中的模板
        return """<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>C#代码风格检查报告</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            line-height: 1.6;
            color: #333;
            background-color: #f5f5f5;
        }

        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
        }

        header {
            background-color: #2c3e50;
            color: white;
            padding: 20px;
            border-radius: 5px;
            margin-bottom: 20px;
        }

        h1, h2, h3, h4 {
            margin-bottom: 15px;
        }

        .report-info {
            display: flex;
            justify-content: space-between;
            margin-top: 10px;
        }

        .summary {
            margin-bottom: 30px;
        }

        .summary-cards {
            display: flex;
            justify-content: space-between;
            margin-bottom: 20px;
        }

        .card {
            background-color: white;
            border-radius: 5px;
            padding: 15px;
            width: 23%;
            box-shadow: 0 2px 5px rgba(0,0,0,0.1);
            text-align: center;
        }

        .card-title {
            font-size: 1.1em;
            margin-bottom: 10px;
        }

        .card-value {
            font-size: 2em;
            font-weight: bold;
        }

        .card-total { border-top: 4px solid #3498db; }
        .card-error { border-top: 4px solid #e74c3c; }
        .card-warning { border-top: 4px solid #f39c12; }
        .card-info { border-top: 4px solid #2ecc71; }

        table {
            width: 100%;
            border-collapse: collapse;
            margin-bottom: 20px;
            background-color: white;
            box-shadow: 0 2px 5px rgba(0,0,0,0.1);
        }

        th, td {
            padding: 12px 15px;
            text-align: left;
            border-bottom: 1px solid #ddd;
        }

        th {
            background-color: #f8f9fa;
            font-weight: 600;
        }

        .error-row { background-color: rgba(231, 76, 60, 0.1); }
        .warning-row { background-color: rgba(243, 156, 18, 0.1); }
        .info-row { background-color: rgba(46, 204, 113, 0.1); }

        .file-section {
            background-color: white;
            border-radius: 5px;
            padding: 20px;
            margin-bottom: 20px;
            box-shadow: 0 2px 5px rgba(0,0,0,0.1);
        }

        .file-path {
            color: #777;
            margin-bottom: 15px;
            font-size: 0.9em;
        }

        .issues-table {
            margin-bottom: 20px;
        }

        .code-preview {
            margin-top: 20px;
            padding: 10px;
            background-color: #f8f9fa;
            border-radius: 5px;
            overflow-x: auto;
        }

        pre {
            margin: 0;
            padding: 0;
        }

        code {
            font-family: Consolas, Monaco, 'Andale Mono', monospace;
            font-size: 14px;
            line-height: 1.5;
        }

        .line-number {
            display: inline-block;
            width: 40px;
            color: #999;
            text-align: right;
            padding-right: 10px;
            margin-right: 10px;
            border-right: 1px solid #ddd;
            user-select: none;
        }

        .line-error { background-color: rgba(231, 76, 60, 0.2); }
        .line-warning { background-color: rgba(243, 156, 18, 0.2); }
        .line-info { background-color: rgba(46, 204, 113, 0.2); }

        footer {
            text-align: center;
            margin-top: 50px;
            padding: 20px;
            color: #777;
            border-top: 1px solid #ddd;
        }

        a {
            color: #3498db;
            text-decoration: none;
        }

        a:hover {
            text-decoration: underline;
        }
    </style>
</head>
<body>
    <div class="container">
        <header>
            <h1>C# 代码风格检查报告</h1>
            <div class="report-info">
                <p>生成时间: {{REPORT_DATE}}</p>
                <p>检查文件: {{TOTAL_FILES}} 个</p>
            </div>
        </header>

        <section class="summary">
            <h2>问题摘要</h2>
            <div class="summary-cards">
                <div class="card card-total">
                    <div class="card-title">总问题数</div>
                    <div class="card-value">{{TOTAL_ISSUES}}</div>
                </div>
                <div class="card card-error">
                    <div class="card-title">错误</div>
                    <div class="card-value">{{ERROR_COUNT}}</div>
                </div>
                <div class="card card-warning">
                    <div class="card-title">警告</div>
                    <div class="card-value">{{WARNING_COUNT}}</div>
                </div>
                <div class="card card-info">
                    <div class="card-title">提示</div>
                    <div class="card-value">{{INFO_COUNT}}</div>
                </div>
            </div>

            <h2>文件摘要</h2>
            <table class="summary-table">
                <tr>
                    <th>文件</th>
                    <th>问题数</th>
                    <th>错误</th>
                    <th>警告</th>
                    <th>提示</th>
                </tr>
                {{FILE_SUMMARY}}
            </table>
        </section>

        <section class="details">
            <h2>问题详情</h2>
            {{ISSUE_DETAILS}}
        </section>

        <footer>
            <p>C# 代码风格检查工具 &copy; 2025</p>
        </footer>
    </div>
</body>
</html>"""

