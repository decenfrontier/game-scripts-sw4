import lib
import cm

school_tutor_dict = {"东海龙宫": "水晶宫", "天魔里": "云隐阁", "佛门": "大雄宝殿", "天策": "程府",
                      "南海普陀":"南海普陀", "盘丝岭":"盘丝洞", "幽冥地府":"森罗殿", "无名谷":"无名谷",
                      "魔王山":"魔王山", "镇元五庄":"乾坤殿", "七星方寸":"灵台宫", "万兽岭":"狮王洞",
                      "凌霄天宫":"凌霄殿"}

def 师门任务(wk: cm.Worker):
    wk.cur_task = "[师门]"
    wk.record("开始执行")

    cm.use_qu_mo_xiang(wk)
    switch = {
        "接任务": goto_accept_task,
        "收集物资": shou_ji_wu_zi,
        "捕捉宠物": bu_zhuo_chong_wu,
        "完成": reply_to_tutor,
        "传达师命": chuan_da_shi_ming,
        "寻找物品": xun_zhao_wu_pin,
        "门派巡逻": men_pai_xun_luo,
        "挑战": tiao_zhan,
        "灵墟裂痕": ling_xu_lie_hen,
        "援助同门": yuan_zhu_tong_men,
        "挑战首席": tiao_zhan_shou_xi,
    }
    while wk.done_count < cm.get_cur_task_specify_count(wk):
        task_type = cm.sub_task(wk)
        try:
            switch[task_type](wk)
        except:
            wk.record(f"未知的子任务类型:{task_type}")
        lib.msleep(600)


# 去接任务
def goto_accept_task(wk: cm.Worker):
    wk.record("正在接任务...")
    cm.get_role_school(wk)  # 先识别出本角色门派
    if wk.school == "":
        wk.record("角色门派未识别, 请将回门派技能置于右侧F1")
        return
    school_map = wk.school
    tutor_map = school_tutor_dict[school_map]
    # 若既不在门派地图, 也不在师父地图, 使用回门派技能
    for i in range(3):
        map_name = cm.cur_map(wk)
        if map_name in (school_map, tutor_map):
            break
        else:
            wk.key_press(cm.VK_F1)
            lib.msleep(600)
    # 由 门派地图 到 师父地图
    cm.goto_next_map(wk, school_map, tutor_map)
    # 与师父对话
    x, y = cm.TUTOR_POS[tutor_map]
    for i in range(30):
        if cm.is_talk_open(wk):
            break
        if not wk.is_find_way:
            cm.click_map_wnd_pos(wk, x, y)
        lib.msleep(600)
    # 先判断次数是否做满20次
    if cm.is_task_over(wk, 300):
        return
    # 正式接任务
    cm.click_talk_specify_item(wk, "接师门")
    cm.close_talk(wk, 300)
    cm.set_task_to_cur_task_bar(wk)

# 收集物资
def shou_ji_wu_zi(wk: cm.Worker):
    wk.record("任务类型: 收集物资")
    cm.buy_task_need_goods(wk)


# 捕捉宠物
def bu_zhuo_chong_wu(wk: cm.Worker):
    wk.record("任务类型: 捕捉宠物")
    cm.buy_task_pet(wk)


# 传达师命
def chuan_da_shi_ming(wk: cm.Worker):
    wk.record("任务类型: 传达师命")
    for i in range(30):
        if cm.is_talk_open(wk):
            break
        if not wk.is_find_way and not cm.task_npc_find_way(wk):
            return
        lib.msleep(600)
    if cm.click_talk_first_item(wk):
        lib.msleep(500)
        if cm.is_fight(wk, 300):
            cm.fight_operation(wk)
        else:
            cm.update_task_done_count(wk)
    cm.close_talk(wk)

# 寻找物品
def xun_zhao_wu_pin(wk: cm.Worker):
    wk.record("任务类型: 寻找物品")
    for i in range(30):
        if cm.is_progress_bar_open(wk):
            break
        if not wk.is_find_way and not cm.task_npc_find_way(wk):
            return
        lib.msleep(600)
    wk.record("物品采集中...")
    lib.msleep(4500)  # 等待物品采集完

# 回复师父
def reply_to_tutor(wk: cm.Worker):
    wk.record("任务已完成, 回复门派师父")
    if not cm.goto_task_npc_talk(wk):
        return
    if cm.click_talk_specify_item(wk, "交任务", 200):
        lib.msleep(600)
        if cm.click_talk_specify_item(wk, "交师门", 200):
            lib.msleep(1000)
    # 给予物品或宠物
    cm.give_task_goods_pet(wk)
    # 更新任务完成次数
    if not cm.is_task_on_cur_task_bar(wk):  # 若任务不在当前任务栏才更新次数
        cm.update_task_done_count(wk)
    cm.close_talk(wk)

# 门派巡逻
def men_pai_xun_luo(wk: cm.Worker):
    wk.record("任务类型: 门派巡逻")
    cm.goto_task_npc_talk(wk)
    if cm.is_fight(wk, 300):
        cm.fight_operation(wk)


# 挑战
def tiao_zhan(wk: cm.Worker):
    wk.record("任务类型: 挑战")
    cm.fly_task_map_fight(wk)

# 灵墟裂痕
def ling_xu_lie_hen(wk: cm.Worker):
    wk.record("任务类型: 灵墟裂痕")
    map_name = cm.ocr_task_des_map(wk)
    cm.fly_to_map(wk, map_name)
    is_progress = False  # 是否进度条打开过
    for i in range(30):
        if cm.click_talk_first_item(wk):
            lib.msleep(500)
            if cm.is_progress_bar_open(wk, 300):
                is_progress = True
                lib.msleep(4500)  # 等待进度条开启
                break
        if not wk.is_find_way and not cm.task_npc_find_way(wk):
            return
        lib.msleep(600)
    if cm.is_fight(wk, 300):
        cm.fight_operation(wk)
    elif is_progress:
        cm.update_task_done_count(wk)

# 援助同门
def yuan_zhu_tong_men(wk: cm.Worker):
    wk.record("任务类型: 援助同门")
    cm.fly_task_map_fight(wk)


# 挑战首席
def tiao_zhan_shou_xi(wk: cm.Worker):
    wk.record("任务类型: 挑战首席")
    cm.fly_task_map_fight(wk)