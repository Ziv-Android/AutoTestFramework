#!/usr/bin/env python3
# -*- encoding:utf-8 -*-

"""
@license:   (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@file:      networkData.py
@author:    ziv-peng
@time:      18-6-6
@desc:      
"""
import os
import csv
import time


class Controller(object):
    def __init__(self, count):
        self.counter = count
        self.allData = [("timestamp", "traffic")]

    def TestProcess(self):
        result = os.popen("adb shell ps | grep com.togic.livevideo")
        # 获取进程PID
        pid = result.readlines()[0].split(" ")[5]

        traffic = os.popen("adb shell cat /proc/" + pid + "/net/dev")
        for line in traffic:
            if "eth0" in line:
                # 将所有的空行替换为“#”
                line = "#".join(line.split())
                # 按“#”进行拆分
                receive = line.split("#")[1]
                transmit = line.split("#")[9]
            elif "eth1" in line:
                print("")

        # 计算所有流量的和
        alltraffic = int(receive) + int(transmit)
        # 当前流量单位KB
        alltraffic = alltraffic/1024
        currenttime = self.getCurrentTime()
        self.allData.append((currenttime, alltraffic))

    def Run(self):
        while self.counter > 0:
            self.TestProcess()
            self.counter = self.counter - 1
            time.sleep(5)

    def getCurrentTime(self):
        currentTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        return currentTime

    def SaveDataToCSV(self):
        csvfile = open("traffic.csv", "w")
        writer = csv.writer(csvfile)
        writer.writerows(self.allData)
        csvfile.close()


if __name__ == "__main__":
    controller = Controller(3)
    controller.Run()
    controller.SaveDataToCSV()
