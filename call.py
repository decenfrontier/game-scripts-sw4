# 此文件负责调用函数

from PySide2.QtCore import QThread
import pythoncom

import lib
import cm
from lib import rnd

from task.bao_tu import 宝图任务
from task.da_ye import 带队打野
from task.dui_yuan import 队员挂机
from task.fu_ben import 带队副本, 混队副本
from task.ju_qing import 主线剧情
from task.qing_bao import 清理背包
from task.shi_men import 师门任务
from task.wa_bao import 自动挖宝
from task.xiu_lian import 修炼任务
from task.yun_biao import 运镖任务
from task.zhuo_gui import 带队捉鬼
from task.ling_hu import 灵狐乐园
from task.diao_yu import 休闲钓鱼
from task.fu_jia import 退出队伍, 幸运转盘, 转转乐, 领取双倍, 冻结双倍, 制作烹饪, \
    经验换修, 化龙鼎, 祈福, 修炼宝箱, 天降宝箱, 体力打工
from task.bang_pai import 帮派经商, 帮派玄武, 帮派青龙, 帮派强盗
from task.juan_zhuang import 捐献装备
from task.ren_wu_lian import 任务链
from task.bian_jing import 边境救援
from task.guan_zhi import 官职任务
from task.feng_yao import 带队封妖
from task.zi_nv import 子女温饱
from task.man_dong import 蛮洞密令
from task.qi_bao import 旗包任务

task_dict = {
    "宝图任务": 宝图任务, "带队打野": 带队打野, "队员挂机": 队员挂机, "带队副本": 带队副本, "混队副本": 混队副本,
    "主线剧情": 主线剧情, "清理背包": 清理背包, "师门任务": 师门任务, "自动挖宝": 自动挖宝, "修炼任务": 修炼任务,
    "运镖任务": 运镖任务, "带队捉鬼": 带队捉鬼, "灵狐乐园": 灵狐乐园, "休闲钓鱼": 休闲钓鱼, "退出队伍": 退出队伍,
    "捐献装备": 捐献装备, "帮派经商": 帮派经商, "帮派玄武": 帮派玄武, "帮派青龙": 帮派青龙, "任务链": 任务链,
    "幸运转盘": 幸运转盘, "转转乐": 转转乐, "领取双倍": 领取双倍, "冻结双倍": 冻结双倍, "边境救援": 边境救援,
    "官职任务": 官职任务, "带队封妖": 带队封妖, "制作烹饪": 制作烹饪, "经验换修": 经验换修, "化龙鼎": 化龙鼎,
    "子女温饱": 子女温饱, "蛮洞密令": 蛮洞密令, "旗包任务": 旗包任务, "祈福": 祈福, "修炼宝箱": 修炼宝箱,
    "天降宝箱": 天降宝箱, "帮派强盗": 帮派强盗, "体力打工": 体力打工,
}

# 执行线程
class ThreadExec(QThread):
    def __init__(self, wk: cm.Worker):
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
        task_list = cfg_plan["执行列表"]  # ["师门任务", "清理背包"]

        for task_name in task_list:
            if task_name == "":
                wk.record("此方案未添加任务!")
                break
            func = task_dict.get(task_name)
            if func:
                # 每执行一个任务前, 都重置任务类型和完成次数
                wk.cur_task, wk.sub_task = "", ""
                wk.done_count = 0
                # 在战斗就等战斗结束
                if cm.is_fight(wk):
                    cm.fight_operation(wk)
                # 每执行一个任务前, 都关闭所有界面
                cm.close_all_sub_wnd(wk)
                cm.close_talk(wk)
                # 开始执行任务
                func(wk)
                wk.record("执行完成")
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
    def __init__(self, wk: cm.Worker):
        super().__init__()
        self.wk = wk

    def run(self):
        wk = self.wk
        pythoncom.CoInitialize()

        wk.school = ""
        x1, y1 = cm.cur_pos(wk)
        sleep_gap = 100
        last_time = lib.cur_time_stamp
        while not wk.is_end:
            cm.pass_all_auth(wk)  # 过所有验证
            lib.msleep(sleep_gap)
            cm.check_online_state(wk)  # 检查在线状态
            lib.msleep(sleep_gap)
            cm.right_down_quick_operation(wk)  # 右下角快捷操作
            lib.msleep(sleep_gap)
            cm.close_xiao_xin_tip(wk)  # 关闭小昕提示
            lib.msleep(sleep_gap)
            cm.click_continue_game(wk)  # 关闭继续游戏
            lib.msleep(sleep_gap)
            cm.get_role_school(wk)  # 获取角色门派
            lib.msleep(sleep_gap)
            cm.open_treasure_box(wk)  # 开宝箱
            lib.msleep(sleep_gap)
            cm.close_popup_wnd(wk)  # 关闭弹窗
            lib.msleep(sleep_gap)
            cm.throw_dice(wk)  # 掷骰子
            lib.msleep(sleep_gap)
            cm.check_ju_qing(wk)  # 检查剧情
            lib.msleep(sleep_gap)
            cm.queue_back_server(wk)  # 排队回原服
            cm.close_describe_box(wk)  # 关闭描述框

            x2, y2 = cm.cur_pos(wk)
            wk.is_find_way = False if (x1, y1) == (x2, y2) else True
            x1, y1 = x2, y2

            # 除下列任务外, 每7秒重新寻路一次
            if wk.cur_task not in ("[边境]", "[封妖]", "[修炼宝箱]", "[天降宝箱]"):
                if lib.delta_sec(last_time, lib.cur_time_stamp) > 7:
                    wk.is_find_way = False
                    last_time = lib.cur_time_stamp