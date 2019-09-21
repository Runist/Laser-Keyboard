import cv2 as cv
import numpy as np
import win32api
import win32con
import time

Posion = [[0]*8 for _ in range(64)]

# 1
Posion[1][0] = 50
Posion[1][1] = 30
Posion[1][2] = 53
Posion[1][3] = 54
Posion[1][4] = 72
Posion[1][5] = 26
Posion[1][6] = 82
Posion[1][7] = 54

# 2
Posion[2][0] = 72
Posion[2][1] = 26
Posion[2][2] = 82
Posion[2][3] = 54
Posion[2][4] = 105
Posion[2][5] = 23
Posion[2][6] = 113
Posion[2][7] = 52

# 3
Posion[3][0] = 105
Posion[3][1] = 23
Posion[3][2] = 113
Posion[3][3] = 52
Posion[3][4] = 142
Posion[3][5] = 23
Posion[3][6] = 148
Posion[3][7] = 55

# 4
Posion[4][0] = 142
Posion[4][1] = 23
Posion[4][2] = 148
Posion[4][3] = 55
Posion[4][4] = 178
Posion[4][5] = 24
Posion[4][6] = 180
Posion[4][7] = 57

# 5
Posion[5][0] = 178
Posion[5][1] = 24
Posion[5][2] = 180
Posion[5][3] = 57
Posion[5][4] = 211
Posion[5][5] = 25
Posion[5][6] = 211
Posion[5][7] = 56

# 6
Posion[6][0] = 211
Posion[6][1] = 25
Posion[6][2] = 211
Posion[6][3] = 56
Posion[6][4] = 247
Posion[6][5] = 26
Posion[6][6] = 247
Posion[6][7] = 58

# 7
Posion[7][0] = 247
Posion[7][1] = 26
Posion[7][2] = 247
Posion[7][3] = 58
Posion[7][4] = 285
Posion[7][5] = 28
Posion[7][6] = 283
Posion[7][7] = 61

# 8
Posion[8][0] = 285
Posion[8][1] = 28
Posion[8][2] = 283
Posion[8][3] = 61
Posion[8][4] = 319
Posion[8][5] = 27
Posion[8][6] = 315
Posion[8][7] = 59

# 9
Posion[9][0] = 319
Posion[9][1] = 27
Posion[9][2] = 315
Posion[9][3] = 59
Posion[9][4] = 354
Posion[9][5] = 27
Posion[9][6] = 355
Posion[9][7] = 60

# 0
Posion[10][0] = 354
Posion[10][1] = 27
Posion[10][2] = 355
Posion[10][3] = 60
Posion[10][4] = 393
Posion[10][5] = 32
Posion[10][6] = 388
Posion[10][7] = 63

# -
Posion[11][0] = 393
Posion[11][1] = 32
Posion[11][2] = 388
Posion[11][3] = 63
Posion[11][4] = 431
Posion[11][5] = 32
Posion[11][6] = 428
Posion[11][7] = 60

# +
Posion[12][0] = 431
Posion[12][1] = 32
Posion[12][2] = 428
Posion[12][3] = 60
Posion[12][4] = 457
Posion[12][5] = 39
Posion[12][6] = 457
Posion[12][7] = 69

# Esc
Posion[13][0] = 40
Posion[13][1] = 59
Posion[13][2] = 44
Posion[13][3] = 82
Posion[13][4] = 76
Posion[13][5] = 57
Posion[13][6] = 82
Posion[13][7] = 82

# Q
Posion[14][0] = 76
Posion[14][1] = 57
Posion[14][2] = 82
Posion[14][3] = 82
Posion[14][4] = 113
Posion[14][5] = 58
Posion[14][6] = 117
Posion[14][7] = 82

# W
Posion[15][0] = 113
Posion[15][1] = 58
Posion[15][2] = 117
Posion[15][3] = 82
Posion[15][4] = 145
Posion[15][5] = 58
Posion[15][6] = 147
Posion[15][7] = 81

