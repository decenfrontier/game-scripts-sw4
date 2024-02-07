# 此文件负责调用函数

from PySide2.QtCore import QThread
import pythoncom

import lib
import common
from lib import rnd


task_dict = {}

# 执行线程
class ThreadExec(QThread):
    def __init__(self, wk: common.Worker):
        super().__init__()
        self.wk = wk
        self.thread_guard = ThreadGuard(wk)

    def run(self):
        wk = self.wk
        pythoncom.CoInitialize()
        wk.is_run, wk.is_pause, wk.is_end = True, False, False
        lib.msleep(rnd(500, 1000))

        self.thread_guard.start()  # 启动检测线程

        cmb_plan = lib.cmb_plan_list[wk.row]
        plan_name = cmb_plan.currentText()
        cfg_plan = lib.cfg_plan_dict[plan_name]
        task_list = cfg_plan["执行列表"]

        for task_name in task_list:
            if task_name == "":
                wk.record("此方案未添加任务!")
                break
            task_cls = task_dict.get(task_name)
            if task_cls:
                task = task_cls(wk)
                task.before_run()
                task.run()
                task.after_run()

            else:
                wk.record(f"{task_name} -> 暂未开发, 敬请期待")
            lib.msleep(600)

        wk.cur_task, wk.sub_task = "", ""
        wk.record("任务执行完毕")
        wk.is_run, wk.is_pause, wk.is_end = False, False, True
        wk.write_tbe_console(lib.COL_END, lib.SELECTED)

    def pause(self):
        wk = self.wk
        wk.mutex.lock()
        wk.record("任务暂停执行")
        wk.is_run, wk.is_pause, wk.is_end = False, True, False

    def resume(self):
        wk = self.wk
        wk.mutex.unlock()
        wk.record("任务恢复执行")
        wk.is_run, wk.is_pause, wk.is_end = True, False, False

    def end(self):
        wk = self.wk
        if not wk.is_pause:
            wk.mutex.lock()
        self.terminate()
        self.wait()
        wk.record("任务终止执行")
        wk.is_run, wk.is_pause, wk.is_end = False, False, True
        wk.write_tbe_console(lib.COL_END, lib.SELECTED)
        wk.mutex.unlock()


# 守护线程
class ThreadGuard(QThread):
    def __init__(self, wk: common.Worker):
        super().__init__()
        self.wk = wk

    def run(self):
        wk = self.wk
        pythoncom.CoInitialize()

        wk.school = ""
        x1, y1 = common.cur_pos(wk)
        sleep_gap = 100
        last_time = lib.cur_time_stamp
        while not wk.is_end:
            common.pass_all_auth(wk)  # 过所有验证
            lib.msleep(sleep_gap)
            common.check_online_state(wk)  # 检查在线状态
            lib.msleep(sleep_gap)
            common.right_down_quick_operation(wk)  # 右下角快捷操作
            lib.msleep(sleep_gap)
            common.close_xiao_xin_tip(wk)  # 关闭小昕提示
            lib.msleep(sleep_gap)
            common.click_continue_game(wk)  # 关闭继续游戏
            lib.msleep(sleep_gap)
            common.get_role_school(wk)  # 获取角色门派
            lib.msleep(sleep_gap)
            common.open_treasure_box(wk)  # 开宝箱
            lib.msleep(sleep_gap)
            common.close_popup_wnd(wk)  # 关闭弹窗
            lib.msleep(sleep_gap)
            common.throw_dice(wk)  # 掷骰子
            lib.msleep(sleep_gap)
            common.check_ju_qing(wk)  # 检查剧情
            lib.msleep(sleep_gap)
            common.queue_back_server(wk)  # 排队回原服
            common.close_describe_box(wk)  # 关闭描述框

            x2, y2 = common.cur_pos(wk)
            wk.is_find_way = False if (x1, y1) == (x2, y2) else True
            x1, y1 = x2, y2

            # 除下列任务外, 每7秒重新寻路一次
            if wk.cur_task not in ("[边境]", "[封妖]", "[修炼宝箱]", "[天降宝箱]"):
                if lib.delta_sec(last_time, lib.cur_time_stamp) > 7:
                    wk.is_find_way = False
                    last_time = lib.cur_time_stamp