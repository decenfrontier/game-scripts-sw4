# 此文件负责调用函数

from PySide2.QtCore import QThread
import pythoncom

import common
from utils import rnd
import utils
import settings


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
        utils.msleep(rnd(500, 1000))

        self.thread_guard.start()  # 启动检测线程

        cmb_plan = settings.cmb_plan_list[wk.row]
        plan_name = cmb_plan.currentText()
        cfg_plan = settings.cfg_plan_dict[plan_name]
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
            utils.msleep(600)

        wk.cur_task, wk.sub_task = "", ""
        wk.record("任务执行完毕")
        wk.is_run, wk.is_pause, wk.is_end = False, False, True
        wk.write_tbe_console(settings.COL_END, settings.SELECTED)

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
        wk.write_tbe_console(settings.COL_END, settings.SELECTED)
        wk.mutex.unlock()


# 守护线程
class ThreadGuard(QThread):
    def __init__(self, wk: common.Worker):
        super().__init__()
        self.wk = wk

    def run(self):
        wk = self.wk
        pythoncom.CoInitialize()

        x1, y1 = common.cur_pos(wk)
        sleep_gap = 100
        last_time = settings.cur_time_stamp
        while not wk.is_end:
            # 过所有验证
            # common.pass_all_auth(wk)
            utils.msleep(sleep_gap)
