import lib
import common
from lib import rnd


def 退出队伍(wk: common.Worker):
    wk.cur_task = "[退队]"
    wk.record("开始执行")

    common.team.add_leader_sig(wk, "退队")
    common.exit_team(wk)


def 幸运转盘(wk: common.Worker):
    wk.cur_task = "[幸运转盘]"
    wk.record("开始执行")

    wk.record("正在使用 幸运转转玉...")
    common.open_bag(wk)
    wk.find_pic_r_click(*common.RECT_FULL, "物_幸运转转玉.bmp")
    wk.find_pic_r_click(*common.RECT_FULL, "物_幸运转转玉.bmp")
    common.bag_change_page(wk)
    wk.find_pic_r_click(*common.RECT_FULL, "物_幸运转转玉.bmp")
    wk.find_pic_r_click(*common.RECT_FULL, "物_幸运转转玉.bmp")
    common.close_bag(wk)

    wk.record("正在寻路到 幸运小昕...")
    common.fly_to_map(wk, "青河镇")
    x, y = common.NPC_POS_WND["幸运小昕"]
    for i in range(3):
        if common.goto_pos_npc_talk(wk, x, y, "玩下幸运转盘"):
            break
        lib.msleep(500)
    wk.record("正在玩幸运转盘...")
    for i in range(30):
        lib.msleep(600, 800)
        if not wk.find_pic_click(*common.RECT_FULL, "转盘转1.bmp|转盘转2.bmp|转盘停1.bmp|转盘停2.bmp|转盘关1.bmp|转盘关2.bmp", timeout=400):
            break
    common.close_all_sub_wnd(wk)


def 转转乐(wk: common.Worker):
    wk.cur_task = "[转转乐]"
    wk.record("开始执行")

    wk.record("正在打开转转乐...")
    common.open_schedule_ui(wk)
    if common.is_schedule_ui_open(wk):
        lib.msleep(600)
        x, y = common.POS_ZHUAN_LE
        wk.move_click(x + rnd(-3, 3), y + rnd(-3, 3))
        lib.msleep(1000)
        if wk.find_pic(*common.RECT_FULL, "界_转转乐.bmp", timeout=400):
            wk.record("正在玩转转乐...")
            for i in range(12):
                wk.find_pic_click(*common.RECT_FULL, "转转乐开始1.bmp|转转乐开始2.bmp|转转乐结束1.bmp|转转乐结束2.bmp")
                lib.msleep(600)
    lib.msleep(600)
    common.close_all_sub_wnd(wk)


def 领取双倍(wk: common.Worker):
    wk.cur_task = "[领取双倍]"
    wk.record("开始执行")

    common.use_fei_xing_qi(wk, "长安城", common.FLAG_RECT["捉鬼"])
    x, y = common.NPC_POS_WND["领双人"]
    double_time = lib.cfg_main["领取双倍时间"]
    for i in range(3):
        if common.goto_pos_npc_talk(wk, x, y, double_time):
            break
        common.close_talk(wk)
        lib.msleep(600)
    common.close_talk(wk)


def 冻结双倍(wk: common.Worker):
    wk.cur_task = "[冻结双倍]"
    wk.record("开始执行")

    common.team.add_leader_sig(wk, "冻双")
    if wk.find_pic_r_click(*common.RECT_BUFF, "buff_双倍.bmp", timeout=400):
        lib.msleep(600, 1000)
        common.click_confirm(wk)


def 制作烹饪(wk: common.Worker):
    wk.cur_task = "[制作烹饪]"
    wk.record("开始执行")
    max_count = common.get_cur_task_specify_count(wk)

    x, y = wk.get_pic_pos(*common.RECT_QUICK_BAR, "技_烹饪.bmp", timeout=300)
    if x < 0:
        wk.record("右侧技能面板未发现烹饪技能")
    else:
        while wk.done_count < max_count:
            wk.done_count += 1
            wk.move_r_click(x + rnd(5, 10), y + rnd(0, 10), False, False)
            wk.record(f"已制作烹饪数: {wk.done_count}")
            lib.msleep(500, 800)
            if wk.find_pic(*common.RECT_TIP_TOP, "烹饪满次.bmp"):
                break
        wk.re_move()


