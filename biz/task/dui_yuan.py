import lib

import common

from task import ling_hu

def 队员挂机(wk: common.Worker):
    wk.cur_task = "[队员]"
    wk.record("开始执行")

    while not exit_team(wk):  # 只要不退队就一直循环执行
        if common.is_fight(wk):
            if common.team.get_leader_task(wk) == "[灵狐]":
                ling_hu.fight_catch(wk)
            else:
                common.fight_operation(wk)

        if lib.cfg_main["自动关闭对话框"]:
            common.close_talk(wk)  # 里面会自动领双
        common.click_confirm(wk)  # 点击 确定/确认/同意
        freeze_double_exp(wk)
        unfreeze_double_exp(wk)
        lib.msleep(800)


# 冻结双倍经验
def freeze_double_exp(wk: common.Worker):
    if "冻双" not in common.team.get_leader_sig(wk):
        return
    # 若响应失败, 则直接返回
    if not common.team.response_leader_sig(wk, "冻双"):
        return
    wk.record("收到队长发出的冻双信号")
    if lib.cfg_main["跟随队长冻双"]:
        common.freeze_double_exp(wk)
        return

# 解冻双倍经验
def unfreeze_double_exp(wk: common.Worker):
    if "解双" not in common.team.get_leader_sig(wk):
        return
    # 若响应失败, 则直接返回
    if not common.team.response_leader_sig(wk, "解双"):
        return
    wk.record("收到队长发出的解双信号")
    if lib.cfg_main["跟随队长解双"]:
        common.unfreeze_double_exp(wk)
        return

# 退出队伍
def exit_team(wk: common.Worker):
    if "退队" not in common.team.get_leader_sig(wk):
        return False
    # 若响应失败, 则直接返回
    if not common.team.response_leader_sig(wk, "退队"):
        return
    wk.record("收到队长发出的退队信号")
    if lib.cfg_main["跟随队长退队"]:
        common.exit_team(wk)
        return True
    return False