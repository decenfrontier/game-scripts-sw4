import lib
import cm

def 修炼任务(wk: cm.Worker):
    wk.cur_task = "[修炼]"
    wk.record("开始执行")

    cm.use_qu_mo_xiang(wk)
    while wk.done_count < cm.get_cur_task_specify_count(wk):
        task_type = cm.sub_task(wk)
        if task_type == "接任务":
            goto_accept_task(wk)
        elif task_type in ("找人", "完成"):
            zhao_ren(wk)
        elif task_type == "寻物":
            xun_wu(wk)
        elif task_type == "捕捉宠物":
            bu_zhuo_chong_wu(wk)
        elif task_type == "战斗":
            zhan_dou(wk)
        elif task_type == "疯道人":
            feng_dao_ren(wk)
        lib.msleep(800)

# 去接任务
def goto_accept_task(wk: cm.Worker):
    wk.record("正在接任务...")
    cm.fly_to_map(wk, "临仙镇")
    x, y = cm.NPC_POS_WND["玄修"]
    if cm.goto_pos_npc_talk(wk, x, y, "接修炼"):
        lib.msleep(300)
        if cm.is_task_over(wk, 300):
            return
        cm.close_talk(wk)
        cm.set_task_to_cur_task_bar(wk)

# 找人
def zhao_ren(wk: cm.Worker):
    wk.record("任务类型: 找人")
    if not cm.fly_task_npc_talk(wk):
        return
    if cm.click_talk_specify_item(wk, "交任务", 200):
        lib.msleep(600)
        cm.click_talk_specify_item(wk, "交修炼", 200)
        lib.msleep(800)
    if cm.is_task_over(wk, 300):
        return
    cm.close_talk(wk)
    cm.give_task_goods_pet(wk)
    cm.update_task_done_count(wk)

# 寻物
def xun_wu(wk: cm.Worker):
    wk.record("任务类型: 寻物")
    goods_name = cm.ocr_task_need_goods(wk)
    # 帮贡完成
    if lib.cfg_main["寻物用帮贡完成"]:
        x, y = cm.get_cur_task_pos(wk)
        if wk.find_str_click(x-18, y, x+174, y+43, "帮派协助", cm.COLOR_CYAN):
            lib.msleep(500)
            if cm.click_talk_specify_item(wk, "帮贡直接完成", 300) and cm.click_confirm(wk, 400):
                wk.record("使用帮贡完成任务成功")
                return
            else:
                wk.record("使用帮贡完成任务失败,自动购买物品")
            cm.close_talk(wk)
    # 自制家具庭院
    if lib.cfg_main["自制家具和庭院装饰"] and goods_name in cm.JIA_JU | cm.TING_YUAN:
        cm.make_jia_ju_ting_yuan(wk, goods_name)
    # 购买物品
    if cm.sub_task(wk) != "完成":
        cm.buy_goods(wk, goods_name)

# 捕捉宠物
def bu_zhuo_chong_wu(wk: cm.Worker):
    wk.record("任务类型: 捕捉宠物")
    cm.close_talk(wk)
    cm.buy_task_pet(wk)

# 战斗
def zhan_dou(wk: cm.Worker):
    wk.record("任务类型: 战斗")
    cm.fly_task_map_fight(wk)

# 疯道人
def feng_dao_ren(wk: cm.Worker):
    wk.record("任务类型: 疯道人")
    map_name = cm.ocr_task_des_map(wk)
    cm.fly_to_map(wk, map_name)
    for i in range(30):
        if cm.is_talk_open(wk):
            if cm.is_task_over(wk):
                return
            if lib.cfg_main["疯道人预言截图"]:
                wk.capture(*cm.RECT_FULL, f"{lib.DIR_TEMP}\\疯道人_{lib.cur_time_stamp}.bmp")
            cm.click_talk_first_item(wk)
            cm.close_talk(wk)
        if cm.is_fight(wk):
            cm.fight_operation(wk)
            break
        if not wk.is_find_way and not cm.task_npc_find_way(wk):
            return
        lib.msleep(600)
