from PySide2.QtCore import QMutex, QMutexLocker
from const.const import DIR_RES, SLEEP_AFTER_CLICK, SLEEP_TIME
from utils.utils import msleep, rnd
from win32process import GetProcessTimes, WriteProcessMemory
from win32api import OpenProcess, GetModuleHandle

from utils.wnd import activate_wnd


class Lw():
    COM_NAME = 'lw.lwsoft3'
    def __init__(self, obj):
        # Com组件对象
        self.obj = obj
        # 线程锁
        self.mutex = QMutex(QMutex.Recursive)

    def set_path(self, path_res: str):
        # 设置资源路径
        self.obj.SetPath(path_res)

    def set_dict(self, idx: int, file_zk: str):
        # 设置字库序号, lw设置字库时可设置解密的pwd
        self.obj.SetDict(idx, file_zk, self.zk_pwd)

    def set_pic_pwd(self, pic_pwd=""):
        self.obj.SetPicPwd(pic_pwd.center(10, "*"))

    def set_dict_pwd(self, zk_pwd=""):
        self.zk_pwd = zk_pwd.center(10, "*")

    def bind_window(self, hwnd: str) -> bool:
        locker = QMutexLocker(self.mutex)
        ret = self.obj.BindWindow(
            hwnd, mode_display, mode_mouse, mode_keypad, mode_public, mode_back)
        if ret:  # 绑定窗口成功后激活窗口才能运行
            activate_wnd(hwnd)
        return ret

    # 获取子窗口句柄, 没找到返回0
    def get_son_hwnd(self, hwnd: int) -> int:
        locker = QMutexLocker(self.mutex)
        son = self.obj.GetSonWindow(hwnd)
        if son == 0:
            return 0
        son_son = self.obj.GetSonWindow(son)
        son_son_son = self.obj.GetSonWindow(son_son)
        return son_son_son

    def unbind_window(self):
        locker = QMutexLocker(self.mutex)
        self.obj.UnBindWindow()

    # 切换绑定检测窗口
    def switch_bind_detect_window(self, hwnd: int):
        locker = QMutexLocker(self.mutex)
        self.obj.UnBindWindow()
        gdi, windows3, windows = 1, 2, 1
        self.obj.BindWindow(hwnd, gdi, windows3, windows, 0, 0)

    # 切换绑定游戏窗口
    def switch_bind_game_window(self, hwnd: int):
        locker = QMutexLocker(self.mutex)
        self.obj.UnBindWindow()
        self.obj.BindWindow(hwnd, mode_display, mode_mouse,
                            mode_keypad, mode_public, mode_back)
        activate_wnd(hwnd)  # 过完验证要激活窗口

    def lock_input(self, state: str):
        locker = QMutexLocker(self.mutex)
        map_dict = {"关闭锁定": 0, "锁定键鼠": 1, "锁定鼠标": 2, "锁定键盘": 3}
        flag = map_dict[state]
        self.obj.LockInput(flag)

    def capture(self, x1, y1, x2, y2, save_path):
        # type: (int, int, int, int, str) -> None
        locker = QMutexLocker(self.mutex)
        self.obj.Capture(x1, y1, x2, y2, save_path)

    # 获取通配符对应的文件集合，每个图片以|分割
    def match_pic(self, pic: str, dir="") -> str:
        locker = QMutexLocker(self.mutex)
        if dir != "":  # 设置指定路径
            self.obj.SetPath(dir)
        ret = self.obj.MatchPicName(pic)
        if dir != "":  # 设置回原路径
            self.obj.SetPath(DIR_RES)
        return ret

    # 枚举窗口, 枚举到返回一个整数列表, 没枚举出返回空列表
    def enum_window(self) -> [int]:
        locker = QMutexLocker(self.mutex)
        hwnds = self.obj.EnumWindow(WND_TITLE, WND_CLASS, PROC_NAME)
        if hwnds is None or hwnds == "":
            return []
        hwnd_list = hwnds.split(",")
        ret_list = [int(hwnd) for hwnd in hwnd_list]

        # lw还需要判断窗口进程创建时间来对窗口排序
        time_hwnd_dict = {}
        for hwnd in ret_list:
            pid = self.obj.GetWindowProcessId(hwnd)
            hProcess = OpenProcess(PROCESS_ALL_ACCESS, False, pid)
            time_dict = GetProcessTimes(hProcess)
            # pywintypes.datetime(2020, 12, 26, 0, 59, 33, 948000, tzinfo=TimeZoneInfo('GMT Standard Time', True))
            create_time = time_dict["CreationTime"]
            time_str = str(create_time)  # "2020-12-26 00:59:33.948000+00:00"
            time_str = time_str[:19]  # "2020-12-26 00:59:33"
            time_hwnd_dict[time_str] = hwnd
        time_list = [time_str for time_str in time_hwnd_dict]
        time_list.sort()
        ret_list = []
        for time_str in time_list:
            hwnd = time_hwnd_dict[time_str]
            ret_list.append(hwnd)
        return ret_list

    # 设置显示输入, 若mode="pic", 则xxx~"C\1.bmp", 若mode="mem", 则xxx~"addr"
    def set_display_input(self, mode: str, xxx=""):
        locker = QMutexLocker(self.mutex)
        if mode not in ("screen", "pic", "mem"):
            return
        if mode in ("pic", "mem"):
            self.obj.SetDisplayInput(xxx)
        else:
            self.obj.SetDisplayInput("0")

    # 插件版本号
    def ver(self):
        locker = QMutexLocker(self.mutex)
        ret = self.obj.ver()
        return ret

    # 启用真实鼠标
    def enable_real_mouse(self, enable: bool, delay=16, step=64):
        locker = QMutexLocker(self.mutex)
        if enable:
            self.obj.EnableRealMouse(1, delay, step)
        else:
            self.obj.EnableRealMouse(0, delay, step)

    # 显示错误信息
    def show_error_msg(self, show: bool):
        locker = QMutexLocker(self.mutex)
        self.obj.SetShowErrorMsg(show)

    # 禁用系统睡眠
    def ban_sys_sleep(self):
        locker = QMutexLocker(self.mutex)
        self.obj.DisablePowerSave()

    # 禁用屏幕保护
    def ban_screen_protect(self):
        locker = QMutexLocker(self.mutex)
        self.obj.DisableScreenSave()

    # 关机
    def exit_os(self):
        locker = QMutexLocker(self.mutex)
        self.obj.ExitOs(1)

    # ------------------------ 鼠标相关 ------------------------
    def move_to(self, x: int, y: int, is_delay=True):
        locker = QMutexLocker(self.mutex)
        self.obj.MoveTo(x, y)
        if is_delay:
            msleep(SLEEP_TIME)

    # 相对移动
    def move_relative(self, rx: int, ry: int):
        locker = QMutexLocker(self.mutex)
        self.obj.MoveR(rx, ry)

    def re_move(self, x=-1, y=-1):
        locker = QMutexLocker(self.mutex)
        if (x, y) == (-1, -1):
            x = 5 + rnd(0, 60)
            y = 45 + rnd(0, 8)
        self.obj.MoveTo(x, y)

    def left_down(self):
        locker = QMutexLocker(self.mutex)
        self.obj.LeftDown()
        msleep(SLEEP_TIME)

    def left_up(self):
        locker = QMutexLocker(self.mutex)
        self.obj.LeftUp()
        msleep(SLEEP_TIME)

    def left_click(self, re_move=True):
        locker = QMutexLocker(self.mutex)
        self.obj.LeftClick()
        msleep(SLEEP_AFTER_CLICK)
        if re_move:
            self.re_move()

    def left_db_click(self, re_move=True):
        locker = QMutexLocker(self.mutex)
        self.obj.LeftDoubleClick()
        msleep(SLEEP_AFTER_CLICK)
        if re_move:
            self.re_move()

    def right_click(self, re_move=True):
        locker = QMutexLocker(self.mutex)
        self.obj.RightClick()
        msleep(SLEEP_AFTER_CLICK)
        if re_move:
            self.re_move()

    def move_click(self, x, y, re_move=True):
        # type: (int, int, bool) -> None
        locker = QMutexLocker(self.mutex)
        self.move_to(x, y)
        self.left_click(re_move)

    def move_r_click(self, x, y, is_delay=True, re_move=True):
        # type: (int, int, bool, bool) -> None
        locker = QMutexLocker(self.mutex)
        self.move_to(x, y, is_delay)
        self.right_click(re_move)

    def move_db_click(self, x, y, re_move=True):
        # type: (int, int, bool) -> None
        locker = QMutexLocker(self.mutex)
        self.move_to(x, y)
        self.left_db_click(re_move)

    def move_wheel_down(self, x, y, count=1, re_move=True):
        # type: (int, int, int, bool) -> None
        locker = QMutexLocker(self.mutex)
        self.move_to(x, y)
        for i in range(count):
            self.obj.WheelDown()
            msleep(10)
        if re_move:
            self.re_move()

    def move_wheel_up(self, x, y, count=1, re_move=True):
        # type: (int, int, int, bool) -> None
        locker = QMutexLocker(self.mutex)
        self.move_to(x, y)
        for i in range(count):
            self.obj.WheelUp()
            msleep(10)
        if re_move:
            self.re_move()

    def move_drag_to(self, x0, y0, x, y, re_move=True):
        # type: (int, int, int, int, bool) -> None
        locker = QMutexLocker(self.mutex)
        self.move_to(x0, y0)
        msleep(SLEEP_TIME)
        self.left_down()
        self.move_to(x, y)
        msleep(SLEEP_TIME)
        self.left_up()
        if re_move:
            self.re_move()

    # ------------------------ 键盘相关 ------------------------
    def key_press(self, vk_code, num=1, delay=10):
        # type: (int, int, int) -> None
        locker = QMutexLocker(self.mutex)
        for i in range(num):
            self.obj.KeyPress(vk_code)
            msleep(delay)

    # 发送ASCII字符串
    def key_press_str(self, asc_str):
        locker = QMutexLocker(self.mutex)
        self.obj.KeyPressStr(asc_str, 25)

    # 按组合键
    def key_press_combo(self, vk_state: int, vk_code: int):
        locker = QMutexLocker(self.mutex)
        self.obj.KeyDown(vk_state)
        msleep(10, 30)
        self.obj.KeyPress(vk_code)
        msleep(10, 30)
        self.obj.KeyUp(vk_state)

    # 按下键
    def key_down(self, vk_code: int):
        locker = QMutexLocker(self.mutex)
        self.obj.KeyDown(vk_code)

    # 抬起键
    def key_up(self, vk_code: int):
        locker = QMutexLocker(self.mutex)
        self.obj.KeyUp(vk_code)

    # 发送任意字符串
    def send_string(self, string):
        locker = QMutexLocker(self.mutex)
        self.obj.SendString(string, 1)  # lw默认向绑定的窗口发送, 用模式2

    # ------------------------ 找图相关 ------------------------
    # 找图, 找到返回True, 未找到返回False
    def find_pic(self, x1, y1, x2, y2, pic, delta_color="101010", sim=0.95, order=0, timeout=0):
        # type: (int, int, int, int, str, str, float, int, int) -> bool
        locker = QMutexLocker(self.mutex)
        while True:
            ret = self.obj.FindPic(x1, y1, x2, y2, pic,
                                   delta_color, sim, order)
            if ret or timeout <= 0:
                break
            msleep(SLEEP_TIME)
            timeout -= SLEEP_TIME
        return ret

    # 找图扩展, 同时找多个图, 得到形如[(0,100,20), (1,30,40)]的列表
    def find_pic_ex(self, x1, y1, x2, y2, pic, delta_color="101010", sim=0.95, order=0, timeout=0):
        # type: (int, int, int, int, str, str, float, int, int) -> []
        locker = QMutexLocker(self.mutex)
        while True:
            ret_str = self.obj.FindPicEx(
                x1, y1, x2, y2, pic, delta_color, sim, order)
            if ret_str or timeout <= 0:
                break
            msleep(SLEEP_TIME)
            timeout -= SLEEP_TIME
        # "1,100,20|2,30,40" -> [(0,100,20), (1,30,40)]
        ret_list = []
        if ret_str:
            pos_list = ret_str.split("|")  # ["1,100,20", "2,30,40"]
            for pos in pos_list:  # "1,100,20"
                kk = pos.split(",")  # ["1", "100", "20"]
                idx, x, y = int(kk[0]) - 1, int(kk[1]), int(kk[2])
                ret_list.append((idx, x, y))
        return ret_list

    # 找图左键点击, 找到返回True, 未找到返回False
    def find_pic_click(self, x1, y1, x2, y2, pic, delta_color="101010", sim=0.95, order=0, timeout=0):
        # type: (int, int, int, int, str, str, float, int, int) -> bool
        locker = QMutexLocker(self.mutex)
        while True:
            ret = self.obj.FindPic(x1, y1, x2, y2, pic,
                                   delta_color, sim, order)
            if ret or timeout <= 0:
                break
            msleep(SLEEP_TIME)
            timeout -= SLEEP_TIME
        if ret:
            self.move_click(self.obj.x() + rnd(2, 4), self.obj.y() + rnd(2, 4))
        return ret

    # 找图右键点击, 找到返回True, 未找到返回False
    def find_pic_r_click(self, x1, y1, x2, y2, pic, delta_color="101010", sim=0.95, order=0, timeout=0):
        # type: (int, int, int, int, str, str, float, int, int) -> bool
        locker = QMutexLocker(self.mutex)
        while True:
            ret = self.obj.FindPic(x1, y1, x2, y2, pic,
                                   delta_color, sim, order)
            if ret or timeout <= 0:
                break
            msleep(SLEEP_TIME)
            timeout -= SLEEP_TIME
        if ret:
            self.move_r_click(self.obj.x() + rnd(2, 4),
                              self.obj.y() + rnd(2, 4))
        return ret

    # 找图左键双击, 找到返回True, 未找到返回False
    def find_pic_db_click(self, x1, y1, x2, y2, pic, delta_color="101010", sim=0.95, order=0, timeout=0):
        # type: (int, int, int, int, str, str, float, int, int) -> bool
        locker = QMutexLocker(self.mutex)
        while True:
            ret = self.obj.FindPic(x1, y1, x2, y2, pic,
                                   delta_color, sim, order)
            if ret or timeout <= 0:
                break
            msleep(SLEEP_TIME)
            timeout -= SLEEP_TIME
        if ret:
            self.move_db_click(self.obj.x() + rnd(2, 4),
                               self.obj.y() + rnd(2, 4))
        return ret

    # 找图shift+鼠标右击, 找到返回True, 未找到返回False
    def find_pic_shift_r_click(self, x1, y1, x2, y2, pic, delta_color="101010", sim=0.95, order=0, timeout=0):
        # type: (int, int, int, int, str, str, float, int, int) -> bool
        locker = QMutexLocker(self.mutex)
        while True:
            ret = self.obj.FindPic(x1, y1, x2, y2, pic,
                                   delta_color, sim, order)
            if ret or timeout <= 0:
                break
            msleep(SLEEP_TIME)
            timeout -= SLEEP_TIME
        if ret:
            VK_SHIFT = 16
            self.key_down(VK_SHIFT)
            self.move_r_click(self.obj.x() + rnd(2, 4),
                              self.obj.y() + rnd(2, 4))
            self.key_up(VK_SHIFT)
        return ret

    # 返回图片所在窗口的坐标, 没找到返回-1,-1
    def get_pic_pos(self, x1, y1, x2, y2, pic, delta_color="101010", sim=0.95, order=0, timeout=0):
        # type: (int, int, int, int, str, str, float, int, int) -> (int, int)
        locker = QMutexLocker(self.mutex)
        while True:
            ret = self.obj.FindPic(x1, y1, x2, y2, pic,
                                   delta_color, sim, order)
            if ret or timeout <= 0:
                break
            msleep(SLEEP_TIME)
            timeout -= SLEEP_TIME
        ret_x, ret_y = -1, -1
        if ret:
            ret_x, ret_y = self.obj.x(), self.obj.y()
        return ret_x, ret_y

    # 返回找到的图片的序号,从0开始索引.如果没找到返回-1
    def get_pic_idx(self, x1, y1, x2, y2, pic, delta_color="101010", sim=0.95, order=0, timeout=0):
        # type: (int, int, int, int, str, str, float, int, int) -> int
        locker = QMutexLocker(self.mutex)
        while True:
            ret = self.obj.FindPic(x1, y1, x2, y2, pic,
                                   delta_color, sim, order)
            if ret or timeout <= 0:
                break
            msleep(SLEEP_TIME)
            timeout -= SLEEP_TIME
        if not ret:  # self.obj.idx()可能不会自动置为-1
            return -1
        return self.obj.idx() - 1  # lw插件内的所有序号都是从1开始数的

    # 返回找到的图片的数量
    def get_pic_num(self, x1, y1, x2, y2, pic, delta_color="101010", sim=0.95, order=0, timeout=0):
        # type: (int, int, int, int, str, str, float, int, int) -> int
        tuple_list = self.find_pic_ex(
            x1, y1, x2, y2, pic, delta_color, sim, order, timeout)
        ret = len(tuple_list)
        return ret

    # 返回找到的图片名"物_驱魔香", 未找到返回""(注意:没有图片后缀名)
    def get_pic_name(self, x1, y1, x2, y2, pic, delta_color="101010", sim=0.95, order=0, timeout=0, dir=""):
        # type: (int, int, int, int, str, str, float, int, int, str) -> str
        locker = QMutexLocker(self.mutex)
        if dir != "":  # 设置指定路径
            self.obj.SetPath(dir)
        while True:
            ret = self.obj.FindPic(x1, y1, x2, y2, pic,
                                   delta_color, sim, order)
            if ret or timeout <= 0:
                break
            msleep(SLEEP_TIME)
            timeout -= SLEEP_TIME
        ret_str = ""
        if ret:
            ret_str = self.obj.GetFindedPicName()
            ret_str = ret_str.rstrip(".bmp")
        if dir != "":  # 设置回原路径
            self.obj.SetPath(DIR_RES)
        return ret_str

    # 找出距离某点最近的图片位置
    def find_pic_nearest_pos(self, x1, y1, x2, y2, pic, cx, cy, delta_color="101010", sim=0.95, order=0,
                             timeout=0):
        # type: (int, int, int, int, str, int, int, str, float, int, int) -> (int, int)
        locker = QMutexLocker(self.mutex)
        while True:
            all_pos = self.obj.FindPicEx(
                x1, y1, x2, y2, pic, delta_color, sim, order)
            if all_pos or timeout <= 0:
                break
            msleep(SLEEP_TIME)
            timeout -= SLEEP_TIME
        ret_x, ret_y = -1, -1
        if all_pos:
            id_x_y = self.obj.FindNearestPos(all_pos, 0, cx, cy)  # "0,100,200"
            _, ret_x, ret_y = id_x_y.split(",")
            ret_x, ret_y = int(ret_x), int(ret_y)
        return ret_x, ret_y

    # ------------------------ 找色相关 ------------------------
    # 找色, 找到返回True, 未找到返回False
    def find_color(self, x1, y1, x2, y2, color, sim=1.0, order=0, timeout=0):
        # type: (int, int, int, int, str, float, int, int) -> bool
        locker = QMutexLocker(self.mutex)
        while True:
            ret = self.obj.FindColor(x1, y1, x2, y2, color, sim, order)
            if ret or timeout <= 0:
                break
            msleep(SLEEP_TIME)
            timeout -= SLEEP_TIME
        return ret

    # 找色左键点击, 找到返回True, 未找到返回False
    def find_color_click(self, x1, y1, x2, y2, color, sim=1.0, order=0, timeout=0):
        # type: (int, int, int, int, str, float, int, int) -> bool
        locker = QMutexLocker(self.mutex)
        while True:
            ret = self.obj.FindColor(x1, y1, x2, y2, color, sim, order)
            if ret or timeout <= 0:
                break
            msleep(SLEEP_TIME)
            timeout -= SLEEP_TIME
        if ret:
            self.move_click(self.obj.x() + rnd(2, 4), self.obj.y() + rnd(2, 4))
        return ret

    # 返回颜色所在窗口坐标, 没找到返回-1,-1
    def get_color_pos(self, x1, y1, x2, y2, color, sim=1.0, order=0, timeout=0):
        # type: (int, int, int, int, str, float, int, int) -> (int, int)
        locker = QMutexLocker(self.mutex)
        while True:
            ret = self.obj.FindColor(x1, y1, x2, y2, color, sim, order)
            if ret or timeout <= 0:
                break
            msleep(SLEEP_TIME)
            timeout -= SLEEP_TIME
        ret_x, ret_y = -1, -1
        if ret:
            ret_x, ret_y = self.obj.x(), self.obj.y()
        return ret_x, ret_y

    # 返回指定坐标的颜色, "RRGGBB"全小写
    def get_pos_color(self, x: int, y: int):
        locker = QMutexLocker(self.mutex)
        ret = self.obj.GetColor(x, y)
        return ret

    # ------------------------ 文字相关 ------------------------
    # 找字, 找到返回True, 未找到返回False
    def find_str(self, x1, y1, x2, y2, string, color, sim=0.95, zk=0, timeout=0):
        # type: (int, int, int, int, str, str, float, int, int) -> bool
        locker = QMutexLocker(self.mutex)
        self.obj.UseDict(zk)
        while True:
            ret = self.obj.FindStrFast(x1, y1, x2, y2, string, color, sim)
            if ret or timeout <= 0:
                break
            msleep(SLEEP_TIME)
            timeout -= SLEEP_TIME
        return ret

    # 找字扩展, 找到形如[(0,100,20), (1,30,40)]的列表, 一个都没找到返回[]
    def find_str_ex(self, x1, y1, x2, y2, string, color, sim=0.95, zk=0, timeout=0):
        # type: (int, int, int, int, str, str, float, int, int) -> []
        locker = QMutexLocker(self.mutex)
        self.obj.UseDict(zk)
        while True:
            ret_str = self.obj.FindStrFastEx(
                x1, y1, x2, y2, string, color, sim)
            if ret_str or timeout <= 0:
                break
            msleep(SLEEP_TIME)
            timeout -= SLEEP_TIME
        # "1,100,20|2,30,40" -> [(0,100,20), (1,30,40)]
        ret_list = []
        if ret_str:
            pos_list = ret_str.split("|")  # ["1,100,20", "2,30,40"]
            for pos in pos_list:
                kk = pos.split(",")  # ["1", "100", "20"]
                idx, x, y = int(kk[0]) - 1, int(kk[1]), int(kk[2])
                ret_list.append((idx, x, y))
        return ret_list

    # 找字左键点击, 找到返回True, 未找到返回False
    def find_str_click(self, x1, y1, x2, y2, string, color, sim=0.95, zk=0, timeout=0):
        # type: (int, int, int, int, str, str, float, int, int) -> bool
        locker = QMutexLocker(self.mutex)
        self.obj.UseDict(zk)
        while True:
            ret = self.obj.FindStrFast(x1, y1, x2, y2, string, color, sim)
            if ret or timeout <= 0:
                break
            msleep(SLEEP_TIME)
            timeout -= SLEEP_TIME
        if ret:
            self.move_click(self.obj.x() + rnd(2, 4), self.obj.y() + rnd(2, 4))
        return ret

    # 返回字所在窗口坐标, 没找到返回-1,-1
    def get_str_pos(self, x1, y1, x2, y2, string, color, sim=0.95, zk=0, timeout=0):
        # type: (int, int, int, int, str, str, float, int, int) -> (int, int)
        locker = QMutexLocker(self.mutex)
        self.obj.UseDict(zk)
        while True:
            ret = self.obj.FindStrFast(x1, y1, x2, y2, string, color, sim)
            if ret or timeout <= 0:
                break
            msleep(SLEEP_TIME)
            timeout -= SLEEP_TIME
        ret_x, ret_y = -1, -1
        if ret:
            ret_x, ret_y = self.obj.x(), self.obj.y()
        return ret_x, ret_y

    # 找出距离某点最近的字位置
    def find_str_nearest_pos(self, x1, y1, x2, y2, string, color, cx, cy, sim=0.95, zk=0, timeout=0):
        # type: (int, int, int, int, str, str, int, int, float, int, int) -> (int, int)
        locker = QMutexLocker(self.mutex)
        self.obj.UseDict(zk)
        while True:
            all_pos = self.obj.FindStrFastEx(
                x1, y1, x2, y2, string, color, sim)
            if all_pos or timeout <= 0:
                break
            msleep(SLEEP_TIME)
            timeout -= SLEEP_TIME
        ret_x, ret_y = -1, -1
        if all_pos:
            id_x_y = self.obj.FindNearestPos(all_pos, 0, cx, cy)  # "0,100,200"
            _, ret_x, ret_y = id_x_y.split(",")
            ret_x, ret_y = int(ret_x), int(ret_y)
        return ret_x, ret_y

    # 识别文字, 未识别出返回""
    def ocr(self, x1, y1, x2, y2, color, sim=1.0, zk=0, timeout=0):
        # type: (int, int, int, int, str, float, int, int) -> str
        locker = QMutexLocker(self.mutex)
        self.obj.UseDict(zk)
        while True:
            ret_str = self.obj.Ocr(x1, y1, x2, y2, color, sim)  # 未识别出返回None
            if ret_str or timeout <= 0:
                break
            msleep(SLEEP_TIME)
            timeout -= SLEEP_TIME
        if ret_str is None:
            ret_str = ""
        return ret_str


