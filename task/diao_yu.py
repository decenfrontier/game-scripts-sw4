import lib
import cm
from lib import rnd

def 休闲钓鱼(wk: cm.Worker):
    wk.cur_task = "[钓鱼]"
    cm.team.set_leader_task(wk, wk.cur_task)
    wk.record("开始执行")

    while wk.done_count < cm.get_cur_task_specify_count(wk):
        ret = case(wk)
        if ret == "等待":
            lib.msleep(600)
        elif ret == "抛竿确定力度":
            case_pao_gan(wk)
        elif ret == "收取":
            case_shou_qu(wk)
        elif ret == "对话":
            case_talk(wk)
        elif ret == "协力":
            case_xie_li(wk)
        elif ret == "去钓鱼地点":
            case_goto_diao_yu_place(wk)
        lib.msleep(100)

    close_diaoyu_ui(wk)
    cm.team.set_leader_task(wk)


# 情况
def case(wk: cm.Worker):
    if cm.is_fight(wk):
        cm.fight_operation(wk)
    else:
        cm.close_around_list(wk)
        cm.close_map(wk)
        cm.close_bag(wk)

    if wk.flag:
        wk.record("等待中...")

    wk.flag = 1
    lib.msleep(100)
    if wk.find_pic(*cm.RECT_DIAO_YU, "钓鱼确定.bmp|钓鱼确定2.bmp"):
        return "抛竿确定力度"

    lib.msleep(100)
    if wk.find_pic_click(*cm.RECT_DIAO_YU, "钓鱼抛竿.bmp|钓鱼抛竿2.bmp"):
        wk.record("已点击 抛竿")

    lib.msleep(100)
    if wk.find_pic_click(*cm.RECT_DIAO_YU, "钓鱼收竿.bmp|钓鱼收竿2.bmp"):
        wk.record("已点击 收竿")

    lib.msleep(100)
    if wk.find_pic(*cm.RECT_DIAO_YU, "钓鱼收取.bmp|钓鱼收取2.bmp|钓鱼收取3.bmp"):
        return "收取"

    lib.msleep(100)
    if wk.find_pic(*cm.RECT_DIAO_YU, "协力钓鱼1.bmp|协力钓鱼2.bmp"):
        return "协力"

    lib.msleep(100)
    if not is_diao_yu_ui_open(wk):
        return "去钓鱼地点"

    lib.msleep(100)
    if cm.is_talk_open(wk):
        return "对话"

    wk.flag = 0
    return "等待"


# 是否钓鱼界面打开
def is_diao_yu_ui_open(wk: cm.Worker):
    if wk.find_pic(*cm.RECT_DIAO_YU, "界_钓鱼.bmp|钓鱼退出1.bmp|钓鱼退出2.bmp|钓鱼宝物1.bmp|钓鱼宝物2.bmp"):
        return True
    return False


# 情况-抛竿
def case_pao_gan(wk: cm.Worker):
    wk.record("正在调整抛竿力度...")
    x, y = cm.POS_CENTER
    x, y = x + rnd(-5, 5), y + rnd(-2, 2)
    if lib.cfg_main["钓鱼抛竿"] == "立刻抛竿":
        wk.move_click(x, y)
        return
    # 移到确定处
    wk.move_to(x, y)
    # 找到力度条黄区左边位置
    left_x, _ = wk.get_color_pos(*cm.RECT_FORCE_BAR, cm.COLOR_FORCE_BAR)  # 力度条黄区左边
    right_x = left_x + 15
    if left_x < 0:
        return
    center_x = left_x + 7  # 黄区中心X
    for i in range(200):
        lib.msleep(25)
        slider_x, _ = wk.get_pic_pos(*cm.RECT_FORCE_BAR, "力度条滑块.bmp")
        slider_x += 8  # 滑块中心X
        dist = slider_x - center_x
        if abs(dist) < 15:
            wk.left_click(False)
            break
    lib.msleep(300, 500)
    wk.re_move()


# 情况-收取
def case_shou_qu(wk: cm.Worker):
    wk.record("钓鱼成功, 选择 收藏 或 兑换积分..")
    if lib.cfg_main["钓鱼处理"] == "优先收藏":
        if wk.find_pic_click(*cm.RECT_DIAO_YU, "钓鱼收藏.bmp|钓鱼收藏2.bmp"):
            wk.record("鱼已收藏")
        elif wk.find_pic_click(*cm.RECT_DIAO_YU, "钓鱼兑换1.bmp|钓鱼兑换2.bmp"):
            wk.record("鱼已兑换积分")
    else:  # 全部换积分,优先直接换积分,若因为有收藏价值,不能直接换积分,则先收取到背包中
        if wk.find_pic_click(*cm.RECT_DIAO_YU, "钓鱼兑换1.bmp|钓鱼兑换2.bmp"):
            wk.record("鱼已兑换积分")
        elif wk.find_pic_click(*cm.RECT_DIAO_YU, "钓鱼收取.bmp|钓鱼收取2.bmp|钓鱼收取3.bmp"):
            wk.record("鱼已收取")


