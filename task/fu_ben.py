import lib
import cm


def 带队副本(wk: cm.Worker):
    wk.cur_task = "[副本]"
    cm.team.set_leader_task(wk, wk.cur_task)
    wk.record("开始执行")

    lead_fu_ben(wk, 1)  # 副本1
    from_ready_hall_return_chang_an(wk)
    lead_fu_ben(wk, 2)  # 副本2
    from_ready_hall_return_chang_an(wk)

    cm.team.set_leader_task(wk)


def 混队副本(wk: cm.Worker):
    wk.cur_task = "[混队副本]"
    wk.record("开始执行")

    follow_fu_ben(wk, 1)  # 副本1

    cm.exit_team(wk)
    from_ready_hall_return_chang_an(wk)

    follow_fu_ben(wk, 2)  # 副本2

    cm.exit_team(wk)
    from_ready_hall_return_chang_an(wk)


# 是否在副本中
def is_in_fu_ben(wk: cm.Worker):
    if cm.cur_map(wk) in cm.MAP_FU_BEN:
        return True
    return False



# 进入洪荒副本
def enter_hong_huang_fu_ben(wk: cm.Worker):
    for i in range(10):
        if not wk.is_find_way:
            cm.around_list_click_npc(wk, "周围_流火.bmp")
        lib.msleep(600)
        if cm.click_talk_specify_item(wk, "进入洪荒战场"):
            break
    else:
        return
    wait_mate_confirm(wk, ori_map="长安城")  # 若队伍已经组满人, 点击"进入洪荒战场"后, 要等待队友确定

# 进入副本 或 准备厅
def enter_fu_ben_or_ready_hall(wk: cm.Worker, fb_name: str, idx: int):
    map_name = cm.cur_map(wk)
    if map_name == "准备厅" or map_name in cm.MAP_FU_BEN:
        return
    wk.record("正在进入副本...")

    cm.use_fei_xing_qi(wk, "长安城", cm.FLAG_RECT["说书先生"])
    if fb_name == "洪荒战场":
        enter_hong_huang_fu_ben(wk)
        return
    if not open_fu_ben_ui(wk):
        return
    if not select_specify_fu_ben(wk, fb_name, idx):
        return
    lib.msleep(500)
    ori_map = cm.cur_map(wk)
    wait_mate_confirm(wk, ori_map="长安城")

# 是否副本界面打开
def is_fu_ben_ui_open(wk: cm.Worker):
    wk.re_move()  # 防tooltip遮挡
    ret = wk.find_pic(*cm.RECT_FULL, "界_副本1.bmp|界_副本2.bmp")
    return ret

# 打开副本界面
def open_fu_ben_ui(wk: cm.Worker):
    for i in range(10):
        if is_fu_ben_ui_open(wk):
            return True
        if not wk.is_find_way:
            x, y = cm.NPC_POS_WND["说书先生"]
            cm.click_map_wnd_pos(wk, x, y)
        if cm.is_talk_open(wk):
            cm.click_talk_specify_item(wk, "听故事")
        lib.msleep(500)
    return False

# 选择设定副本
def select_specify_fu_ben(wk: cm.Worker, fb_name: str, idx: int):
    pic = f"fb_{fb_name}A.bmp|fb_{fb_name}B.bmp"
    for i in range(4):
        x, y = wk.get_pic_pos(*cm.RECT_FULL, pic)
        # 若该副本今日已完成4次
        if x > 0 and wk.find_color(x+67, y+27, x+92, y+45, cm.COLOR_FU_BEN_LINE):
            wk.done_count = int(lib.cfg_main["副本一次数"]) if idx == 1 else int(lib.cfg_main["副本二次数"])
            wk.record("今日已达此副本上限!")
            return False
        if wk.find_pic(*cm.RECT_FULL, f"fb_{fb_name}C.bmp"):
            wk.done_count = int(lib.cfg_main["副本一次数"]) if idx == 1 else int(lib.cfg_main["副本二次数"])
            wk.record("本周已达此副本上限!")
            return False
        if wk.find_pic_click(*cm.RECT_FULL, pic):
            wk.record("已找到并选中设定副本")
            return True
        wk.record("未找到对应副本,继续往下寻找")
        wk.move_wheel_down(299,303,40)
        lib.msleep(100, 200)
    cm.close_all_sub_wnd(wk)
    return False

