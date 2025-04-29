# -*- coding: utf-8 -*-

"""命名相关的规则实现"""

import re
from typing import List
from csharp_style_checker.rules.base_rule import BaseRule
from csharp_style_checker.models.code_issue import CodeIssue


class ClassNamePascalCaseRule(BaseRule):
    """检查类名是否符合PascalCase命名规范"""

    def __init__(self):
        super().__init__(
            rule_id="CS0001",
            name="ClassNamePascalCase",
            description="类名应该使用PascalCase命名法",
            category="naming",
            severity="warning"
        )

    def analyze(self, lines: List[str], source_code: str, file_path: str) -> List[CodeIssue]:
        issues = []

        # 查找类定义
        class_pattern = re.compile(r'(public|private|protected|internal|abstract)?\s+class\s+([a-zA-Z0-9_]+)')

        for i, line in enumerate(lines):
            match = class_pattern.search(line)
            if match:
                class_name = match.group(2)

                # 检查是否符合PascalCase（首字母大写）
                if class_name and not class_name[0].isupper():
                    issues.append(CodeIssue(
                        line=i + 1,
                        column=match.start(2) + 1,
                        message=f"类名 '{class_name}' 应该使用PascalCase命名法（首字母大写）",
                        rule_id=self.rule_id,
                        severity=self.severity,
                        file_path=file_path
                    ))

        return issues


class PrivateFieldUnderscoreRule(BaseRule):
    """检查私有字段是否使用下划线前缀"""

    def __init__(self):
        super().__init__(
            rule_id="CS0002",
            name="PrivateFieldUnderscorePrefix",
            description="私有字段应该使用下划线前缀",
            category="naming",
            severity="warning"
        )

    def analyze(self, lines: List[str], source_code: str, file_path: str) -> List[CodeIssue]:
        issues = []

        # 查找私有字段定义
        field_pattern = re.compile(r'private\s+[a-zA-Z0-9_<>.\[\]]+\s+([a-zA-Z0-9_]+)\s*[;=]')

        for i, line in enumerate(lines):
            match = field_pattern.search(line)
            if match:
                field_name = match.group(1)

                # 检查是否以下划线开头
                if field_name and not field_name.startswith('_'):
                    issues.append(CodeIssue(
                        line=i + 1,
                        column=match.start(1) + 1,
                        message=f"私有字段 '{field_name}' 应该使用下划线前缀",
                        rule_id=self.rule_id,
                        severity=self.severity,
                        file_path=file_path
                    ))

        return issues


class MethodNamePascalCaseRule(BaseRule):
    """检查方法名是否符合PascalCase命名规范"""

    def __init__(self):
        super().__init__(
            rule_id="CS0003",
            name="MethodNamePascalCase",
            description="方法名应该使用PascalCase命名法",
            category="naming",
            severity="warning"
        )

    def analyze(self, lines: List[str], source_code: str, file_path: str) -> List[CodeIssue]:
        issues = []

        # 查找方法定义
        method_pattern = re.compile(
            r'(public|private|protected|internal|static|virtual|override|abstract)?\s+[a-zA-Z0-9_<>.\[\]]+\s+([a-zA-Z0-9_]+)\s*\(')

        for i, line in enumerate(lines):
            match = method_pattern.search(line)
            if match:
                method_name = match.group(2)

                # 跳过构造函数和特殊方法
                if method_name not in ["Dispose", "Main"] and not self._is_constructor(method_name, source_code):
                    # 检查是否符合PascalCase（首字母大写）
                    if method_name and not method_name[0].isupper():
                        issues.append(CodeIssue(
                            line=i + 1,
                            column=match.start(2) + 1,
                            message=f"方法名 '{method_name}' 应该使用PascalCase命名法（首字母大写）",
                            rule_id=self.rule_id,
                            severity=self.severity,
                            file_path=file_path
                        ))

        return issues

    def _is_constructor(self, method_name: str, source_code: str) -> bool:
        """检查方法是否是构造函数"""
        # 简单检查：查找类名与方法名相同的情况
        class_pattern = re.compile(r'class\s+(' + method_name + r')\b')
        return bool(class_pattern.search(source_code))


