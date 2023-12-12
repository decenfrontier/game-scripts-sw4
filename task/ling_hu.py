import lib
import cm
from lib import rnd


def 灵狐乐园(wk: cm.Worker):
    wk.cur_task = "[灵狐]"
    cm.team.set_leader_task(wk, wk.cur_task)
    wk.record("开始执行")

    while wk.done_count < 20:
        if cm.cur_map(wk) != "灵狐乐园":
            goto_accept_ling_hu(wk)
        else:
            if cm.is_fight(wk):
                fight_catch(wk)
            else:
                cm.walk_around_until_fight(wk)

    if cm.is_fight(wk):
        cm.fight_operation(wk)
    wk.record("已完成20只,飞出灵狐乐园")
    cm.fly_to_map(wk, "临仙镇")
    cm.team.set_leader_task(wk)


# 进入灵狐乐园
def goto_accept_ling_hu(wk: cm.Worker):
    wk.record("正在进入灵狐乐园...")
    cm.use_fei_xing_qi(wk, "长安城", cm.FLAG_RECT["捉鬼"])
    x, y = cm.NPC_POS_WND["小狐仙"]
    for i in range(30):
        if cm.cur_map(wk) == "灵狐乐园":
            cm.close_around_list(wk)
            return
        if cm.click_talk_specify_item(wk, "出发吧", 300):
            cm.click_talk_specify_item(wk, "确定", 300)
        cm.close_talk(wk)
        if not wk.is_find_way:
            cm.click_map_wnd_pos(wk, x, y)
            cm.around_list_click_npc(wk, "周围_小狐仙.bmp")
        lib.msleep(600)


# 战斗捕捉
def fight_catch(wk: cm.Worker):
    wk.record("战斗开始")
    cm.close_all_sub_wnd(wk)
    lib.msleep(500)
    round = 0
    while cm.is_fight(wk, 300):
        lib.msleep(400)
        if cm.is_in_fight_ready(wk, 300):
            round += 1
            wk.record(f"战斗中, 第{round}轮")
            if not catch_hu_xiao_meng(wk):
                cm.fight_operation(wk)
                return
        else:
            cm.click_defend(wk)  # 宠物未操作则点击防御
    wk.record("战斗结束")
    cm.schedule_query_cur_task_done_count(wk, 20)
    lib.msleep(500)


# 捉狐小萌
def catch_hu_xiao_meng(wk: cm.Worker):
    if not cm.is_in_fight_ready(wk):
        return False
    x, y = wk.get_str_pos(*cm.RECT_ENEMY, "萌狐|小萌", cm.COLOR_FIGHT_UNIT)
    if x < 0:
        wk.record("未发现狐小萌")
        return False
    if wk.find_str(x-70, y-5, x, y+20, "受惊", cm.COLOR_FIGHT_UNIT):
        wk.record("发现受惊的狐小萌, 杀!")
        return False
    wk.record("发现狐小萌, 正在捕捉...")
    cm.click_catch(wk)
    lib.msleep(100, 500)
    for i in range(20):
        wk.move_to(x + rnd(-15, 15), y - rnd(40, 50))
        lib.msleep(100, 200)
        if wk.find_str(*cm.RECT_ENEMY, "萌狐|小萌", cm.COLOR_RED, timeout=200):
            wk.left_click()
            lib.msleep(500)
            if cm.is_specify_target_success(wk):
                cm.click_defend(wk)
                return True
    return False

