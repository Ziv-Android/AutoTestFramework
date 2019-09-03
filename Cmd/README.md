# Python执行Shell探究
## 使用场景
1. 命令执行会一次性返回所有结果，结果处理
2. 命令执行的同时，实时获取命令的持续输出，做一些爱做的事情

## 方案调研
1. 命令持续输出,就不能采用阻塞的命令,会卡死当前,无法执行后续处理逻辑
2. 命令一次性返回所有,对命令是否会阻塞没有要求,只要有正确完整的输出即可

### 管道
非阻塞, 通过Linux管道机制实现输出信息过滤处理
`adb logcat | python Cmd/proxy_output.py`

### os模块
#### os.system
阻塞，返回shell执行参数命令的状态,即成功返回0, 失败返回-1
`os.system('cat /proc/cpuinfo')`
执行流程
1.fork一个子进程； 
2.在子进程中调用exec函数去执行命令； 
3.在父进程中调用wait（阻塞）去等待子进程结束。
#### os.popen
阻塞，返回file read的对象，对该对象进行 read() 可以获取shell执行参数命令的结果，即标准输出
`os.popen('cat /proc/cpuinfo')`

### sys模块

### commands模块
#### commands.getstatus
阻塞，返回参数指定的系统文件的详细属性
`commands.getstatus('/proc/cputinfo')`
#### commands.getoutput
阻塞，返回shell执行参数命令的结果
`commands.getoutput('cat /proc/cpuinfo')`
#### commands.getstatusoutput
阻塞，返回shell状态和shell输出的元组(status, output)
`commands.getstatusoutput('cat /proc/cpuinfo')`

### subprocess模块
#### subprocess.call
阻塞，返回shell状态，禁用 PIPE 参数
`subprocess.call(args, *, stdin=None, stdout=None, stderr=None, shell=False)`
#### subprocess.check_call
阻塞，shell 执行成功返回0, 否则无返回，并抛出包含shell错误状态的 CalledProcessError 异常，禁用PIPE参数
`subprocess.check_call(args, *, stdin=None, stdout=None, stderr=None, shell=False)`
#### subprocess.check_output
阻塞，shell 执行成功返回shell结果，否则无返回，并抛出包含shell错误状态的 CalledProcessError 异常，禁用PIPE参数
`subprocess.check_output(args, *, stdin=None, stderr=None, shell=False, universal_newlines=False)`
#### subprocess.Popen
不阻塞，返回Popen对象
`subprocess.Popen(args, bufsize=0, executable=None, stdin=None, stdout=None, stderr=None, preexec_fn=None, close_fds=False, shell=False, cwd=None, env=None, universal_newlines=False, startupinfo=None, creationflags=0)`
subprocess 参数:
args: 字符串或列表（*nix 下第一项视为命令，后面是命令参数）
bufsize: 默认 0 不缓冲，1 行缓冲，其他正数表示缓冲大小，负数表示使用系统默认全缓冲
executable: 一般不用,args字符串或列表第一项表示程序名
stdin stdout stderr: None 表示继承父进程,不做重定向 subprocess.PIPE 表示管道操作，subprocess.STDOUT 表示输出到标准输出 文件对象/文件描述符
preexec_fn: 钩子函数,在fork和exec之间执行 *nix 下子进程被执行前调用
close_fds: 
shell: **True 时表示指定命令在shell里解释执行**
cwd: 设置工作目录
env: 设置环境变量
universal_newlines: 统一换行符处理为`\n`

Popen 对象属性:
Popen.poll(): 检查子进程是否结束，0 表示退出
Popen.wait(): 等待子进程结束，注意子进程是否写管道
Popen.communicate(input=None): 与子进程交互，字符串数据发送到stdin，并从stdout和stderr读数据，知道EOF，等待子进程结束。注意读写stdin、stdout或stderr时要给定PIPE参数。返回元组(stdoutdata, stderrdata)。
Popen.send_signal(signal): 给子进程发送信号
Popen.terminate(): 停止子进程
Popen.kill(): 杀死子进程
Popen.stdin Popen.stdout Popen.stderr: PIPE参数时为文件对象，否则None
Popen.pid: 子进程的进程号
Popen.returncode None表示子进程没终止，负数-N表示子进程被N号信号终止

## 实战方案
### 管道
管道是linux提供的一种常见的进程通信工具,将`|`左边的命令输出,导向右边的命令输入
如:`adb logcat | python Cmd/proxy_output.py`
`proxy_output.py`文件的简单实现如下
```python
#!/usr/bin/env python3
# -*- encoding:utf-8 -*-

import sys

for line in sys.stdin:
    print(line)
```
优点:
1. 简单
2. 非阻塞, 可连续处理

缺点:
1. 处理效率率不高, 实时性较低

### subprocess模块
从 Popen 类源码 738 行`self.stdout = os.fdopen(c2pread, 'rU', bufsize)`,且`os.fdopen`通过注释信息得知

> Return an open file object connected to a file descriptor.

`Popen.stdout`返回的是一个文件对象, 即可使用`readline`读取

```python
#!/usr/bin/env python3
# -*- encoding:utf-8 -*-

import subprocess

p = subprocess.Popen(['adb', 'logcat'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
for i in iter(p.stdout.readline, ''):
    print(i.strip())
```
注意这里使用了 `iter()` 内置函数，将 `p.stdout` 转换为一个迭代器，并使用 `p.stdout.readline` 替换迭代器的 `next` 方法，后面 `''` 的意思就是当 `p.stdout.readline` 返回的值是 `''` 的时候，迭代器终止

Surprise, 与终端直接执行`adb logcat`对比近乎同步,终于可以做你们爱做的事情了...(疑车有据)

## 参考资料
https://docs.python.org/zh-cn/3/library/subprocess.html
https://my.oschina.net/colben/blog/488373
https://www.cnblogs.com/zhoug2020/p/5079407.html
https://zhuanlan.zhihu.com/p/33093791
