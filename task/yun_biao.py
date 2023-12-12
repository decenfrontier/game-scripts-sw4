import cm
import lib

def 运镖任务(wk: cm.Worker):
    wk.cur_task = "[运镖]"
    wk.record("开始执行")

    while wk.done_count < cm.get_cur_task_specify_count(wk):
        task_type = cm.sub_task(wk)
        if task_type in ("接任务", "抵押完成"):
            goto_accept_task(wk)
        elif task_type == "护送人员":
            hu_song_ren_yuan(wk)
        elif task_type in ("运送镖物", "劫镖完成"):
            yun_song_biao_wu(wk)
        elif task_type == "物品抵押":
            wu_pin_di_ya(wk)
        elif task_type == "劫镖事件":
            jie_biao_shi_jian(wk)
        lib.msleep(800)


# 去接任务
def goto_accept_task(wk: cm.Worker):
    wk.record("正在接任务...")
    cm.use_fei_xing_qi(wk, "长安城", cm.FLAG_RECT["运镖宝图"])
    if not cm.is_pos_near(wk, "长安城", *cm.NPC_POS_TRUE["李少镖头"]):
        # 说明运镖任务已接, 只是没有勾选
        cm.set_task_to_cur_task_bar(wk)
        return

    x, y = cm.NPC_POS_WND["李少镖头"]
    if cm.goto_pos_npc_talk(wk, x, y, "接运镖"):
        lib.msleep(300)
        if cm.is_task_over(wk, 300):
            return
        if cm.click_talk_specify_item(wk, "见习运镖"):
            lib.msleep(200, 300)
            cm.click_talk_specify_item(wk, "愿意", 200)
        cm.close_talk(wk)
        cm.set_task_to_cur_task_bar(wk)


# 护送人员
def hu_song_ren_yuan(wk: cm.Worker):
    wk.record("任务类型: 护送人员")
    des_map = cm.ocr_task_des_map(wk)
    if des_map == "":
        return
    if not goto_des_map(wk, des_map):
        return
    # 找交付Npc对话
    for i in range(10):  # 走10秒
        if cm.is_talk_open(wk):
            cm.close_talk(wk)
            return
        if cm.is_fight(wk):
            cm.fight_operation(wk)
        if not wk.is_find_way:
            cm.goto_task_question_npc(wk, "护送交付")
        lib.msleep(1000)


# 运送镖物
def yun_song_biao_wu(wk: cm.Worker):
    wk.record("任务类型: 运送镖物")
    des_map = cm.ocr_task_des_map(wk)
    if des_map == "":
        return
    if not goto_des_map(wk, des_map):
        return
    # 找门派师父Npc对话
    x, y = cm.TUTOR_POS[des_map]
    for i in range(10):  # 走10秒
        if cm.is_talk_open(wk):
            if cm.click_talk_specify_item(wk, "交任务"):
                cm.click_talk_specify_item(wk, "交运镖", 400)
            cm.close_talk(wk)
            return
        if cm.is_fight(wk):
            cm.fight_operation(wk)
        if not wk.is_find_way:
            cm.click_map_wnd_pos(wk, x, y)
        lib.msleep(1000)

# 物品抵押
def wu_pin_di_ya(wk: cm.Worker):
    wk.record("任务类型: 物品抵押")
    goods_name = cm.ocr_task_need_goods(wk)
    wk.record(f"需求物品:{goods_name}")
    # 自制家具庭院
    if lib.cfg_main["自制家具和庭院装饰"] and goods_name in cm.JIA_JU | cm.TING_YUAN:
        cm.make_jia_ju_ting_yuan(wk, goods_name)
    # 购买物品
    if cm.sub_task(wk) != "抵押完成":
        cm.buy_goods(wk, goods_name)


# 劫镖事件
def jie_biao_shi_jian(wk: cm.Worker):
    wk.record("任务类型: 劫镖事件")
    des_map = cm.ocr_task_des_map(wk)
    cm.fly_to_map(wk, des_map)
    for i in range(10):
        if not wk.is_find_way:
            if not cm.goto_task_question_npc(wk, "九黎大盗"):
                return
        lib.msleep(1000)
        if cm.is_fight(wk):
            cm.fight_operation(wk)


# 到目的地
def goto_des_map(wk: cm.Worker, des_map: str):
    # 获取源地图
    src_map = cm.cur_map(wk)
    if src_map == des_map:
        return True
    # 初始化
    wk.path = [src_map]  # 走过的地图名设定为只有源地图
    wk.min_dist = 999
    wk.min_path = []
    # 递归地进行深度优先搜索
    DFS(wk, src_map, des_map)  # wk.min_path = ["长安城", "长安城外", "青河镇"]
    if wk.min_path == []:
        wk.record("计算路线失败")
        lib.msleep(1000)
        return False
    # 输出最短路径上的所有地图
    min_path = "-".join(wk.min_path)  # min_path = "长安城-长安城外-青河镇"
    wk.record(f"路线:{min_path}")
    # 按路线依次走到目标地图
    for i in range(len(wk.min_path)):
        if i < len(wk.min_path)-1:
            cm.goto_next_map(wk, wk.min_path[i], wk.min_path[i + 1])
    return True if cm.cur_map(wk) == des_map else False


# Deep First Search
def DFS(wk: cm.Worker, start_city: str, end_city: str, dist=0):
    if start_city == end_city:  # 如果已经抵达终点
        if dist < wk.min_dist:
            wk.min_dist = dist
            wk.min_path = wk.path[:]
        return
    if dist > wk.min_dist:  # 还没跑完的路径,若距离已经大于跑完的最短距离
        return
    for mid_city in cm.MAP_YUN_BIAO:  # 遍历所有运镖地图
        if mid_city in wk.path:  # 若已经走过该路径
            continue
        if f"{start_city}-{mid_city}" not in cm.PATH_POS:  # 若路径不可达(start_city, mid_city)
            continue
        wk.path.append(mid_city)
        DFS(wk, mid_city, end_city, dist + 1)
        wk.path.remove(mid_city)

