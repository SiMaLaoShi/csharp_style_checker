# -*- coding: utf-8 -*-

"""规则定义包"""

from csharp_style_checker.rules.base_rule import BaseRule
from csharp_style_checker.rules.naming_rules import (
    ClassNamePascalCaseRule,
    PrivateFieldUnderscoreRule,
    MethodNamePascalCaseRule,
    VariableCamelCaseRule,
    ConstantNameAllCapsRule,
    StructNamingRule,
    InterfaceNamingRule,
    StaticFieldNamingRule,
    CollectionPluralNamingRule,
)
from csharp_style_checker.rules.structure_rules import BraceOnNewLineRule
from csharp_style_checker.rules.readability_rules import LineIsTooLongRule

__all__ = [
    'BaseRule',
    'ClassNamePascalCaseRule',
    'PrivateFieldUnderscoreRule',
    'MethodNamePascalCaseRule',
    'BraceOnNewLineRule',
    'LineIsTooLongRule',
    'VariableCamelCaseRule',
    'ConstantNameAllCapsRule',
    'StructNamingRule',
    'InterfaceNamingRule',
    'StaticFieldNamingRule',
    'CollectionPluralNamingRule',
]

