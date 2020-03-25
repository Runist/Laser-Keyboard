import cv2 as cv
import numpy as np
import win32api
import win32con
import time

Position = [[0]*8 for _ in range(64)]

# 1
Position[1][0] = 50
Position[1][1] = 30
Position[1][2] = 53
Position[1][3] = 54
Position[1][4] = 72
Position[1][5] = 26
Position[1][6] = 82
Position[1][7] = 54

# 2
Position[2][0] = 72
Position[2][1] = 26
Position[2][2] = 82
Position[2][3] = 54
Position[2][4] = 105
Position[2][5] = 23
Position[2][6] = 113
Position[2][7] = 52

# 3
Position[3][0] = 105
Position[3][1] = 23
Position[3][2] = 113
Position[3][3] = 52
Position[3][4] = 142
Position[3][5] = 23
Position[3][6] = 148
Position[3][7] = 55

# 4
Position[4][0] = 142
Position[4][1] = 23
Position[4][2] = 148
Position[4][3] = 55
Position[4][4] = 178
Position[4][5] = 24
Position[4][6] = 180
Position[4][7] = 57

# 5
Position[5][0] = 178
Position[5][1] = 24
Position[5][2] = 180
Position[5][3] = 57
Position[5][4] = 211
Position[5][5] = 25
Position[5][6] = 211
Position[5][7] = 56

# 6
Position[6][0] = 211
Position[6][1] = 25
Position[6][2] = 211
Position[6][3] = 56
Position[6][4] = 247
Position[6][5] = 26
Position[6][6] = 247
Position[6][7] = 58

# 7
Position[7][0] = 247
Position[7][1] = 26
Position[7][2] = 247
Position[7][3] = 58
Position[7][4] = 285
Position[7][5] = 28
Position[7][6] = 283
Position[7][7] = 61

# 8
Position[8][0] = 285
Position[8][1] = 28
Position[8][2] = 283
Position[8][3] = 61
Position[8][4] = 319
Position[8][5] = 27
Position[8][6] = 315
Position[8][7] = 59

# 9
Position[9][0] = 319
Position[9][1] = 27
Position[9][2] = 315
Position[9][3] = 59
Position[9][4] = 354
Position[9][5] = 27
Position[9][6] = 355
Position[9][7] = 60

# 0
Position[10][0] = 354
Position[10][1] = 27
Position[10][2] = 355
Position[10][3] = 60
Position[10][4] = 393
Position[10][5] = 32
Position[10][6] = 388
Position[10][7] = 63

# -
Position[11][0] = 393
Position[11][1] = 32
Position[11][2] = 388
Position[11][3] = 63
Position[11][4] = 431
Position[11][5] = 32
Position[11][6] = 428
Position[11][7] = 60

# +
Position[12][0] = 431
Position[12][1] = 32
Position[12][2] = 428
Position[12][3] = 60
Position[12][4] = 457
Position[12][5] = 39
Position[12][6] = 457
Position[12][7] = 69

# Esc
Position[13][0] = 40
Position[13][1] = 59
Position[13][2] = 44
Position[13][3] = 82
Position[13][4] = 76
Position[13][5] = 57
Position[13][6] = 82
Position[13][7] = 82

# Q
Position[14][0] = 76
Position[14][1] = 57
Position[14][2] = 82
Position[14][3] = 82
Position[14][4] = 113
Position[14][5] = 58
Position[14][6] = 117
Position[14][7] = 82

# W
Position[15][0] = 113
Position[15][1] = 58
Position[15][2] = 117
Position[15][3] = 82
Position[15][4] = 145
Position[15][5] = 58
Position[15][6] = 147
Position[15][7] = 81

# E
Position[16][0] = 145
Position[16][1] = 58
Position[16][2] = 147
Position[16][3] = 81
Position[16][4] = 177
Position[16][5] = 59
Position[16][6] = 180
Position[16][7] = 84

# R
Position[17][0] = 177
Position[17][1] = 59
Position[17][2] = 180
Position[17][3] = 84
Position[17][4] = 215
Position[17][5] = 58
Position[17][6] = 213
Position[17][7] = 86

# T
Position[18][0] = 215
Position[18][1] = 58
Position[18][2] = 213
Position[18][3] = 86
Position[18][4] = 247
Position[18][5] = 62
Position[18][6] = 250
Position[18][7] = 89

# Y
Position[19][0] = 247
Position[19][1] = 62
Position[19][2] = 250
Position[19][3] = 89
Position[19][4] = 282
Position[19][5] = 60
Position[19][6] = 284
Position[19][7] = 88

# U
Position[20][0] = 282
Position[20][1] = 88
Position[20][2] = 284
Position[20][3] = 88
Position[20][4] = 319
Position[20][5] = 62
Position[20][6] = 318
Position[20][7] = 90

# I
Position[21][0] = 319
Position[21][1] = 62
Position[21][2] = 318
Position[21][3] = 90
Position[21][4] = 356
Position[21][5] = 66
Position[21][6] = 352
Position[21][7] = 91

