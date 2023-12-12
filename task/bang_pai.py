import lib
import cm
from lib import rnd


def 帮派经商(wk: cm.Worker):
    wk.cur_task = "[经商]"
    wk.record("开始执行")

    while wk.done_count < cm.get_cur_task_specify_count(wk):
        cur_map = cm.cur_map(wk)
        if cur_map != "经商之路":
            goto_accept_bai_hu(wk)  # 接白虎任务, 进入经商之路
        else:
            wk.re_move(rnd(300, 600), rnd(100, 400))  # 避免卡商店
            if is_js_turn_me(wk):
                if wk.find_pic_r_click(*cm.RECT_JS_CARD, "经商购地卡.bmp"):
                    wk.record("已使用购地卡")
            lib.msleep(100, 200)
            js_click_talk(wk)  # 经商点击对话

            if wk.find_pic_click(*cm.RECT_FULL, "经商彩票3.bmp|经商彩票4.bmp|经商彩票5.bmp|经商彩票6.bmp|经商彩票8.bmp"):
                wk.record("已购买彩票")
            lib.msleep(100, 200)

            if wk.find_pic_click(*cm.RECT_FULL, "经商离开1.bmp|经商离开2.bmp"):
                wk.record("已关闭卡片商店")
            lib.msleep(100, 200)
            js_click_talk(wk)  # 经商点击对话

            if is_js_turn_me(wk):
                wk.find_str_click(*cm.RECT_TIP_CENTER, "GO", cm.COLOR_BLACK)
                wk.record("已掷骰子")
            lib.msleep(100, 200)

            if cm.click_confirm(wk):
                wk.record("已点击确定")
            lib.msleep(100, 200)

            if wk.find_pic_click(*cm.RECT_FULL, "经商马市.bmp"):
                wk.record("已建造马市")
            lib.msleep(100, 200)
            js_click_talk(wk)  # 经商点击对话

            if wk.find_pic_click(*cm.RECT_TIP_CENTER, "经商返回帮派1.bmp|经商返回帮派2.bmp"):
                wk.done_count += 1
                wk.record(f"经商完成次数: {wk.done_count}/{cm.get_cur_task_specify_count(wk)}")
                lib.msleep(1000)
        lib.msleep(400)
        # 防止一次没点到
        wk.find_pic_click(*cm.RECT_TIP_CENTER, "经商返回帮派1.bmp|经商返回帮派2.bmp")


def 帮派玄武(wk: cm.Worker):
    wk.cur_task = "[玄武]"
    wk.record("开始执行")

    switch = {
        "接任务": goto_accept_xuan_wu,
        "完成": submit_task,
        "消灭强盗": xiao_mie_qiang_dao,
        "巡逻任务": xun_luo_ren_wu,
        "筹集物资": chou_ji_wu_zi,
        "训练守护兽": xun_lian_shou_hu_shou,
        # 下面三个是青龙专属
        "捕捉宠物": qing_long_buy_pet,
        "材料收集": cai_liao_shou_ji,
        "招募工匠": zhao_mu_gong_jiang,
    }
    while wk.done_count < cm.get_cur_task_specify_count(wk):
        task_type = cm.sub_task(wk)
        try:
            switch[task_type](wk)
        except:
            wk.record(f"未知的子任务类型:{task_type}")
        lib.msleep(600)


def 帮派青龙(wk: cm.Worker):
    wk.cur_task = "[青龙]"
    wk.record("开始执行")

    switch = {
        "接任务": goto_accept_qing_long,
        "完成": submit_task,
        "捕捉宠物": qing_long_buy_pet,
        "材料收集": cai_liao_shou_ji,
        "招募工匠": zhao_mu_gong_jiang,
        # 下面四个是玄武专属
        "消灭强盗": xiao_mie_qiang_dao,
        "巡逻任务": xun_luo_ren_wu,
        "筹集物资": chou_ji_wu_zi,
        "训练守护兽": xun_lian_shou_hu_shou,
    }
    while wk.done_count < cm.get_cur_task_specify_count(wk):
        task_type = cm.sub_task(wk)
        try:
            switch[task_type](wk)
        except:
            wk.record(f"未知的子任务类型:{task_type}")
        lib.msleep(600)


def 帮派强盗(wk: cm.Worker):
    wk.cur_task = "[帮派强盗]"
    wk.record("开始执行")

    if not back_to_faction(wk):
        return
    start = lib.cur_time_stamp
    for i in range(100):
        if lib.delta_minute(start, lib.cur_time_stamp) > 2:
            wk.record("超过2分钟未找到强盗, 自动结束")
            break
        wk.record("正在寻找帮派强盗...")
        cm.walk_in_order_until_around_click(wk, "周围_强盗.bmp")
        for i in range(5):
            lib.msleep(500, 800)
            if cm.click_talk_specify_item(wk, "看打", 400):
                wk.record("找到强盗, 对话进入战斗")
                start = lib.cur_time_stamp
                if cm.is_fight(wk, 400):
                    cm.fight_operation(wk)
                break
            else:
                cm.close_talk(wk)