# E
Posion[16][0] = 145
Posion[16][1] = 58
Posion[16][2] = 147
Posion[16][3] = 81
Posion[16][4] = 177
Posion[16][5] = 59
Posion[16][6] = 180
Posion[16][7] = 84

# R
Posion[17][0] = 177
Posion[17][1] = 59
Posion[17][2] = 180
Posion[17][3] = 84
Posion[17][4] = 215
Posion[17][5] = 58
Posion[17][6] = 213
Posion[17][7] = 86

# T
Posion[18][0] = 215
Posion[18][1] = 58
Posion[18][2] = 213
Posion[18][3] = 86
Posion[18][4] = 247
Posion[18][5] = 62
Posion[18][6] = 250
Posion[18][7] = 89

# Y
Posion[19][0] = 247
Posion[19][1] = 62
Posion[19][2] = 250
Posion[19][3] = 89
Posion[19][4] = 282
Posion[19][5] = 60
Posion[19][6] = 284
Posion[19][7] = 88

# U
Posion[20][0] = 282
Posion[20][1] = 88
Posion[20][2] = 284
Posion[20][3] = 88
Posion[20][4] = 319
Posion[20][5] = 62
Posion[20][6] = 318
Posion[20][7] = 90

# I
Posion[21][0] = 319
Posion[21][1] = 62
Posion[21][2] = 318
Posion[21][3] = 90
Posion[21][4] = 356
Posion[21][5] = 66
Posion[21][6] = 352
Posion[21][7] = 91

# O
Posion[22][0] = 356
Posion[22][1] = 66
Posion[22][2] = 352
Posion[22][3] = 91
Posion[22][4] = 393
Posion[22][5] = 66
Posion[22][6] = 387
Posion[22][7] = 92

# P
Posion[23][0] = 393
Posion[23][1] = 66
Posion[23][2] = 387
Posion[23][3] = 92
Posion[23][4] = 432
Posion[23][5] = 67
Posion[23][6] = 424
Posion[23][7] = 93

# BackSpace
Posion[24][0] = 432
Posion[24][1] = 67
Posion[24][2] = 424
Posion[24][3] = 93
Posion[24][4] = 471
Posion[24][5] = 70
Posion[24][6] = 468
Posion[24][7] = 93

# CAP
Posion[25][0] = 24
Posion[25][1] = 86
Posion[25][2] = 31
Posion[25][3] = 106
Posion[25][4] = 60
Posion[25][5] = 85
Posion[25][6] = 66
Posion[25][7] = 108

# TAB
Posion[26][0] = 60
Posion[26][1] = 85
Posion[26][2] = 66
Posion[26][3] = 108
Posion[26][4] = 92
Posion[26][5] = 85
Posion[26][6] = 98
Posion[26][7] = 108

# A
Posion[27][0] = 92
Posion[27][1] = 85
Posion[27][2] = 98
Posion[27][3] = 108
Posion[27][4] = 124
Posion[27][5] = 86
Posion[27][6] = 129
Posion[27][7] = 108

# S
Posion[28][0] = 124
Posion[28][1] = 86
Posion[28][2] = 129
Posion[28][3] = 108
Posion[28][4] = 159
Posion[28][5] = 87
Posion[28][6] = 158
Posion[28][7] = 109

# D
Posion[29][0] = 159
Posion[29][1] = 87
Posion[29][2] = 158
Posion[29][3] = 109
Posion[29][4] = 232
Posion[29][5] = 101
Posion[29][6] = 236
Posion[29][7] = 131

# F
Posion[30][0] = 232
Posion[30][1] = 101
Posion[30][2] = 236
Posion[30][3] = 131
Posion[30][4] = 222
Posion[30][5] = 88
Posion[30][6] = 224
Posion[30][7] = 111

# G
Posion[31][0] = 222
Posion[31][1] = 88
Posion[31][2] = 224
Posion[31][3] = 111
Posion[31][4] = 257
Posion[31][5] = 91
Posion[31][6] = 256
Posion[31][7] = 114

