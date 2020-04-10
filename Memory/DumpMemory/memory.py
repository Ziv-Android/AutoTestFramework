#!/usr/bin/env python3
# -*- encoding:utf-8 -*-

"""
@license:   (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@software:  PyCharm
@file:      AutoTestFramework_memory.py
@author:    ziv
@time:      2020/4/9
@version:   v1.0.0
@desc:      脚本功能描述
"""

import os


class Controller(object):
    def __init__(self):
        print("init")

    def test_cmd(self, cmd):
        result = os.popen(cmd)
        for line in result.readlines():
            print(line)

    def get_root_permission(self):
        cmd = "adb root"
        self.test_cmd(cmd)

    def get_program_pid(self, package_name):
        cmd = "adb shell ps | grep " + package_name
        result = os.popen(cmd)
        return result.readlines()[0].split(" ")[4]

    def get_system_env(self):
        cmd = "adb shell getprop|grep dalvik.vm.heapsize"
        cmd = "adb shell getprop|grep heapgrowthlimit"
        cmd = "adb shell getprop|grep dalvik.vm.heapstartsize"

    def run_gc(self, program_pid):
        # adb需要root权限, 否则不能执行gc操作
        self.get_root_permission()
        cmd = "adb shell su -c kill -10 " + program_pid
        self.test_cmd(cmd)

    def dump_heap(self):
        cmd = "adb shell am dumpheap com.togic.livevideo /data/local/tmp/memory_new_ui_mainActivity.hprof"

    def close_app(self, package_name):
        cmd = "adb shell am force-stop " + package_name


if __name__ == '__main__':
    controller = Controller()
    pid = controller.get_program_pid("com.togic.livevideo")
    controller.run_gc(pid)
    print("pid:", pid)
