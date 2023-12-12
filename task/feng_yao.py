import lib
import cm

def 带队封妖(wk: cm.Worker):
    wk.cur_task = "[封妖]"
    cm.team.set_leader_task(wk, wk.cur_task)
    wk.record("开始执行")

    cm.close_task_track(wk)
    fy_map = lib.cfg_main["封妖地图"]
    while wk.done_count < cm.get_cur_task_specify_count(wk):
        cm.use_qu_mo_xiang(wk)  # 中途补下驱魔香
        if cm.cur_map(wk) != fy_map:  # 若不在设定地图,则先飞到指定地图
            wk.record(f"正在前往封妖地图:{fy_map}")
            cm.fly_to_map(wk, fy_map)
        lib.msleep(800)
        if not talk_with_yuan_gu(wk) and not wk.is_find_way:
            goto_next_pos(wk)
        if cm.is_fight(wk):
            cm.fight_operation(wk)
            cm.update_task_done_count(wk)
    cm.open_task_track(wk)
    cm.team.set_leader_task(wk)


def talk_with_yuan_gu(wk: cm.Worker):
    for i in range(10):
        if cm.click_talk_specify_item(wk, "开打", 400):
            lib.msleep(400)
            cm.close_talk(wk)
            return True
        if not click_nearest_yuan_gu(wk) and not wk.is_find_way:
            return False
        lib.msleep(600)


def goto_next_pos(wk: cm.Worker):
    cm.close_all_sub_wnd(wk)
    wk.record("未发现远古妖怪, 边跑边找...")
    cm.walk_in_order(wk, click_nearest_yuan_gu)



def click_nearest_yuan_gu(wk: cm.Worker):
    cx, cy = cm.POS_CENTER
    x, y = wk.find_pic_nearest_pos(*cm.RECT_FULL, "远古.bmp|远古2.bmp", cx, cy, sim=0.9)
    if x > 0:
        wk.move_click(x + 32, y - 30, False)  # 点击远古妖怪
        return True
    return False
