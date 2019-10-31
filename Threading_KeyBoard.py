import numpy as np
import cv2 as cv
import time
import KeyBoardPosion
import threading as td
from queue import Queue



def Trackbar(x):
    """
    创建滑动条
    :param x:None
    :return: None
    """
    pass


def Threshold(frame):
    """
    图像二值化
    :param frame:原图像
    :return: 二值化后的黑白两色图像
    """
    Sensitivity = cv.getTrackbarPos('Sen', 'Binary_Image')
    gray = cv.cvtColor(frame, cv.COLOR_RGB2GRAY)
    ret, binary_img = cv.threshold(gray, Sensitivity, 255, cv.THRESH_BINARY)    # 目测估计140-160比较好
    return binary_img


def Erode(frame):
    """
    图像形态学腐蚀
    :param frame:原图像
    :return: 腐蚀后的图像
    """
    kernel = cv.getStructuringElement(cv.RECURS_FILTER, (2, 2))
    erode_img = cv.erode(frame, kernel, iterations=1)
    cv.imshow("Binary_Image", erode_img)
    return erode_img


def Get_Posion(frame, flag):
    """
    给出单个手指按下或是多个手指按下的坐标
    :param frame: 图像
    :param flag: 标志位
    :return: 单个或多个手指的坐标
    """
    (cnts, _) = cv.findContours(frame.copy(), cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    # 无手指情况，发生概率极高
    # 为了防止图像漆黑一片，报错。并且可以让手指离开键盘时，停止按键扫描与输入。
    if not cnts:
        return

    # 单指情况
    if flag == 0:
        return Only_One_Finger(cnts, frame)
    # 多指情况
    else:
        return Two_or_More_Finger(cnts, frame)


def Only_One_Finger(cnt, frame):
    """
    一个手指按下的情况
    :param cnt: 手指轮廓子集
    :param frame: 图像
    :return: 单个手指的坐标
    """
    c = sorted(cnt, key=cv.contourArea, reverse=True)[0]
    # 计算最大轮廓的旋转边界盒
    rect = cv.minAreaRect(c)

    Key_Press_Position_X = np.int(rect[0][0])
    Key_Press_Position_Y = np.int(rect[0][1])

    cv.circle(frame, (Key_Press_Position_X, Key_Press_Position_Y), 4, (0, 155, 255), -1)
    key_value = KeyBoardPosion.KeyScan(Key_Press_Position_X, Key_Press_Position_Y)

    cv.imshow('image', frame)
    return key_value


def Two_or_More_Finger(cnts, frame):
    """
    两个手指按下的情况
    :param cnts: 多个手指轮廓子集
    :param frame: 图像
    :return: 多个手指的坐标
    """
    figure_num = 0
    finger_list = []

    # 获取实际按下手指的个数
    for cnt in cnts:
        M = cv.moments(cnt)

        # 无手指情况，一般不会发生
        if M['m10'] == 0 or M['m00'] == 0 or M['m01'] == 0:
            pass
        else:
            Key_Press_Position_X = int(M['m10'] / M['m00'])
            Key_Press_Position_Y = int(M['m01'] / M['m00'])
            cv.circle(frame, (Key_Press_Position_X, Key_Press_Position_Y), 4, (0, 155, 255), -1)

            key_value = KeyBoardPosion.KeyScan(Key_Press_Position_X, Key_Press_Position_Y)
            finger_list.append(key_value)

            figure_num += 1
            # 修改多指识别的按键数
            if figure_num > 1:
                break
    cv.imshow('image', frame)
    return finger_list


def main(key_in, flag_in, finger_out):
    """
    主函数
    :param key_in:主线程队列的键值 输入
    :param flag_in: 主线程队列的标志位 输入
    :param finger_out: 主线程队列手指个数 输出
    :return: 通过线程间队列通信
    """
    cap = cv.VideoCapture(1)
    cv.namedWindow('Binary_Image')
    cv.createTrackbar('Sen', 'Binary_Image', 160, 255, Trackbar)
    Finger_Flag = 0
    while True:
        ret, frame = cap.read()
        h, w, _ = frame.shape
        center = (w // 2, h // 2)
        M = cv.getRotationMatrix2D(center, -6.8, 1.0)

        rotated = cv.warpAffine(frame, M, (w, h), flags=cv.INTER_CUBIC, borderMode=cv.BORDER_REPLICATE)
        frame = rotated[220:400, 100:670]

        binary_image = Threshold(frame)
        erode_image = Erode(binary_image)
        key_value = Get_Posion(erode_image, Finger_Flag)

        if not key_value or key_value == 0:
            flag_in.put(0)
            key_value = 0
        else:
            flag_in.put(1)

        Finger_Flag = finger_out.get()

        key_in.put(key_value)

        # frame = KeyBoardPosion.debug_point(frame)
        cv.imshow("frame", frame)

        # 注意这里暂停时间是要和子线程一致
        time.sleep(0.15)

        if cv.waitKey(1) == 27:
            break

    cap.release()
    cv.destroyAllWindows()

if __name__ == '__main__':
    # 多线程键值队列
    Key = Queue()
    # 多线程是否按下标志位队列
    Down_flag = Queue()
    # 多线程多指标志位队列
    Fingers_Flag = Queue()

    t1 = td.Thread(target=main, args=(Key, Down_flag, Fingers_Flag,))
    t2 = td.Thread(target=KeyBoardPosion.KeyBoard_Output, args=(Key, Down_flag, Fingers_Flag,))

    t1.start()
    t2.start()