class Dm():
    COM_NAME = 'dm.dmsoft'
    def __init__(self, obj: BaseObj):
        # com组件对象
        self.obj = obj
        # 线程锁
        self.mutex = QMutex(QMutex.Recursive)

    def reg(self, reg_code: str, add_code: str) -> bool:
        ret = self.obj.Reg(reg_code, add_code+"q")
        return ret

    # 版本号
    def ver(self):
        locker = QMutexLocker(self.mutex)
        ret = self.obj.Ver()
        return ret

    def set_path(self, path_res: str):
        # 设置资源路径
        self.obj.SetPath(path_res)

    def set_dict(self, idx: int, file_zk: str, zk_pwd=""):
        # 设置字库序号
        self.obj.SetDict(idx, file_zk)

    def set_pic_pwd(self, pic_pwd=""):
        pic_pwd = pic_pwd.center(10, "*")
        self.obj.SetPicPwd(pic_pwd)

    def set_dict_pwd(self, zk_pwd=""):
        zk_pwd = zk_pwd.center(10, "*")
        self.obj.SetDictPwd(zk_pwd)

    # 绑定成功, 返回1, 未绑定成功, 返回错误码
    def bind_window(self, hwnd: int) -> int:
        locker = QMutexLocker(self.mutex)
        ret = self.obj.BindWindowEx(
            hwnd, mode_display, mode_mouse, mode_keypad, mode_public, mode_back)
        if ret == 1:  # 绑定窗口成功后激活窗口才能运行
            activate_wnd(hwnd)
        else:
            ret = self.obj.GetLastError()
        return ret

    # 获取子窗口句柄, 没找到返回0
    def get_son_hwnd(self, hwnd: int) -> int:
        locker = QMutexLocker(self.mutex)
        son = self.obj.GetWindow(hwnd, 1)
        if son == 0:
            return 0
        son_son = self.obj.GetWindow(son, 1)
        son_son_son = self.obj.GetWindow(son_son, 1)
        return son_son_son

    def unbind_window(self):
        locker = QMutexLocker(self.mutex)
        self.obj.UnBindWindow()

    # 切换绑定检测窗口
    def switch_bind_detect_window(self, hwnd: int):
        locker = QMutexLocker(self.mutex)
        self.obj.UnBindWindow()
        self.obj.BindWindow(hwnd, "gdi", "windows", "windows", 0)

    # 切换绑定游戏窗口
    def switch_bind_game_window(self, hwnd: int):
        locker = QMutexLocker(self.mutex)
        self.obj.UnBindWindow()
        self.obj.BindWindowEx(hwnd, mode_display, mode_mouse,
                              mode_keypad, mode_public, mode_back)
        activate_wnd(hwnd)  # 过完验证要激活窗口

    def lock_input(self, state: str):
        locker = QMutexLocker(self.mutex)
        map_dict = {"关闭锁定": 0, "锁定键鼠": 1, "锁定鼠标": 2, "锁定键盘": 3}
        flag = map_dict[state]
        self.obj.LockInput(flag)

    # 截图bmp
    def capture(self, x1, y1, x2, y2, save_path):
        # type: (int, int, int, int, str) -> None
        locker = QMutexLocker(self.mutex)
        self.obj.Capture(x1, y1, x2, y2, save_path)

    # 获取通配符对应的文件集合，每个图片以|分割
    def match_pic(self, pic: str, dir="") -> str:
        locker = QMutexLocker(self.mutex)
        if dir != "":  # 设置指定路径
            self.obj.SetPath(dir)
        ret = self.obj.MatchPicName(pic)
        if dir != "":  # 设置回原路径
            self.obj.SetPath(DIR_RES)
        return ret

    # 枚举窗口, 枚举到返回一个整数列表, 没枚举出返回空列表
    def enum_window(self) -> [int, ...]:
        locker = QMutexLocker(self.mutex)
        hwnds = self.obj.EnumWindowByProcess(
            PROC_NAME, WND_TITLE, WND_CLASS, 1 + 2 + 8 + 32)
        if hwnds is None or hwnds == "":
            return []
        hwnd_list = hwnds.split(",")
        hwnd_list = [int(hwnd) for hwnd in hwnd_list]
        return hwnd_list

    # 设置显示输入, 若mode="pic", 则xxx~"C\1.bmp", 若mode="mem", 则xxx~"addr,size"
    def set_display_input(self, mode: str, xxx=""):
        locker = QMutexLocker(self.mutex)
        if mode not in ("screen", "pic", "mem"):
            return
        if mode == "pic":
            self.obj.SetDisplayInput(f"pic:{xxx}")
        elif mode == "mem":
            self.obj.SetDisplayInput(f"mem:{xxx}")
        else:
            self.obj.SetDisplayInput("screen")

    # 启用真实鼠标
    def enable_real_mouse(self, enable: bool, delay=16, step=64):
        locker = QMutexLocker(self.mutex)
        if enable:
            self.obj.EnableRealMouse(2, delay, step)
        else:
            self.obj.EnableRealMouse(0, delay, step)

    # 显示错误信息
    def show_error_msg(self, show: bool):
        locker = QMutexLocker(self.mutex)
        self.obj.SetShowErrorMsg(show)

    # 禁用系统睡眠
    def ban_sys_sleep(self):
        locker = QMutexLocker(self.mutex)
        self.obj.DisablePowerSave()

    # 禁用屏幕保护
    def ban_screen_protect(self):
        locker = QMutexLocker(self.mutex)
        self.obj.DisableScreenSave()

    # 关机
    def exit_os(self):
        locker = QMutexLocker(self.mutex)
        self.obj.ExitOs(1)

    #  ------------------------- 鼠标相关 -------------------------
    def move_to(self, x: int, y: int, is_delay=True):
        locker = QMutexLocker(self.mutex)
        self.obj.MoveTo(x, y)
        if is_delay:
            msleep(SLEEP_TIME)

    # 相对移动
    def move_relative(self, rx: int, ry: int):
        locker = QMutexLocker(self.mutex)
        self.obj.MoveR(rx, ry)

    def re_move(self, x=-1, y=-1):
        locker = QMutexLocker(self.mutex)
        if (x, y) == (-1, -1):
            x = 5 + rnd(0, 60)
            y = 45 + rnd(0, 8)
        self.obj.MoveTo(x, y)

    def left_down(self):
        locker = QMutexLocker(self.mutex)
        self.obj.LeftDown()
        msleep(SLEEP_TIME)

    def left_up(self):
        locker = QMutexLocker(self.mutex)
        self.obj.LeftUp()
        msleep(SLEEP_TIME)

    def left_click(self, re_move=True):
        locker = QMutexLocker(self.mutex)
        self.obj.LeftClick()
        msleep(SLEEP_AFTER_CLICK)
        if re_move:
            self.re_move()

    def left_db_click(self, re_move=True):
        locker = QMutexLocker(self.mutex)
        self.obj.LeftClick()
        msleep(SLEEP_TIME)
        self.obj.LeftClick()
        if re_move:
            self.re_move()

    def right_click(self, re_move=True):
        locker = QMutexLocker(self.mutex)
        self.obj.RightClick()
        msleep(SLEEP_AFTER_CLICK)
        if re_move:
            self.re_move()

    def move_click(self, x, y, re_move=True):
        # type: (int, int, bool) -> None
        locker = QMutexLocker(self.mutex)
        self.move_to(x, y)
        self.left_click(re_move)

    def move_r_click(self, x, y, is_delay=True, re_move=True):
        # type: (int, int, bool, bool) -> None
        locker = QMutexLocker(self.mutex)
        self.move_to(x, y, is_delay)
        self.right_click(re_move)

    def move_db_click(self, x, y, re_move=True):
        # type: (int, int, bool) -> None
        locker = QMutexLocker(self.mutex)
        self.move_to(x, y)
        self.left_db_click(re_move)

    def move_wheel_down(self, x, y, count=1, re_move=True):
        # type: (int, int, int, bool) -> None
        locker = QMutexLocker(self.mutex)
        self.move_to(x, y)
        for i in range(count):
            self.obj.WheelDown()
            msleep(10)
        if re_move:
            self.re_move()

    def move_wheel_up(self, x, y, count=1, re_move=True):
        # type: (int, int, int, bool) -> None
        locker = QMutexLocker(self.mutex)
        self.move_to(x, y)
        for i in range(count):
            self.obj.WheelUp()
            msleep(10)
        if re_move:
            self.re_move()

    def move_drag_to(self, x0, y0, x, y, re_move=True):
        # type: (int, int, int, int, bool) -> None
        locker = QMutexLocker(self.mutex)
        self.move_to(x0, y0)
        msleep(SLEEP_TIME)
        self.left_down()
        self.move_to(x, y)
        msleep(SLEEP_TIME)
        self.left_up()
        if re_move:
            self.re_move()

    # ------------------------- 键盘相关 -------------------------
    def key_press(self, vk_code: int, num=1, delay=10):
        locker = QMutexLocker(self.mutex)
        for i in range(num):
            self.obj.KeyPress(vk_code)
            msleep(delay)

    # 发送ASCII字符串
    def key_press_str(self, asc_str):
        locker = QMutexLocker(self.mutex)
        self.obj.KeyPressStr(asc_str, 25)

    # 按组合键
    def key_press_combo(self, vk_state: int, vk_code: int):
        locker = QMutexLocker(self.mutex)
        self.obj.KeyDown(vk_state)
        msleep(10, 30)
        self.obj.KeyPress(vk_code)
        msleep(10, 30)
        self.obj.KeyUp(vk_state)

    # 按下键
    def key_down(self, vk_code: int):
        locker = QMutexLocker(self.mutex)
        self.obj.KeyDown(vk_code)

    # 抬起键
    def key_up(self, vk_code: int):
        locker = QMutexLocker(self.mutex)
        self.obj.KeyUp(vk_code)

    # 发送任意字符串
    def send_string(self, string):
        locker = QMutexLocker(self.mutex)
        hwnd = self.obj.GetBindWindow()
        self.obj.SendString(hwnd, string)

    # ------------------------- 找图相关 -------------------------
    # 找图, 找到返回True, 未找到返回False
    def find_pic(self, x1, y1, x2, y2, pic, delta_color="101010", sim=0.95, order=0, timeout=0):
        # type: (int, int, int, int, str, str, float, int, int) -> bool
        locker = QMutexLocker(self.mutex)
        while True:
            # ret = (0, 43, 31)  或 (-1, -1, -1)
            ret = self.obj.FindPic(x1, y1, x2, y2, pic,
                                   delta_color, sim, order)
            if ret[0] >= 0 or timeout <= 0:
                break
            msleep(SLEEP_TIME)
            timeout -= SLEEP_TIME
        ret = True if ret[0] >= 0 else False
        return ret

    # 找图扩展, 同时找多个图, 得到形如[(0,100,20), (1,30,40)]的列表, 一个都未找到返回[]
    def find_pic_ex(self, x1, y1, x2, y2, pic, delta_color="101010", sim=0.95, order=0, timeout=0):
        # type: (int, int, int, int, str, str, float, int, int) -> []
        locker = QMutexLocker(self.mutex)
        while True:
            ret_str = self.obj.FindPicEx(
                x1, y1, x2, y2, pic, delta_color, sim, order)
            if ret_str or timeout <= 0:
                break
            msleep(SLEEP_TIME)
            timeout -= SLEEP_TIME
        # "0,100,20|1,30,40" -> [(0,100,20), (1,30,40)]
        ret_list = []
        if ret_str:
            pos_list = ret_str.split("|")  # ["1,100,20", "2,30,40"]
            for pos in pos_list:  # "1,100,20"
                kk = pos.split(",")  # ["1", "100", "20"]
                idx, x, y = int(kk[0]), int(kk[1]), int(kk[2])
                ret_list.append((idx, x, y))
        return ret_list

    # 找图左键点击, 找到返回True, 未找到返回False
    def find_pic_click(self, x1, y1, x2, y2, pic, delta_color="101010", sim=0.95, order=0, timeout=0):
        # type: (int, int, int, int, str, str, float, int, int) -> bool
        locker = QMutexLocker(self.mutex)
        while True:
            # ret = (0, 43, 31) 或 (-1, -1, -1)
            ret = self.obj.FindPic(x1, y1, x2, y2, pic,
                                   delta_color, sim, order)
            if ret[0] >= 0 or timeout <= 0:
                break
            msleep(SLEEP_TIME)
            timeout -= SLEEP_TIME
        if ret[0] >= 0:
            self.move_click(ret[1] + rnd(2, 4), ret[2] + rnd(2, 4))
        ret = True if ret[0] >= 0 else False
        return ret

    # 找图右键点击, 找到返回True, 未找到返回False
    def find_pic_r_click(self, x1, y1, x2, y2, pic, delta_color="101010", sim=0.95, order=0, timeout=0):
        # type: (int, int, int, int, str, str, float, int, int) -> bool
        locker = QMutexLocker(self.mutex)
        while True:
            # ret = (0, 43, 31) 或 (-1, -1, -1)
            ret = self.obj.FindPic(x1, y1, x2, y2, pic,
                                   delta_color, sim, order)
            if ret[0] >= 0 or timeout <= 0:
                break
            msleep(SLEEP_TIME)
            timeout -= SLEEP_TIME
        if ret[0] >= 0:
            self.move_r_click(ret[1] + rnd(2, 4), ret[2] + rnd(2, 4))
        ret = True if ret[0] >= 0 else False
        return ret

    # 找图shift+鼠标右击, 找到返回True, 未找到返回False
    def find_pic_shift_r_click(self, x1, y1, x2, y2, pic, delta_color="101010", sim=0.95, order=0, timeout=0):
        # type: (int, int, int, int, str, str, float, int, int) -> bool
        locker = QMutexLocker(self.mutex)
        while True:
            # ret = (0, 43, 31) 或 (-1, -1, -1)
            ret = self.obj.FindPic(x1, y1, x2, y2, pic,
                                   delta_color, sim, order)
            if ret[0] >= 0 or timeout <= 0:
                break
            msleep(SLEEP_TIME)
            timeout -= SLEEP_TIME
        if ret[0] >= 0:
            VK_SHIFT = 16
            self.key_down(VK_SHIFT)
            self.move_r_click(ret[1] + rnd(2, 4), ret[2] + rnd(2, 4))
            self.key_up(VK_SHIFT)
        ret = True if ret[0] >= 0 else False
        return ret

    # 找图左键双击, 找到返回True, 未找到返回False
    def find_pic_db_click(self, x1, y1, x2, y2, pic, delta_color="101010", sim=0.95, order=0, timeout=0):
        # type: (int, int, int, int, str, str, float, int, int) -> bool
        locker = QMutexLocker(self.mutex)
        while True:
            # ret = (0, 43, 31) 或 (-1, -1, -1)
            ret = self.obj.FindPic(x1, y1, x2, y2, pic,
                                   delta_color, sim, order)
            if ret[0] >= 0 or timeout <= 0:
                break
            msleep(SLEEP_TIME)
            timeout -= SLEEP_TIME
        if ret[0] >= 0:
            self.move_db_click(ret[1] + rnd(2, 4), ret[2] + rnd(2, 4))
        ret = True if ret[0] >= 0 else False
        return ret

    # 返回图片所在窗口在坐标, 找到返回相应坐标, 没找到返回-1, -1
    def get_pic_pos(self, x1, y1, x2, y2, pic, delta_color="101010", sim=0.95, order=0, timeout=0):
        # type: (int, int, int, int, str, str, float, int, int) -> (int, int)
        locker = QMutexLocker(self.mutex)
        while True:
            # ret = (0, 43, 31) 或 (-1, -1, -1)
            ret = self.obj.FindPic(x1, y1, x2, y2, pic,
                                   delta_color, sim, order)
            if ret[0] >= 0 or timeout <= 0:
                break
            msleep(SLEEP_TIME)
            timeout -= SLEEP_TIME
        return ret[1], ret[2]

    # 返回找到的图片的索引, 从0开始, 如果没找到返回-1
    def get_pic_idx(self, x1, y1, x2, y2, pic, delta_color="101010", sim=0.95, order=0, timeout=0):
        # type: (int, int, int, int, str, str, float, int, int) -> int
        locker = QMutexLocker(self.mutex)
        while True:
            # ret = (0, 43, 31) 或 (-1, -1, -1)
            ret = self.obj.FindPic(x1, y1, x2, y2, pic,
                                   delta_color, sim, order)
            if ret[0] >= 0 or timeout <= 0:
                break
            msleep(SLEEP_TIME)
            timeout -= SLEEP_TIME
        return ret[0]

    # 返回找到的图片名"物_驱魔香", 未找到返回""(注意:没有图片后缀名)
    def get_pic_name(self, x1, y1, x2, y2, pic, delta_color="101010", sim=0.95, order=0, timeout=0, dir=""):
        # type: (int, int, int, int, str, str, float, int, int, str) -> str
        locker = QMutexLocker(self.mutex)
        if dir != "":  # 设置指定路径
            self.obj.SetPath(dir)
        ret_str = ""
        while True:
            # ret = ("物_驱魔香.bmp", 364, 302) 或 ("", -1, -1)
            ret = self.obj.FindPicS(
                x1, y1, x2, y2, pic, delta_color, sim, order)
            if ret[0] != "" or timeout <= 0:
                ret_str = ret[0].rstrip(".bmp")
                break
            msleep(SLEEP_TIME)
            timeout -= SLEEP_TIME
        if dir != "":  # 设置回原路径
            self.obj.SetPath(DIR_RES)
        return ret_str

    # 返回找到的图片的数量
    def get_pic_num(self, x1, y1, x2, y2, pic, delta_color="101010", sim=0.95, order=0, timeout=0):
        # type: (int, int, int, int, str, str, float, int, int) -> (int, int)
        tuple_list = self.find_pic_ex(
            x1, y1, x2, y2, pic, delta_color, sim, order, timeout)
        ret = len(tuple_list)
        return ret

    # 找出距离某点最近的图片位置
    def find_pic_nearest_pos(self, x1, y1, x2, y2, pic, cx, cy, delta_color="101010", sim=0.95, order=0,
                             timeout=0):
        # type: (int, int, int, int, str, int, int, str, float, int, int) -> (int, int)
        locker = QMutexLocker(self.mutex)
        while True:
            all_pos = self.obj.FindPicEx(
                x1, y1, x2, y2, pic, delta_color, sim, order)
            if all_pos or timeout <= 0:
                break
            msleep(SLEEP_TIME)
            timeout -= SLEEP_TIME
        ret_x, ret_y = -1, -1
        if all_pos:
            id_x_y = self.obj.FindNearestPos(all_pos, 0, cx, cy)  # "0,100,200"
            _, ret_x, ret_y = id_x_y.split(",")
            ret_x, ret_y = int(ret_x), int(ret_y)
        return ret_x, ret_y

    # -------------------------找色相关 -------------------------
    # 找色, 找到返回True, 未找到返回False
    def find_color(self, x1, y1, x2, y2, color, sim=1.0, order=0, timeout=0):
        # type: (int, int, int, int, str, float, int, int) -> bool
        locker = QMutexLocker(self.mutex)
        while True:
            # ret = (1, 33, 227) 或 (0, -1, -1)
            ret = self.obj.FindColor(x1, y1, x2, y2, color, sim, order)
            if ret[0] or timeout <= 0:
                break
            msleep(SLEEP_TIME)
            timeout -= SLEEP_TIME
        return ret[0]

    # 找色左键点击, 找到返回True, 未找到返回False
    def find_color_click(self, x1, y1, x2, y2, color, sim=1.0, order=0, timeout=0):
        # type: (int, int, int, int, str, float, int, int) -> bool
        locker = QMutexLocker(self.mutex)
        while True:
            # ret = (1, 33, 227) 或 (0, -1, -1)
            ret = self.obj.FindColor(x1, y1, x2, y2, color, sim, order)
            if ret[0] or timeout <= 0:
                break
            msleep(SLEEP_TIME)
            timeout -= SLEEP_TIME
        if ret[0]:
            self.move_click(ret[1] + rnd(2, 4), ret[2] + rnd(2, 4))
        return ret[0]

    # 返回颜色所在窗口坐标, 没找到返回-1,-1
    def get_color_pos(self, x1, y1, x2, y2, color, sim=1.0, order=0, timeout=0):
        # type: (int, int, int, int, str, float, int, int) -> (int, int)
        locker = QMutexLocker(self.mutex)
        while True:
            # ret = (1, 33, 227) 或 (0, -1, -1)
            ret = self.obj.FindColor(x1, y1, x2, y2, color, sim, order)
            if ret[0] or timeout <= 0:
                break
            msleep(SLEEP_TIME)
            timeout -= SLEEP_TIME
        return ret[1], ret[2]

    # 返回指定坐标的颜色, "RRGGBB"全小写
    def get_pos_color(self, x: int, y: int):
        locker = QMutexLocker(self.mutex)
        ret = self.obj.GetColor(x, y)
        return ret

    # ------------------------文字相关 ------------------------
    # 找到字返回True, 没找到返回False
    def find_str(self, x1, y1, x2, y2, string, color, sim=0.95, zk=0, timeout=0):
        # type: (int, int, int, int, str, str, float, int, int) -> bool
        locker = QMutexLocker(self.mutex)
        self.obj.UseDict(zk)
        while True:
            # ret = (0, 26, 263) 或 (-1, -1, -1)
            ret = self.obj.FindStrFast(x1, y1, x2, y2, string, color, sim)
            if ret[0] >= 0 or timeout <= 0:
                break
            msleep(SLEEP_TIME)
            timeout -= SLEEP_TIME
        ret = True if ret[0] >= 0 else False
        return ret

    # 找字扩展, 找到形如[(0,100,20), (1,30,40)]的列表, 一个都没找到返回[]
    def find_str_ex(self, x1, y1, x2, y2, string, color, sim=0.95, zk=0, timeout=0):
        # type: (int, int, int, int, str, str, float, int, int) -> []
        locker = QMutexLocker(self.mutex)
        self.obj.UseDict(zk)
        while True:
            ret_str = self.obj.FindStrFastEx(
                x1, y1, x2, y2, string, color, sim)
            if ret_str or timeout <= 0:
                break
            msleep(SLEEP_TIME)
            timeout -= SLEEP_TIME
        # "1,100,20|2,30,40" -> [(0,100,20), (1,30,40)]
        ret_list = []
        if ret_str:
            pos_list = ret_str.split("|")  # ["1,100,20", "2,30,40"]
            for pos in pos_list:
                kk = pos.split(",")  # ["1", "100", "20"]
                idx, x, y = int(kk[0]), int(kk[1]), int(kk[2])
                ret_list.append((idx, x, y))
        return ret_list

    # 找字左键点击, 找到返回True, 未找到返回False
    def find_str_click(self, x1, y1, x2, y2, string, color, sim=0.95, zk=0, timeout=0):
        # type: (int, int, int, int, str, str, float, int, int) -> bool
        self.obj.UseDict(zk)
        while True:
            # ret = (0, 26, 263) 或 (-1, -1, -1)
            ret = self.obj.FindStrFast(x1, y1, x2, y2, string, color, sim)
            if ret[0] >= 0 or timeout <= 0:
                break
            msleep(SLEEP_TIME)
            timeout -= SLEEP_TIME
        if ret[0] >= 0:
            self.move_click(ret[1] + rnd(2, 4), ret[2] + rnd(2, 4))
        ret = True if ret[0] >= 0 else False
        return ret

    # 返回字所在窗口坐标, 没找到返回-1,-1
    def get_str_pos(self, x1, y1, x2, y2, string, color, sim=0.95, zk=0, timeout=0):
        # type: (int, int, int, int, str, str, float, int, int) -> (int, int)
        locker = QMutexLocker(self.mutex)
        self.obj.UseDict(zk)
        while True:
            # ret = (0, 26, 263) 或 (-1, -1, -1)
            ret = self.obj.FindStrFast(x1, y1, x2, y2, string, color, sim)
            if ret[0] >= 0 or timeout <= 0:
                break
            msleep(SLEEP_TIME)
            timeout -= SLEEP_TIME
        return ret[1], ret[2]

    # 找出距离某点最近的字位置
    def find_str_nearest_pos(self, x1, y1, x2, y2, string, color, cx, cy, sim=0.95, zk=0, timeout=0):
        # type: (int, int, int, int, str, str, int, int, float, int, int) -> (int, int)
        locker = QMutexLocker(self.mutex)
        self.obj.UseDict(zk)
        while True:
            all_pos = self.obj.FindStrFastEx(
                x1, y1, x2, y2, string, color, sim)
            if all_pos or timeout <= 0:
                break
            msleep(SLEEP_TIME)
            timeout -= SLEEP_TIME
        ret_x, ret_y = -1, -1
        if all_pos:
            id_x_y = self.obj.FindNearestPos(all_pos, 0, cx, cy)  # "0,100,200"
            _, ret_x, ret_y = id_x_y.split(",")
            ret_x, ret_y = int(ret_x), int(ret_y)
        return ret_x, ret_y

    # 识别文字,未识别出返回""
    def ocr(self, x1, y1, x2, y2, color, sim=1.0, zk=0, timeout=0):
        # type: (int, int, int, int, str, float, int, int) -> str
        locker = QMutexLocker(self.mutex)
        self.obj.UseDict(zk)
        while True:
            # ret = "制" 或 ""
            ret = self.obj.Ocr(x1, y1, x2, y2, color, sim)
            if ret or timeout <= 0:
                break
            msleep(SLEEP_TIME)
            timeout -= SLEEP_TIME
        return ret