# 等待队员确定
def wait_mate_confirm(wk: cm.Worker, ori_map: str):
    wk.record("等待其它队员确定...")
    start_sec = lib.cur_time_stamp
    while lib.cur_time_stamp - start_sec < 120:
        if wk.find_pic_click(*cm.RECT_FULL, "进入副本.bmp|进入副本2.bmp") or \
                cm.click_talk_specify_item(wk, "出发吧") or \
                cm.click_confirm(wk):
            start_sec = lib.cur_time_stamp
        now_map = cm.cur_map(wk)
        if now_map in cm.MAP_FU_BEN or now_map != ori_map:
            return True  # 若已在副本中 或 地图改变
        lib.msleep(1000)
        # 副本成为XX, 若已经组满就不会出这个弹窗
        if wk.cur_task == "[副本]":
            wk.find_pic_click(*cm.RECT_FULL, "副本成为队长.bmp|副本成为队长2.bmp")
        elif wk.cur_task == "[混队副本]":
            wk.find_pic_click(*cm.RECT_FULL, "副本成为队员.bmp|副本成为队员2.bmp")
        if cm.is_talk_open(wk):
            if cm.is_talk_have_content(wk, "有人没点确定"):
                cm.close_talk(wk)
                break
            cm.close_talk(wk)
    wk.record("进入副本失败, 自动退队, 重新开始匹配")
    cm.exit_team(wk)
    return False

# 从准备厅进入副本
def from_ready_hall_enter_fu_ben(wk: cm.Worker):
    if cm.cur_map(wk) != "准备厅":
        return
    wk.record("正在从准备厅进入副本...")
    ret = False
    if wk.cur_task == "[副本]":
        for i in range(30):
            if cm.click_talk_specify_item(wk, "出发吧", 200):
                ret = True
                break
            if not wk.is_find_way:
                cm.around_list_click_npc(wk, "周围_说书先生.bmp")
            lib.msleep(600)
    else:  # 混队副本
        for i in range(200):  # 200*600 = 120s
            cm.request_join_team(wk)  # 申请入队
            if cm.click_confirm(wk):
                ret = True
                break
            lib.msleep(600)
        else:
            wk.record("2分钟内未成功进入副本, 正在退队...")
            cm.exit_team(wk)
    if ret:
        wait_mate_confirm(wk, ori_map="准备厅")


# 从准备厅返回长安城
def from_ready_hall_return_chang_an(wk: cm.Worker):
    if cm.cur_map(wk) != "准备厅":
        return
    wk.record("从准备厅返回长安...")
    if wk.find_pic_click(*cm.RECT_TIP_DETAIL, "离开.bmp"):
        cm.click_confirm(wk, 300)
    else:
        for i in range(30):
            cm.around_list_click_npc(wk, "周围_说书先生.bmp|周围_流火.bmp")
            lib.msleep(600)
            if cm.click_talk_specify_item(wk, "回到长安"):
                break
    for i in range(30):
        lib.msleep(600)
        if cm.cur_map(wk) == "长安城":
            wk.record("已返回长安城")
            return
    wk.record("未成功返回长安城")


# 计算副本次数
def calc_fu_ben_count(wk: cm.Worker, fb_count: int):
    if not cm.is_confirm_cancel_open(wk):
        return False
    if wk.find_pic(*cm.RECT_TIP_CENTER, "队伍投票.bmp"):    # 有队员申请解除契约, 同意解除契约
        wk.find_pic_click(*cm.RECT_TIP_CENTER, "同意1.bmp|同意2.bmp")
        # 是否添加自动退队
        return True
    cm.update_task_done_count(wk, fb_count)
    if wk.done_count < fb_count:
        if cm.click_confirm(wk, 300):
            wk.record("未达到设定次数, 已点击 确定")
    else:
        if cm.click_cancel(wk, 300):
            wk.record("已达到设定次数, 已点击 取消")
    lib.msleep(1000)
    return True

