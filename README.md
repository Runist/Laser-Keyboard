# 激光键盘使用说明

![timg.jpg](https://i.loli.net/2020/03/25/WFuMCiUGVNodYh2.jpg)

## 目录

- [配置信息](#配置信息)
- [程序结构](#程序结构)
- [注意事项](#注意事项)

## 配置信息

Python版本

- 推荐Python3.5以上

所需库文件

- cv2 -- 对应pip opencv-python
- numpy
- time
- threading
- queue
- win32api、win32con --对应pip pywin32

## 程序结构

### *KeyBoardPosition.py*

功能：

- 定义各个键位的四个坐标点
- 按键扫描
- 按键输出

### *Threading_KeyBoard.py*

功能：

- 从摄像头读入图像，并进行预处理
- 获取图像中手指光斑轮廓信息，计算质心
- 开启多个线程（可选，为了实现多指按下的功能，如果只是验证单指功能，可以不用）

## 注意事项

该程序需要结合硬件使用，也就意味着使用者必须先搭建机械结构，有一定的硬件基础。而且每个作品做出来不一样的投射位置，也需要改动*KeyBoardPosition.py*中的坐标。