# H
Posion[32][0] = 257
Posion[32][1] = 91
Posion[32][2] = 256
Posion[32][3] = 114
Posion[32][4] = 291
Posion[32][5] = 90
Posion[32][6] = 289
Posion[32][7] = 116

# J
Posion[33][0] = 291
Posion[33][1] = 90
Posion[33][2] = 289
Posion[33][3] = 116
Posion[33][4] = 328
Posion[33][5] = 92
Posion[33][6] = 322
Posion[33][7] = 116

# K
Posion[34][0] = 328
Posion[34][1] = 92
Posion[34][2] = 322
Posion[34][3] = 116
Posion[34][4] = 361
Posion[34][5] = 92
Posion[34][6] = 304
Posion[34][7] = 171

# L
Posion[35][0] = 361
Posion[35][1] = 92
Posion[35][2] = 304
Posion[35][3] = 171
Posion[35][4] = 365
Posion[35][5] = 96
Posion[35][6] = 387
Posion[35][7] = 119

# ;
Posion[36][0] = 365
Posion[36][1] = 96
Posion[36][2] = 387
Posion[36][3] = 119
Posion[36][4] = 430
Posion[36][5] = 95
Posion[36][6] = 424
Posion[36][7] = 118

# 回车
Posion[37][0] = 430
Posion[37][1] = 95
Posion[37][2] = 424
Posion[37][3] = 118
Posion[37][4] = 492
Posion[37][5] = 96
Posion[37][6] = 484
Posion[37][7] = 121

# 左shift
Posion[38][0] = 10
Posion[38][1] = 115
Posion[38][2] = 15
Posion[38][3] = 136
Posion[38][4] = 48
Posion[38][5] = 115
Posion[38][6] = 56
Posion[38][7] = 137

# ~
Posion[39][0] = 48
Posion[39][1] = 115
Posion[39][2] = 56
Posion[39][3] = 137
Posion[39][4] = 78
Posion[39][5] = 116
Posion[39][6] = 86
Posion[39][7] = 140

# |
Posion[40][0] = 78
Posion[40][1] = 116
Posion[40][2] = 86
Posion[40][3] = 140
Posion[40][4] = 111
Posion[40][5] = 116
Posion[40][6] = 115
Posion[40][7] = 139

# Z
Posion[41][0] = 111
Posion[41][1] = 116
Posion[41][2] = 115
Posion[41][3] = 139
Posion[41][4] = 143
Posion[41][5] = 116
Posion[41][6] = 144
Posion[41][7] = 140

# X
Posion[42][0] = 182
Posion[42][1] = 116
Posion[42][2] = 144
Posion[42][3] = 144
Posion[42][4] = 174
Posion[42][5] = 116
Posion[42][6] = 176
Posion[42][7] = 141

# C
Posion[43][0] = 174
Posion[43][1] = 116
Posion[43][2] = 176
Posion[43][3] = 141
Posion[43][4] = 207
Posion[43][5] = 116
Posion[43][6] = 208
Posion[43][7] = 142

# V
Posion[44][0] = 207
Posion[44][1] = 116
Posion[44][2] = 208
Posion[44][3] = 142
Posion[44][4] = 239
Posion[44][5] = 120
Posion[44][6] = 240
Posion[44][7] = 144

# B
Posion[45][0] = 239
Posion[45][1] = 120
Posion[45][2] = 240
Posion[45][3] = 144
Posion[45][4] = 272
Posion[45][5] = 120
Posion[45][6] = 270
Posion[45][7] = 143

# N
Posion[46][0] = 272
Posion[46][1] = 120
Posion[46][2] = 270
Posion[46][3] = 143
Posion[46][4] = 304
Posion[46][5] = 122
Posion[46][6] = 302
Posion[46][7] = 141

# M
Posion[47][0] = 304
Posion[47][1] = 122
Posion[47][2] = 302
Posion[47][3] = 141
Posion[47][4] = 336
Posion[47][5] = 120
Posion[47][6] = 337
Posion[47][7] = 145

