# -*- coding: utf-8 -*-

"""文件处理工具函数"""

import os
from typing import List


def find_csharp_files(directory_path: str) -> List[str]:
    """查找目录中的所有C#文件"""
    csharp_files = []
    for root, _, files in os.walk(directory_path):
        for file in files:
            if file.endswith('.cs'):
                csharp_files.append(os.path.join(root, file))
    return csharp_files


def read_file_content(file_path: str) -> str:
    """读取文件内容"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read()
    except UnicodeDecodeError:
        # 尝试以其他编码读取
        with open(file_path, 'r', encoding='gbk') as f:
            return f.read()

