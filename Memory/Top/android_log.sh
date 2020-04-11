#!/bin/bash

echo "Start logcat"
adb logcat -v time > log.txt