# O
Position[22][0] = 356
Position[22][1] = 66
Position[22][2] = 352
Position[22][3] = 91
Position[22][4] = 393
Position[22][5] = 66
Position[22][6] = 387
Position[22][7] = 92

# P
Position[23][0] = 393
Position[23][1] = 66
Position[23][2] = 387
Position[23][3] = 92
Position[23][4] = 432
Position[23][5] = 67
Position[23][6] = 424
Position[23][7] = 93

# BackSpace
Position[24][0] = 432
Position[24][1] = 67
Position[24][2] = 424
Position[24][3] = 93
Position[24][4] = 471
Position[24][5] = 70
Position[24][6] = 468
Position[24][7] = 93

# CAP
Position[25][0] = 24
Position[25][1] = 86
Position[25][2] = 31
Position[25][3] = 106
Position[25][4] = 60
Position[25][5] = 85
Position[25][6] = 66
Position[25][7] = 108

# TAB
Position[26][0] = 60
Position[26][1] = 85
Position[26][2] = 66
Position[26][3] = 108
Position[26][4] = 92
Position[26][5] = 85
Position[26][6] = 98
Position[26][7] = 108

# A
Position[27][0] = 92
Position[27][1] = 85
Position[27][2] = 98
Position[27][3] = 108
Position[27][4] = 124
Position[27][5] = 86
Position[27][6] = 129
Position[27][7] = 108

# S
Position[28][0] = 124
Position[28][1] = 86
Position[28][2] = 129
Position[28][3] = 108
Position[28][4] = 159
Position[28][5] = 87
Position[28][6] = 158
Position[28][7] = 109

# D
Position[29][0] = 159
Position[29][1] = 87
Position[29][2] = 158
Position[29][3] = 109
Position[29][4] = 232
Position[29][5] = 101
Position[29][6] = 236
Position[29][7] = 131

# F
Position[30][0] = 232
Position[30][1] = 101
Position[30][2] = 236
Position[30][3] = 131
Position[30][4] = 222
Position[30][5] = 88
Position[30][6] = 224
Position[30][7] = 111

# G
Position[31][0] = 222
Position[31][1] = 88
Position[31][2] = 224
Position[31][3] = 111
Position[31][4] = 257
Position[31][5] = 91
Position[31][6] = 256
Position[31][7] = 114

# H
Position[32][0] = 257
Position[32][1] = 91
Position[32][2] = 256
Position[32][3] = 114
Position[32][4] = 291
Position[32][5] = 90
Position[32][6] = 289
Position[32][7] = 116

# J
Position[33][0] = 291
Position[33][1] = 90
Position[33][2] = 289
Position[33][3] = 116
Position[33][4] = 328
Position[33][5] = 92
Position[33][6] = 322
Position[33][7] = 116

# K
Position[34][0] = 328
Position[34][1] = 92
Position[34][2] = 322
Position[34][3] = 116
Position[34][4] = 361
Position[34][5] = 92
Position[34][6] = 304
Position[34][7] = 171

# L
Position[35][0] = 361
Position[35][1] = 92
Position[35][2] = 304
Position[35][3] = 171
Position[35][4] = 365
Position[35][5] = 96
Position[35][6] = 387
Position[35][7] = 119

# ;
Position[36][0] = 365
Position[36][1] = 96
Position[36][2] = 387
Position[36][3] = 119
Position[36][4] = 430
Position[36][5] = 95
Position[36][6] = 424
Position[36][7] = 118

# 回车
Position[37][0] = 430
Position[37][1] = 95
Position[37][2] = 424
Position[37][3] = 118
Position[37][4] = 492
Position[37][5] = 96
Position[37][6] = 484
Position[37][7] = 121

# 左shift
Position[38][0] = 10
Position[38][1] = 115
Position[38][2] = 15
Position[38][3] = 136
Position[38][4] = 48
Position[38][5] = 115
Position[38][6] = 56
Position[38][7] = 137

# ~
Position[39][0] = 48
Position[39][1] = 115
Position[39][2] = 56
Position[39][3] = 137
Position[39][4] = 78
Position[39][5] = 116
Position[39][6] = 86
Position[39][7] = 140

# |
Position[40][0] = 78
Position[40][1] = 116
Position[40][2] = 86
Position[40][3] = 140
Position[40][4] = 111
Position[40][5] = 116
Position[40][6] = 115
Position[40][7] = 139

# Z
Position[41][0] = 111
Position[41][1] = 116
Position[41][2] = 115
Position[41][3] = 139
Position[41][4] = 143
Position[41][5] = 116
Position[41][6] = 144
Position[41][7] = 140

# X
Position[42][0] = 182
Position[42][1] = 116
Position[42][2] = 144
Position[42][3] = 144
Position[42][4] = 174
Position[42][5] = 116
Position[42][6] = 176
Position[42][7] = 141

# C
Position[43][0] = 174
Position[43][1] = 116
Position[43][2] = 176
Position[43][3] = 141
Position[43][4] = 207
Position[43][5] = 116
Position[43][6] = 208
Position[43][7] = 142

