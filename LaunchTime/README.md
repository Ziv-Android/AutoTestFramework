## 启动时间测试
获取Package：`adb logcat | grep START`

### 冷启动
应用由完全关闭状态到启动完毕的耗时检测, 进程首次启动并进行加载数据
```
adb shell am start -W -n Package/activity
adb shell am force-stop Package
```

### 热启动
应用由后台重新切换至前台显示的耗时检测, 进程已经启动但在后台运行
```
adb shell am start -W -n Package/activity
adb shell input keyevent 3 
```

### 数据分析
计算均值和曲线观察波动情况

### 数据标准
对比竟品耗时参考
对比版本间数据