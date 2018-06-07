#!/usr/bin/env python3
# -*- encoding:utf-8 -*-

"""
@license:   (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@file:      batteryPower.py
@author:    ziv-peng
@time:      18-6-6
@desc:      
"""
import csv
import os
import time

class Controller(object):
    def __init__(self, count):
        self.counter = count
        self.alldata = [("", "")]

    def testProcess(self):
        result = os.popen("adb shell dumpsys battery")
        for line in result:
            if "level" in line:
                power = line.split(":")[1]

        current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        self.alldata.append((current_time, power))
        print("%s ,power level =%s" % (current_time, power))

    def run(self):
        while self.counter > 0:
            self.testProcess()
            self.counter = self.counter - 1
            time.sleep(5)

    def saveDataToCSV(self):
        csvfile = open("power.csv", "w")
        writer = csv.writer(csvfile)
        writer.writerows(self.alldata)
        csvfile.close()


if __name__ == "__main__":
    controller = Controller(3)
    controller.run()
    controller.saveDataToCSV()
