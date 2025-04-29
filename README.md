# C# 代码风格检查工具

![版本](https://img.shields.io/badge/%E7%89%88%E6%9C%AC-1.0.0-blue.svg)
![许可](https://img.shields.io/badge/%E8%AE%B8%E5%8F%AF-MIT-green.svg)
![Python](https://img.shields.io/badge/Python-3.6+-yellow.svg)

一个强大、可扩展的C#代码风格检查工具，用于检查代码是否符合规范并生成详细的HTML报告。该工具可以帮助团队保持代码风格一致性，提高代码质量和可维护性。

## 功能特点

- **多规则支持**：内置多种代码风格检查规则
- **详细报告**：生成美观的HTML格式报告，包含问题摘要和详细代码预览
- **高度可扩展**：简单的插件式架构，易于添加新规则
- **灵活配置**：支持检查单个文件或整个目录
- **多级别问题**：区分错误(error)、警告(warning)和建议(info)

## 支持的规则

## 本工具目前支持以下代码风格规则检查：

|            规则ID            |           规则名称           |                      描述                      | 严重级别 |
| :--------------------------: | :--------------------------: | :--------------------------------------------: | :------: |
|    **命名规则 (Naming)**     |                              |                                                |          |
|            CSN001            |     ClassNamePascalCase      |          类名应该使用PascalCase命名法          |   警告   |
|            CSN002            |   InterfaceNameStartsWithI   |  接口名称必须以'I'开头并遵循PascalCase命名法   |   警告   |
|            CSN003            |    StructNameStartsWithSt    | 结构体名称必须以'st'开头并遵循PascalCase命名法 |   警告   |
|            CSN004            |     MethodNamePascalCase     |         方法名应该使用PascalCase命名法         |   警告   |
|            CSN005            | PrivateFieldUnderscorePrefix |           私有字段应该使用下划线前缀           |   警告   |
|            CSN006            |      StaticFieldNaming       |   静态字段应该使用s_+[类型缩写]+变量名称格式   |   警告   |
|            CSN007            |     ConstantNameAllCaps      |     常量名应该全部大写并使用下划线分隔单词     |   警告   |
|            CSN008            |      VariableCamelCase       |        局部变量应该使用camelCase命名法         |   警告   |
|            CSN009            |    CollectionPluralNaming    |        集合类型变量的命名应使用复数形式        |   提示   |
|   **结构规则 (Structure)**   |                              |                                                |          |
|            CSS001            |        BraceOnNewLine        |       开括号应该放在新行上（Allman风格）       |   警告   |
| **可读性规则 (Readability)** |                              |                                                |          |
|            CSR001            |         LineTooLong          |            行长度不应超过指定字符数            |   提示   |

## 示例

[示例代码](example/StyleRulesTest.cs)

[示例结果](https://simalaoshi.github.io/csharp_style_checker/example/csharp_style_report.html)

