#!/usr/bin/env python3
# -*- encoding:utf-8 -*-

"""
@license:   (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@software:  PyCharm
@file:      AutoTestFramework_adb_tool.py
@author:    ziv
@time:      2019/8/30
@version:   v1.0.0
@desc:      adb命令辅助工具
"""

import os
import sys
import subprocess


class Adb(object):
    def __init__(self):
        self.__adb_cmd = None
        self.adb_server_port = 5555
        print("Adb_tool init")

    def adb(self):
        if "ANDROID_HOME" in os.environ:
            print("OS name:", os.name)
            adb_cmd = os.path.join(os.environ["ANDROID_HOME"], "platform-tools", "adb")
            print(adb_cmd)
            if not os.path.exists(adb_cmd):
                raise EnvironmentError("Adb not found in $ANDROID_HOME path: %s." % os.environ["ANDROID_HOME"])
            else:
                self.__adb_cmd = adb_cmd
        return self.__adb_cmd

    # def cmd(self):
        # serial = self.device_serial()

    def device(self):
        return self.cmd(self.adb(), "logcat")

    def version(self):
        return self.cmd(self.adb(), "version")

    def cmd(self, cmd, *args):
        cmd_line = [cmd] + list(args)
        cmd_line = " ".join(cmd_line)
        print(cmd_line)
        # return subprocess.Popen(cmd_line, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        # return subprocess.Popen(cmd_line, shell=True, stdout=open('test.txt', 'w'), stderr=subprocess.PIPE)
        return subprocess.Popen(cmd_line, shell=True, stdout=None, stderr=subprocess.PIPE)


tool = Adb()
# version = tool.version().communicate()[0].decode("utf-8")
# version = tool.device()
# print(version)
# p = os.popen('adb shell ps | grep com.togic.livevideo | awk "{print$1}"')
p = os.popen('adb logcat')
value = sys.stdin.readline()
print(value)
