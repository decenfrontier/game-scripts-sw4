import lib
import cm

def 任务链(wk: cm.Worker):
    wk.cur_task = "[任务链]"
    wk.record("开始执行")

    cm.use_qu_mo_xiang(wk)
    while wk.done_count < cm.get_cur_task_specify_count(wk):
        task_type = cm.sub_task(wk)
        if task_type == "接任务":
            goto_accept_ren_wu_lian(wk)
        elif task_type in ("找人", "完成"):
            zhao_ren(wk)
        elif task_type == "寻物":
            xun_wu(wk)
        elif task_type == "捕捉宠物":
            bu_zhuo_chong_wu(wk)
        elif task_type == "战斗":
            zhan_dou(wk)
        lib.msleep(800)

def goto_accept_ren_wu_lian(wk: cm.Worker):
    wk.record("正在接任务...")
    cm.fly_to_map(wk, "临仙镇")
    x, y = cm.NPC_POS_WND["楚千机"]
    for i in range(10):
        if cm.is_talk_open(wk):
            break
        if not wk.is_find_way:
            cm.click_map_wnd_pos(wk, x, y)
        lib.msleep(500)
    if cm.click_talk_specify_item(wk, "接任务链"):  # 若对话打开
        lib.msleep(500)
        over = cm.is_task_over(wk, 300)
        cm.close_talk(wk)
        if not over:
            cm.set_task_to_cur_task_bar(wk)

# 找人
def zhao_ren(wk: cm.Worker):
    wk.record("任务类型: 找人")
    if not cm.fly_task_npc_talk(wk):
        return
    if cm.click_talk_specify_item(wk, "交任务", 200):
        lib.msleep(600)
        cm.click_talk_specify_item(wk, "交任务链", 200)
        lib.msleep(800)
        cm.click_talk_specify_item(wk, "确定", 200)  # 确定开启
    if cm.is_task_over(wk, 300):
        return
    cm.give_task_goods_pet(wk)
    cm.update_task_done_count(wk)
    cm.close_talk(wk)

# 寻物
def xun_wu(wk: cm.Worker):
    wk.record("任务类型: 寻物")
    goods_name = cm.ocr_task_need_goods(wk)
    need = False if goods_name in ("50级装备", "60级装备", "70级装备") else True
    # 自制家具庭院
    if lib.cfg_main["自制家具和庭院装饰"] and goods_name in cm.JIA_JU | cm.TING_YUAN:
        cm.make_jia_ju_ting_yuan(wk, goods_name)
    # 购买物品
    if cm.sub_task(wk) != "完成":
        cm.buy_goods(wk, goods_name, is_need=need)

# 捕捉宠物
def bu_zhuo_chong_wu(wk: cm.Worker):
    wk.record("任务类型: 捕捉宠物")
    cm.close_talk(wk)
    cm.buy_task_pet(wk)

# 战斗
def zhan_dou(wk: cm.Worker):
    wk.record("任务类型: 战斗")
    map_name = cm.ocr_task_des_map(wk)
    cm.fly_to_map(wk, map_name)
    for i in range(30):
        if cm.click_talk_specify_item(wk, "交任务"):
            lib.msleep(600)
            cm.click_talk_specify_item(wk, "交任务链", 200)
            lib.msleep(800)
            cm.click_talk_specify_item(wk, "确定", 200)  # 确定开启
        if cm.is_task_over(wk, 300):
            return
        if cm.is_fight(wk):
            cm.fight_operation(wk)
            break
        if not wk.is_find_way:
            cm.task_npc_find_way(wk)
        lib.msleep(600)