# 找车夫送到帮派地点
def goto_car_man_faction_pos(wk: cm.Worker, place: str):
    x, y = cm.NPC_POS_WND["帮派车夫"]
    for i in range(10):
        if cm.goto_pos_npc_talk(wk, x, y, place):
            lib.msleep(1000)  # 传送时间
            break


# 回到本帮派
def back_to_faction(wk: cm.Worker):
    if cm.cur_map(wk) == "帮派地图":
        return True
    if wk.find_pic_r_click(*cm.RECT_QUICK_BAR, "技_帮派传送符.bmp"):
        wk.record("使用帮派传送符 回帮派 ")
        lib.msleep(800)
    x, y = cm.NPC_POS_WND["帮派总管"]
    for i in range(10):
        if cm.cur_map(wk) == "帮派地图":
            return True
        wk.record("使用飞行旗 回帮派")
        cm.use_fei_xing_qi(wk, "长安城", cm.FLAG_RECT["帮派"])
        cm.goto_pos_npc_talk(wk, x, y, "送我回帮派")
        lib.msleep(1000)
        cm.close_talk(wk)  # 防止卡对话
    return False

# 获取帮派NPC位置
def get_faction_npc_pos(wk: cm.Worker):
    if (-1, -1) not in wk.faction_npc_pos.values():  # 若已经获取过直接返回
        return
    wk.record("正在获取帮派NPC位置...")
    cm.click_map_wnd_pos(wk, *cm.POS_FACTION_AVOID)

    for i in range(3):
        if (-1, -1) not in wk.faction_npc_pos.values():
            break
        cm.open_map(wk)
        if wk.faction_npc_pos["白虎"] == (-1, -1):
            x, y = wk.get_str_pos(*cm.RECT_FULL, "白虎", cm.COLOR_MAP_NPC)
            if (x, y) != (-1, -1):
                wk.faction_npc_pos["白虎"] = x + 33, y + 18
        if wk.faction_npc_pos["青龙"] == (-1, -1):
            x, y = wk.get_str_pos(*cm.RECT_FULL, "青龙", cm.COLOR_MAP_NPC)
            if (x, y) != (-1, -1):
                wk.faction_npc_pos["青龙"] = x + 33, y + 18
        if wk.faction_npc_pos["玄武"] == (-1, -1):
            x, y = wk.get_str_pos(*cm.RECT_FULL, "玄武", cm.COLOR_MAP_NPC)
            if (x, y) != (-1, -1):
                wk.faction_npc_pos["玄武"] = x + 33, y + 18
        cm.close_map(wk)
        lib.msleep(600)

    wk.record("获取帮派NPC位置完成")


# --------------------------- 帮派经商 ---------------------------
# 去接白虎
def goto_accept_bai_hu(wk: cm.Worker):
    if not back_to_faction(wk):
        return
    # 回到帮派后识别NPC位置
    get_faction_npc_pos(wk)
    # 找车夫送到白虎堂
    x, y = cm.wnd_pos_to_true_pos("帮派地图", *wk.faction_npc_pos["白虎"])
    wk.record("正在接任务...")
    if not cm.is_pos_near(wk, "帮派地图", x, y):  # 若坐标较远, 先找车夫
        goto_car_man_faction_pos(wk, "白虎堂")
    # 和白虎堂总管对话
    for i in range(10):
        if cm.is_talk_open(wk):
            if cm.click_talk_specify_item(wk, "进行经商"):
                lib.msleep(600)
                if cm.is_talk_have_content(wk, "经商满次"):
                    wk.done_count = 2
                    wk.record(f"经商完成次数: {wk.done_count}/2")
                    return
            cm.close_talk(wk)
        if wk.find_pic(*cm.RECT_FULL, "经商选择角色.bmp", timeout=300):
            lib.msleep(400, 600)
            break
        if not wk.is_find_way:
            cm.click_map_wnd_pos(wk, *wk.faction_npc_pos["白虎"])
        lib.msleep(1000)
    else:
        return
    wk.record("正在选择角色和难度...")
    # 选择角色
    role = lib.cfg_main["经商角色"]
    dfct = lib.cfg_main["经商难度"]
    pic_role = f"经商{role}.bmp"
    pic_dfct = f"经商{dfct}.bmp"
    wk.find_pic_click(*cm.RECT_FULL, pic_role)
    lib.msleep(400, 600)
    wk.find_pic_click(*cm.RECT_FULL, pic_dfct)
    lib.msleep(400, 600)
    wk.move_click(*cm.POS_JS_CONFIRM)
    lib.msleep(800, 1000)

