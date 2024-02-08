from biz.constants.constants import ZK_ALL
import lib
from utils.plugin import PLUGIN_SDK


class Worker(PLUGIN_SDK):
    def __init__(self, hwnd: int, obj, row: int):
        # ---------------- 工人状态 ---------------
        self.is_run = False  # 是否在运行(在干活)
        self.is_pause = False  # 是否在暂停(在休息)
        self.is_end = True  # 是否已结束(干完活 或 没活干)
        # 初始化Com类
        super().__init__(obj)
        # 设置图片和字库
        self.set_pic_pwd(lib.pwd_pic)
        self.set_dict_pwd(lib.pwd_zk)
        self.set_path(lib.DIR_RES)
        self.set_dict(ZK_ALL, "0全部.txt")
        # 模拟真实鼠标
        self.simulate_real_mouse()
        self.show_error_msg(False)
        # ---------------- 窗口属性 ---------------
        self.hwnd = hwnd  # 窗口句柄
        self.row = row  # 窗口在中控表格的第几行,从0开始
        self.is_lock = False  # 窗口是否锁定
        self.thread = None  # 执行线程对象
        self.h_thread = 0  # 执行线程的线程句柄
        self.x = 0  # 窗口左上角坐标x
        self.y = 0  # 窗口左上角坐标y
        # ---------------- 业务相关 ---------------
        self.cfg_plan = lib.cfg_plan_dict["0内置默认"]
        self.cur_task = ""  # 当前执行任务
        self.sub_task = ""  # 当前执行的子任务
        self.done_count = 0  # 当前任务完成次数

    def write_tbe_console(self, col: int, info: str):
        lib.wnd_main.sig_info.emit(self.row, col, info)

    def record(self, info):
        info = f"{lib.cur_time_fmt} [{self.cur_task}] {info}"
        self.write_tbe_console(lib.COL_LOG, info)
        row_num = self.row + 1
        lib.file_append_content(f"{lib.DIR_LOG}\\{row_num}.txt", f"{info}\n")

    # 隐藏窗口
    def hide_wnd(self, prev_x: int, prev_y: int):
        self.x, self.y = prev_x, prev_y  # 记忆之前坐标
        lib.show_task_bar_icon(self.hwnd, False)
        hide_x, hide_y = lib.HIDE_X, lib.rnd(0, 200)
        lib.set_wnd_pos(self.hwnd, hide_x, hide_y)

    # 显示窗口
    def show_wnd(self):
        lib.show_task_bar_icon(self.hwnd, True)
        lib.set_wnd_pos(self.hwnd, self.x, self.y)

    # 模拟真实鼠标
    def simulate_real_mouse(self):
        self.enable_real_mouse(False)