# 副本寻路战斗
def fu_ben_find_way_fight(wk: cm.Worker, fb_count: int):
    for i in range(10):
        if cm.is_talk_open(wk) or cm.is_fight(wk):
            break
        if not wk.is_find_way and not cm.task_npc_find_way(wk):
            break
        lib.msleep(800)
    cm.talk_proc(wk)
    if cm.is_fight(wk, 400):
        cm.fight_operation(wk)
        cm.open_treasure_box(wk)


# 神魔前线带队
def shen_mo_qian_xian(wk: cm.Worker, fb_count: int):
    if wk.find_str(*cm.RECT_CUR_TASK, "招募助阵英雄", cm.COLOR_WHITE):
        wk.record("招募助阵英雄...")
        if cm.cur_map(wk) == "血吼深渊":
            pos = cm.POS_SHEN_MO_LX
            pic_npc = "周围_灵心.bmp"
        else:
            pos = cm.POS_SHEN_MO_GC
            pic_npc = "周围_鬼车.bmp"
        for i in range(10):
            if cm.click_talk_specify_item(wk, "并肩作战", 300):
                lib.msleep(500)
                cm.click_talk_specify_item(wk, "确定", 300)
                cm.close_all_sub_wnd(wk)
                return
            if not wk.is_find_way:
                cm.click_map_wnd_pos(wk, *pos)
                cm.around_list_click_npc(wk, pic_npc)
            lib.msleep(1000)
    elif wk.find_str(*cm.RECT_CUR_TASK, "消灭天庭前锋|消灭九黎前锋", f"{cm.COLOR_WHITE}|{cm.COLOR_CYAN}"):
        wk.record("消灭 天庭前锋|九黎前锋...")
        fu_ben_find_way_fight(wk, fb_count)
    elif wk.find_str(*cm.RECT_CUR_TASK, "进入圣火城", cm.COLOR_WHITE):
        wk.record("进入 圣火城...")
        for i in range(10):
            if cm.cur_map(wk) == "圣火城":
                return
            if not wk.is_find_way:
                cm.click_map_wnd_pos(wk, *cm.PATH_POS["水帘洞-神弃平原"])
            lib.msleep(1000)
    elif wk.find_str(*cm.RECT_CUR_TASK, "进入血吼深渊", cm.COLOR_WHITE):
        wk.record("进入 血吼深渊...")
        for i in range(10):
            if cm.cur_map(wk) == "血吼深渊":
                return
            if not wk.is_find_way:
                cm.click_map_wnd_pos(wk, *cm.PATH_POS["神弃平原-水帘洞"])
            lib.msleep(1000)
    elif wk.find_str(*cm.RECT_CUR_TASK, "摧毁灵兽树林|摧毁萨满居所", f"{cm.COLOR_WHITE}|{cm.COLOR_CYAN}"):
        wk.record("摧毁 灵兽树林|萨满居所...")
        for i in range(10):
            if cm.click_talk_specify_item(wk, "开始进攻", 300):
                lib.msleep(1000)
                if cm.is_fight(wk):
                    cm.fight_operation(wk)
                    return
            if not wk.is_find_way:
                cm.close_talk(wk)
                wk.find_str_click(*cm.RECT_CUR_TASK, "灵兽树林|萨满居所", cm.COLOR_CYAN)
            lib.msleep(1000)
    elif wk.find_str(*cm.RECT_CUR_TASK, "摧毁力士营地|摧毁勇士王座", f"{cm.COLOR_WHITE}|{cm.COLOR_CYAN}"):
        wk.record("摧毁 力士营地|勇士王座...")
        for i in range(10):
            if cm.click_talk_specify_item(wk, "开始进攻", 300):
                lib.msleep(1000)
                if cm.is_fight(wk):
                    cm.fight_operation(wk)
                    return
            if not wk.is_find_way:
                cm.close_talk(wk)
                wk.find_str_click(*cm.RECT_CUR_TASK, "力士营地|勇士王座", cm.COLOR_CYAN)
            lib.msleep(1000)
    elif wk.find_str(*cm.RECT_CUR_TASK, "摧毁神使圣堂|摧毁巫师圆环", f"{cm.COLOR_WHITE}|{cm.COLOR_CYAN}"):
        wk.record("摧毁 神使圣堂|巫师圆环...")
        for i in range(10):
            if cm.click_talk_specify_item(wk, "开始进攻", 300):
                lib.msleep(1000)
                if cm.is_fight(wk):
                    cm.fight_operation(wk)
                    return
            if not wk.is_find_way:
                cm.close_talk(wk)
                wk.find_str_click(*cm.RECT_CUR_TASK, "神使圣堂|巫师圆环", cm.COLOR_CYAN)
            lib.msleep(1000)
    elif wk.find_str(*cm.RECT_CUR_TASK, "攻陷圣火要塞|攻陷血吼部落", f"{cm.COLOR_WHITE}|{cm.COLOR_CYAN}"):
        wk.record("攻陷 圣火要塞|血吼部落...")
        for i in range(10):
            if cm.click_talk_specify_item(wk, "开始进攻", 300):
                lib.msleep(1000)
                if cm.is_fight(wk):
                    cm.fight_operation(wk)
                    return
            if not wk.is_find_way:
                cm.close_talk(wk)
                wk.find_str_click(*cm.RECT_CUR_TASK, "圣火要塞|血吼部落", cm.COLOR_CYAN)
            lib.msleep(1000)
    else:  # 副本完成
        lib.msleep(1000)