def 经验换修(wk: common.Worker):
    wk.cur_task = "[经验换修]"
    wk.record("开始执行")

    common.fly_to_map(wk, "临仙镇")
    x, y = common.NPC_POS_WND["玄修"]
    for i in range(5):
        if common.goto_pos_npc_talk(wk, x, y, "兑换修炼经验"):
            lib.msleep(300)
            for i in range(6):
                if common.click_talk_first_item(wk):
                    wk.done_count += 1
                    wk.record(f"已换修次数: {wk.done_count}")
                lib.msleep(300, 600)
            break
        else:
            common.close_talk(wk)
        lib.msleep(800)


def 化龙鼎(wk: common.Worker):
    wk.cur_task = "[化龙鼎]"
    wk.record("开始执行")

    if common.open_hld_ui(wk):
        for i in range(3):
            x, y = wk.get_pic_pos(*common.RECT_FULL, "化龙鼎正常修炼.bmp|化龙鼎额外修炼.bmp")
            if x > 0:
                break
            wk.find_pic_click(*common.RECT_FULL, "化龙鼎修炼.bmp")
            lib.msleep(600)
        if x > 0:
            wk.record("正常修炼中...")
            for i in range(50):
                wk.move_click(x + rnd(0, 30), y + rnd(0, 10), False)
                lib.msleep(200, 300)
                if common.is_talk_open(wk):
                    break
        else:
            wk.record("未找到 化龙鼎正常修炼")
        if lib.cfg_main["化龙鼎额外修炼"]:
            common.click_talk_specify_item(wk, "进行额外修炼", 200)
            x, y = wk.get_pic_pos(*common.RECT_FULL, "化龙鼎额外修炼.bmp")
            if x > 0:
                wk.record("额外修炼中...")
                for i in range(7):
                    wk.move_click(x + rnd(0, 30), y + rnd(0, 10), False)
                    lib.msleep(200, 300)
            else:
                wk.record("未找到 化龙鼎额外修炼")
    common.close_all_sub_wnd(wk)

    if lib.cfg_main["化龙鼎兑换龙魂"] and common.open_hld_ui(wk):
        if wk.find_pic_click(*common.RECT_FULL, "化龙鼎加号.bmp"):
            lib.msleep(1000)
            for i in range(3):
                wk.move_click(*common.POS_HLD_DUI_HUAN, False)
                lib.msleep(500, 600)
        common.close_all_sub_wnd(wk)


def 祈福(wk: common.Worker):
    wk.cur_task = "[祈福]"
    wk.record("开始执行")

    # 如果已经做完, 直接返回
    if common.schedule_query_cur_task_done_count(wk, 1):
        return
    # 到祈福僧人处祈福
    wk.record("正在前往祈福僧人处祈福...")
    common.fly_to_map(wk, "傲来国")
    x, y = common.NPC_POS_WND["祈福僧人"]
    for i in range(4):
        if common.goto_pos_npc_talk(wk, x, y, "我要祈福"):
            break
        lib.msleep(800)
        common.close_talk(wk)
    lib.msleep(800)
    # 若未进入祈福转盘, 直接返回
    if not wk.find_pic(*common.RECT_FULL, "祈福接受祝福2.bmp", timeout=400):
        wk.record("祈福转盘未打开, 祈福失败")
        return
    # 祈福转盘
    wk.record("正在祈福中...")
    x, y = common.POS_QF_START_STOP
    for i in range(30):
        lib.msleep(600, 1000)
        if wk.find_pic_click(*common.RECT_FULL, "祈福接受祝福1.bmp"):
            wk.record("祈福接受祝福")
            lib.msleep(600)
            break
        wk.move_click(x + rnd(-5, 5), y + rnd(-5, 5))
    # 防止一次没点到, 多点几次
    for i in range(3):
        lib.msleep(500)
        common.click_confirm(wk)
        wk.find_pic_click(*common.RECT_FULL, "祈福接受祝福1.bmp")


