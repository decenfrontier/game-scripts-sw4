import cm
import lib


from cm import RECT_BUFF, RECT_FULL, RECT_TALK_CONTENT_BIG, rnd
from task.wa_bao import dig_treasure, ALL_TREASURE_MAP

USABLE_GOODS = "物_卷宗.bmp|物_队长礼盒.bmp|物_豪华队长礼盒.bmp|物_小许愿果.bmp|" \
               "物_大许愿果.bmp|物_三界密录.bmp|物_开学礼.bmp|" \
               "物_家具设计图.bmp|物_装饰设计图.bmp"

OTHER_GOODS = "物_swb_月亮石.bmp|物_swb_太阳石.bmp|物_swb_舍利子.bmp|物_swb_红玛瑙.bmp|物_swb_神秘石.bmp|" \
              "物_swb_黑宝石.bmp|物_swb_红宝石.bmp|物_swb_黄宝石.bmp|物_swb_蓝宝石.bmp|物_swb_绿宝石.bmp|" \
              "物_swb_洗炼石.bmp|物_swb_宠物经验心得.bmp|物_swb_穹玉.bmp|" \
              "物_金香果.bmp|物_江湖志.bmp|物_炼化符.bmp|物_精灵之心.bmp|物_还童丹.bmp|" \
              "物_荆棘之刺.bmp|物_古藤甲.bmp|物_星光护符.bmp|" \
              "物_雷兽之牙.bmp|物_硬板甲.bmp|物_月光护符.bmp|" \
              "物_蛮兽之角.bmp|物_玄武之铠.bmp|物_阳光护符.bmp|" \
              "物_南明离火.bmp|物_绝对领域.bmp|物_银河加护.bmp|" \
              "物_豆沙元宵.bmp|物_桂花元宵.bmp|物_玫瑰元宵.bmp|物_山渣元宵.bmp|物_芝麻元宵.bmp|" \
              "物_羊皮卷碎片.bmp"


def 清理背包(wk: cm.Worker):
    wk.cur_task = "[清包]"
    wk.record("开始执行")

    while wk.done_count < 5:
        if not receive_mail(wk):  # 收取邮件
            wk.done_count = 4  # 若是无邮件可收,只执行一遍流程即可
        clean_usable_goods(wk)  # 清理可用的物品
        clean_fish(wk)  # 清理鱼
        clean_treasure_map(wk)  # 清理藏宝图
        clean_swb_goods(wk)  # 清理SW币物品
        clean_cash_goods(wk)  # 清理现金物品
        clean_other_goods(wk)  # 清理其它物品
        wk.done_count += 1
        lib.msleep(600)

    cm.tidy_bag(wk)  # 整理背包
    cm.close_bag(wk)  # 关闭背包

# 清理邮件


def receive_mail(wk: cm.Worker):
    if not wk.find_pic(*RECT_BUFF, "buff_邮件.bmp"):
        return False
    wk.record("正在收取邮件...")
    cm.use_fei_xing_qi(wk, "傲来国", cm.FLAG_RECT["天魔里"])
    if cm.cur_map(wk) != "傲来国":
        return False
    for i in range(10):
        if not wk.is_find_way:
            x, y = cm.NPC_POS_WND["邮差"]
            cm.click_map_wnd_pos(wk, x, y)
        lib.msleep(500)
        if cm.is_talk_open(wk, 300):
            if not cm.click_talk_specify_item(wk, "查收信件"):
                cm.close_talk(wk)
        if wk.find_pic_click(*RECT_FULL, "全部.bmp|全部2.bmp", timeout=200):
            cm.close_all_sub_wnd(wk)
            return True
    return False


# 清理可用的物品
def clean_usable_goods(wk: cm.Worker):
    if not cm.is_bag_have_goods(wk, USABLE_GOODS):
        wk.record("背包里没有卷宗或队长礼盒等物品,不需要清理")
        return
    wk.record("正在清理 卷宗 或 队长礼盒等物品...")
    for i in range(3):
        if not cm.bag_use_goods(wk, USABLE_GOODS):
            continue
        lib.msleep(200, 400)
        cm.close_talk(wk)  # 交卷宗时会出对话


# 清理鱼
def clean_fish(wk: cm.Worker):
    if not cm.is_bag_have_goods(wk, cm.PIC_FISH):
        wk.record("背包里没有鱼,不需要清理")
        return
    wk.record("背包需清理 鱼")
    if wk.find_pic_r_click(*RECT_FULL, cm.PIC_FISH):
        lib.msleep(500)
        cm.fish_batch_exchange_score(wk)
    cm.close_all_sub_wnd(wk)


# 清理藏宝图
def clean_treasure_map(wk: cm.Worker):
    if not cm.is_bag_have_goods(wk, ALL_TREASURE_MAP):
        wk.record("背包里没有藏宝图,不需要清理")
        cm.close_bag(wk)
        return
    wk.record("正在清理 藏宝图...")
    if lib.cfg_main["清理背包藏宝图"] == "自动挖宝":
        dig_treasure(wk)
    else:
        cm.close_bag(wk)
        cm.goods_put_depot(wk, ALL_TREASURE_MAP)


# 清理现金物品
def clean_cash_goods(wk: cm.Worker):
    wk.record("正在清理 现金物品...")
    pic_xj = wk.match_pic("物_xj_*.bmp")
    if wk.school != "天魔里":
        pic_aq = "物_梅花镖.bmp|物_罗汉钱.bmp|物_乾坤圈.bmp|物_暴雨梨花针.bmp|物_夺魂珠.bmp|" \
                 "物_毒蝠王.bmp|物_命刻.bmp|物_生死符.bmp|物_修罗闪.bmp|物_迷离.bmp"
        pic_xj = f"{pic_xj}|{pic_aq}"
    if lib.cfg_main["清理背包现金"] == "上架寄售":
        cm.sell_goods_ji_shou(wk, pic_xj)
    else:
        cm.goods_put_depot(wk, pic_xj)


# 清理SW币物品
def clean_swb_goods(wk: cm.Worker):
    wk.record("正在清理 SW币物品...")
    pic_swb = wk.match_pic("物_swb_*.bmp")
    if lib.cfg_main["清理背包SW币"] == "商城出售":
        cm.sell_goods_swb(wk, pic_swb)
    else:
        cm.goods_put_depot(wk, pic_swb)


# 清理其它物品
def clean_other_goods(wk: cm.Worker):
    # 若使用还童丹买宠, 则不存还童丹
    if lib.cfg_main["优先使用还童丹买宠"]:
        pic = OTHER_GOODS.replace("物_还童丹.bmp|", "")
    else:
        pic = OTHER_GOODS
    if not cm.is_bag_have_goods(wk, pic):
        wk.record("背包里没有需要存到仓库的物品")
        cm.close_bag(wk)
        return
    wk.record("正在将 其它物品 存到仓库...")
    cm.close_bag(wk)
    cm.goods_put_depot(wk, pic)
