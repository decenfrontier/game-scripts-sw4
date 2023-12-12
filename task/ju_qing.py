import lib
import cm
from lib import rnd
from cm import RECT_FULL

def 主线剧情(wk: cm.Worker):
    wk.cur_task = "[剧情]"
    wk.record("开始执行")

    while wk.done_count < 3:  # 有3次没找到主线剧情则结束
        task_type = cm.sub_task(wk)
        if task_type == "找人":
            proc_find_people(wk)
        elif task_type == "对话":
            cm.talk_proc(wk)
        elif task_type == "购买物品":
            proc_buy_goods(wk)
        elif task_type == "青河小霸王":
            qing_he_xiao_ba_wang(wk)
        elif task_type == "接任务":
            cm.set_task_to_cur_task_bar(wk)
            wk.done_count += 1
        elif task_type == "等级不足":
            wk.record("人物等级未达到剧情要求, 自动结束主线剧情")
            break
        lib.msleep(600)


def qing_he_xiao_ba_wang(wk: cm.Worker):
    wk.record("任务类型: 青河小霸王")
    # 跑去青河小霸王处对话
    for i in range(100):
        if not wk.is_find_way:
            cm.task_npc_find_way(wk)
        lib.msleep(500)
        if cm.is_talk_open(wk):
            cm.talk_proc(wk)
            break
    # 战斗, 捕捉
    while cm.is_fight(wk, 300):
        if cm.is_in_fight_ready(wk, 300):
            if cm.click_catch(wk):
                wk.move_click(cm.POS_QHXBW[0], cm.POS_QHXBW[1])
        lib.msleep(500)
    cm.close_talk(wk)

def proc_buy_goods(wk: cm.Worker):
    wk.record("任务类型: 购买物品")
    goods_name = cm.ocr_task_need_goods(wk)
    cm.buy_goods(wk, goods_name)

def proc_find_people(wk: cm.Worker):
    wk.record("任务类型: 找人")
    for i in range(10):
        if cm.is_talk_open(wk):
            wk.record("对话中...")
            cm.talk_proc(wk)
            break
        if wk.find_pic_click(*cm.RECT_SKIP_ANIMATION, "跳过动画.bmp"):
            wk.record("检测到出现动画, 已自动跳过")
            lib.msleep(500)
            break
        if not wk.is_find_way:
            cm.task_npc_find_way(wk)
        lib.msleep(500, 1000)