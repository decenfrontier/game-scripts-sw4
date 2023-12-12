import lib
import cm


def 蛮洞密令(wk: cm.Worker):
    wk.cur_task = "[蛮洞]"
    cm.team.set_leader_task(wk, wk.cur_task)
    wk.record("开始执行")

    while wk.done_count < cm.get_cur_task_specify_count(wk):
        lib.msleep(800)
        if not goto_accept_man_dong(wk):
            continue
        if calc_man_dong_count(wk):
            continue
        for i in range(10):
            if cm.is_talk_open(wk):
                cm.click_talk_first_item(wk)
                cm.close_talk(wk)
            lib.msleep(1000)
            if cm.is_fight(wk):
                cm.fight_operation(wk)
                break
            if not wk.is_find_way and not cm.task_npc_find_way(wk):
                lib.msleep(1000)
                break

    cm.team.set_leader_task(wk)


def goto_accept_man_dong(wk: cm.Worker):
    if cm.cur_map(wk) == "蛮荒山":
        return True
    wk.record("正在进入蛮荒山...")
    if not cm.fly_to_map(wk, "大唐境外"):
        return False
    x, y = cm.NPC_POS_WND["边境将领"]
    if cm.goto_pos_npc_talk(wk, x, y, "送我们过去"):
        lib.msleep(800)
        cm.click_talk_specify_item(wk, "普通蛮洞密令", 300)
        lib.msleep(800)
        cm.click_talk_first_item(wk, 300)
        lib.msleep(1000)
        if cm.cur_map(wk) == "蛮荒山":
            wk.record("已成功进入蛮荒山")
            return True
    return False

# 计算蛮洞次数
def calc_man_dong_count(wk: cm.Worker):
    if not cm.is_confirm_cancel_open(wk):
        return False
    cm.update_task_done_count(wk)
    if wk.done_count < cm.get_cur_task_specify_count(wk):
        if cm.click_confirm(wk, 300):
            wk.record("未达到设定次数, 已点击 确定")
    else:
        if cm.click_cancel(wk, 300):
            wk.record("已达到设定次数, 已点击 取消")
    lib.msleep(1600)
    return True
