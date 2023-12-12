import lib
import cm

def 带队捉鬼(wk: cm.Worker):
    wk.cur_task = "[捉鬼]"
    cm.team.set_leader_task(wk, wk.cur_task)
    wk.record("开始执行")

    cm.use_qu_mo_xiang(wk)
    while wk.done_count < cm.get_cur_task_specify_count(wk):
        task_type = cm.sub_task(wk)
        if task_type == "接任务":
            goto_accept_task(wk)
        else:
            shou_fu_you_hun(wk)
        lib.msleep(800)
    cm.team.set_leader_task(wk)


# 去接任务
def goto_accept_task(wk: cm.Worker):
    wk.record("正在接任务...")
    cm.use_fei_xing_qi(wk, "长安城", cm.FLAG_RECT["捉鬼"])

    for i in range(10):
        if cm.is_talk_open(wk):
            break
        if not wk.is_find_way:
            x, y = cm.NPC_POS_WND["钟馗"]
            cm.click_map_wnd_pos(wk, x, y)
        lib.msleep(500)
    if cm.is_talk_open(wk):  # 若对话打开
        cm.click_talk_specify_item(wk, "接捉鬼")
        cm.is_task_over(wk, 300)
        cm.close_talk(wk)
        cm.set_task_to_cur_task_bar(wk)


def shou_fu_you_hun(wk: cm.Worker):
    wk.record("任务类型: 收服游魂")
    map_name = cm.ocr_task_des_map(wk)
    cm.fly_to_map(wk, map_name)
    for i in range(60):
        if not wk.is_find_way:
            cm.task_npc_find_way(wk)
        lib.msleep(1000)
        if cm.is_fight(wk):
            cm.fight_operation(wk)
            break
