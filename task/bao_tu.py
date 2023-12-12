import lib
import cm

def 宝图任务(wk: cm.Worker):
    wk.cur_task = "[宝图]"
    wk.record("开始执行")

    while wk.done_count < cm.get_cur_task_specify_count(wk):
        task_type = cm.sub_task(wk)
        if task_type == "接任务":
            goto_accept_task(wk)
        elif task_type == "藏宝之徒":
            cang_bao_zhi_tu(wk)
        lib.msleep(600)


def goto_accept_task(wk: cm.Worker):
    wk.record("正在接任务...")
    cm.use_fei_xing_qi(wk, "长安城", cm.FLAG_RECT["运镖宝图"])

    x, y = cm.NPC_POS_WND["江湖密探"]
    if cm.goto_pos_npc_talk(wk, x, y, "接宝图"):
        lib.msleep(300)
        if cm.is_task_over(wk, 300):
            return
        cm.close_talk(wk)
        cm.set_task_to_cur_task_bar(wk)


def cang_bao_zhi_tu(wk: cm.Worker):
    wk.record("任务类型: 藏宝之徒")
    des_map = cm.ocr_task_des_map(wk)
    cm.fly_to_map(wk, des_map)
    for i in range(20):
        if cm.is_fight(wk):
            cm.fight_operation(wk)
            break
        if not wk.is_find_way:
            cm.task_npc_find_way(wk)
        lib.msleep(500, 1000)