import lib
import cm

OPENED_TREASURE_MAP = "物_藏宝图1.bmp|物_藏宝图2.bmp|物_藏宝图3.bmp|物_藏宝图4.bmp|物_藏宝图5.bmp|" \
                      "物_藏宝图6.bmp|物_藏宝图7.bmp|物_藏宝图8.bmp|物_藏宝图9.bmp"
UNOPENED_TREASURE_MAP = "物_藏宝图.bmp"
ALL_TREASURE_MAP = f"{OPENED_TREASURE_MAP}|{UNOPENED_TREASURE_MAP}"


def 自动挖宝(wk: cm.Worker):
    wk.cur_task = "[挖宝]"
    wk.record("开始执行")
    dig_treasure(wk)


# 挖宝
def dig_treasure(wk: cm.Worker):
    cm.use_qu_mo_xiang(wk)
    cm.tidy_bag(wk)
    not_find_count = 0
    while not_find_count < 3:
        if not is_bag_have_treasure_map(wk):
            not_find_count += 1
            lib.msleep(1000)
            continue
        # 识别并飞到藏宝地图
        map_name = ocr_treasure_map(wk)
        if map_name == "":
            lib.msleep(500)
            continue
        cm.fly_to_map(wk, map_name)
        # 点开藏宝标记
        if not open_treasure_flag(wk):
            cm.tidy_bag(wk)
            continue
        cm.close_bag(wk)
        # 到最近藏宝坐标挖宝
        goto_nearest_treasure_pos(wk)
        lib.msleep(600)
    cm.close_bag(wk)


# 是否背包有宝图
def is_bag_have_treasure_map(wk: cm.Worker):
    cm.open_bag(wk)
    x, y = wk.get_pic_pos(*cm.RECT_FULL, "行囊页.bmp|行囊页2.bmp")
    if x == -1:  # 若背包未打开
        wk.record("背包打开失败")
        return False
    x1, y1, x2, y2 = x - 259, y - 40, x, y + 355  # 背包物品格范围
    if wk.find_pic(x1, y1, x2, y2, ALL_TREASURE_MAP):
        return True
    cm.bag_change_page(wk)
    if wk.find_pic(x1, y1, x2, y2, ALL_TREASURE_MAP):
        cm.tidy_bag(wk)  # 整理背包, 把第二页的藏宝图自动转到第一页去
        return True
    return False


# 识别藏宝地图名
def ocr_treasure_map(wk: cm.Worker):
    cm.open_bag(wk)
    x, y = wk.get_pic_pos(*cm.RECT_FULL, ALL_TREASURE_MAP)
    map_name = ""
    if x > 0:
        wk.move_to(x, y)
        lib.msleep(600)
        p_x, p_y = wk.get_str_pos(*cm.RECT_FULL, "宝地点", cm.COLOR_YELLOW, timeout=400)
        if p_x > 0:
            map_name = wk.ocr(p_x - 5, p_y, p_x + 120, p_y + 60, cm.COLOR_TREASURE)
            wk.record(f"藏宝地点: {map_name}")
        wk.re_move()
    cm.close_bag(wk)
    return map_name


# 打开藏宝标记
def open_treasure_flag(wk: cm.Worker):
    cm.open_bag(wk)
    # 若打开背包即发现标记打开
    if wk.find_pic(*cm.RECT_FULL, OPENED_TREASURE_MAP):
        return True
    # 右击藏宝图
    if not wk.find_pic_r_click(*cm.RECT_FULL, UNOPENED_TREASURE_MAP):
        return False
    return True


# 获取最近藏宝图索引, 没找到返回0, 若索引1最近, 则返回1
def get_nearest_treasure_map_idx(wk: cm.Worker):
    x, y = cm.get_role_pos(wk)
    if x < 0:
        return 0
    cm.open_map(wk)
    # pos_list = [(0,100,20), (1,30,40)]
    pos_list = wk.find_str_ex(*cm.RECT_FULL, "1|2|3|4|5|6|7|8|9", cm.COLOR_TREASURE_IDX, zk=cm.ZK_DIGIT_CLEAR)
    # 逐个计算与人物坐标x,y的距离, 并找出距离最短的idx
    min_dist, min_idx = 1000000, 0
    for pos in pos_list:  # (0, 100, 20)
        idx, p_x, p_y = pos[0], pos[1], pos[2]
        dist = (p_x - x) ** 2 + (p_y - y) ** 2
        if dist < min_dist:
            min_dist = dist
            min_idx = idx + 1
    return min_idx


# 到最近藏宝坐标
def goto_nearest_treasure_pos(wk: cm.Worker):
    for i in range(9):
        # 跑到最近藏宝坐标
        idx = get_nearest_treasure_map_idx(wk)
        cm.open_map(wk)
        font = str(idx) if idx > 0 else "1|2|3|4|5|6|7|8|9"  # 未找到最近的, 则随便找一个
        if not wk.find_str_click(*cm.RECT_FULL, font, cm.COLOR_TREASURE_IDX, zk=cm.ZK_DIGIT_CLEAR):
            break
        cm.close_map(wk)
        # 若在寻路, 则等待, 至多20秒
        for i in range(40):
            lib.msleep(500)
            if not wk.is_find_way:
                cm.right_down_use(wk)
                lib.msleep(500)
                if cm.is_fight(wk, 400):
                    cm.fight_operation(wk)
                break
    cm.close_map(wk)