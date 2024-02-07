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
TBE_CONSOLE_COL = 7
COL_HWND = 0
COL_PLAN = 1
COL_SCHOOL = 2
COL_RUN = 3
COL_PAUSE = 4
COL_END = 5
COL_LOG = 6
SELECTED = "√"
HIDE_X = 7680

SLEEP_TIME = 100  # 等待时间ms, 越大执行速度越慢, 占用CPU越少
SLEEP_AFTER_CLICK = 150  # 点击后的等待时间ms
