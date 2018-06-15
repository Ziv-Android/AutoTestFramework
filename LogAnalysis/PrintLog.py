#!/usr/bin/env python3
# -*- encoding:utf-8 -*-

"""
@license:   (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@file:      PrintLog.py
@author:    ziv-peng
@time:      18-5-31
@desc:      Android日志分析
"""

import subprocess

subprocess.call("adb devices", shell=True)

order = "adb logcat"
pipe = subprocess.Popen(order, shell=True, stdout=subprocess.PIPE)
for item in iter(pipe.stdout.readline, ""):
    print(item)