# 情况-对话
def case_talk(wk: cm.Worker):
    # 一般情况: 协力钓鱼 或 放弃任务
    cm.click_talk_specify_item(wk, "发起协力钓鱼|放弃任务")
    # 特殊情况: 购买鱼竿
    if cm.is_talk_have_item(wk, "购买鱼竿"):
        wk.record("发现 没有鱼竿, 购买前保证背包有空位")
        cm.shut_talk(wk)  # 必须关闭对话框才能打开背包
        if cm.bag_use_goods(wk, "可收藏.bmp"):
            lib.msleep(500)
            cm.fish_batch_exchange_score(wk)
        cm.close_bag(wk)
        if wk.find_pic_click(*cm.RECT_DIAO_YU, "钓鱼抛竿.bmp|钓鱼抛竿2.bmp", timeout=300):
            lib.msleep(300, 600)
    cm.close_talk(wk, 300)


# 情况-协力
def case_xie_li(wk: cm.Worker):
    if wk.find_pic_click(*cm.RECT_DIAO_YU, "协力钓鱼1.bmp|协力钓鱼2.bmp"):
        wk.record("已点击 协力钓鱼")
    wk.find_pic_click(*cm.RECT_DIAO_YU, "确定1.bmp|确定2.bmp|发起协力钓鱼.bmp", timeout=300)


# 情况-去钓鱼地点
def case_goto_diao_yu_place(wk: cm.Worker):
    map_name = lib.cfg_main["钓鱼地图"]
    wk.record(f"正在前往钓鱼地图:{map_name}")
    if not cm.fly_to_map(wk, map_name):
        return
    wk.record("正在跑向渔夫...")
    map_wndpos_dict = {"青河镇外": (431, 475), "长安城外": (607, 380), "傲来国": (471, 471),
                       "花果山": (299, 351), "桃花岛": (525, 564)}
    map_truepos_dict = {"青河镇外": (66,6), "长安城外": (131, 26), "傲来国": (100,9),
                       "花果山": (66,42), "桃花岛": (96,11)}
    wnd_x, wnd_y = map_wndpos_dict[map_name]
    true_x, true_y = map_truepos_dict[map_name]

    for i in range(30):
        if is_diao_yu_ui_open(wk):
            break
        if cm.is_fight(wk):
            cm.fight_operation(wk)
        if not wk.is_find_way:
            cm.click_map_wnd_pos(wk, wnd_x, wnd_y)
        lib.msleep(600)
        cur_x, cur_y = cm.cur_pos(wk)
        if abs(true_x - cur_x) < 10 and abs(true_y - cur_y) < 10:
            use_yu_gan(wk)
            break


# 使用鱼竿
def use_yu_gan(wk: cm.Worker):
    cm.back_to_team(wk)
    if cm.bag_use_goods(wk, "物_鱼竿.bmp"):
        lib.msleep(500)
        if cm.is_talk_have_content(wk, "官职不能钓鱼", 300):
            cm.close_talk(wk)
            cm.abondon_task(wk, "官职")
        return
    cm.close_bag(wk)

    # 购买鱼竿
    cm.temporary_exit_team(wk)
    for i in range(10):
        cm.around_list_click_npc(wk, "周围_渔夫.bmp")
        lib.msleep(600)
        if cm.is_talk_open(wk):
            if cm.click_talk_specify_item(wk, "购买鱼竿"):
                break
            cm.close_talk(wk)
    cm.back_to_team(wk)

    wk.record("正在使用鱼竿...")
    cm.bag_use_goods(wk, "物_鱼竿.bmp")
    lib.msleep(500)
    if cm.is_talk_have_content(wk, "官职不能钓鱼", 300):
        cm.close_talk(wk)
        cm.abondon_task(wk, "官职")
    cm.close_bag(wk)


# 关闭钓鱼界面
def close_diaoyu_ui(wk: cm.Worker):
    wk.record("钓鱼完成, 退出钓鱼...")
    cm.close_all_sub_wnd(wk)
    # 连续检测两次确保退出
    wk.find_pic_click(*cm.RECT_DIAO_YU, "钓鱼退出1.bmp|钓鱼退出2.bmp", timeout=300)
    wk.find_pic_click(*cm.RECT_DIAO_YU, "钓鱼退出1.bmp|钓鱼退出2.bmp", timeout=300)