class VariableCamelCaseRule(BaseRule):
    """检查局部变量是否使用camelCase命名规范"""

    def __init__(self):
        super().__init__(
            rule_id="CS0006",
            name="VariableCamelCase",
            description="局部变量应该使用camelCase命名法",
            category="naming",
            severity="warning"
        )

    def analyze(self, lines: List[str], source_code: str, file_path: str) -> List[CodeIssue]:
        issues = []

        # 查找方法内的变量声明
        # 简化版：查找形如 "TypeName variableName" 的模式
        variable_pattern = re.compile(r'\b([A-Z][a-zA-Z0-9_<>.\[\]]+)\s+([a-zA-Z][a-zA-Z0-9_]*)\s*[;=]')

        for i, line in enumerate(lines):
            # 跳过可能的字段声明
            if re.search(r'\b(public|private|protected|internal)\b', line):
                continue

            # 查找局部变量
            for match in variable_pattern.finditer(line):
                type_name = match.group(1)
                variable_name = match.group(2)

                # 检查是否符合camelCase（首字母小写）
                if variable_name and variable_name[0].isupper():
                    issues.append(CodeIssue(
                        line=i + 1,
                        column=match.start(2) + 1,
                        message=f"变量名 '{variable_name}' 应该使用camelCase命名法（首字母小写）",
                        rule_id=self.rule_id,
                        severity=self.severity,
                        file_path=file_path
                    ))

        return issues


class ConstantNameAllCapsRule(BaseRule):
    """检查常量命名是否全部大写"""

    def __init__(self):
        super().__init__(
            rule_id="CS0006",
            name="ConstantNameAllCaps",
            description="常量名应该全部大写并使用下划线分隔单词",
            category="naming",
            severity="warning"
        )

    def analyze(self, lines: List[str], source_code: str, file_path: str) -> List[CodeIssue]:
        issues = []

        # 查找常量定义 - 包含const关键字的成员
        constant_pattern = re.compile(r'(public|private|protected|internal)\s+const\s+[a-zA-Z0-9_<>.\[\]]+\s+([a-zA-Z0-9_]+)\s*[=;]')

        for i, line in enumerate(lines):
            match = constant_pattern.search(line)
            if match:
                constant_name = match.group(2)

                # 检查是否全部大写 (允许数字和下划线)
                if not re.match(r'^[A-Z0-9_]+$', constant_name):
                    issues.append(CodeIssue(
                        line=i + 1,
                        column=match.start(2) + 1,
                        message=f"常量名 '{constant_name}' 应该全部大写并使用下划线分隔单词",
                        rule_id=self.rule_id,
                        severity=self.severity,
                        file_path=file_path
                    ))

        return issues


class StructNamingRule(BaseRule):
    """检查结构体名称是否以st开头并符合PascalCase命名规范"""

    def __init__(self):
        super().__init__(
            rule_id="CS0009",
            name="StructNameStartsWithSt",
            description="结构体名称必须以'st'开头并遵循PascalCase命名法",
            category="naming",
            severity="warning"
        )

    def analyze(self, lines: List[str], source_code: str, file_path: str) -> List[CodeIssue]:
        issues = []

        # 查找结构体定义
        struct_pattern = re.compile(r'(public|internal|private)?\s+struct\s+([a-zA-Z0-9_]+)')

        for i, line in enumerate(lines):
            match = struct_pattern.search(line)
            if match:
                struct_name = match.group(2)

                # 检查是否以st开头
                if not struct_name.startswith('st'):
                    issues.append(CodeIssue(
                        line=i + 1,
                        column=match.start(2) + 1,
                        message=f"结构体名 '{struct_name}' 必须以'st'开头",
                        rule_id=self.rule_id,
                        severity=self.severity,
                        file_path=file_path
                    ))
                # 检查是否符合PascalCase（st后首字母大写）
                elif len(struct_name) > 2 and not struct_name[2].isupper():
                    issues.append(CodeIssue(
                        line=i + 1,
                        column=match.start(2) + 1,
                        message=f"结构体名 '{struct_name}' 必须遵循PascalCase命名法(st后首字母大写，如stMyStruct)",
                        rule_id=self.rule_id,
                        severity=self.severity,
                        file_path=file_path
                    ))

        return issues


class InterfaceNamingRule(BaseRule):
    """检查接口名称是否以I开头并符合PascalCase命名规范"""

    def __init__(self):
        super().__init__(
            rule_id="CS0007",
            name="InterfaceNameStartsWithI",
            description="接口名称必须以'I'开头并遵循PascalCase命名法",
            category="naming",
            severity="warning"
        )

    def analyze(self, lines: List[str], source_code: str, file_path: str) -> List[CodeIssue]:
        issues = []

        # 查找接口定义
        interface_pattern = re.compile(r'(public|internal)?\s+interface\s+([a-zA-Z0-9_]+)')

        for i, line in enumerate(lines):
            match = interface_pattern.search(line)
            if match:
                interface_name = match.group(2)

                # 检查是否以I开头
                if not interface_name.startswith('I'):
                    issues.append(CodeIssue(
                        line=i + 1,
                        column=match.start(2) + 1,
                        message=f"接口名 '{interface_name}' 必须以'I'开头",
                        rule_id=self.rule_id,
                        severity=self.severity,
                        file_path=file_path
                    ))
                # 检查首字母后的部分是否符合PascalCase
                elif len(interface_name) > 1 and not interface_name[1].isupper():
                    issues.append(CodeIssue(
                        line=i + 1,
                        column=match.start(2) + 1,
                        message=f"接口名 '{interface_name}' 必须遵循PascalCase命名法(I后首字母大写)",
                        rule_id=self.rule_id,
                        severity=self.severity,
                        file_path=file_path
                    ))

        return issues


