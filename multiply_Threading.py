import cv2 as cv
import threading as td
import time
from queue import Queue
import win32api
import win32con
import numpy as np


def Cap_job(x):
    cap = cv.VideoCapture(1)
    i = 0
    j = 0
    while True:
        ret, frame = cap.read()
        frame = frame[180:400, 60:700]
        cv.imshow("frame", frame)
        if cv.waitKey(1) == 27:
            break
        i = i + 1
        x.put(i)
        j = j + 1
        x.put(j)
    cap.release()
    cv.destroyAllWindows()


def other_job(x):
    while True:
        n = x.get()
        print('----')
        print(n)


if __name__ == '__main__':
    # q = Queue()
    # t1 = td.Thread(target=Cap_job, args=(q,))
    # t2 = td.Thread(target=other_job, args=(q,))
    # t1.start()
    # t2.start()
    # KeyValue = [0, 97, 98, 99, 100, 101, 102, 103, 104, 105, 96, 109, 107, 27, 81, 87, 69, 82, 84, 89, 85, 73, 79, 80,
    #             8,
    #             20, 9, 65, 83, 68, 70, 71, 72, 74, 75, 76, 186, 13, 160, 192, 220, 90, 88, 67, 86, 66, 78, 77, 188, 190,
    #             38, 191, 161, 17, 18, 91, 219, 221, 32, 222, 37, 40, 39, 46]
    #
    # win32api.keybd_event(KeyValue[53], 0, 0, 0)
    # win32api.keybd_event(KeyValue[54], 0, 0, 0)
    # win32api.keybd_event(KeyValue[63], 0, 0, 0)
    # win32api.keybd_event(KeyValue[53], 0, win32con.KEYEVENTF_KEYUP, 0)
    # win32api.keybd_event(KeyValue[54], 0, win32con.KEYEVENTF_KEYUP, 0)
    # win32api.keybd_event(KeyValue[63], 0, win32con.KEYEVENTF_KEYUP, 0)

    mask = np.ones([200, 200, 1], np.uint8)
    dst = cv.bitwise_not(mask)
    cv.circle(dst, (100, 100), 4, (150, 150, 150), -1)
    cv.imshow("mask", dst)

    cv.waitKey(0)
    # cv.destroyAllWindows()

'''

from queue import Queue
from threading import Thread
import time

_sentinel = object()

# A thread that produces data
def producer(out_q):
    n = 0
    while True:
        n += 1
        time.sleep(1)
        print("producer:",n)
        # 产生数据到队列里
        out_q.put(n)
        if n >= 5:
            #表示生产线程结束
            out_q.put(_sentinel)
            break
    print("producer done")

# A thread that consumes data
def consumer(in_q):
    while True:
        data = in_q.get()
        # 出来数据 the data
        if data is _sentinel:
            in_q.put(_sentinel)
            break
        else:
            print("consumer:",data)
    print("consumer done")

#设置共享的队列q,然后启动两个线程：消费者和生成者
q = Queue()
t1 = Thread(target=consumer, args=(q,))
t2 = Thread(target=producer, args=(q,))
t1.start()
t2.start()
'''