# <
Posion[48][0] = 336
Posion[48][1] = 120
Posion[48][2] = 337
Posion[48][3] = 145
Posion[48][4] = 376
Posion[48][5] = 122
Posion[48][6] = 369
Posion[48][7] = 147

# >
Posion[49][0] = 376
Posion[49][1] = 122
Posion[49][2] = 369
Posion[49][3] = 147
Posion[49][4] = 407
Posion[49][5] = 123
Posion[49][6] = 402
Posion[49][7] = 146

# UP
Posion[50][0] = 407
Posion[50][1] = 123
Posion[50][2] = 402
Posion[50][3] = 146
Posion[50][4] = 442
Posion[50][5] = 122
Posion[50][6] = 434
Posion[50][7] = 144

# ?
Posion[51][0] = 442
Posion[51][1] = 122
Posion[51][2] = 434
Posion[51][3] = 144
Posion[51][4] = 474
Posion[51][5] = 122
Posion[51][6] = 466
Posion[51][7] = 147

# 右shift
Posion[52][0] = 474
Posion[52][1] = 122
Posion[52][2] = 466
Posion[52][3] = 147
Posion[52][4] = 509
Posion[52][5] = 123
Posion[52][6] = 500
Posion[52][7] = 147

# CTRL
Posion[53][0] = 15
Posion[53][1] = 136
Posion[53][2] = 27
Posion[53][3] = 159
Posion[53][4] = 51
Posion[53][5] = 137
Posion[53][6] = 59
Posion[53][7] = 160

# ALT
Posion[54][0] = 51
Posion[54][1] = 137
Posion[54][2] = 59
Posion[54][3] = 160
Posion[54][4] = 80
Posion[54][5] = 137
Posion[54][6] = 84
Posion[54][7] = 156

# Fn
Posion[55][0] = 80
Posion[55][1] = 137
Posion[55][2] = 84
Posion[55][3] = 156
Posion[55][4] = 114
Posion[55][5] = 140
Posion[55][6] = 119
Posion[55][7] = 160

# {
Posion[56][0] = 114
Posion[56][1] = 140
Posion[56][2] = 119
Posion[56][3] = 160
Posion[56][4] = 142
Posion[56][5] = 140
Posion[56][6] = 148
Posion[56][7] = 159

# }
Posion[57][0] = 142
Posion[57][1] = 140
Posion[57][2] = 148
Posion[57][3] = 159
Posion[57][4] = 175
Posion[57][5] = 142
Posion[57][6] = 179
Posion[57][7] = 162

# Space
Posion[58][0] = 175
Posion[58][1] = 142
Posion[58][2] = 179
Posion[58][3] = 162
Posion[58][4] = 336
Posion[58][5] = 145
Posion[58][6] = 333
Posion[58][7] = 169

# "
Posion[59][0] = 336
Posion[59][1] = 145
Posion[59][2] = 333
Posion[59][3] = 169
Posion[59][4] = 369
Posion[59][5] = 147
Posion[59][6] = 365
Posion[59][7] = 169

# Left
Posion[60][0] = 369
Posion[60][1] = 147
Posion[60][2] = 365
Posion[60][3] = 169
Posion[60][4] = 402
Posion[60][5] = 146
Posion[60][6] = 397
Posion[60][7] = 169

# Down
Posion[61][0] = 402
Posion[61][1] = 146
Posion[61][2] = 397
Posion[61][3] = 169
Posion[61][4] = 434
Posion[61][5] = 144
Posion[61][6] = 428
Posion[61][7] = 170

# Right
Posion[62][0] = 434
Posion[62][1] = 144
Posion[62][2] = 428
Posion[62][3] = 170
Posion[62][4] = 466
Posion[62][5] = 147
Posion[62][6] = 459
Posion[62][7] = 170

# Del
Posion[63][0] = 466
Posion[63][1] = 147
Posion[63][2] = 459
Posion[63][3] = 170
Posion[63][4] = 498
Posion[63][5] = 149
Posion[63][6] = 487
Posion[63][7] = 170


