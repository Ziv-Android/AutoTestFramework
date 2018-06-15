#!/usr/bin/env python3
# -*- encoding:utf-8 -*-

"""
@license:   (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@author:    ziv-peng
@time:      18-6-11
@desc:      
"""


class Controller(object):
    def __init__(self):
        self.allData = []

    # 读取固定规则
    def readFile(self, filename):
        datafile = open(filename, "r")
        content = datafile.readlines()
        datafile.close()
        return content

    # android和java包下的import可忽略
    def dynamicRule(self, text):
        for line in text:
            ans = line.split()[1]
            if not ans.startswith(("android.", "java.")):
                print(ans)
                return False
        return True

    # 分析文本
    def analyzeFile(self, filename, rulefile):
        # 读取静态规则
        rule = self.readFile(rulefile)
        # 读取待判断文本
        data = self.readFile(filename)
        for line in data:
            if "import" in line:
                self.allData.append(line)

        # 是否是android或java包下的import
        return self.dynamicRule(set(controller.allData).difference(set(rule)))


if __name__ == "__main__":
    controller = Controller()
    if not controller.analyzeFile("AdFilter.java", "config.txt"):
        raise RuntimeError("Extra import, review code first!!!")