def 修炼宝箱(wk: common.Worker):
    wk.cur_task = "[修炼宝箱]"
    wk.record("开始执行")

    if common.schedule_query_cur_task_done_count(wk, 10):
        return
    common.close_task_track(wk)
    common.use_qu_mo_xiang(wk)
    xn_map = lib.cfg_main["修炼宝箱地图"]
    wk.record(f"正在前往地图 {xn_map}...")
    common.fly_to_map(wk, xn_map)

    for i in range(100):
        if i % 10 == 0:
            common.close_all_sub_wnd(wk)
        wk.record("正在寻找宝箱...")
        common.close_ui(wk)
        common.hide_other_player(wk)
        common.walk_in_order(wk, common.pick_xl_box)
        common.pick_xl_box(wk)  # 再点一次, 防止没点到
        common.update_xl_box_count(wk)
        if wk.done_count >= 10:
            break
        lib.msleep(500)
    common.open_task_track(wk)


def 天降宝箱(wk: common.Worker):
    wk.cur_task = "[天降宝箱]"
    wk.record("开始执行")

    if lib.cur_time_fmt < "18:00:00" or lib.cur_time_fmt > "22:00:00":
        wk.record("未到天降宝箱时间")
        return

    common.close_task_track(wk)
    common.use_qu_mo_xiang(wk)
    xn_map = lib.cfg_main["天降宝箱地图"]
    wk.record(f"正在前往地图 {xn_map}...")
    common.fly_to_map(wk, xn_map)

    start = lib.cur_time_stamp
    for i in range(100):
        # 若已完成, 或持续时间超过5分钟
        if wk.done_count >= 3 or lib.delta_minute(start, lib.cur_time_stamp) > 5:
            break
        if i % 10 == 0:
            common.close_all_sub_wnd(wk)
        wk.record("正在寻找宝箱...")
        common.close_ui(wk)
        common.hide_other_player(wk)
        common.walk_in_order(wk, common.pick_tj_box)
        common.pick_tj_box(wk)  # 再点一次, 防止没点到
        lib.msleep(1000)
        if common.is_progress_bar_open(wk, 400):
            wk.record("已打开宝箱")
            lib.msleep(5000)
            x1, y1 = wk.get_pic_pos(*common.RECT_FULL, "天降宝箱猜拳.bmp")
            if x1 > 0:
                wk.move_click(x1 + rnd(5, 10), y1 - rnd(20, 40), False)
                lib.msleep(1000)
            x2, y2 = wk.get_pic_pos(*common.RECT_FULL, "天降宝箱答案.bmp", order=rnd(0, 3))
            if x2 > 0:
                wk.move_click(x2 + rnd(60, 65), y2 + rnd(5, 10), False)
                lib.msleep(1000)
            wk.re_move()
            wk.done_count += 1
            wk.record(f"已完成: {wk.done_count}/3")
        common.close_all_sub_wnd(wk)
    common.open_task_track(wk)


def 体力打工(wk: common.Worker):
    wk.cur_task = "[体力打工]"
    wk.record("开始执行")

    common.use_fei_xing_qi(wk, "长安城", common.FLAG_RECT["帮派"])
    x, y = common.NPC_POS_WND["林惊羽"]
    for i in range(3):
        if common.goto_pos_npc_talk(wk, x, y, "我要打工"):
            wk.move_to(*common.POS_TALK_BLANK)
            wk.record("已点击 我要打工")
            lib.msleep(600)
            common.click_talk_specify_item(wk, "体力全部", 400)
            break
        common.close_talk(wk)
        lib.msleep(600)
    common.close_talk(wk)
