import lib
import cm

def 边境救援(wk: cm.Worker):
    wk.cur_task = "[边境]"
    cm.team.set_leader_task(wk, wk.cur_task)
    wk.record("开始执行")

    while wk.done_count < cm.get_cur_task_specify_count(wk):
        lib.msleep(800)
        if not goto_accept_bian_jing(wk):
            continue
        if calc_bian_jing_count(wk):
            continue
        if not talk_with_around_npc(wk) and not wk.is_find_way:
            goto_next_pos(wk)
        if cm.is_talk_open(wk):
            cm.talk_proc(wk)
            lib.msleep(300)
        if cm.is_fight(wk):
            cm.fight_operation(wk)


    wk.cur_task = ""
    cm.team.set_leader_task(wk, wk.cur_task)

# 跑去接边境
def goto_accept_bian_jing(wk: cm.Worker):
    if cm.cur_map(wk) == "边境秘营":
        return True
    wk.record("正在进入边境秘营...")
    cm.use_fei_xing_qi(wk, "长安城", cm.FLAG_RECT["捉鬼"])
    x, y = cm.NPC_POS_WND["昭武校尉"]
    for i in range(30):
        if cm.click_talk_specify_item(wk, "进入边境", 200):
            lib.msleep(600)
            if cm.is_task_over(wk, 200):
                return False
            else:
                cm.click_talk_first_item(wk, 200)
        if not wk.is_find_way:
            cm.click_map_wnd_pos(wk, x, y)
            cm.around_list_click_npc(wk, "周围_昭武校尉.bmp")
        lib.msleep(1000)
        if cm.cur_map(wk) == "边境秘营":
            wk.record("已成功进入边境秘营")
            return True
    return False


# 和周围npc说话
def talk_with_around_npc(wk: cm.Worker):
    if not cm.around_list_click_npc(wk, "周围_边境守卫.bmp|周围_边境受困.bmp|周围_边境统领.bmp"):
        return False
    wk.record("正在和周围受困民众说话...")
    for i in range(10):
        lib.msleep(600, 1000)
        if cm.is_talk_open(wk):
            return True
    return False

# 跑去下一地点
def goto_next_pos(wk: cm.Worker):
    cm.close_talk(wk)
    cm.close_around_list(wk)
    if wk.find_str_click(*cm.RECT_CUR_TASK, "蛮族统领", cm.COLOR_CYAN):
        wk.record("正在寻路到蛮族统领...")
        lib.msleep(1000)
        return
    wk.record("正在寻找受困民众...")
    x, y = cm.get_role_pos(wk)
    nx, ny = wk.find_str_nearest_pos(*cm.RECT_FULL, "受困|蛮族", cm.COLOR_MAP_NPC, x, y)
    if nx > 0:
        wk.record("地图上找到受困民众")
        wk.move_click(nx + 36, ny + 20)
        lib.msleep(1000, 1600)
        return
    if x < cm.CENTER_X:
        if y < cm.CENTER_Y:  # 在左上角, 往左下角跑
            cm.click_map_wnd_pos(wk, *cm.POS_MAP_LEFT_DOWN)
        else:  # 在左下角, 往右下角跑
            cm.click_map_wnd_pos(wk, *cm.POS_MAP_RIGHT_DOWN)
    else:
        if y < cm.CENTER_Y:  # 在右上角, 往左上角跑
            cm.click_map_wnd_pos(wk, *cm.POS_MAP_LEFT_UP)
        else:  # 在右下角, 往右上角跑
            cm.click_map_wnd_pos(wk, *cm.POS_MAP_RIGHT_UP)

# 计算边境次数
def calc_bian_jing_count(wk: cm.Worker):
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
    cm.is_task_over(wk, 400)
    return True