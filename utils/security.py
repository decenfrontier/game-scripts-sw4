# my_dll = ctypes.WinDLL(f"dll\\{DLL_MY_NAME}")
# anti_vm = my_dll.fn1
# anti_debug1 = my_dll.fn2
# anti_debug2 = my_dll.fn3
# anti_debug3 = my_dll.fn4
# anti_anti_debug4 = my_dll.fn5
# show_task_bar_icon = my_dll.fn6

# def is_user_dangerous():
#     global action_code
#     ret = False

#     ret1 = anti_vm()
#     if ret1:
#         print("检测到虚拟机")
#         action_code = action_code_dict["检测到虚拟机"]
#         ret = True
#     ret2 = anti_debug1()
#     ret3 = anti_debug2()
#     ret4 = anti_debug3()
#     ret5 = anti_anti_debug4()
#     if True in [ret2, ret3, ret4, ret5]:
#         action_code = action_code_dict["检测到调试器"]
#         ret = True
#     return ret

# # 检测多开, 检测到返回真
# def detect_multi_run():
#     global hMutex
#     hMutex = CreateMutex(None, False, "TX_DETT_MR")  # 若存在, 会使该互斥体引用量加1
#     if GetLastError() == ERROR_ALREADY_EXISTS:
#         CloseHandle(hMutex)  # 使该互斥体引用量减1
#         return True
#     return False