class StaticFieldNamingRule(BaseRule):
    """检查静态字段命名是否符合 s_+[类型缩写]+变量名称 格式"""

    def __init__(self):
        super().__init__(
            rule_id="CS0010",
            name="StaticFieldNaming",
            description="静态字段应该使用 s_+[类型缩写]+变量名称 格式",
            category="naming",
            severity="warning"
        )
        # 常见类型的缩写映射
        self.type_abbreviations = {
            'int': 'i',
            'long': 'l',
            'float': 'f',
            'double': 'd',
            'bool': 'b',
            'string': 'str',
            'char': 'c',
            'byte': 'b',
            'List': 'lst',
            'Dictionary': 'dict',
            'Array': 'arr',
            'object': 'obj',
            'Vector2': 'v2',
            'Vector3': 'v3',
            'GameObject': 'go',
            'Transform': 'trans',
            # 可以根据项目需要添加更多类型缩写
        }

    def analyze(self, lines: List[str], source_code: str, file_path: str) -> List[CodeIssue]:
        issues = []

        # 查找静态字段定义
        # 匹配 static [类型] [名称] 的模式
        static_field_pattern = re.compile(
            r'(public|private|protected|internal)\s+static\s+([a-zA-Z0-9_<>.\[\]]+)\s+([a-zA-Z0-9_]+)\s*[;=]')

        for i, line in enumerate(lines):
            match = static_field_pattern.search(line)
            if match:
                access = match.group(1)  # 访问修饰符
                type_name = match.group(2)  # 类型
                field_name = match.group(3)  # 字段名

                # 1. 检查是否以s_开头
                if not field_name.startswith('s_'):
                    issues.append(CodeIssue(
                        line=i + 1,
                        column=match.start(3) + 1,
                        message=f"静态字段 '{field_name}' 应该以's_'开头",
                        rule_id=self.rule_id,
                        severity=self.severity,
                        file_path=file_path
                    ))
                    continue

                # 获取类型的基本名称（去除泛型部分和数组符号）
                base_type = re.sub(r'<.*>|\[.*\]', '', type_name).strip()

                # 2. 尝试检查类型缩写
                # 对于常见类型，检查是否包含适当的类型缩写
                if base_type in self.type_abbreviations:
                    expected_prefix = f"s_{self.type_abbreviations[base_type]}"
                    if not field_name.startswith(expected_prefix):
                        issues.append(CodeIssue(
                            line=i + 1,
                            column=match.start(3) + 1,
                            message=f"静态字段 '{field_name}' 应使用格式 's_{self.type_abbreviations[base_type]}变量名'，类型 {base_type} 的建议缩写为 '{self.type_abbreviations[base_type]}'",
                            rule_id=self.rule_id,
                            severity="info",  # 将这部分设为info级别，较为宽松
                            file_path=file_path
                        ))

                # 3. 对于const静态字段，应该使用全大写蛇形命名法而非s_前缀
                if "const" in line:
                    if not re.match(r'^[A-Z0-9_]+$', field_name):
                        issues.append(CodeIssue(
                            line=i + 1,
                            column=match.start(3) + 1,
                            message=f"常量静态字段 '{field_name}' 应该使用全大写加下划线命名法，而非's_'前缀",
                            rule_id=self.rule_id,
                            severity=self.severity,
                            file_path=file_path
                        ))

        return issues


