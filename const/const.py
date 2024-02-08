import os

client_ver = "5.4.40"  # 客户端版本号

# dll名称
DLL_NAME_DM = "dm.dll"
DLL_NAME_REGDM = "DmReg.dll"
DLL_NAME_LW = "lw.dll"

DIR_WORK = os.getcwd()
DIR_RES = os.path.join(DIR_WORK, "res")
DIR_QT_RES = os.path.join(DIR_RES, "qt_res")
DIR_DLL = os.path.join(DIR_WORK, "dll")

TBE_CONSOLE_ROW = 15
TBE_CONSOLE_COL = 6
COL_HWND = 0
COL_PLAN = 1
COL_RUN = 2
COL_PAUSE = 3
COL_END = 4
COL_LOG = 5
SELECTED = "√"
HIDE_X = 7680

SLEEP_TIME = 100  # 等待时间ms, 越大执行速度越慢, 占用CPU越少
SLEEP_AFTER_CLICK = 150  # 点击后的等待时间ms

SOFT_NAME = "wssoft"
PATH_SOFTWARE = os.path.join(os.path.expanduser("~"), SOFT_NAME)
PATH_SOFTWARE_LOG = os.path.join(PATH_SOFTWARE, "logs")  # 日志文件
PATH_SOFTWARE_PLAN = os.path.join(PATH_SOFTWARE, "plans.json")  # 不同方案的配置
PATH_SOFTWARE_COMMON = os.path.join(PATH_SOFTWARE, "common.json")  # 软件的通用配置
