#!/usr/bin/env python3
# -*- encoding:utf-8 -*-

"""
@license:   (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@software:  PyCharm
@file:      AutoTestFramework_commands.py
@author:    ziv
@time:      2019/8/21
@version:   v1.0.0
@desc:      Android内存优化相关工具命令
"""

# Android GC算法: 分代式计算法 -> 年轻代 老年代 持久代

# 内存泄漏常见类型
# 静态类相关: 静态对象的生命周期伴随整个程序的生命周期, 与之关联的对象在应用结束前无法回收
# 资源释放: cursor的关闭 IO流的关闭, bitmap的回收等, 带有缓存的资源使用结束后一定要关闭或释放
# Handler: Handler持有创建其activity的引用, 调用delay message的handler, handler开启线程下载文件还没有完成时, 使用handlerThread执行延迟方法, 都会导致系统认为对象正在使用无法回收
# 注册引用方法: 在使用interface接口注册后, 相关页面结束一定要unRegister
# 对象缓存: 在容器内缓存大量数据后导致数据溢出

# 系统级内存管理
# Low Memory Kill机制
# 当系统使用内存不足时, 根据/proc/[pid]/oom_adj的大小结束相关进程释放资源, 越大越危险, 系统进程-16
# 进程优先级: 前台进程(界面可见且运行, 基本不死) -> 可见进程(界面可见但被遮挡, 对话框) -> 服务进程(拥有系统服务, 如播放器) -> 后台进程(Home键, 无服务支撑) -> 空进程(退出程序后, 系统为加快启动速率保留的进程, 最优先)

# 内存抖动: 内存频繁分配回收
# 频繁GC导致卡顿, 产生大量内存碎片, 导致总体有剩余内存但无法分配导致OOM

# VSS - Virtual Set Size 虚拟消耗内存: 进程可访问总地址空间 -> 已使用RAM内存和已分配(malloc)的空间, 无论是否写入, 超过系统内存就一定会引发OOM
# RSS - Resident Set Size 实际使用RAM的物理内存: 计算了所有的共享库(关注操作后的内存变化)
# PSS - Proportional Set Size 按比例显示实际使用RAM的物理内存, **内存使用是否优质的表现**
# USS - Unique Set Size 进程独占物理内存(不包含共享库占用的内存) **重要的标准, 表示的是一个增量信息**
# 一般来说内存占用大小有如下规律：VSS >= RSS >= PSS >= USS


# 获取Android设备OOM临界值: dalvik.vm.heapgrowthlimit
# adb shell getprop | findstr "heap"

# dumpsys [Option]
# meminfo:显示内存信息 cpuinfo:显示CPU信息 account:显示accounts信息 activity:显示所有的activities的信息 window:显示键盘，窗口和它们的关系 wifi:显示wifi信息
# `top | grep app名称`
# `ps | grep app名称`
# `procrank | grep app名称` 需要Root
# `sysmem`

# https://elinux.org/Android_Memory_Usage
# https://elinux.org/Using_smem_on_Android
# https://blog.csdn.net/berber78/article/details/47819139