# V
Position[44][0] = 207
Position[44][1] = 116
Position[44][2] = 208
Position[44][3] = 142
Position[44][4] = 239
Position[44][5] = 120
Position[44][6] = 240
Position[44][7] = 144

# B
Position[45][0] = 239
Position[45][1] = 120
Position[45][2] = 240
Position[45][3] = 144
Position[45][4] = 272
Position[45][5] = 120
Position[45][6] = 270
Position[45][7] = 143

# N
Position[46][0] = 272
Position[46][1] = 120
Position[46][2] = 270
Position[46][3] = 143
Position[46][4] = 304
Position[46][5] = 122
Position[46][6] = 302
Position[46][7] = 141

# M
Position[47][0] = 304
Position[47][1] = 122
Position[47][2] = 302
Position[47][3] = 141
Position[47][4] = 336
Position[47][5] = 120
Position[47][6] = 337
Position[47][7] = 145

# <
Position[48][0] = 336
Position[48][1] = 120
Position[48][2] = 337
Position[48][3] = 145
Position[48][4] = 376
Position[48][5] = 122
Position[48][6] = 369
Position[48][7] = 147

# >
Position[49][0] = 376
Position[49][1] = 122
Position[49][2] = 369
Position[49][3] = 147
Position[49][4] = 407
Position[49][5] = 123
Position[49][6] = 402
Position[49][7] = 146

# UP
Position[50][0] = 407
Position[50][1] = 123
Position[50][2] = 402
Position[50][3] = 146
Position[50][4] = 442
Position[50][5] = 122
Position[50][6] = 434
Position[50][7] = 144

# ?
Position[51][0] = 442
Position[51][1] = 122
Position[51][2] = 434
Position[51][3] = 144
Position[51][4] = 474
Position[51][5] = 122
Position[51][6] = 466
Position[51][7] = 147

# 右shift
Position[52][0] = 474
Position[52][1] = 122
Position[52][2] = 466
Position[52][3] = 147
Position[52][4] = 509
Position[52][5] = 123
Position[52][6] = 500
Position[52][7] = 147

# CTRL
Position[53][0] = 15
Position[53][1] = 136
Position[53][2] = 27
Position[53][3] = 159
Position[53][4] = 51
Position[53][5] = 137
Position[53][6] = 59
Position[53][7] = 160

# ALT
Position[54][0] = 51
Position[54][1] = 137
Position[54][2] = 59
Position[54][3] = 160
Position[54][4] = 80
Position[54][5] = 137
Position[54][6] = 84
Position[54][7] = 156

# Fn
Position[55][0] = 80
Position[55][1] = 137
Position[55][2] = 84
Position[55][3] = 156
Position[55][4] = 114
Position[55][5] = 140
Position[55][6] = 119
Position[55][7] = 160

# {
Position[56][0] = 114
Position[56][1] = 140
Position[56][2] = 119
Position[56][3] = 160
Position[56][4] = 142
Position[56][5] = 140
Position[56][6] = 148
Position[56][7] = 159

# }
Position[57][0] = 142
Position[57][1] = 140
Position[57][2] = 148
Position[57][3] = 159
Position[57][4] = 175
Position[57][5] = 142
Position[57][6] = 179
Position[57][7] = 162

# Space
Position[58][0] = 175
Position[58][1] = 142
Position[58][2] = 179
Position[58][3] = 162
Position[58][4] = 336
Position[58][5] = 145
Position[58][6] = 333
Position[58][7] = 169

# "
Position[59][0] = 336
Position[59][1] = 145
Position[59][2] = 333
Position[59][3] = 169
Position[59][4] = 369
Position[59][5] = 147
Position[59][6] = 365
Position[59][7] = 169

# Left
Position[60][0] = 369
Position[60][1] = 147
Position[60][2] = 365
Position[60][3] = 169
Position[60][4] = 402
Position[60][5] = 146
Position[60][6] = 397
Position[60][7] = 169

# Down
Position[61][0] = 402
Position[61][1] = 146
Position[61][2] = 397
Position[61][3] = 169
Position[61][4] = 434
Position[61][5] = 144
Position[61][6] = 428
Position[61][7] = 170

# Right
Position[62][0] = 434
Position[62][1] = 144
Position[62][2] = 428
Position[62][3] = 170
Position[62][4] = 466
Position[62][5] = 147
Position[62][6] = 459
Position[62][7] = 170

# Del
Position[63][0] = 466
Position[63][1] = 147
Position[63][2] = 459
Position[63][3] = 170
Position[63][4] = 498
Position[63][5] = 149
Position[63][6] = 487
Position[63][7] = 170


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
    for i in range(1, len(Position)):
        for j in l:
            cv.circle(frame, (Position[i][j], Position[i][j+1]), 2, (255, 255, 255), -1)

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
        if Position[i][0] < x < Position[i][6] and Position[i][5] < y < Position[i][3]:
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