def pass_dm_vip(com_obj):
    ver = com_obj.ver()
    print(ver)
    dwDllBase = GetModuleHandle("dll\\dm.dll")
    ret = True
    if ver == "3.1233":
        WriteProcessMemory(-1, dwDllBase + 883572, b"\x01")
        WriteProcessMemory(-1, dwDllBase + 883692, b"\x01")
        WriteProcessMemory(-1, dwDllBase + 883696, b"\x01")
        WriteProcessMemory(-1, dwDllBase + 883707, b"\x01")
        WriteProcessMemory(-1, dwDllBase + 883734, b"\x01")
        WriteProcessMemory(-1, dwDllBase + 884224, b"\x01")
        WriteProcessMemory(-1, dwDllBase + 884264, b"\x01")
    elif ver == "5.1423":
        WriteProcessMemory(-1, dwDllBase + 1074128, b"\x01")
        WriteProcessMemory(-1, dwDllBase + 1074132, b"\x01")
        WriteProcessMemory(-1, dwDllBase + 1074660, b"\x01")
        WriteProcessMemory(-1, dwDllBase + 1074708, b"\x01")
        WriteProcessMemory(-1, dwDllBase + 1074712, b"\x01")
        WriteProcessMemory(-1, dwDllBase + 1076388, b"\x01")
    elif ver == "6.1538":
        WriteProcessMemory(-1, dwDllBase + 1078240, b"\x01")
        WriteProcessMemory(-1, dwDllBase + 1078244, b"\x01")
        WriteProcessMemory(-1, dwDllBase + 1078772, b"\x01")
        WriteProcessMemory(-1, dwDllBase + 1078820, b"\x01")
        WriteProcessMemory(-1, dwDllBase + 1078824, b"\x01")
    elif ver == "6.1544":
        WriteProcessMemory(-1, dwDllBase + 1086864, b"\x01")
        WriteProcessMemory(-1, dwDllBase + 1086868, b"\x01")
        WriteProcessMemory(-1, dwDllBase + 1087396, b"\x01")
        WriteProcessMemory(-1, dwDllBase + 1087444, b"\x01")