# 副本中操作
def fu_ben_operation(wk: cm.Worker, fb_name: str, fb_count: int):
    if not is_in_fu_ben(wk):
        return
    cm.set_task_to_cur_task_bar(wk)
    if wk.find_pic(*cm.RECT_FULL, "退出队列.bmp|恭喜完成副本.bmp"):
        lib.msleep(1000)  # 副本还在自动匹配队员,或副本刚做完,等待队长和队员做选择
        return

    if fb_name == "神魔前线":
        shen_mo_qian_xian(wk, fb_count)
    else:
        fu_ben_find_way_fight(wk, fb_count)

# 带副本
def lead_fu_ben(wk: cm.Worker, idx:int):
    wk.done_count = 0
    wk.record(f"副本{idx} 开始执行")
    fb_name = lib.cfg_main["副本一名称"] if idx == 1 else lib.cfg_main["副本二名称"]
    fb_count = int(lib.cfg_main["副本一次数"]) if idx == 1 else int(lib.cfg_main["副本二次数"])
    while wk.done_count < fb_count:
        enter_fu_ben_or_ready_hall(wk, fb_name, idx)
        from_ready_hall_enter_fu_ben(wk)
        flag = 0
        while is_in_fu_ben(wk):
            if flag == 0:
                wk.record("已成功进入副本")
                flag = 1
            fb_count = int(lib.cfg_main["副本一次数"]) if idx == 1 else int(lib.cfg_main["副本二次数"])  # 允许中途更改副本次数
            fu_ben_operation(wk, fb_name, fb_count)
            calc_fu_ben_count(wk, fb_count)
            lib.msleep(600, 1000)
        lib.msleep(600)
    wk.record(f"副本{idx} 执行完成")
    lib.msleep(1000)

# 混副本
def follow_fu_ben(wk: cm.Worker, idx:int):
    wk.done_count = 0
    wk.record(f"副本{idx} 开始执行")
    fb_name = lib.cfg_main["副本一名称"] if idx == 1 else lib.cfg_main["副本二名称"]
    fb_count = int(lib.cfg_main["副本一次数"]) if idx == 1 else int(lib.cfg_main["副本二次数"])
    while wk.done_count < fb_count:
        enter_fu_ben_or_ready_hall(wk, fb_name, idx)
        from_ready_hall_enter_fu_ben(wk)
        flag = 0
        while is_in_fu_ben(wk):
            if flag == 0:
                wk.record("已成功进入副本")
                flag = 1
            if cm.is_fight(wk):
                cm.fight_operation(wk)
            lib.msleep(600, 1000)
            fb_count = int(lib.cfg_main["副本一次数"]) if idx == 1 else int(lib.cfg_main["副本二次数"])  # 允许中途更改副本次数
            calc_fu_ben_count(wk, fb_count)
        lib.msleep(600)
        if flag == 1 and lib.cur_time_stamp - wk.done_sec > 60 and cm.cur_map(wk) in ("准备厅", "长安城"):
            # 若从 副本中出来到 准备厅 或 长安城, 且 距离上次加次数大于60秒
            cm.update_task_done_count(wk, fb_count)
    wk.record(f"副本{idx} 执行完成")
    lib.msleep(1000)

