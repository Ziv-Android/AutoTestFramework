#!/usr/bin/env python3
# -*- encoding:utf-8 -*-

"""
@license:   (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@file:      cpuInfo.py
@author:    ziv-peng
@time:      18-6-4
@desc:      
"""
import csv
import os
import time


class Controller(object):
    def __init__(self, count):
        self.counter = count
        self.allData = [("timestamp", "cpustatus")]

    def TestProcess(self):
        result = os.popen("adb shell dumpsys cpuinfo | grep com.togic.livevideo")
        for line in result.readlines():
            cpuvalue = line.split("%")[0]
            print(line)

        currenttime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        self.allData.append((currenttime, cpuvalue))

    def run(self):
        while self.counter > 0:
            self.TestProcess()
            self.counter = self.counter - 1
            time.sleep(5)

    def SaveDataToCSV(self):
        csvfile = open("cpustatus.csv", "w")
        writer = csv.writer(csvfile)
        writer.writerrows(self.allData)
        csvfile.close()


if __name__ == "__main__":
    controller = Controller(3)
    controller.run()
    controller.SaveDataToCSV()