class CollectionPluralNamingRule(BaseRule):
    """检查集合类型的变量名是否使用复数形式"""

    def __init__(self):
        super().__init__(
            rule_id="CS0006",
            name="CollectionPluralNaming",
            description="集合类型(如列表、字典、堆栈等)的变量命名应使用复数形式",
            category="naming",
            severity="info"  # 使用info级别，因为这是建议而非强制
        )

        # 集合类型关键词列表
        self.collection_types = [
            "List", "Dictionary", "HashSet", "Queue", "Stack",
            "Collection", "Set", "Map", "Array", "[]", "IEnumerable",
            "ICollection", "IList", "IDictionary", "HashTable"
        ]

        # 不需要检查复数形式的例外词
        self.exceptions = [
            "data", "status", "canvas", "class", "physics", "graphics", "news",
            "mathematics", "series", "species", "analysis", "media",
            "access", "process", "progress", "success", "bus", "cache"
        ]

    def analyze(self, lines: List[str], source_code: str, file_path: str) -> List[CodeIssue]:
        issues = []

        # 1. 字段声明模式 - 查找包含访问修饰符的字段
        field_pattern = re.compile(
            r'(public|private|protected|internal|static)\s+([a-zA-Z0-9_<>\[\],\s\.]+)\s+([a-zA-Z0-9_]+)\s*[;=]'
        )

        # 2. 属性声明模式
        property_pattern = re.compile(
            r'(public|private|protected|internal)?\s+([a-zA-Z0-9_<>\[\],\s\.]+)\s+([a-zA-Z0-9_]+)\s*\{'
        )

        # 3. 局部变量声明模式 - 简化后不使用后向查找
        local_var_pattern = re.compile(
            r'\b([a-zA-Z0-9_<>\[\],\s\.]+)\s+([a-zA-Z0-9_]+)\s*[;=]'
        )

        # 分析每一行
        for i, line in enumerate(lines):
            # 检查字段声明
            for match in field_pattern.finditer(line):
                type_name = match.group(2).strip()
                var_name = match.group(3)

                if self._is_collection_type(type_name) and not self._is_plural_name(var_name):
                    issues.append(CodeIssue(
                        line=i + 1,
                        column=match.start(3) + 1,
                        message=f"集合类型字段 '{var_name}' 的命名建议使用复数形式",
                        rule_id=self.rule_id,
                        severity=self.severity,
                        file_path=file_path
                    ))

            # 检查属性声明
            for match in property_pattern.finditer(line):
                if match.group(2):  # 确保匹配到了类型
                    type_name = match.group(2).strip()
                    prop_name = match.group(3)

                    if self._is_collection_type(type_name) and not self._is_plural_name(prop_name):
                        issues.append(CodeIssue(
                            line=i + 1,
                            column=match.start(3) + 1,
                            message=f"集合类型属性 '{prop_name}' 的命名建议使用复数形式",
                            rule_id=self.rule_id,
                            severity=self.severity,
                            file_path=file_path
                        ))

            # 检查局部变量声明
            for match in local_var_pattern.finditer(line):
                # 跳过类定义、方法定义、接口定义等
                if "class " in line or "interface " in line or "struct " in line or "enum " in line:
                    continue

                # 跳过包含访问修饰符的行（这些会被前面的模式捕获）
                if re.search(r'\b(public|private|protected|internal|static)\b', line):
                    continue

                type_name = match.group(1).strip()
                var_name = match.group(2)

                # 跳过控制结构和关键字
                if var_name in ["if", "for", "foreach", "while", "switch", "using", "try", "catch"]:
                    continue

                if self._is_collection_type(type_name) and not self._is_plural_name(var_name):
                    issues.append(CodeIssue(
                        line=i + 1,
                        column=match.start(2) + 1,
                        message=f"集合类型变量 '{var_name}' 的命名建议使用复数形式",
                        rule_id=self.rule_id,
                        severity=self.severity,
                        file_path=file_path
                    ))

        return issues

    def _is_collection_type(self, type_name: str) -> bool:
        """判断类型是否为集合类型"""
        # 去除空格，使检查更准确
        type_name = type_name.replace(" ", "")

        # 检查是否是数组
        if type_name.endswith("[]"):
            return True

        # 检查是否包含集合类型关键词
        for collection_type in self.collection_types:
            if collection_type in type_name:
                return True

        return False

    def _is_plural_name(self, name: str) -> bool:
        """判断名称是否是复数形式"""
        # 检查例外情况
        if name.lower() in self.exceptions or name.startswith('_') and name[1:].lower() in self.exceptions:
            return True

        # 去掉私有字段前缀以进行检查
        if name.startswith('_'):
            name = name[1:]

        # 基本检查：是否以's'结尾
        if name.endswith('s') or name.endswith('S'):
            return True

        # 检查常见的集合后缀
        common_collection_suffixes = ['List', 'Array', 'Collection', 'Set', 'Map', 'Dictionary']
        for suffix in common_collection_suffixes:
            if name.endswith(suffix):
                return True

        # 检查是否包含"Items"等暗示复数的词
        plural_indicators = ['Items', 'Elements', 'Entries', 'Values', 'Keys', 'Pairs', 'Group']
        for indicator in plural_indicators:
            if indicator in name:
                return True

        return False








