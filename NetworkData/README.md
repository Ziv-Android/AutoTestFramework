## 网络数据流量测试
### 获取流量命令
获取进程ID`adb shell ps | grep packagename`
获取进程流量`adb shell cat  /proc/pid/net/dev`

Receive: app接收的数据
Transmit: app发出的请求的数据   

总流量=  Receive + Transmit ，即为当前app消耗的流量的总值

### 数据分析
对app进行一些测试操作，再次执行获取流量的命令，然后和和上次统计的流量作差，差值即为测试期间app消耗的流量

### 数据标准
对比竟品耗时参考
对比版本间数据