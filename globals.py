import time
import os

from const.const import TBE_CONSOLE_ROW
from utils.plugin import *

PluginSDK = Dm
COM_NAME = Lw.COM_NAME if PluginSDK == Lw else Dm.COM_NAME

SOFT_NAME = "Input_Your_App_Name"
PATH_SOFTWARE = os.path.join(os.path.expanduser("~"), SOFT_NAME)
PATH_SOFTWARE_LOG = os.path.join(PATH_SOFTWARE, "logs")
PATH_SOFTWARE_CONFIG = os.path.join(PATH_SOFTWARE, "config")
PATH_SOFTWARE_PLAN = os.path.join(PATH_SOFTWARE, "plans")


log = None  # 日志对象

wnd_login = None  # 登录窗口对象
wnd_main = None  # 主窗口对象

cur_time_stamp = int(time.time())
cur_time_fmt = time.strftime("%H:%M:%S")

worker_list = [None for _ in range(TBE_CONSOLE_ROW)]  # 存放所有窗口工人对象的列表
cmb_plan_list = [None for _ in range(TBE_CONSOLE_ROW)]  # 方案下拉框对象列表


