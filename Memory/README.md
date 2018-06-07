## 内存检测
### 获取内存
`adb shell top -d 1 -m 5`
-d 控制间隔多少秒更新一次数据
-m 输出前m的数据

VSS - Virtual Set Size 虚拟消耗内存
RSS - Resident Set Size 实际使用物理内存

| 表头信息 | 代指含义 |
| --- | --- |
| PID | 进程号 |
| USER |  |
| PR |  |
| NI |  |
| CPU% | cpu使用率 |
| S | |
| #THR | |
| VSS | 虚拟消耗内存(重点关注) |
| RSS | 实际使用物理内存(重点关注) |
| PCY | |
| Name | |

### 数据分析
注意虚存和实存需要独立分析

### 改进建议
1. 需要先使用命令获取信息到log文件，才能进行数据分析
