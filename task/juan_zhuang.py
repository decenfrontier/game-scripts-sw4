import lib
import cm


def 捐献装备(wk: cm.Worker):
    wk.cur_task = "[捐装]"
    wk.record("开始执行")

    level = lib.cfg_main["捐献装备等级"]
    num = int(lib.cfg_main["捐献装备数量"])
    buy_zhuang_bei_ling(wk, level, num)
    make_zhuang_bei(wk, num)
    donate_zhuang_bei(wk)
    cm.close_all_sub_wnd(wk)


# 购买装备灵
def buy_zhuang_bei_ling(wk: cm.Worker, level: int, num: int):
    wk.record("正在购买装备灵...")
    cm.open_swb_ui(wk)
    if not cm.is_swb_ui_open(wk):
        return
    pic = f"{level}级装备之灵.bmp"
    wk.find_pic_click(*cm.RECT_FULL, "装备相关.bmp", timeout=300)
    lib.msleep(600)
    wk.find_pic_click(*cm.RECT_FULL, pic, timeout=300)
    lib.msleep(1000)
    # 找出最便宜的, 买num个
    min_price, min_pos = cm.swb_get_cheapest_price_pos(wk)
    wk.record(f"当前最低价装备之灵价格:{min_price}, 位置:{min_pos}")
    # 选中要购买的物品, 点两次防止没点到
    wk.move_click(*min_pos)
    wk.move_click(*min_pos, False)
    # 点击购买
    for i in range(1, num+1):
        wk.move_click(*cm.POS_SWB_BUY, False)
        wk.record(f"已购买装备灵: {i}个")
        lib.msleep(500, 700)
    cm.close_all_sub_wnd(wk)
    wk.record("购买装备灵完成")
    lib.msleep(600, 800)


# 制作装备
def make_zhuang_bei(wk: cm.Worker, num: int):
    wk.record("正在制作装备...")
    cm.open_bag(wk)
    cm.tidy_bag(wk)
    lib.msleep(600)
    cm.bag_use_goods(wk, cm.PIC_ZB_LING)
    lib.msleep(500)
    if not cm.is_zhuang_bei_ui_open(wk, 300):
        wk.record("制作装备失败, 装备界面未成功打开")
        return False
    wk.find_pic_click(*cm.RECT_FULL, "装备强化制造.bmp")
    wk.find_pic_click(*cm.RECT_FULL, "装备不鉴定.bmp")
    for i in range(1, num+1):
        wk.move_click(*cm.POS_MAKE_ZB, False)
        wk.record(f"已制作装备: {i}个")
        lib.msleep(500, 800)
    wk.record("制作装备完成")
    return True


# 捐献装备
def donate_zhuang_bei(wk: cm.Worker):
    cm.open_zhuang_bei_ui(wk)
    if not cm.is_zhuang_bei_ui_open(wk):
        wk.record("装备界面打开失败")
        return
    wk.move_click(*cm.POS_DONATE_SELL_ZB)
    lib.msleep(600, 800)
    wk.move_click(*cm.POS_DONATE_ZB)
    lib.msleep(600, 800)
    # 快速选择 非贵重
    wk.move_click(*cm.POS_GOODS_SEL_LBTN)
    lib.msleep(600, 800)
    # 选中 贵重
    if lib.cfg_main["捐献贵重装备"]:
        # pos_list = [(0,100,20), (0,30,40)]
        pos_list = wk.find_pic_ex(*cm.RECT_FULL, "贵重.bmp")
        for idx, x, y in pos_list:
            wk.move_click(x, y)
            lib.msleep(300, 500)
        lib.msleep(600, 800)
    for i in range(3):
        if cm.click_confirm(wk):  # 确认
            break
        wk.move_click(*cm.POS_GOODS_SEL_RBTN)  # 确定
        lib.msleep(600)
