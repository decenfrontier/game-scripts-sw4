import ctypes
import subprocess
from win32com.client import Dispatch
from comtypes.client import CreateObject
from const.const import DIR_DLL, DLL_NAME_DM, DLL_NAME_LW, DLL_NAME_REGDM
from utils.plugin import DM, LW


def reg_com_to_system(com_name: str) -> bool:
    obj_dll_dict = {LW.COM_NAME: DLL_NAME_LW,
                    DM.COM_NAME: DLL_NAME_DM}
    dll_name = obj_dll_dict[com_name]
    path_dll = f"{DIR_DLL}\\{dll_name}"
    if com_name == DM.COM:
        DmReg = ctypes.WinDLL(f"dll\\{DLL_NAME_REGDM}")  # 免注册插件要用32位py
        ret = DmReg.SetDllPathW(path_dll, 1)  # SetDllPathW
    else:  # 此种注册方式需要以管理员运行
        ret = run_command_with_admin(
            f"C:\\Windows\\System32\\regsvr32 {path_dll} /s")
        ret = True if ret == 0 else False
    return ret


# 创建com组件对象
def create_com_obj(com_name: str):
    obj = None
    try:
        if com_name == LW.COM_NAME:
            obj = CreateObject(com_name)  # lw
        else:
            obj = Dispatch(com_name)  # dm, tr, op
    except:
        print(f"创建com对象{com_name}失败")
    return obj


def run_command_with_admin(command):
    start_info = subprocess.STARTUPINFO()
    start_info.dwFlags |= subprocess.STARTF_USESHOWWINDOW
    ret = subprocess.call(f'runas /user:Administrator {command}')
    return ret
