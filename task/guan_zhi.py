import cm
import lib

def 官职任务(wk: cm.Worker):
    wk.cur_task = "[官职]"
    wk.record("开始执行")

    while wk.done_count < cm.get_cur_task_specify_count(wk):
        task_type = cm.sub_task(wk)
        if task_type == "接任务":
            goto_accept_task(wk)
        elif task_type == "除暴安良":
            chu_bao_an_liang(wk)
        elif task_type == "收集物资":
            shou_ji_wu_zi(wk)
        elif task_type == "下听民声":
            xia_ting_ming_sheng(wk)
        elif task_type == "完成":
            reply_to_lee(wk)
        lib.msleep(1000)

def goto_accept_task(wk: cm.Worker):
    wk.record("正在接任务...")
    cm.open_zhuang_bei_ui(wk)
    if not cm.is_zhuang_bei_ui_open(wk):
        wk.record("装备界面打开失败")
        return
    wk.move_click(*cm.POS_DONATE_SELL_ZB)
    lib.msleep(600, 800)
    if cm.is_talk_open(wk):  # 若对话打开
        cm.click_talk_specify_item(wk, "接官职")
        over = cm.is_task_over(wk, 300)
        cm.close_talk(wk)
        if not over:
            cm.set_task_to_cur_task_bar(wk)

def chu_bao_an_liang(wk: cm.Worker):
    wk.record("任务类型: 除暴安良")
    cm.fly_task_map_fight(wk)

def shou_ji_wu_zi(wk: cm.Worker):
    wk.record("任务类型: 收集物资")
    cm.buy_task_need_goods(wk)

def xia_ting_ming_sheng(wk: cm.Worker):
    wk.record("任务类型: 下听民声")
    if not cm.fly_task_npc_talk(wk):
        return
    if cm.click_talk_specify_item(wk, "交任务", 200):
        lib.msleep(600)
        cm.click_talk_specify_item(wk, "交官职", 200)
        lib.msleep(800)
    if cm.is_task_over(wk, 300):
        return
    cm.close_talk(wk)
    cm.give_task_goods_pet(wk)
    cm.update_task_done_count(wk)

def reply_to_lee(wk: cm.Worker):
    wk.record("正在回复李将军...")
    cm.fly_to_npc(wk, "长安城", "李将军")
    if not cm.goto_task_npc_talk(wk):
        return
    if cm.click_talk_specify_item(wk, "交任务", 200):
        lib.msleep(600)
        cm.click_talk_specify_item(wk, "交官职", 200)
        lib.msleep(800)
    if cm.is_task_over(wk, 300):
        return
    cm.close_talk(wk)
    cm.give_task_goods_pet(wk)
    cm.update_task_done_count(wk)