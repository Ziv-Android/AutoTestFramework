#!/usr/bin/env python3
# -*- encoding:utf-8 -*-

"""
@license:   (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@file:      memory.py
@author:    ziv-peng
@time:      18-6-7
@desc:      
"""
import csv


class Controller(object):
    def __init__(self):
        self.alldata = [(0, "", "")]

    def analyzeData(self):
        content = self.readFile()
        i = 0
        for line in content:
            if "com.togic.livevideo" in line:
                print(line)
                line = "#".join(line.split())
                vss = line.split("#")[5].strip("K")
                rss = line.split("#")[6].strip("K")

                self.alldata.append((i, vss, rss))
                i = i + 1

    def saveDataToCSV(self):
        csvfile = open("meminfo.csv", "w")
        writer = csv.writer(csvfile)
        writer.writerows(self.alldata)
        csvfile.close()

    def readFile(self):
        datafile = open("meminfo.log", "r")
        content = datafile.readlines()
        datafile.close()
        return content


if __name__ == "__main__":
    controller = Controller()
    controller.analyzeData()
    controller.saveDataToCSV()