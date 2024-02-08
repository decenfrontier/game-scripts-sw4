from win32gui import GetWindowRect, SetWindowPos, SetForegroundWindow
from win32con import PROCESS_ALL_ACCESS, HWND_TOP, SWP_NOSIZE
from win32process import GetWindowThreadProcessId, TerminateProcess
from win32api import OpenProcess
from PySide2.QtWidgets import QApplication


def get_wnd_pos(hwnd):
    rect = GetWindowRect(hwnd)
    x, y = rect[0], rect[1]
    return x, y


def set_wnd_pos(hwnd, x, y):
    ret = SetWindowPos(hwnd, HWND_TOP, x, y, 0, 0, SWP_NOSIZE)
    return ret


def activate_wnd(hwnd):
    # pythoncom.CoInitialize()
    # 在该函数调用前，需要先发送一个其他键给屏幕，如ALT键, 否则可能报错
    # shell = Dispatch("WScript.Shell")
    # shell.SendKeys("%")  # 发送ALT键，ALT-%, CTRL-^, SHIFT-+, ENTER-~
    try:
        SetForegroundWindow(hwnd)
    except:
        pass


def terminate_wnd(hwnd):
    tid, pid = GetWindowThreadProcessId(hwnd)
    hProcess = OpenProcess(PROCESS_ALL_ACCESS, False, pid)
    TerminateProcess(hProcess, 0)


# 获取 主屏幕 宽高
def get_main_screen_wh():
    pri_screen = QApplication.primaryScreen()
    rect = pri_screen.geometry()
    w = rect.width()
    h = rect.height()
    return w, h


# 排列所有窗口
def arrange_all_wnd(idx):
    if idx == 0:
        return
    screen_w, screen_h = get_main_screen_wh()
    if screen_h <= 670 or screen_w <= 870:
        return
    # 获取 游戏窗口数
    wnd_num = 0
    for wk in settings.worker_list:
        if wk is None:
            continue
        wnd_num += 1
    if wnd_num < 2:
        return
    group_num = ((wnd_num - 1) // 5) + 1
    if idx == 1:  # 垂直排列
        # (group_num-1)*delta_x + 800(末窗宽) + 70(左侧预留) = screen_w
        delta_x = (screen_w - 870) // (group_num - 1) if group_num > 1 else 0
        for group in range(group_num):
            gap_num = 4 if group < group_num - 1 else (wnd_num - 1) % 5
            pos_x = 70 + group * delta_x
            # gap_num*delta_y + 600(末窗高) + 40(状态栏) + 30(末窗标题栏) = screen_h
            delta_y = (screen_h - 670) // gap_num if gap_num > 0 else 0
            start, end = group * 5, group * 5 + gap_num + 1
            for row in range(start, end):
                wk = settings.worker_list[row]
                pos_y = (row % 5) * delta_y
                set_wnd_pos(wk.hwnd, pos_x, pos_y)
                wk.x, wk.y = pos_x, pos_y

    elif idx == 2:  # 水平排列
        # (group_num-1)*delta_y + 600(末窗高) + 40(状态栏) + 30(末窗标题栏) = screen_h
        delta_y = (screen_h - 670) // (group_num - 1) if group_num > 1 else 0
        for group in range(group_num):
            gap_num = 4 if group < group_num - 1 else (wnd_num - 1) % 5
            pos_y = group * delta_y
            # gap_num*delta_x + 800(末窗宽) + 70(左侧预留) = screen_w
            delta_x = (screen_w - 870) // gap_num if gap_num > 0 else 0
            start, end = group * 5, group * 5 + gap_num + 1
            for row in range(start, end):
                wk = settings.worker_list[row]
                pos_x = 70 + (row % 5) * delta_x
                set_wnd_pos(wk.hwnd, pos_x, pos_y)
                wk.x, wk.y = pos_x, pos_y

    elif idx == 3:  # 斜排列
        delta_x = int((screen_w - 870) / (wnd_num - 1))
        delta_y = int((screen_h - 670) / (wnd_num - 1))
        for wk in settings.worker_list:
            if wk is None:
                continue
            pos_x = wk.row * delta_x + 70
            pos_y = wk.row * delta_y
            set_wnd_pos(wk.hwnd, pos_x, pos_y)
            wk.x, wk.y = pos_x, pos_y
