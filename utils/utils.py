import time
from PySide2.QtCore import QThread
import random

# 随机数
def rnd(min: int, max: int):
    return random.randint(min, max)


# 随机返回序列中的一个元素
def rnd_choice(seq: list):
    return random.choice(seq)


# 间隔多少秒数
def delta_sec(start_sec: int, end_sec: int):
    gap_sec = end_sec - start_sec
    return gap_sec


# 间隔多少分钟
def delta_minute(start_sec: int, end_sec: int):
    gap_sec = end_sec - start_sec
    gap_min = gap_sec // 60
    return gap_min


# 线程阻塞毫秒
def msleep(min_ms: int, max_ms=None):
    if max_ms is None:
        t_ms = min_ms
    else:
        t_ms = rnd(min_ms, max_ms)
    QThread.msleep(t_ms)


# 时间串 转 时间戳, "2020-12-26 00:59:30" -> 1608915570
def time_str_to_time_stamp(time_str: str):
    format_time = time.strptime(time_str, "%Y-%m-%d %H:%M:%S")
    time_stamp = int(time.mktime(format_time))
    return time_stamp