KeyValue = [0, 49, 50, 51, 52, 53, 54, 55, 56, 57, 0, 109, 107, 27, 81, 87, 69, 82, 84, 89, 85, 73, 79, 80, 8,
            20, 9, 65, 83, 68, 70, 71, 72, 74, 75, 76, 186, 13, 160, 192, 220, 90, 88, 67, 86, 66, 78, 77, 188, 190,
            38, 191, 161, 17, 18, 91, 219, 221, 32, 222, 37, 40, 39, 46]
#                 ESC  CAP   SHITF   CTR ALT WIN
# FunctionalKey = [27, 20, 160, 160, 17, 18, 93] # 功能键
l = [0, 2, 4, 6]


def debug_point(frame):
    """
    键值校准图像
    :param frame: 原图像
    :return: 加上坐标后的图像
    """
    for i in range(1, len(Posion)):
        for j in l:
            cv.circle(frame, (Posion[i][j], Posion[i][j+1]), 2, (255, 255, 255), -1)

    return frame


# 函数名称：KeyScan()
# 输入参数：x, y
# 输出参数：key_value
# 功能：键值扫描
# 说明：无
def KeyScan(x, y):
    """
    按键扫描
    :param x: 手指x坐标
    :param y: 手指y坐标
    :return: 具体键值
    """
    key_value = 0
    for i in range(1, 64):
        if Posion[i][0] < x < Posion[i][6] and Posion[i][5] < y < Posion[i][3]:
            key_value = i
    return key_value


# 函数名称：KeyBoard_Output()
# 输入参数：key_out, flag_out, finger_in
# 输出参数：无
# 功能：按键输出
# 说明：该函数为多线程t2
def KeyBoard_Output(key_out, flag_out, finger_in):
    """
    子线程按键按下触发事件
    :param key_out: 主线程队列的键值 输出
    :param flag_out: 主线程队列的标志位 输出
    :param finger_in: 主线程队列手指个数 输入
    :return: None
    """
    while True:
        exist_flag = flag_out.get()
        finger_in.put(0)
        key = key_out.get()
        keys = []
        if isinstance(key, int) and exist_flag == 1 and key != 0:
            if key == 13 or key == 25 or key == 38 or key == 52 or key == 53 or key == 54 or key == 55:
                win32api.keybd_event(KeyValue[key], 0, 0, 0)
                while (key == 13 or key == 25 or key == 38 or key == 52 or key == 53 or key == 54 or key == 55)\
                        and keys != 0:
                    # 多指标志位，1为切换多指，0为单指
                    finger_in.put(1)
                    keys = key_out.get()
                    print(win32api.GetKeyState(KeyValue[key]))
                    if isinstance(keys, int):
                        pass
                    # 三指快捷键太少了，这个函数库也不支持使用
                    # elif len(keys) == 3:
                    #     Third_Key(keys)
                    else:
                        for hot_key in keys:
                            win32api.keybd_event(KeyValue[hot_key], 0, 0, 0)
                            # if hot_key ==
                            print(hot_key)
            else:
                win32api.keybd_event(KeyValue[key], 0, 0, 0)
                print(win32api.GetKeyState(KeyValue[key]))
            win32api.keybd_event(KeyValue[key], 0, win32con.KEYEVENTF_KEYUP, 0)
        else:
            pass

        # 注意这里暂停时间是要和主线程一致
        time.sleep(0.15)


def Third_Key(keys):
    """
    三指同时按下
    :param keys:键值
    :return: None
    """
    i = 0
    while i < 2:
        win32api.keybd_event(KeyValue[keys[i]], 0, 0, 0)
        print(win32api.GetKeyState(KeyValue[keys[i]]))
        i = i + 1
    for key in keys:
        if key != 13 and key != 25 and key != 38 and key != 52 and key != 53 and key != 54 and key != 55 and key != 0:
            win32api.keybd_event(KeyValue[key], 0, win32con.KEYEVENTF_KEYUP, 0)
