import time

from const.const import TBE_CONSOLE_ROW


wnd_login = None  # 登录窗口对象
wnd_main = None  # 主窗口对象

cur_time_stamp = int(time.time())
cur_time_fmt = time.strftime("%H:%M:%S")

worker_list = [None for _ in range(TBE_CONSOLE_ROW)]  # 存放所有窗口工人对象的列表
cmb_plan_list = [None for _ in range(TBE_CONSOLE_ROW)]  # 方案下拉框对象列表
cfg_plan_dict = {}

cfg_common = {}
