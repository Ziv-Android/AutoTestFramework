#!/usr/bin/env python3
# -*- encoding:utf-8 -*-

"""
@license:   (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@file:      launchTime.py
@author:    ziv-peng
@time:      18-6-4
"""
import csv
import os
import time


class App(object):
    def __init__(self):
        self.content = ""
        self.startTime = 0

    def LaunchApp(self):
        cmd = "adb shell am start -W -n com.togic.livevideo/com.togic.launcher.SplashActivity"
        self.content = os.popen(cmd)

    def StopApp(self):
        # 冷启动关闭
        cmd = "adb shell am force-stop com.togic.livevideo"
        # 热启动关闭
        cmd = "adb shell input keyevent 3"
        os.popen(cmd)

    def GetLaunchedTime(self):
        for line in self.content.readlines():
            if "ThisTime" in line:
                self.startTime = line.split(":")[1]
                break
        return self.startTime

# 控制类
class Controller(object):
    def __init__(self, count):
        self.app = App()
        self.counter = count
        # (测试时间点, 命令完成时间)
        self.addData = [("timestamp", "elapsedtime")]

    # 单次测试过程
    def TestProcess(self):
        self.app.LaunchApp()
        time.sleep(5)
        elapsedtime = self.app.GetLaunchedTime()
        self.app.StopApp()
        time.sleep(3)
        currenttime = self.GetCurrentTime()
        self.addData.append((currenttime, elapsedtime))

    def Run(self):
        while self.counter > 0:
            self.TestProcess()
            self.counter = self.counter - 1

    # 获取当前时间戳
    def GetCurrentTime(self):
        currentTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        return currentTime

    def SaveDataToCSV(self):
        csvFile = open("LaunchTime2.csv", "w")
        writer = csv.writer(csvFile)
        writer.writerows(self.addData)
        csvFile.close()


if __name__ == "__main__":
    controller = Controller(10)
    controller.Run()
    controller.SaveDataToCSV()
