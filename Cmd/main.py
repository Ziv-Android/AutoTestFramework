#!/usr/bin/env python3
# -*- encoding:utf-8 -*-

"""
@license:   (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@software:  PyCharm
@file:      AutoTestFramework_main.py
@author:    ziv
@time:      2019/9/2
@version:   v1.0.0
@desc:      python执行shell探究
"""

import sys
import subprocess


def run_cmd(cmd):
    return subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)


def cmd_check_out(cmd):
    return subprocess.check_output(cmd, timeout=10, stderr=subprocess.STDOUT)


# returnCode = subprocess.call('adb devices', shell=True)
# print(returnCode)
#
# std_out = run_cmd(['ls', '-la'])
# print(std_out.communicate())


# p = run_cmd(['ping', 'zhihu.com'])
# for i in iter(p.stdout.readline, ''):
#     print(i.strip())

p = run_cmd(['adb', 'logcat'])
for i in iter(p.stdout.readline, ''):
    print(i.strip())
