#!/usr/bin/env python3
# -*- encoding:utf-8 -*-

"""
@license:   (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@software:  PyCharm
@file:      AutoTestFramework_proxy_output.py
@author:    ziv
@time:      2019/9/2
@version:   v1.0.0
@desc:      中转代理控制台输出, 可在此处做一些统计or逻辑处理
"""

import sys

for line in sys.stdin:
    print(line)
