#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name="csharp_style_checker",
    version="0.1.0",
    description="C# 代码风格检查工具",
    author="恶霸威",
    author_email="your.email@example.com",
    url="https://github.com/SiMaLaoShi/csharp_style_checker",
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'csharp-style-check=main:main',
        ],
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    python_requires=">=3.6",
)