# 是否经商轮到自己
def is_js_turn_me(wk: cm.Worker):
    if wk.find_str(*cm.RECT_TIP_CENTER, "GO", cm.COLOR_BLACK):
        return True
    return False


# 经商点击对话
def js_click_talk(wk: cm.Worker):
    wk.find_color_click(*cm.RECT_TALK_BACK, cm.COLOR_TALK_BACK)



# --------------------------- 帮派玄武 ---------------------------
# 去接玄武
def goto_accept_xuan_wu(wk: cm.Worker):
    if not back_to_faction(wk):
        return
    # 回到帮派后识别NPC位置
    get_faction_npc_pos(wk)
    # 找车夫送到玄武堂
    x, y = wk.faction_npc_pos["玄武"]
    tx, ty = cm.wnd_pos_to_true_pos("帮派地图", x, y)
    wk.record("正在接任务...")
    if not cm.is_pos_near(wk, "帮派地图", tx, ty):  # 若坐标较远, 先找车夫
        goto_car_man_faction_pos(wk, "玄武堂")
    # 和玄武堂总管对话
    if cm.goto_pos_npc_talk(wk, x, y, "接玄武"):
        lib.msleep(300)
        if cm.is_task_over(wk, 300):
            return
        cm.close_talk(wk)
        cm.set_task_to_cur_task_bar(wk)



# 找总管交任务 (青龙, 玄武通用)
def submit_task(wk: cm.Worker):
    if not back_to_faction(wk):
        return
    if not cm.goto_task_npc_talk(wk):
        return
    if cm.click_talk_specify_item(wk, "交任务", 200):
        lib.msleep(600)
        if cm.click_talk_specify_item(wk, "交帮派", 200):
            lib.msleep(800)
    # 给予物品或宠物
    cm.give_task_goods_pet(wk)
    # 更新任务完成次数
    if not cm.is_task_on_cur_task_bar(wk):  # 若任务不在当前任务栏才更新次数
        cm.update_task_done_count(wk)
    cm.close_talk(wk)

def xiao_mie_qiang_dao(wk: cm.Worker):
    wk.record("任务类型: 消灭强盗")
    cm.fly_task_map_fight(wk)

def xun_luo_ren_wu(wk: cm.Worker):
    wk.record("任务类型: 巡逻任务")
    back_to_faction(wk)
    for i in range(30):
        if cm.is_fight(wk):
            cm.fight_operation(wk)
            cm.update_task_done_count(wk)
            break
        else:
            cm.walk_around_until_fight(wk)
        lib.msleep(600)

def chou_ji_wu_zi(wk: cm.Worker):
    wk.record("任务类型: 筹集物资")
    cm.buy_task_need_goods(wk)

def xun_lian_shou_hu_shou(wk: cm.Worker):
    wk.record("任务类型: 训练守护兽")
    if not back_to_faction(wk):
        return
    cm.goto_task_npc_talk(wk)
    cm.close_talk(wk)
    if cm.is_fight(wk):
        cm.fight_operation(wk)


# --------------------------- 帮派青龙 ---------------------------
def goto_accept_qing_long(wk: cm.Worker):
    if not back_to_faction(wk):
        return
    # 回到帮派后识别NPC位置
    get_faction_npc_pos(wk)
    # 找车夫送到青龙堂
    x, y = wk.faction_npc_pos["青龙"]
    tx, ty = cm.wnd_pos_to_true_pos("帮派地图", x, y)
    wk.record("正在接任务...")
    if not cm.is_pos_near(wk, "帮派地图", tx, ty):  # 若坐标较远, 先找车夫
        goto_car_man_faction_pos(wk, "青龙堂")
    # 和青龙堂总管对话
    if cm.goto_pos_npc_talk(wk, x, y, "接青龙"):
        lib.msleep(300)
        if cm.is_task_over(wk, 300):
            return
        cm.close_talk(wk)
        cm.set_task_to_cur_task_bar(wk)


def qing_long_buy_pet(wk: cm.Worker):
    wk.record("任务类型: 捕捉宠物")
    cm.buy_task_pet(wk)


def cai_liao_shou_ji(wk: cm.Worker):
    wk.record("任务类型: 材料收集")
    cm.buy_task_need_goods(wk)

def zhao_mu_gong_jiang(wk: cm.Worker):
    wk.record("任务类型: 招募工匠")
    cm.fly_task_npc_talk(wk)
    if cm.is_talk_open(wk):
        cm.close_talk(wk)
        cm.update_task_done_count(wk)


# --------------------------- 帮派强盗 ---------------------------
