from threading import Thread
import math
from win32com.client import Dispatch
import zlib
import copy
import itertools

# 本地库
import lib
from lib import rnd, Lw, Dm


class Worker(lib.CLS_NAME):
    def __init__(self, hwnd: int, obj, row: int):
        # 初始化Com类
        super().__init__(obj)
        # 设置图片和字库
        self.set_pic_pwd(lib.pwd_pic)
        self.set_dict_pwd(lib.pwd_zk)
        self.set_path(lib.DIR_RES)
        self.set_dict(ZK_ALL, "0全部.txt")
        self.set_dict(ZK_DIGIT_BLUR, "1数字模糊.txt")
        self.set_dict(ZK_DIGIT_CLEAR, "2数字清晰.txt")
        self.set_dict(ZK_TALK, "3对话内容.txt")
        self.set_dict(ZK_TASK_TYPE, "4任务类型.txt")
        self.set_dict(ZK_SUB_TASK, "5子任务.txt")
        self.set_dict(ZK_AUTH_CLOCK, "6验证时钟.txt")
        self.set_dict(ZK_AUTH_OTHER, "7验证其它.txt")
        # 模拟真实鼠标
        self.simulate_real_mouse()
        self.show_error_msg(False)

        # ---------------- 窗口属性 ---------------
        self.hwnd = hwnd  # 窗口句柄
        self.row = row  # 窗口在中控表格的第几行,从0开始
        self.is_lock = False  # 窗口是否锁定
        self.thread = None  # 执行线程对象
        self.h_thread = 0  # 执行线程的线程句柄
        self.x = 0  # 窗口左上角坐标x
        self.y = 0  # 窗口左上角坐标y

        # ---------------- 工人状态 ---------------
        self.is_run = False  # 是否在运行(在干活)
        self.is_pause = False  # 是否在暂停(在休息)
        self.is_end = True  # 是否已结束(干完活 或 没活干)

        # ---------------- 业务相关 ---------------
        self.cfg_plan = lib.cfg_plan_dict["0内置默认"]
        self.cur_task = ""  # 当前执行任务
        self.sub_task = ""  # 当前执行的子任务
        self.done_count = 0  # 当前任务完成次数
        self.done_sec = 0  # 记录加任务完成次数的时间点
        self.path = []  # 走过的地图名
        self.min_path = []  # 起点到终点的最短路径
        self.min_dist = 999  # 起点到终点的最短距离
        self.is_find_way = False  # 寻路标志位
        self.drug_num = {"豆腐": 0, "五加皮": 0, "升丹": 0, "高宠粮": 0}  # 药品数量
        self.price_list = []  # 价格列表
        self.school = ""  # 角色门派
        # 帮派NPC位置
        self.faction_npc_pos = {"白虎": (-1, -1), "青龙": (-1, -1), "玄武": (-1, -1)}
        self.flag = 0  # 钓鱼是否输出等待标志位

        # ---------------- 验证相关 ---------------
        self.last_idx = -1  # 上一次的索引
        self.last_word = ""  # 上一次的关键词

    def write_tbe_console(self, col: int, info: str):
        lib.wnd_main.sig_info.emit(self.row, col, info)

    def record(self, info):
        info = f"{lib.cur_time_fmt} {self.cur_task} {info}"
        self.write_tbe_console(lib.COL_LOG, info)
        row_num = self.row + 1
        lib.file_append_content(f"{lib.DIR_LOG}\\{row_num}.txt", f"{info}\n")

    # 隐藏窗口
    def hide_wnd(self, prev_x: int, prev_y: int):
        self.x, self.y = prev_x, prev_y  # 记忆之前坐标
        lib.show_task_bar_icon(self.hwnd, False)
        hide_x, hide_y = lib.HIDE_X, lib.rnd(0, 200)
        lib.set_wnd_pos(self.hwnd, hide_x, hide_y)

    # 显示窗口
    def show_wnd(self):
        lib.show_task_bar_icon(self.hwnd, True)
        lib.set_wnd_pos(self.hwnd, self.x, self.y)

    # 模拟真实鼠标
    def simulate_real_mouse(self):
        self.enable_real_mouse(False)


class Team():
    def __init__(self):
        # 队伍数量
        self.team_num = lib.TBE_CONSOLE_ROW // 5
        # 队长信号列表, 每个队伍用一个集合装信号, 信号种类: "退队", "解双", "冻双"
        self.leader_sig_list = [set() for i in range(self.team_num)]
        # 队员响应列表
        self.mate_response_list = [{"退队": False, "解双": False, "冻双": False} for i in range(lib.TBE_CONSOLE_ROW)]
        # 队长任务列表, 每5人共享一个列表
        self.leader_task_list = ["" for i in range(self.team_num)]

    # 获取队长信号
    def get_leader_sig(self, wk: Worker):
        return self.leader_sig_list[wk.row // 5]

    # 添加队长信号
    def add_leader_sig(self, wk: Worker, sig: str):
        self.leader_sig_list[wk.row // 5].add(sig)
        print(f"队长信号-{sig} 已添加")
        # 开启一个线程, 5秒后自动清除该信号
        Thread(target=self.remove_leader_sig, args=(wk, sig)).start()

    # 清除队长信号
    def remove_leader_sig(self, wk: Worker, sig: str):
        lib.msleep(5000)  # 5秒后再清除信号
        try:
            self.leader_sig_list[wk.row // 5].remove(sig)
        except:
            pass
        print(f"队长信号-{sig} 已清除")

    # 响应队长信号, 返回真表示响应成功, 返回假表示响应失败
    def response_leader_sig(self, wk: Worker, sig: str):
        if not self.mate_response_list[wk.row][sig]:
            self.mate_response_list[wk.row][sig] = True
            return True
        return False

    # 设置队长任务
    def set_leader_task(self, wk: Worker, task=""):
        self.leader_task_list[wk.row // 5] = task

    # 获取队长任务
    def get_leader_task(self, wk: Worker):
        return self.leader_task_list[wk.row // 5]


# 创建Dispatch对象
def create_dispatch_obj(wk: Worker, com_name: str):
    try:
        obj = Dispatch(com_name)
    except:
        wk.record("创建组件对象异常")
        raise "创建组件对象异常"
    return obj


# 调整自动战斗框
def adjust_zi_dong_zhan_dou(wk: Worker):
    x, y = wk.get_pic_pos(*RECT_FULL, "自动战斗框.bmp")
    if x == -1:
        return
    if (x, y) == POS_ZI_DONG_ZHAN_DOU:
        return
    wk.record("正在调整自动战斗框...")
    wk.move_drag_to(x, y, *POS_ZI_DONG_ZHAN_DOU)


# 调整当前任务栏
def adjust_cur_task_bar(wk: Worker):
    x, y = wk.get_str_pos(*RECT_FULL, "前任务", COLOR_WHITE)
    if (x, y) == POS_CUR_TASK_BAR:
        return
    wk.record("正在调整当前任务栏...")
    open_task_track(wk)


# 是否任务界面打开
def is_task_ui_open(wk: Worker, t=0):
    ret = wk.find_pic(*RECT_FULL, "界_任务.bmp|界_任务2.bmp", timeout=t)
    return ret


# 打开任务界面
def open_task_ui(wk: Worker):
    close_talk(wk)
    for i in range(4):
        if not is_task_ui_open(wk, 200):
            wk.key_press_combo(VK_ALT, VK_Q)
            # wk.move_click(POS_UI_TASK[0] + rnd(0, 10), POS_UI_TASK[1] + rnd(0, 10), False)
        else:
            break
        lib.msleep(300)


# 关闭任务界面
def close_task_ui(wk: Worker):
    for i in range(4):
        if is_task_ui_open(wk, 200):
            wk.key_press_combo(VK_ALT, VK_Q)
            # wk.move_click(POS_UI_TASK[0] + rnd(0, 10), POS_UI_TASK[1] + rnd(0, 10))
        else:
            break
        lib.msleep(300)


# 开启任务追踪
def open_task_track(wk: Worker, close=True):
    open_task_ui(wk)
    x, y = wk.get_pic_pos(*RECT_FULL, "界_任务.bmp|界_任务2.bmp")
    if x < 0:  # 界面打开失败
        wk.record("任务界面打开失败")
        return
    pos_x, pos_y = x + rnd(213, 216), y - rnd(25, 28)
    if wk.find_pic(*RECT_FULL, "自动追踪1.bmp", timeout=400):
        wk.move_click(pos_x, pos_y, False)
        lib.msleep(400, 600)
        wk.move_click(pos_x, pos_y)
    else:
        wk.move_click(pos_x, pos_y)
    if close:
        close_task_ui(wk)


# 关闭任务追踪
def close_task_track(wk: Worker):
    if not wk.find_str(*RECT_FULL, "前任务", COLOR_WHITE):  # 未找到说明已经关闭
        return
    open_task_ui(wk)
    x, y = wk.get_pic_pos(*RECT_FULL, "界_任务.bmp|界_任务2.bmp")
    if x < 0:  # 界面打开失败
        wk.record("任务界面打开失败")
        return
    pos_x, pos_y = x + rnd(213, 216), y - rnd(25, 28)
    if wk.find_pic(*RECT_FULL, "自动追踪1.bmp", timeout=400):
        wk.move_click(pos_x, pos_y)
    else:
        wk.move_click(pos_x, pos_y, False)
        lib.msleep(400, 600)
        wk.move_click(pos_x, pos_y)
    close_task_ui(wk)


# 当前地图名
def cur_map(wk: Worker) -> str:
    for i in range(10):
        map_name = wk.get_pic_name(*RECT_CUR_MAP, PIC_MAP, dir=lib.DIR_MAP)
        if map_name != "":
            break
        if i == 6:
            close_all_sub_wnd(wk)  # 防挡
        lib.msleep(400)
    else:
        wk.record("卡在未知地图")
    return map_name


# 是否地图打开
def is_map_open(wk: Worker, t=0):
    ret = wk.find_pic(*RECT_FULL, "不能打开地图.bmp|地图标志.bmp|地图标志2.bmp", timeout=t)
    return ret


# 打开地图
def open_map(wk: Worker):
    for i in range(3):
        if is_map_open(wk):
            break
        else:
            wk.key_press(VK_TAB)
        lib.msleep(300)


# 关闭地图
def close_map(wk: Worker):
    for i in range(2):
        if is_map_open(wk):
            wk.key_press(VK_TAB)
        else:
            break
        lib.msleep(300)


# 关闭地图飞行点
def close_map_fei_xing(wk: Worker):
    x, y = wk.get_pic_pos(*RECT_FULL, "地图飞行点.bmp")
    if x > 0:
        wk.move_click(x + 20, y + 7)


# 打开地图特殊
def open_map_te_shu(wk: Worker):
    x, y = wk.get_pic_pos(*RECT_FULL, "地图特殊.bmp")
    if x > 0:
        wk.move_click(x + 20, y + 7)


# 打开地图商人
def open_map_shang_ren(wk: Worker):
    x, y = wk.get_pic_pos(*RECT_FULL, "地图商人.bmp")
    if x > 0:
        wk.move_click(x + 20, y + 7)


# 关闭所有子窗
def close_all_sub_wnd(wk: Worker):
    wk.key_press(VK_ESC)
    lib.msleep(400)
    click_continue_game(wk)


# 关闭界面
def close_ui(wk: Worker):
    if wk.find_pic(*RECT_RIGHT_UP, "界_关闭1.bmp|界_关闭2.bmp|界_关闭3.bmp|界_关闭4.bmp"):
        wk.key_press(VK_ESC)
        lib.msleep(400)


# 点击地图窗口坐标
def click_map_wnd_pos(wk: Worker, x: int, y: int, is_close=True):
    if is_chuan_song_fu_ui_open(wk):  # 若传送符界面已开, 则先关掉, 否则会走不动
        close_all_sub_wnd(wk)
    if is_close:  # 是否允许关闭对话框
        close_talk(wk)
    open_map(wk)
    close_map_fei_xing(wk)
    open_map_te_shu(wk)
    open_map_shang_ren(wk)
    wk.move_click(x + rnd(-2, 2), y + rnd(-2, 2), False)
    lib.msleep(100, 200)
    close_map(wk)
    wk.re_move()


# 是否对话框打开
def is_talk_open(wk: Worker, t=0):
    ret = wk.find_pic(*RECT_CLOSE_TALK, "界_关闭1.bmp|界_关闭2.bmp|界_关闭3.bmp|界_关闭4.bmp", timeout=t)
    return ret


# 是否给予框打开
def is_give_open(wk: Worker):
    ret = wk.find_pic(*RECT_FULL, "界_给予.bmp|界_给予2.bmp")
    return ret


# 选中任务物品
def select_task_goods(wk: Worker, idx_exclude=-1):
    x, y = wk.get_pic_pos(*RECT_FULL, "行囊页.bmp|行囊页2.bmp", timeout=300)
    if x < 0:
        return -1
    goods_name = wk.match_pic("物_*.bmp")
    find_list = wk.find_pic_ex(x - 259, y - 40, x, y + 355, goods_name)
    if find_list == []:
        return -1
    for idx, x, y in find_list:
        if idx == idx_exclude:
            continue
        wk.move_click(x, y)
        return idx
    return -1


# 给予任务物品或宠物
def give_task_goods_pet(wk: Worker):
    if not is_give_open(wk):
        return
    # 给予宠物 或 给予物品
    if wk.find_pic(*RECT_FULL, "给予宠物.bmp"):  # 给予宠物
        wk.find_pic_click(*RECT_FULL, "给予宝宝.bmp")
    else:  # 给予物品
        idx1 = select_task_goods(wk)
        if idx1 == -1:
            bag_change_page(wk)
            idx1 = select_task_goods(wk)
        idx2 = select_task_goods(wk, idx1)
        if idx2 == -1:
            bag_change_page(wk)
            idx2 = select_task_goods(wk, idx1)
    # 提交 并 确认
    for i in range(3):
        if is_give_open(wk):
            wk.key_press(VK_ENTER)
        else:
            break
        lib.msleep(500)
    click_talk_specify_item(wk, "确认", 300)


# 更新任务完成次数
def update_task_done_count(wk: Worker, specify_count=0):
    if lib.cur_time_stamp - wk.done_sec < 3:
        return  # 若距离上次加任务次数不足3秒
    wk.done_count += 1
    wk.done_sec = lib.cur_time_stamp
    if specify_count == 0:
        wk.record(f"已完成{wk.done_count}/{get_cur_task_specify_count(wk)}")
    else:
        wk.record(f"已完成{wk.done_count}/{specify_count}")


# 继续领取任务
def continue_accept_task(wk: Worker):
    if wk.done_count >= get_cur_task_specify_count(wk):
        if wk.cur_task in {"[宝图]", "[师门]"}:
            shut_talk(wk)  # 继续领取Esc不掉
        return
    if wk.cur_task == "[捉鬼]":
        if lib.cfg_main["打千年老妖"]:
            click_talk_specify_item(wk, "要怎么帮你", 300)
        click_talk_specify_item(wk, "继续领取", 300)
    else:
        click_talk_specify_item(wk, "继续领取", 300)
    lib.msleep(200)  # 点完选项等待任务刷新


# 是否进度条打开
def is_progress_bar_open(wk: Worker, t=0):
    ret = wk.find_pic(*RECT_TIP_CENTER, "进度条.bmp", timeout=t)
    return ret


# 是否确定取消打开
def is_confirm_cancel_open(wk: Worker, t=0):
    ret = wk.find_pic(*RECT_TIP_CENTER, "确定1.bmp|确定2.bmp|确定3.bmp|取消1.bmp|取消2.bmp|同意1.bmp|反对1.bmp", timeout=t)
    return ret


# 领取双倍经验
def get_double_exp(wk: Worker):
    if not lib.cfg_main["跟随队长领双"]:  # 跟随队员领双冻双
        return
    if is_talk_open(wk):
        double_time = lib.cfg_main["领取双倍时间"]
        click_talk_specify_item(wk, double_time)


# 关闭对话框
def close_talk(wk: Worker, t=0, is_fighted=False):
    if not is_talk_open(wk, t):
        return
    # 出现对话框 且 刚经历过战斗 且 正在执行下列任务
    task_add_count = ("[捉鬼]", "[宝图]", "[师门]", "[修炼]", "[玄武]", "[官职]")
    if is_fighted and wk.cur_task in task_add_count:
        update_task_done_count(wk)
    # 根据任务和对话内容判断是否加次数
    if wk.cur_task == "[运镖]" and is_talk_have_content(wk, "少侠一路辛苦|少侠神勇"):
        update_task_done_count(wk)
    elif wk.cur_task == "[钓鱼]":
        if wk.done_count < get_cur_task_specify_count(wk):
            if click_talk_specify_item(wk, "购买鱼竿", 200):
                update_task_done_count(wk)
        if is_talk_have_content(wk, "钓鱼满次"):
            wk.record("本周钓鱼时间用尽")
            wk.done_count = get_cur_task_specify_count(wk)
    # 若对话框有选项
    if is_talk_have_item(wk):
        continue_accept_task(wk)
        get_double_exp(wk)
    close_all_sub_wnd(wk)  # 按Esc关闭对话
    if is_talk_open(wk):  # 没Esc掉, 可能是奇遇, 点完选项再叉掉
        click_talk_first_item(wk)  # 接奇遇任务
        shut_talk(wk)  # 强制关闭对话框


# 强制关闭对话框
def shut_talk(wk: Worker):
    wk.find_pic_click(*RECT_CLOSE_TALK, "界_关闭1.bmp|界_关闭2.bmp|界_关闭3.bmp|界_关闭4.bmp")


# 点击对话框第一项
def click_talk_first_item(wk: Worker, t=0):
    if not is_talk_open(wk, t):
        return False
    ret = False
    if wk.find_color_click(*RECT_TALK_CONTENT_SMALL, COLOR_CYAN) or \
            wk.find_color_click(*RECT_TALK_CONTENT_BIG, COLOR_CYAN) or \
            wk.find_color_click(*RECT_TALK_CONTENT_SMALL, f"{COLOR_CYAN}|{COLOR_HOVER}") or \
            wk.find_color_click(*RECT_TALK_CONTENT_BIG, f"{COLOR_CYAN}|{COLOR_HOVER}"):
        ret = True
    return ret


# 点击对话框指定项
def click_talk_specify_item(wk: Worker, text: str, t=0):
    if not is_talk_open(wk, t):
        return False
    if text == "":
        return True
    ret = wk.find_str_click(*RECT_TALK_CONTENT_BIG, text, COLOR_TALK_ITEM, sim=0.85, zk=ZK_TALK)
    return ret


# 是否对话框有指定项
def is_talk_have_item(wk: Worker, text="", t=0) -> bool:
    if not is_talk_open(wk, t):
        return False
    if text == "":
        ret = wk.find_color(*RECT_TALK_CONTENT_SMALL, COLOR_CYAN)
    else:
        ret = wk.find_str(*RECT_TALK_CONTENT_BIG, text, COLOR_TALK_ITEM, sim=0.85, zk=ZK_TALK)
    return ret


# 是否对话框有指定内容
def is_talk_have_content(wk: Worker, text: str, t=0) -> bool:
    if not is_talk_open(wk, t):
        return False
    ret = wk.find_str(*RECT_TALK_CONTENT_BIG, text, COLOR_WHITE_BLUR, sim=0.85, zk=ZK_TALK)
    return ret


# 对话过程
def talk_proc(wk):
    for i in range(10):
        if not is_talk_open(wk):
            break
        if not click_talk_first_item(wk):
            wk.move_click(POS_TALK_BLANK[0] + rnd(0, 270), POS_TALK_BLANK[1] + rnd(0, 18), False)
        lib.msleep(50, 100)


# 当前坐标(真实)
def cur_pos(wk: Worker):
    x, y = 0, 0
    for i in range(3):
        ret = wk.ocr(*RECT_CUR_POS, COLOR_CUR_POS, sim=0.8, zk=ZK_DIGIT_BLUR)
        if "Y" in ret:  # "329Y280"
            pos_list = ret.split("Y")  # ["329", "280"]
            try:
                x = int(pos_list[0])
                y = int(pos_list[1])
            except:
                ...
        if x > 0 and y > 0:
            break
        lib.msleep(100)
    return x, y


# 是否坐标相近
def is_pos_near(wk: Worker, map_name: str, true_pos_x: int, true_pos_y: int, dist=50):
    if cur_map(wk) == map_name:
        cur_x, cur_y = cur_pos(wk)
        if abs(cur_x - true_pos_x) < dist and abs(cur_y - true_pos_y) < dist:
            return True
    return False


# 窗口坐标 转 真实坐标
def wnd_pos_to_true_pos(map_name: str, wnd_pos_x: int, wnd_pos_y: int):
    ratio_info = MAP_RATIO.get(map_name)
    if ratio_info:
        wnd_zero_x, wnd_zero_y, ratio_x, ratio_y = ratio_info
        true_pos_x = round((wnd_pos_x - wnd_zero_x) / ratio_x)
        true_pos_y = round((wnd_pos_y - wnd_zero_y) / ratio_y)
    else:
        true_pos_x, true_pos_y = -1, -1
    return true_pos_x, true_pos_y


# 隐藏其它玩家
def hide_other_player(wk: Worker):
    if wk.find_pic(*RECT_QUQUE_BACK, "屏蔽中.bmp"):
        return
    wk.key_press(VK_F9)  # 隐藏其它玩家


# 是否传送符界面打开
def is_chuan_song_fu_ui_open(wk: Worker):
    ret = wk.find_pic(*RECT_TIP_CENTER, "界_传送符.bmp")
    return ret


# 使用传送符
def use_chuan_song_fu(wk: Worker, map_name: str):
    if is_fight(wk):
        fight_operation(wk)
    if lib.cfg_main["自动购买传送符"]:
        if wk.find_pic(*RECT_QUICK_BAR, "缺少传送符0.bmp|缺少传送符1.bmp"):
            wk.record("缺少传送符，前往长安杂货店购买")
            buy_goods(wk, "传送符", "40", False)
    d = {"长安城": VK_1, "傲来国": VK_2, "青河镇": VK_3, "临仙镇": VK_4, "女儿国": VK_5}
    if map_name not in d:
        return False
    vk_code = d[map_name]
    for i in range(5):
        # 打开传送符界面
        wk.key_press(VK_F2)
        lib.msleep(300, 400)
        # 找图单击
        wk.key_press(vk_code)
        lib.msleep(700, 900)
        wk.key_press(VK_BACK)  # 清一下聊天框
        if cur_map(wk) == map_name:
            wk.record(f"抵达 {map_name}")
            hide_other_player(wk)
            return True
    else:
        wk.record("使用传送符失败, 请检查是否将F2设置为传送符")
        return False


# 是否飞行旗界面打开
def is_fei_xing_qi_ui_open(wk: Worker):
    ret = wk.find_pic(*RECT_FULL, "界_飞行旗.bmp")
    return ret


# 使用飞行旗
def use_fei_xing_qi(wk: Worker, map_name: str, rect: (int, int, int, int)):
    # 计算此范围中心点对应的真实坐标
    x1, y1, x2, y2 = rect
    wnd_pos_x, wnd_pos_y = (x1 + x2) / 2, (y1 + y2) / 2
    true_pos_x, true_pos_y = wnd_pos_to_true_pos(map_name, wnd_pos_x, wnd_pos_y)
    # 先判断是否坐标相近
    if is_pos_near(wk, map_name, true_pos_x, true_pos_y):
        return
    # 打开飞行旗界面, 现在游戏会自动补充旗包
    for i in range(5):
        if is_fei_xing_qi_ui_open(wk):
            break
        wk.key_press(VK_F3)
        lib.msleep(400, 600)
    else:
        wk.record("错误, 请检查F3是否设置为飞行旗")
        return
    # 切换地图模式
    if wk.find_pic_click(*RECT_FULL, "切换地图模式.bmp"):
        lib.msleep(400, 600)
    # 切到对应地图
    map_vk = {"长安城": VK_1, "傲来国": VK_2, "青河镇": VK_3, "临仙镇": VK_4, "女儿国": VK_5}
    vk = map_vk[map_name]
    # 点击飞行旗
    for i in range(3):
        wk.key_press(vk)
        lib.msleep(500)
        wk.find_pic_click(*rect, "飞行旗1.bmp|飞行旗2.bmp|飞行旗3.bmp|飞行旗4.bmp", timeout=400, sim=0.9)
        if not is_fei_xing_qi_ui_open(wk):  # 飞行旗界面没打开, 说明飞成功了
            break
    else:
        wk.record(f"未发现飞行旗, 地图:{map_name}, 范围:{rect}")
        close_all_sub_wnd(wk)
    lib.msleep(1000)


# 是否周围列表打开
def is_around_list_open(wk: Worker):
    ret = wk.find_pic(*RECT_FULL, "界_周围列表1.bmp|界_周围列表2.bmp|界_周围列表3.bmp")
    return ret


# 打开周围列表
def open_around_list(wk: Worker):
    for i in range(3):
        if not is_around_list_open(wk):
            wk.key_press_combo(VK_ALT, VK_F)
            # wk.move_click(POS_UI_FRIEND[0] + rnd(0, 10), POS_UI_FRIEND[1] + rnd(0, 10), False)
        else:
            break
        lib.msleep(300)
    else:
        return
    # 调整周围列表的位置
    x, y = wk.get_pic_pos(*RECT_FULL, "界_周围列表1.bmp")
    if x > 0 and (x, y) != (57, 57):
        wk.move_drag_to(x, y, 57, 57)
    # 切换到周围列表
    wk.find_pic_click(*RECT_FULL, "界_周围列表2.bmp")
    # 展开周围列表
    wk.find_pic_click(*RECT_AROUND_LIST, "展开周围列表.bmp")


# 关闭周围列表
def close_around_list(wk: Worker):
    for i in range(3):
        if is_around_list_open(wk):
            wk.key_press_combo(VK_ALT, VK_F)
            # wk.move_click(POS_UI_FRIEND[0] + rnd(0, 10), POS_UI_FRIEND[1] + rnd(0, 10))
        else:
            break
        lib.msleep(300)


# 周围列表点击npc
def around_list_click_npc(wk: Worker, pic: str):
    if is_talk_open(wk):  # 若对话框打开, 会导致点击npc无效, 直接返回失败
        return False
    open_around_list(wk)
    ret = wk.find_pic_click(*RECT_AROUND_LIST, pic)
    return ret


# 是否背包打开
def is_bag_open(wk: Worker, t=0):
    ret = wk.find_pic(*RECT_FULL, "背包整理.bmp|背包页.bmp|行囊页.bmp|界_背包.bmp|界_背包2.bmp", timeout=t)
    return ret


# 打开背包
def open_bag(wk: Worker):
    close_talk(wk)
    if is_chuan_song_fu_ui_open(wk):
        close_all_sub_wnd(wk)
    for i in range(5):
        if is_bag_open(wk):
            break
        else:
            wk.key_press_combo(VK_ALT, VK_E)
            # wk.move_click(POS_UI_BAG[0] + rnd(0, 10), POS_UI_BAG[1] + rnd(0, 10), False)
        lib.msleep(600)
    else:
        wk.record("打开背包失败")
    wk.re_move()


# 关闭背包
def close_bag(wk: Worker):
    for i in range(4):
        if is_bag_open(wk):
            wk.key_press_combo(VK_ALT, VK_E)
            # wk.move_click(POS_UI_BAG[0] + rnd(0, 10), POS_UI_BAG[1] + rnd(0, 10))
        else:
            break
        lib.msleep(400)
    else:
        wk.record("关闭背包失败")


# 背包换页
def bag_change_page(wk: Worker) -> bool:
    ret = True
    if not wk.find_pic_click(*RECT_FULL, "行囊页.bmp"):
        ret = wk.find_pic_click(*RECT_FULL, "背包页.bmp", timeout=300)
    lib.msleep(300)  # 换页后等待物品加载出来
    return ret


# 是否背包有指定物品
def is_bag_have_goods(wk: Worker, pic: str):
    open_bag(wk)
    x, y = wk.get_pic_pos(*RECT_FULL, "行囊页.bmp|行囊页2.bmp")
    if x == -1:  # 若背包未打开
        return False
    x1, y1, x2, y2 = x - 259, y - 40, x, y + 355  # 背包物品格范围
    if wk.find_pic(x1, y1, x2, y2, pic):
        return True
    bag_change_page(wk)
    if wk.find_pic(x1, y1, x2, y2, pic):
        return True
    return False


# 整理背包
def tidy_bag(wk: Worker):
    open_bag(wk)
    wk.find_pic_click(*RECT_FULL, "背包整理.bmp")
    lib.msleep(500)


# 背包使用物品
def bag_use_goods(wk: Worker, pic: str) -> bool:
    open_bag(wk)
    x, y = wk.get_pic_pos(*RECT_FULL, "行囊页.bmp|行囊页2.bmp")
    if x == -1:  # 若背包未打开
        return False
    x1, y1, x2, y2 = x - 259, y - 40, x, y + 355  # 背包物品格范围
    if wk.find_pic_r_click(x1, y1, x2, y2, pic):
        return True
    bag_change_page(wk)
    if wk.find_pic_r_click(x1, y1, x2, y2, pic):
        return True
    return False


# 是否有buff
def is_have_buff(wk: Worker, buff_name: str):
    pic = f"buff_{buff_name}.bmp"
    ret = wk.find_pic(*RECT_BUFF, pic)
    return ret


# 使用驱魔香
def use_qu_mo_xiang(wk: Worker):
    if not lib.cfg_main["自动使用驱魔香"]:
        return
    ret = True
    if not is_have_buff(wk, "驱魔香"):  # 若没有驱魔香buff 才使用驱魔香
        ret = bag_use_goods(wk, "物_驱魔香.bmp")
        close_bag(wk)
    if lib.cfg_main["自动购买驱魔香"] and not ret:  # 若 用户设定自动买驱魔香 且 背包没有驱魔香
        wk.record("背包中驱魔香不足,正在前往购买")
        buy_goods(wk, "驱魔香", "20")
        bag_use_goods(wk, "物_驱魔香.bmp")
        close_bag(wk)


# 取消驱魔香
def cancel_qu_mo_xiang(wk: Worker):
    if wk.find_pic_r_click(*RECT_BUFF, "buff_驱魔香.bmp"):
        lib.msleep(600)
        click_confirm(wk, 400)


# 人物补血
def role_add_hp(wk: Worker):
    if not lib.cfg_main["人宠自动补血"]:
        return
    wk.move_r_click(POS_ROLE_HP[0] + rnd(-10, 10), POS_ROLE_HP[1] + rnd(-3, 3), False, False)


# 人物补蓝
def role_add_mp(wk: Worker):
    if not lib.cfg_main["人宠自动补蓝"]:
        return
    wk.move_r_click(POS_ROLE_MP[0] + rnd(-10, 10), POS_ROLE_MP[1] + rnd(-3, 3), False, False)


# 宠物补血
def pet_add_hp(wk: Worker):
    if not lib.cfg_main["人宠自动补血"]:
        return
    wk.move_r_click(POS_PET_HP[0] + rnd(-10, 10), POS_PET_HP[1] + rnd(-3, 3), False, False)


# 宠物补蓝
def pet_add_mp(wk: Worker):
    if not lib.cfg_main["人宠自动补蓝"]:
        return
    wk.move_r_click(POS_PET_MP[0] + rnd(-10, 10), POS_PET_MP[1] + rnd(-3, 3), False, False)


# 宠物补忠诚
def pet_add_loyal(wk: Worker):
    if not lib.cfg_main["补充宠物忠诚"]:
        return
    x, y = wk.get_color_pos(*RECT_PET_LOYAL, COLOR_PET_LOYAL, order=ORDER_RLUD)
    if 0 < x < X_LIMIT_ADD_LOYAL:
        wk.move_r_click(POS_PET_LOYAL[0] + rnd(-10, 10), POS_PET_LOYAL[1] + rnd(-3, 3), False)


# 人宠补血蓝
def role_pet_add_hp_mp(wk: Worker):
    if is_have_buff(wk, "气血恢复"):
        wk.record("发现气血恢复开启,无需自动加血")
    else:
        role_add_hp(wk)
        pet_add_hp(wk)

    if is_have_buff(wk, "魔法恢复"):
        wk.record("发现魔法恢复开启,无需自动补蓝")
    else:
        role_add_mp(wk)
        pet_add_mp(wk)
    wk.re_move()  # 防鼠标遮挡


# 计算当前页药品数量
def calc_page_drug_num(wk: Worker):
    wk.drug_num["豆腐"] += wk.get_pic_num(*RECT_FULL, "物_五味羹.bmp") * 300
    wk.drug_num["五加皮"] += wk.get_pic_num(*RECT_FULL, "物_玉琼浆.bmp") * 150
    wk.drug_num["升丹"] += wk.get_pic_num(*RECT_FULL, "物_玉蓉糕.bmp") * 500
    # ret = [(0,100,20), (1,30,40)]
    ret = wk.find_pic_ex(*RECT_FULL, "物_豆腐.bmp|物_五加皮.bmp|物_升丹.bmp|物_高宠粮.bmp", timeout=400)
    if not ret:
        return
    for pos in ret:
        idx, pos_x, pos_y = pos
        x1, y1, x2, y2 = pos_x - 15, pos_y + 10, pos_x + 25, pos_y + 30
        ocr_ret = wk.ocr(x1, y1, x2, y2, COLOR_WHITE, zk=ZK_DIGIT_CLEAR)
        if not ocr_ret:
            continue
        num = int(ocr_ret)
        map_dict = {0: "豆腐", 1: "五加皮", 2: "升丹", 3: "高宠粮"}
        wk.drug_num[map_dict[idx]] += num


# 计算背包药品数量
def calc_bag_drug_num(wk: Worker):
    wk.drug_num.update({"豆腐": 0, "五加皮": 0, "升丹": 0, "高宠粮": 0})  # 所有消耗品数量清0
    open_bag(wk)
    if not is_bag_open(wk, 300):
        return
    calc_page_drug_num(wk)
    if bag_change_page(wk):  # 若换页成功, 才计算数量
        calc_page_drug_num(wk)
    close_bag(wk)
    wk.record(f"{wk.drug_num}".strip("{|}"))


# 是否商店界面打开
def is_shop_ui_open(wk: Worker):
    wk.re_move()  # 防鼠标遮挡
    ret = wk.find_pic(*RECT_FULL, "界_出售.bmp|界_出售2.bmp")
    return ret


# 打开天仙店铺
def open_tian_xian(wk: Worker):
    for i in range(4):
        if is_shop_ui_open(wk):
            click_prev_page(wk)  # 确保在第一页
            return True
        if not wk.find_pic_r_click(*RECT_QUICK_BAR, "技_天仙店铺.bmp", timeout=400):
            wk.record("未在右侧快捷面板发现天仙店铺图标")
            return False
        lib.msleep(400)
    return False


# 现金或信誉购买
def buy_cash_or_credit(wk: Worker):
    if lib.cfg_main["购物货币"] == "信誉":
        if not wk.find_pic_click(*RECT_FULL, "信誉购买.bmp", timeout=400):
            wk.record("使用信誉购买失败, 改用现金购买")
            wk.find_pic_click(*RECT_FULL, "现金购买.bmp")
    else:
        if not wk.find_pic_click(*RECT_FULL, "现金购买.bmp", timeout=400):
            wk.record("使用现金购买失败, 改用信誉购买")
            wk.find_pic_click(*RECT_FULL, "信誉购买.bmp")
    lib.msleep(600)


# 商店购买物品
def buy_goods_at_shop(wk: Worker, goods_name: str, goods_num="1") -> bool:
    if not is_shop_ui_open(wk):
        return False
    ret = True
    x, y = wk.get_pic_pos(*RECT_FULL, "界_出售.bmp|界_出售2.bmp", timeout=300)
    if goods_name in ["豆腐", "五加皮", "升丹", "高宠粮", "驱魔香", "传送符"]:
        ret = wk.find_pic_click(x + 25, y - 80, x + 400, y + 400, f"物_{goods_name}.bmp", timeout=400)
        if ret:
            wk.key_press(VK_BACK)  # 删掉默认的1
            wk.key_press_str(goods_num)  # 输入要买的数量
    elif goods_name == "飞刀|梅花镖":
        ret = wk.find_pic_click(x + 25, y - 80, x + 400, y + 400, "物_飞刀.bmp|物_梅花镖.bmp", order=ORDER_LRDU, timeout=400)
    lib.msleep(500)
    # 其它情况下任务会自动帮我们选中物品, 不需要点击指定物品
    buy_cash_or_credit(wk)
    return ret


# 购买药品_天仙店铺
def buy_drug_tian_xian(wk: Worker):
    if not lib.cfg_main["自动买药"]:
        return
    limit_num_dou_fu = int(lib.cfg_main["加血药数量"])
    limit_num_wu_jia_pi = int(lib.cfg_main["加蓝药数量"])
    limit_num_sheng_dan = int(lib.cfg_main["伤势药数量"])
    limit_num_gcl = int(lib.cfg_main["高宠粮数量"])
    flag = False

    if lib.cfg_main["血药购买地点"] == "天仙店铺" and wk.drug_num["豆腐"] < limit_num_dou_fu:
        wk.record("缺少 豆腐, 在天仙店铺中购买200个")
        open_tian_xian(wk)
        buy_goods_at_shop(wk, "豆腐", "200")
        wk.drug_num["豆腐"] = limit_num_dou_fu
        flag = True

    if lib.cfg_main["蓝药购买地点"] == "天仙店铺" and wk.drug_num["五加皮"] < limit_num_wu_jia_pi:
        wk.record("缺少 五加皮, 在天仙店铺中购买200个")
        open_tian_xian(wk)
        buy_goods_at_shop(wk, "五加皮", "200")
        wk.drug_num["五加皮"] = limit_num_wu_jia_pi
        flag = True

    if lib.cfg_main["伤药购买地点"] == "天仙店铺" and wk.drug_num["升丹"] < limit_num_sheng_dan:
        wk.record("缺少 升丹, 在天仙店铺中购买200个")
        open_tian_xian(wk)
        buy_goods_at_shop(wk, "升丹", "200")
        wk.drug_num["升丹"] = limit_num_sheng_dan
        flag = True

    if lib.cfg_main["宠粮购买地点"] == "天仙店铺" and wk.drug_num["高宠粮"] < limit_num_gcl:
        wk.record("缺少 高宠粮, 在天仙店铺中购买100个")
        open_tian_xian(wk)
        buy_goods_at_shop(wk, "高宠粮", "100")
        wk.drug_num["高宠粮"] = limit_num_gcl
        flag = True

    if flag:
        close_all_sub_wnd(wk)


# 购买药品_寄售中心
def buy_drug_ji_shou(wk: Worker):
    if not lib.cfg_main["自动买药"]:
        return
    limit_num_dou_fu = int(lib.cfg_main["加血药数量"])
    limit_num_wu_jia_pi = int(lib.cfg_main["加蓝药数量"])
    limit_num_sheng_dan = int(lib.cfg_main["伤势药数量"])
    limit_num_gcl = int(lib.cfg_main["高宠粮数量"])
    flag = False

    if lib.cfg_main["血药购买地点"] == "寄售中心" and wk.drug_num["豆腐"] < limit_num_dou_fu:
        wk.record("缺少 五味羹, 在寄售中心中购买1个")
        buy_goods_goto_ji_shou(wk, "五味羹", False)
        wk.drug_num["豆腐"] = limit_num_dou_fu
        flag = True

    if lib.cfg_main["蓝药购买地点"] == "寄售中心" and wk.drug_num["五加皮"] < limit_num_wu_jia_pi:
        wk.record("缺少 玉琼浆, 在寄售中心中购买1个")
        buy_goods_goto_ji_shou(wk, "玉琼浆", False)
        wk.drug_num["五加皮"] = limit_num_wu_jia_pi
        flag = True

    if lib.cfg_main["伤药购买地点"] == "寄售中心" and wk.drug_num["升丹"] < limit_num_sheng_dan:
        wk.record("缺少 玉蓉糕, 在寄售中心中购买1个")
        buy_goods_goto_ji_shou(wk, "玉蓉糕", False)
        wk.drug_num["升丹"] = limit_num_sheng_dan
        flag = True

    if flag:
        close_all_sub_wnd(wk)


# 是否寄售界面打开
def is_ji_shou_ui_open(wk: Worker):
    ret = wk.find_pic(*RECT_FULL, "界_寄售中心.bmp|界_寄售中心2.bmp")
    return ret


# 打开寄售界面
def open_ji_shou_ui(wk: Worker):
    for i in range(5):
        if not is_ji_shou_ui_open(wk):
            wk.key_press_combo(VK_ALT, VK_J)
            # wk.move_click(POS_UI_JI_SHOU[0] + rnd(0, 10), POS_UI_JI_SHOU[1] + rnd(0, 10))
        else:
            break
        lib.msleep(800)
    else:
        wk.record("打开寄售界面失败")


# 点击前一页
def click_prev_page(wk: Worker, t=0, is_press=False) -> bool:
    if is_press:
        ret = wk.find_pic(*RECT_FULL, "前一页.bmp|上一页.bmp", timeout=t)
        wk.key_press(VK_LEFT)
    else:
        ret = wk.find_pic_click(*RECT_FULL, "前一页.bmp|上一页.bmp", timeout=t)
    if ret:
        lib.msleep(300)
    return ret


# 点击后一页
def click_next_page(wk: Worker, t=0, is_press=False) -> bool:
    if is_press:
        ret = wk.find_pic(*RECT_FULL, "后一页.bmp|下一页.bmp", timeout=t)
        wk.key_press(VK_RIGHT)
    else:
        ret = wk.find_pic_click(*RECT_FULL, "后一页.bmp|下一页.bmp", timeout=t)
    if ret:
        lib.msleep(300)
    return ret


# 点击 确定/确认/同意
def click_confirm(wk: Worker, t=0):
    ret = wk.find_pic_click(*RECT_TIP_CENTER, "确定1.bmp|确定2.bmp|确定3.bmp|确认1.bmp|确认2.bmp|"
                                              "同意1.bmp|同意2.bmp|确橙1.bmp|确橙2.bmp", timeout=t)
    if ret:  # 再点一次, 以防没点好
        wk.find_pic_click(*RECT_TIP_CENTER, "确定1.bmp|确定2.bmp|确定3.bmp|确认1.bmp|确认2.bmp|"
                                            "同意1.bmp|同意2.bmp|确橙1.bmp|确橙2.bmp")
    return ret


# 点击 取消/反对
def click_cancel(wk: Worker, t=0):
    ret = wk.find_pic_click(*RECT_TIP_CENTER, "取消1.bmp|取消2.bmp|反对1.bmp|反对2.bmp", timeout=t)
    return ret


# 点击 捕捉
def click_catch(wk: Worker, t=0):
    ret = wk.find_pic_click(*RECT_FULL, "捕捉.bmp|捕捉2.bmp", timeout=t)
    return ret


# 点击 防御
def click_defend(wk: Worker, t=0):
    wk.find_pic_click(*RECT_FULL, "防御.bmp|防御2.bmp", timeout=t)


# 是否指定目标成功
def is_specify_target_success(wk: Worker):
    if wk.find_pic(*RECT_TIP_BOTTOM, "目标未指定.bmp"):
        return False
    return True


# 冻结双倍经验
def freeze_double_exp(wk: Worker):
    if wk.find_pic_r_click(*RECT_BUFF, "buff_双倍.bmp"):
        click_confirm(wk, 400)


# 解冻双倍经验
def unfreeze_double_exp(wk: Worker):
    if wk.find_pic_r_click(*RECT_BUFF, "buff_双倍冻结.bmp"):
        click_confirm(wk, 400)


# 获取页最低价商品信息
def get_page_min_price_goods_info(wk: Worker, pic: str, is_need=True) -> (int, int, int):
    min_price, min_x, min_y = 999999, -1, -1
    if pic == "环装":
        x0, y0 = POS_JI_SHOU_PRICE_LT
        dx, dy = 53, 74
        for row in range(5):
            for col in range(5):
                x1, y1 = x0 + dx * row, y0 + dy * col
                x2, y2 = x1 + 46, y1 + 18
                ret = wk.ocr(x1, y1, x2, y2, COLOR_WHITE, zk=ZK_DIGIT_CLEAR)
                if ret == "":
                    continue
                price = int(ret)
                wk.price_list.append(price)
                if price < min_price:
                    min_price = price
                    min_x, min_y = x1 + 25, y1 - 25
    else:
        if not wk.find_pic(*RECT_GOODS, pic, delta_color="101010", timeout=300):
            wk.record("本页未找到指定物品")
            return min_price, min_x, min_y
        pos_list = wk.find_pic_ex(*RECT_GOODS, pic)  # [(0,100,20), (1,30,40)]
        for pos in pos_list:
            idx, pos_x, pos_y = pos
            if is_need:  # 购买需求物品
                x1, y1, x2, y2 = pos_x - 18, pos_y + 40, pos_x + 33, pos_y + 64
            else:  # 购买 五味羹, 玉琼浆...
                x1, y1, x2, y2 = pos_x - 29, pos_y + 23, pos_x + 22, pos_y + 47
            ret = wk.ocr(x1, y1, x2, y2, COLOR_WHITE, zk=ZK_DIGIT_CLEAR)
            if ret == "":
                continue
            price = int(ret)
            wk.price_list.append(price)
            if price < min_price:
                min_price = price
                min_x, min_y = pos_x, pos_y
    wk.record(f"本页最低价商品, 价格:{min_price}, 坐标:{min_x, min_y}")
    return min_price, min_x, min_y


# 寄售中心买物
def buy_goods_at_ji_shou(wk: Worker, pic: str, is_need=True) -> bool:
    wk.price_list = []  # 清空价格列表
    for i in range(30):  # 向后翻页统计该物品数据
        if wk.find_pic(*RECT_FULL, "商品星级.bmp|商品等级.bmp"):  # 若发现出现星级
            wk.key_press(VK_ALT)
            lib.msleep(200)
        get_page_min_price_goods_info(wk, pic, is_need)
        if len(wk.price_list) >= 4:  # 若已经找到4个商品,则跳出遍历
            break
        if not click_next_page(wk, 300, True):  # 若直到找完,也没找到4个商品,则跳出遍历
            break
        lib.msleep(500)
    if not wk.price_list:  # 若直到找完,一个商品也没找到
        wk.record("寄售中心未找到商品")
        return False
    avg_price = sum(wk.price_list) // len(wk.price_list) + 1
    # wk.record(f"寄售中心该商品均价约为:{avg_price}")
    for i in range(30):  # 向前翻页购买低于均价的商品
        price, x, y = get_page_min_price_goods_info(wk, pic, is_need)
        if price <= avg_price:
            wk.move_click(x + rnd(-2, 2), y + rnd(2, 5))
            wk.key_press(VK_ENTER)
            if not wk.find_pic(*RECT_TIP_CENTER, "超出成交均价.bmp", timeout=400):
                click_confirm(wk)
                wk.record("物品购买成功!")
                return True
            click_cancel(wk, 400)
        if not click_prev_page(wk, 300, True):  # 前一页
            return False
        lib.msleep(500)
    return False


# 购买物品-商店
def buy_goods_goto_shop(wk: Worker, shop_name: str, goods_name: str, goods_num="1", is_need=True) -> bool:
    ret = False
    if fly_to_map(wk, shop_name):
        around_list_click_npc(wk, "周围_店铺老板.bmp")
        for i in range(10):
            if click_talk_specify_item(wk, "购买物品", 300):
                lib.msleep(1000)
                ret = buy_goods_at_shop(wk, goods_name, goods_num)
                break
            lib.msleep(300)
    return ret


# 购买物品-寄售中心
def buy_goods_goto_ji_shou(wk: Worker, goods_name: str, is_need=True) -> bool:
    ret = False
    open_ji_shou_ui(wk)
    if not is_ji_shou_ui_open(wk):
        return False
    if goods_name in ER_JI_YAO:
        wk.find_pic_click(*RECT_FULL, "界_二级药.bmp", timeout=300)
    elif goods_name in SAN_JI_YAO:
        wk.find_pic_click(*RECT_FULL, "界_三级药.bmp", timeout=300)
    elif goods_name in PENG_REN:
        wk.find_pic_click(*RECT_FULL, "界_烹饪.bmp", timeout=300)
    elif goods_name in SHI_PIN:
        wk.find_pic_click(*RECT_FULL, "界_食品.bmp", timeout=300)
    elif goods_name in GU_DONG:
        wk.find_pic_click(*RECT_FULL, "界_古董.bmp", timeout=300)
    elif goods_name in JIA_JU:
        wk.find_pic_click(*RECT_FULL, "界_家具.bmp", timeout=300)
    elif goods_name in TING_YUAN:
        wk.find_pic_click(*RECT_FULL, "界_庭院.bmp", timeout=300)
    elif goods_name in ("50级装备", "60级装备", "70级装备"):
        wk.find_pic_click(*RECT_FULL, "界_装备.bmp", timeout=300)
    elif goods_name == "暗器":
        wk.find_pic_click(*RECT_FULL, "界_暗器.bmp", timeout=300)
    elif goods_name in ("红玫瑰", "雪莲花"):
        wk.find_pic_click(*RECT_FULL, "界_鲜花.bmp", timeout=300)
    else:
        wk.record(f"{goods_name} 未正确识别!")
        return False
    if is_need:  # 购买任务需求物品
        ret = buy_goods_at_ji_shou(wk, "高品.bmp|需求.bmp", is_need)
    else:  # 购买指定物品
        if goods_name in ["50级装备", "60级装备", "70级装备"]:
            pic = "环装"
        else:
            pic = f"物_{goods_name}.bmp"
        ret = buy_goods_at_ji_shou(wk, pic, is_need)
    return ret


# 出售当前页物品
def sell_cur_page_goods(wk: Worker, x: int, y: int, pic: str):
    for i in range(40):
        if not wk.find_pic_shift_r_click(x - 259, y - 40, x, y + 355, pic, timeout=300):
            break
        lib.msleep(300, 500)


# 出售物品-寄售中心
def sell_goods_ji_shou(wk: Worker, pic: str):
    open_ji_shou_ui(wk)
    x, y = wk.get_pic_pos(*RECT_FULL, "行囊页.bmp|行囊页2.bmp")
    if x > 0:
        sell_cur_page_goods(wk, x, y, pic)
        bag_change_page(wk)  # 背包换页
        sell_cur_page_goods(wk, x, y, pic)
    close_all_sub_wnd(wk)


# 购买物品-SW币中心
def buy_goods_swb(wk: Worker, goods_name: str):
    open_swb_ui(wk)
    if not is_swb_ui_open(wk):
        return False
    ret = False
    wk.find_pic_click(*RECT_FULL, "SW币页展开.bmp", timeout=200)  # 折叠起来
    lib.msleep(400)
    if goods_name == "装备之灵":
        wk.find_pic_click(*RECT_FULL, "装备相关.bmp", timeout=200)
        lib.msleep(600)
        ret = wk.find_pic_click(*RECT_FULL, "3级装备之灵.bmp", timeout=300)
        lib.msleep(600)
        # 选中随机一个适用
        wk.find_pic_click(*RECT_FULL, "适用.bmp", timeout=300)
        lib.msleep(300)
        # 点击购买
        wk.move_click(POS_SWB_BUY[0], POS_SWB_BUY[1])
    elif goods_name == "魔兽要诀":
        wk.find_pic_click(*RECT_FULL, "魔兽要诀.bmp", timeout=200)
        lib.msleep(600)
        wk.find_pic_click(*RECT_FULL, "低级魔兽要诀.bmp", timeout=300)
        lib.msleep(600)
        # 选一个最便宜的
        min_price, min_pos = swb_get_cheapest_price_pos(wk)
        wk.record(f"当前最低价魔兽要诀价格:{min_price}, 位置:{min_pos}")
        if min_price != 99999:
            ret = True
            wk.move_click(*min_pos, False)
            wk.move_click(POS_SWB_BUY[0], POS_SWB_BUY[1])  # 点击购买
    elif goods_name == "百花露":
        wk.find_pic_click(*RECT_FULL, "其他.bmp", timeout=200)
        lib.msleep(600)
        if wk.find_pic_click(*RECT_FULL, "百花露.bmp", timeout=300):
            ret = True
            lib.msleep(600)
            wk.move_click(POS_SWB_BUY_ONE[0], POS_SWB_BUY_ONE[1])  # 点击"购买1个"
    elif goods_name == "宝石":
        wk.find_pic_click(*RECT_FULL, "宝石.bmp", timeout=200)
        lib.msleep(600)
        # 买一个神秘石
        wk.move_click(POS_SWB_SMS[0], POS_SWB_SMS[1], False)
        # 点击购买
        wk.move_click(POS_SWB_BUY_ONE[0], POS_SWB_BUY_ONE[1])
    return ret


# SW币获取最便宜物品价格和坐标
def swb_get_cheapest_price_pos(wk: Worker):
    min_price, min_idx = 99999, -1
    x0, y0 = POS_SWB_PRICE
    for idx in range(16):
        y = y0 + 22 * idx
        price = wk.ocr(x0, y, x0 + 46, y + 22, COLOR_SCHEDULE_DIGIT, sim=0.8, zk=ZK_DIGIT_BLUR)
        if price == "":
            lib.msleep(100)
            continue
        price = int(price)
        if price < min_price:
            min_price = price
            min_idx = idx
    min_pos = (x0, y0 + 22 * min_idx + 11)
    return min_price, min_pos


# 是否SW币界面打开
def is_swb_ui_open(wk: Worker):
    ret = wk.find_pic(*RECT_FULL, "界_交易中心.bmp|界_交易中心2.bmp")
    return ret


# 打开SW币界面
def open_swb_ui(wk: Worker):
    for i in range(5):
        if not is_swb_ui_open(wk):
            wk.key_press_combo(VK_ALT, VK_O)
            # wk.move_click(POS_UI_SWB[0] + rnd(0, 10), POS_UI_SWB[1] + rnd(0, 10))
        else:
            break
        lib.msleep(800)
    else:
        wk.record("打开SW币界面失败")


# 出售物品-SW币交易中心
def sell_goods_swb(wk: Worker, pic: str):
    open_swb_ui(wk)
    x, y = wk.get_pic_pos(*RECT_FULL, "行囊页.bmp|行囊页2.bmp")
    if x > 0:
        sell_cur_page_goods(wk, x, y, pic)
        bag_change_page(wk)  # 背包换页
        sell_cur_page_goods(wk, x, y, pic)
    close_all_sub_wnd(wk)


# 是否宠物界面打开
def is_pet_ui_open(wk: Worker, t=0):
    if wk.find_pic(*RECT_FULL, "界_宠物.bmp|界_宠物2.bmp", timeout=t):
        return True
    return False


# 打开宠物界面
def open_pet_ui(wk: Worker):
    for i in range(3):
        if is_pet_ui_open(wk):
            break
        else:
            wk.move_click(POS_UI_PET[0] + rnd(0, 10), POS_UI_PET[1] + rnd(0, 10))
        lib.msleep(500)


# 购买任务宠
def buy_task_pet(wk: Worker):
    if lib.cfg_main["优先使用还童丹买宠"]:
        huan_tong_dan_buy_pet(wk)
        if sub_task(wk) == "完成":
            return
    use_fei_xing_qi(wk, "长安城", FLAG_RECT["交易中心"])
    for i in range(5):
        if is_talk_open(wk):
            break
        if not wk.is_find_way:
            x, y = NPC_POS_WND["交易中心"]
            click_map_wnd_pos(wk, x, y)
        lib.msleep(600)
    if not click_talk_specify_item(wk, "宠物", 200):
        close_talk(wk)
        return
    lib.msleep(300, 500)
    if not wk.find_pic(*RECT_FULL, "界_宠物中心.bmp", timeout=400):
        return
    buy_cash_or_credit(wk)
    close_all_sub_wnd(wk)


# 还童丹买宠
def huan_tong_dan_buy_pet(wk: Worker):
    if not bag_use_goods(wk, "物_还童丹.bmp"):
        return False
    lib.msleep(400)
    if not is_pet_ui_open(wk, 300):
        return False
    wk.move_click(POS_HTD_FC[0] + rnd(-2, 2), POS_HTD_FC[1] + rnd(-2, 2))  # 放入宠物
    lib.msleep(600)
    wk.move_click(POS_HTD_CWJY[0] + rnd(-2, 2), POS_HTD_CWJY[1] + rnd(-2, 2))  # 宠物交易中心
    lib.msleep(400)
    if not wk.find_pic(*RECT_FULL, "界_宠物中心.bmp", timeout=400):
        return False
    lib.msleep(300)
    buy_cash_or_credit(wk)
    lib.msleep(300)
    close_all_sub_wnd(wk)
    wk.record("还童丹买宠成功")
    lib.msleep(500)
    return True


# 购买物品
def buy_goods(wk: Worker, goods_name: str, goods_num="1", is_need=True) -> bool:
    if goods_name == "":
        return False
    if goods_name in YAO_PIN:
        ret = buy_goods_goto_shop(wk, "长安药店", goods_name, goods_num)
    elif goods_name in ZA_HUO:
        ret = buy_goods_goto_shop(wk, "长安杂货店", goods_name, goods_num)
    elif goods_name in FU_SHI_0_20:
        ret = buy_goods_goto_shop(wk, "长安服饰店", goods_name)
    elif goods_name in WU_QI_0_20:
        ret = buy_goods_goto_shop(wk, "长安武器店", goods_name)
    elif goods_name in FU_SHI_10:
        ret = buy_goods_goto_shop(wk, "青河服饰店", goods_name)
    elif goods_name in WU_QI_10:
        ret = buy_goods_goto_shop(wk, "青河武器店", goods_name)
    elif goods_name in FU_SHI_30:
        ret = buy_goods_goto_shop(wk, "傲来服饰店", goods_name)
    elif goods_name in WU_QI_30:
        ret = buy_goods_goto_shop(wk, "傲来武器店", goods_name)
    elif goods_name in FU_SHI_40:
        ret = buy_goods_goto_shop(wk, "临仙服饰店", goods_name)
    elif goods_name in WU_QI_40:
        ret = buy_goods_goto_shop(wk, "临仙武器店", goods_name)
    elif goods_name in {"装备之灵", "魔兽要诀", "百花露", "宝石"}:
        ret = buy_goods_swb(wk, goods_name)
    else:  # 寄售中心买物
        ret = buy_goods_goto_ji_shou(wk, goods_name, is_need)
    close_all_sub_wnd(wk)
    return ret


# 在周围走动16秒, 战斗则返回
def walk_around_until_fight(wk: Worker):
    wk.record("自动遇怪中...")
    flag = 1
    for i in range(20):
        if is_fight(wk):
            return
        if not wk.is_find_way:
            if flag:
                click_map_wnd_pos(wk, POS_CENTER[0] + rnd(-150, 150), POS_CENTER[1] + rnd(70, 80))
                flag = 0
            else:
                click_map_wnd_pos(wk, POS_CENTER[0] + rnd(-150, 150), POS_CENTER[1] + rnd(-80, -70))
                flag = 1
        lib.msleep(800)
    if wk.cur_task == "[打野]":
        cancel_qu_mo_xiang(wk)

# 按顺序走动直到周围列表点击
def walk_in_order_until_around_click(wk: Worker, pic: str):
    x, y = get_role_pos(wk)
    cx, cy = POS_CENTER
    if x < cx:
        if y < cy:  # 在左上角, 往左下角跑
            click_map_wnd_pos(wk, *POS_MAP_LEFT_DOWN)
        else:  # 在左下角, 往右下角跑
            click_map_wnd_pos(wk, *POS_MAP_RIGHT_DOWN)
    else:
        if y < cy:  # 在右上角, 往左上角跑
            click_map_wnd_pos(wk, *POS_MAP_LEFT_UP)
        else:  # 在右下角, 往右上角跑
            click_map_wnd_pos(wk, *POS_MAP_RIGHT_UP)
    for i in range(10):
        lib.msleep(1200, 1600)
        if is_fight(wk):
            fight_operation(wk)
        if around_list_click_npc(wk, pic) or not wk.is_find_way:
            break


# 按顺序走动
def walk_in_order(wk: Worker, fn):
    x, y = get_role_pos(wk)
    cx, cy = POS_CENTER
    if x < cx:
        if y < cy:  # 在左上角, 往左下角跑
            click_map_wnd_pos(wk, *POS_MAP_LEFT_DOWN)
        else:  # 在左下角, 往右下角跑
            click_map_wnd_pos(wk, *POS_MAP_RIGHT_DOWN)
    else:
        if y < cy:  # 在右上角, 往左上角跑
            click_map_wnd_pos(wk, *POS_MAP_LEFT_UP)
        else:  # 在右下角, 往右上角跑
            click_map_wnd_pos(wk, *POS_MAP_RIGHT_UP)
    for i in range(10):
        lib.msleep(1200, 1600)
        if is_fight(wk):
            fight_operation(wk)
        if fn(wk) or not wk.is_find_way:
            break


# 是否战斗中
def is_fight(wk: Worker, t=0):
    ret = wk.find_pic(*RECT_FULL, "战斗_攻击.bmp|战斗_战况.bmp|战斗_回合.bmp", timeout=t)
    return ret


# 是否在战斗准备阶段
def is_in_fight_ready(wk: Worker, t=0):
    ret = wk.find_pic(*RECT_FULL, "自动1.bmp|自动2.bmp|召唤1.bmp|召唤2.bmp", timeout=t)
    return ret


# 点自动
def click_zi_dong(wk: Worker):
    for i in range(5):
        if wk.find_pic(*RECT_FULL, "自动1.bmp|自动2.bmp"):
            wk.key_press_combo(VK_CTRL, VK_A)
        else:
            break
        lib.msleep(500)


# 是否目标打开
def is_target_open(wk: Worker):
    if wk.find_pic(*RECT_LOGO_ENEMY, "怪物标识.bmp"):
        return True
    return False


# 是否主怪活着
def is_boss_alive(wk: Worker):
    if wk.find_pic(*RECT_LOGO_BOSS, "怪物标识.bmp"):
        return True
    return False


# 打开战斗目标
def open_fight_target(wk: Worker):
    if is_talk_open(wk):
        return
    # 通过右键点击, 先把 目标复位
    ret = wk.find_pic_r_click(*RECT_RIGHT_DOWN, "战斗_目标.bmp")
    if not ret:  # 说明 可能是捉鬼等低级战斗, 没有目标
        return False
    ret = is_target_open(wk)
    if not ret:  # 目标还是没点开, 则左键点开
        ret = wk.find_pic_click(*RECT_RIGHT_DOWN, "战斗_目标.bmp")
    return ret


# 打开战斗buff区
def open_fight_buff_region(wk: Worker):
    wk.find_pic_click(*RECT_FIGHT_BUFF, "打开战斗buff区.bmp")


# 是否有宝宝
def is_have_bb(wk: Worker):
    # 既没有说话, 也没有"宝宝",肯定不是
    if not wk.find_pic(*RECT_ENEMY, "聊天气泡.bmp"):
        if not wk.find_str(*RECT_ENEMY, "宝宝", COLOR_FIGHT_UNIT):
            return False
    if wk.find_str(*RECT_ENEMY, "富裕", COLOR_FIGHT_UNIT, sim=0.9):
        return False
    return True


# 捉宝宝_找对话
def catch_bb_find_talk(wk: Worker):
    x, y = wk.get_pic_pos(*RECT_ENEMY, "聊天气泡.bmp")
    if y < 0 or y > 300:  # 不是敌方怪在说话
        return
    if y > 160 and wk.find_str(*RECT_ENEMY, "幸运儿", COLOR_WHITE):
        return
    if not click_catch(wk):
        return
    if wk.find_pic(*RECT_TIP_TOP, "身上宠物已满.bmp", timeout=400):
        wk.record("身上宠物已满,取消捕捉操作")
        wk.key_press(VK_ESC, delay=300)
        return
    for i in range(20):
        off_y = 50
        for j in range(5):
            wk.move_to(x + 14, y + off_y, False)
            if wk.find_str(*RECT_ENEMY, "宝宝", COLOR_RED):
                wk.left_click()
                lib.msleep(500)
                if is_specify_target_success(wk):
                    return
            off_y += 10
            lib.msleep(100, 200)


# 捉宝宝_找字
def catch_bb_find_str(wk: Worker):
    x, y = wk.get_str_pos(*RECT_ENEMY, "宝宝", COLOR_FIGHT_UNIT, sim=0.9)
    if x < 0:
        return
    if not click_catch(wk):
        return
    if wk.find_pic(*RECT_TIP_TOP, "身上宠物已满.bmp", timeout=400):
        wk.record("身上宠物已满,取消捕捉操作")
        wk.key_press(VK_ESC, delay=300)
        return
    for i in range(20):
        off_x, off_y = rnd(-30, 0), 30
        for j in range(11):
            wk.move_to(x + off_x, y - off_y, False)
            if wk.find_str(*RECT_ENEMY, "宝宝", COLOR_RED):
                wk.left_click()
                lib.msleep(500)
                if is_specify_target_success(wk):
                    return
            off_y += 10
            lib.msleep(100, 200)


# 捉宝宝
def catch_bb(wk: Worker):
    if wk.cur_task not in ("[打野]", "[队员]"):
        return
    if team.get_leader_task(wk) != "[打野]":
        return
    if not is_in_fight_ready(wk):
        return
    if not is_have_bb(wk):
        return

    if wk.cfg_plan["宝宝策略"] == "无视":
        wk.record("发现宝宝, 无视")
        return
    elif wk.cfg_plan["宝宝策略"] == "捕捉":
        wk.record("发现宝宝, 捕捉")
        close_all_sub_wnd(wk)
        if wk.find_pic(*RECT_ENEMY, "聊天气泡"):
            catch_bb_find_talk(wk)
        else:
            catch_bb_find_str(wk)
    elif wk.cfg_plan["宝宝策略"] == "防御":
        wk.record("发现宝宝, 防御")
        close_all_sub_wnd(wk)
        click_defend(wk)  # 人物防御
        lib.msleep(400, 600)

    if not is_specify_target_success(wk):
        wk.record("指定目标失败, 放弃操作")
        wk.key_press(VK_ESC, delay=300)
        lib.msleep(500)


# 遇富裕恭喜
def meet_fu_yu_gong_xi(wk: Worker):
    if not wk.cfg_plan["富裕发财"]:
        return
    if not is_in_fight_ready(wk):
        return
    if wk.cur_task not in ("[师门]", "[打野]", "[队员]"):
        return

    x, y = wk.get_str_pos(*RECT_ENEMY, "富裕", COLOR_FIGHT_UNIT, sim=0.8)
    if x < 0:
        return
    wk.record("战斗中发现 富裕怪, 使用 恭喜发财")
    if not wk.find_pic_click(*RECT_QUICK_BAR, "技_恭喜发财.bmp"):
        wk.record("未在右侧快捷面板找到技能-恭喜发财")
        return
    for i in range(5):
        pos_x = x + rnd(37, 55)
        pos_y = y - rnd(35, 115)
        wk.move_click(pos_x, pos_y)
        lib.msleep(200)
        if is_specify_target_success(wk):
            wk.move_r_click(pos_x, pos_y)
            break
    if not is_specify_target_success(wk):
        wk.record("指定目标失败, 放弃操作")
        wk.key_press(VK_ESC)
        lib.msleep(500)


# 打大肉山
def hit_da_rou_shan(wk: Worker):
    if not wk.cfg_plan["普攻大肉山"]:
        return
    if team.get_leader_task(wk) != "[封妖]":
        return
    if not is_in_fight_ready(wk):
        return
    x, y = wk.get_str_pos(*RECT_ENEMY, "肉山", f"{COLOR_FIGHT_UNIT}|{COLOR_RED}")
    if x > 0:
        wk.record("发现大肉山, 平A")
        wk.move_click(x + 6, y - 40, False)  # 人物平A
        lib.msleep(200, 600)
        wk.move_r_click(x + 6, y - 40)  # 宠物默认法术


# 是否队员死亡
def is_mate_die(wk: Worker):
    x, y = wk.get_pic_pos(*RECT_LOGO_FRIEND, "人物死亡1.bmp|人物死亡2.bmp|护送死亡.bmp")
    if x > 0 and not wk.find_color(x, y, x + 10, y + 10, COLOR_RED):
        return True  # 若队员死亡, 且不是自己
    return False


# 辅助门派救人
def assist_school_save_people(wk: Worker):
    if not is_mate_die(wk):
        return
    if wk.school not in ("幽冥地府", "佛门", "南海普陀"):
        return
    wk.record("发现 队友死亡")
    if not wk.find_pic_click(*RECT_QUICK_BAR, "技_DF复活.bmp|技_FM复活.bmp|技_PT复活.bmp"):
        wk.record("在右侧技能面板未发现复活技能")
        return
    if wk.find_pic_click(*RECT_LOGO_FRIEND, "人物死亡1.bmp|人物死亡2.bmp|护送死亡.bmp"):
        wk.record("已复活 队友")
        lib.msleep(600)
        wk.find_pic_r_click(*RECT_LOGO_ENEMY, "怪物标识.bmp")  # 宠物使用默认技能打怪
    else:
        wk.record("复活队友失败, 取消释放技能")
        wk.key_press(VK_ESC)  # 没点到则取消技能操作


# 是否宠物死亡
def is_pet_die(wk: Worker):
    # 找红色, 获取人物logo位置
    x, y = wk.get_color_pos(*RECT_LOGO_FRIEND, COLOR_RED)
    if x < 0:  # 没找到本人logo, 认定为宠物没死
        return False
    # 找人物logo下的宠物logo
    if wk.find_pic(x - 12, y + 30, x + 21, y + 52, "宠物存活.bmp"):
        return False
    return True


# 召唤新宠物
def call_new_pet(wk: Worker):
    if not wk.cfg_plan["自动召唤"]:
        return
    if not is_in_fight_ready(wk):
        return
    if not is_pet_die(wk):
        return
    wk.record("宠物死亡, 召唤宠物")
    for i in range(2):
        if wk.find_pic_click(*RECT_FULL, "可出战1.bmp|可出战2.bmp", timeout=400):
            lib.msleep(800)
            if wk.find_pic_click(*RECT_FULL, "召唤橙1.bmp|召唤橙2.bmp", timeout=300):
                wk.record("点击召唤成功")
                lib.msleep(300)
        else:
            if not wk.find_pic_click(*RECT_FULL, "召唤1.bmp|召唤2.bmp", timeout=300):
                break
        lib.msleep(800)
    close_all_sub_wnd(wk)


# 点击友方随机坐标
def click_friend_rnd_pos(wk: Worker):
    pos_list = [(POS_LOGO_LEADER[0], POS_LOGO_LEADER[1] + 30),
                (POS_LOGO_LEADER[0], POS_LOGO_LEADER[1]),
                (POS_LOGO_LEADER[0] - 27, POS_LOGO_LEADER[1]),
                (POS_LOGO_LEADER[0] + 27, POS_LOGO_LEADER[1]),
                (POS_LOGO_LEADER[0] - 54, POS_LOGO_LEADER[1]),
                (POS_LOGO_LEADER[0] + 54, POS_LOGO_LEADER[1])]
    for pos in pos_list:
        x, y = pos
        wk.move_click(x, y, re_move=False)
        lib.msleep(100, 200)
        if is_specify_target_success(wk):
            return True
    return False


# 对目标使用技能
def use_skill_on_target(wk: Worker, skill: str, target: str):
    if skill == "自动" or not is_target_open(wk):
        click_zi_dong(wk)
        return
    str_vk_dict = {"F1": VK_F1, "F2": VK_F2, "F3": VK_F3, "F4": VK_F4,
                   "F5": VK_F5, "F6": VK_F6, "F7": VK_F7, "F8": VK_F8}
    wk.record(f"使用技能:{skill}, 目标:{target}")
    wk.key_press(str_vk_dict[skill])
    lib.msleep(300, 600)
    if target == "友方":
        if click_friend_rnd_pos(wk):
            wk.record("使用技能 -> 友方目标, 成功")
            wk.find_pic_r_click(*RECT_LOGO_ENEMY, "怪物标识.bmp")  # 宠物使用默认法术攻击
        else:
            wk.record("使用技能 -> 友方目标, 失败, 放弃操作")
            wk.key_press(VK_ESC)
            click_zi_dong(wk)
    else:
        if is_boss_alive(wk):
            wk.record("使用技能 -> 敌方首领, 成功")
            wk.move_click(POS_LOGO_BOSS[0] + rnd(-2, 2), POS_LOGO_BOSS[1] + rnd(-2, 2))
            lib.msleep(300)
            wk.move_r_click(POS_LOGO_BOSS[0] + rnd(-2, 2), POS_LOGO_BOSS[1] + rnd(-2, 2))  # 宠物使用默认法术攻击
        else:
            wk.record("敌方首领已死亡, 随机攻击")
            wk.find_pic_click(*RECT_LOGO_ENEMY, "怪物标识.bmp")
            wk.find_pic_r_click(*RECT_LOGO_ENEMY, "怪物标识.bmp")  # 宠物使用默认法术攻击


# 首回合战斗
def first_round(wk: Worker):
    catch_bb(wk)  # 捉宝宝
    meet_fu_yu_gong_xi(wk)  # 遇富裕使用"恭喜发财"
    hit_da_rou_shan(wk)  # 打大肉山
    df_la_huan(wk)  # 地府拉环
    if not is_in_fight_ready(wk):
        return
    skill = wk.cfg_plan["首个回合技能"]
    target = wk.cfg_plan["首个回合目标"]
    use_skill_on_target(wk, skill, target)


# 其它回合战斗
def other_round(wk: Worker):
    call_new_pet(wk)  # 召唤新宠物
    assist_school_save_people(wk)  # 辅助门派救队友
    df_la_huan(wk)  # 地府拉环
    if not is_in_fight_ready(wk):
        return
    skill = wk.cfg_plan["剩余回合技能"]
    target = wk.cfg_plan["剩余回合目标"]
    use_skill_on_target(wk, skill, target)


# 天魔买暗器
def tm_buy_an_qi(wk: Worker):
    if not wk.cfg_plan["天魔买暗器"]:
        return
    if wk.find_pic(*RECT_QUICK_BAR, "技_雨露千本灰.bmp"):
        wk.record("缺少暗器, 在天仙店铺中购买飞刀或镖花镖")
        open_tian_xian(wk)
        buy_goods_at_shop(wk, "飞刀|梅花镖")
        close_all_sub_wnd(wk)


# 地府拉环
def df_la_huan(wk: Worker):
    if not wk.cfg_plan["地府拉环"]:
        return
    if wk.school != "幽冥地府":
        return
    if not is_in_fight_ready(wk):
        return
    if not wk.find_pic(*RECT_LOGO_ENEMY, "怪物标识.bmp"):
        return
    if wk.find_pic(*RECT_FIGHT_BUFF, "buff_拉环.bmp"):
        return
    if wk.find_pic_click(*RECT_QUICK_BAR, "技_黑暗光环.bmp"):
        lib.msleep(500)
        wk.find_pic_click(*RECT_LOGO_ENEMY, "怪物标识.bmp", order=rnd(0, 3))
        lib.msleep(500)
        # 宠物使用默认法术攻击
        wk.find_pic_r_click(*RECT_LOGO_ENEMY, "怪物标识.bmp", order=rnd(0, 3))


# 战斗中操作
def fight_operation(wk: Worker):
    wk.record("战斗开始")
    lib.msleep(500)
    close_all_sub_wnd(wk)
    open_fight_target(wk)  # 打开任务目标
    open_fight_buff_region(wk)  # 打开战斗buff区

    round, isChecked = 0, False
    while is_fight(wk):
        lib.msleep(600)
        if is_in_fight_ready(wk, 400):  # 在战斗准备阶段
            round += 1
            wk.record(f"战斗中, 第{round}轮")
            if round == 1:
                first_round(wk)
            else:
                other_round(wk)
            if not is_in_fight_ready(wk):  # 防止宠物没操作
                click_defend(wk)  # 宠物防御
        else:  # 不在战斗准备阶段
            if not isChecked and round == 1:  # 若没有检查过, 且是第一回合的间隙
                if wk.cur_task not in ["[剧情]", ""]:  # 不是主线剧情, 才检查药并买药
                    calc_bag_drug_num(wk)  # 打开背包统计药品数量
                    buy_drug_tian_xian(wk)  # 天仙店铺买药
                    buy_drug_ji_shou(wk)  # 寄售中心买药
                role_pet_add_hp_mp(wk)  # 补满状态
                adjust_zi_dong_zhan_dou(wk)  # 调整自动战斗框
                isChecked = True
            lib.msleep(600)
    wk.record("战斗结束")
    lib.msleep(1000)
    close_talk(wk, 400, True)
    role_pet_add_hp_mp(wk)  # 再补满状态一次, 避免没加到
    pet_add_loyal(wk)  # 宠物补忠诚


# 获取当前任务位置
def get_cur_task_pos(wk: Worker, t=0):
    if wk.cur_task == "[边境]":
        cur_task = "[任务]"
    elif wk.cur_task in ("[玄武]", "[青龙]"):
        cur_task = "[帮派]"
    elif wk.cur_task == "[蛮洞]":
        cur_task = "挑战蛮"
    else:
        cur_task = wk.cur_task
    x, y = wk.get_str_pos(*RECT_CUR_TASK, cur_task, COLOR_YELLOW, zk=ZK_TASK_TYPE, timeout=t)
    return x, y


# 获取人物位置
def get_role_pos(wk: Worker):
    x, y = -1, -1
    open_map(wk)
    if is_map_open(wk):
        x, y = wk.get_pic_pos(*RECT_FULL, "人物位置1.bmp|人物位置2.bmp|人物位置3.bmp|寻路目的点标志.bmp")
    return x, y


# 子任务
def sub_task(wk: Worker):
    set_task_to_cur_task_bar(wk)
    x, y = get_cur_task_pos(wk, 300)
    if x == -1:
        return "接任务"
    # 先识别一些特殊的子任务
    if wk.cur_task == "[运镖]":
        if wk.find_pic(x, y - 5, x + 180, y + 30, "物品抵押完成.bmp"):
            return "抵押完成"
        if wk.find_pic(x, y - 5, x + 180, y + 30, "劫镖事件完成.bmp"):
            return "劫镖完成"
    elif wk.cur_task == "[剧情]":
        if wk.find_str(x - 20, y - 3, x + 200, y + 20, "升到", COLOR_YELLOW) \
                and wk.find_str(*RECT_CUR_TASK, "提升人物等级", COLOR_CYAN):
            return "等级不足"
        if wk.find_pic(x - 20, y - 3, x + 200, y + 40, "找到[.bmp"):
            return "购买物品"
        if is_talk_open(wk):
            return "对话"
        if wk.find_pic(x - 20, y - 3, x + 200, y + 40, "青河小霸王.bmp|青河小霸王2.bmp"):
            return "青河小霸王"
        return "找人"
    # 通用的识别子任务方法
    elif wk.ocr(x + 30, y - 5, x + 160, y + 12, COLOR_GREEN) == "完成":
        return "完成"
    task_type = wk.ocr(x + 30, y - 5, x + 160, y + 12, COLOR_YELLOW, zk=ZK_SUB_TASK, timeout=300)
    return task_type


# 识别任务目标地图
def ocr_task_des_map(wk: Worker):
    x1, y1 = get_cur_task_pos(wk, 400)
    if x1 == -1:
        wk.record(f"当前任务栏未找到{wk.cur_task}")
        close_all_sub_wnd(wk)
        return ""
    close_mail(wk)
    ret = ""
    # 获取下一个任务的顶部位置
    x2, y2 = wk.get_color_pos(x1, y1 + 30, x1 + 100, y1 + 100, COLOR_YELLOW)
    if (x2, y2) == (-1, -1):  # 没找到, 说明下面没有任务了
        x2, y2 = x1, y1 + 100
    # 在此任务描述范围找"到|去|交给"
    x, y = wk.get_str_pos(x1 - 20, y1, x1 + 190, y2, "到|去|交给", COLOR_WHITE)
    if x == -1:  # 没找到, 则直接识别绿色字
        ret = wk.ocr(x1 - 20, y1, x1 + 190, y2, COLOR_GREEN)
    else:
        ret1 = wk.ocr(x, y, x1 + 190, y + 14, COLOR_GREEN)  # 识别"到"字右边
        ret2 = wk.ocr(x1 - 20, y + 14, x1 + 190, y2, COLOR_GREEN)  # 识别"到"字下边
        ret = ret1 + ret2
    # 运镖任务要额外进行处理
    if wk.cur_task == "[运镖]":
        des_maps = ["大雄宝殿", "程府", "水晶宫", "云隐阁", "南海普陀", "森罗殿", "盘丝洞", "无名谷", "魔王山", "乾坤殿", "狮王洞",
                    "灵台宫", "凌霄殿", "傲来国", "青河镇外", "青河镇", "临仙镇", "女儿国", "天策", "天魔里", "七星方寸", "北冥",
                    "花果山", "长安城外", "昆仑山", "乌斯藏", "大唐境外", "大唐国境"]
        for des_map in des_maps:
            if des_map in ret:
                ret = des_map
                break

    wk.record(f"任务地点: {ret}")
    return ret


# 识别任务NPC名字
def ocr_task_npc_name(wk: Worker):
    x1, y1 = get_cur_task_pos(wk, 400)
    if x1 == -1:
        wk.record(f"当前任务栏未找到{wk.cur_task}")
        close_all_sub_wnd(wk)
        return ""
    close_mail(wk)
    ret = ""
    # 获取下一个任务的顶部位置
    x2, y2 = wk.get_color_pos(x1, y1 + 30, x1 + 100, y1 + 100, COLOR_YELLOW)
    if (x2, y2) == (-1, -1):  # 没找到, 说明下面没有任务了
        x2, y2 = x1, y1 + 100
    # 在此任务描述范围内找"的|向"字
    x, y = wk.get_str_pos(x1 - 20, y1, x1 + 190, y2, "的|向", COLOR_WHITE)
    if (x, y) == (-1, -1):  # 没找到, 则直接识别青色字
        ret = wk.ocr(x1 - 20, y1, x1 + 190, y2, COLOR_CYAN)
    else:
        ret1 = wk.ocr(x, y, x1 + 190, y + 14, COLOR_CYAN)  # 识别"的"字右边
        ret2 = wk.ocr(x1 - 20, y + 14, x1 + 190, y2, COLOR_CYAN)  # 识别"的"字下边
        ret = ret1 + ret2
    wk.record(f"任务NPC名: {ret}")
    return ret


# 识别任务需求物品
def ocr_task_need_goods(wk: Worker):
    x, y = get_cur_task_pos(wk, 400)
    if x < 0:
        wk.record(f"当前任务栏未找到{wk.cur_task}")
        close_all_sub_wnd(wk)
        return ""
    close_mail(wk)

    ret = ""
    if wk.cur_task == "[师门]":
        xx, yy = wk.get_pic_pos(x - 23, y + 11, x + 155, y + 42, "找到[.bmp")
        if xx > 0:  # 单份
            ret = wk.ocr(xx, yy - 5, xx + 120, yy + 12, COLOR_GREEN)
        else:  # 双份
            xx, yy = wk.get_pic_pos(x, y, x + 155, y + 60, "双份物资.bmp")
            if xx > 0:
                ret = wk.ocr(xx - 88, yy - 3, xx, yy + 12, COLOR_GREEN)
    elif wk.cur_task in ("[修炼]", "[任务链]"):
        ret = wk.ocr(x - 17, y + 12, x + 155, y + 27, COLOR_GREEN)  # 识别绿色
        if not ret:
            ret = wk.ocr(x - 17, y + 12, x + 155, y + 27, COLOR_CYAN)  # 识别青色
            if ret == "级装备之灵":
                ret = "装备之灵"
            elif ret == "级装备":
                level = wk.ocr(x - 17, y + 12, x + 155, y + 27, COLOR_CYAN, zk=ZK_DIGIT_CLEAR)  # 识别环装等级
                ret = level + ret
            elif ret in ("宝石神", "宝石SW"):
                ret = "宝石"
        elif ret in ("下列种物品之一", "下列种物品之"):
            ret = "暗器"
    else:  # 一般情况
        ret = wk.ocr(x - 17, y + 12, x + 155, y + 27, COLOR_GREEN)
    wk.record(f"任务需求物品:{ret}")
    return ret


# 购买任务需求物品
def buy_task_need_goods(wk: Worker):
    goods_name = ocr_task_need_goods(wk)
    buy_goods(wk, goods_name)


# 飞到任务地图战斗
def fly_task_map_fight(wk: Worker):
    map_name = ocr_task_des_map(wk)
    fly_to_map(wk, map_name)
    for i in range(30):
        if is_task_over(wk, 300):
            return
        if is_talk_open(wk):
            talk_proc(wk)
        if is_fight(wk):
            fight_operation(wk)
            return
        if not wk.is_find_way and not task_npc_find_way(wk):
            return
        lib.msleep(600)


# 飞到任务NPC对话
def fly_task_npc_talk(wk: Worker):
    map_name = ocr_task_des_map(wk)
    npc_name = ocr_task_npc_name(wk)
    fly_to_npc(wk, map_name, npc_name)
    if not goto_task_npc_talk(wk):
        return False
    return True


# 跑去和任务npc对话, 出 对话框,给予框,战斗 返回真
def goto_task_npc_talk(wk: Worker):
    for i in range(30):
        if is_talk_open(wk) or is_give_open(wk) or is_fight(wk):
            return True
        if not wk.is_find_way and not task_npc_find_way(wk):
            return False
        lib.msleep(rnd(800, 1200))
    return False


# 跑去和指定坐标的NPC对话, 若触发对话且点击选项返回真
def goto_pos_npc_talk(wk: Worker, x: int, y: int, item_text=""):
    ret = False
    for i in range(10):
        if is_talk_open(wk):
            break
        if not wk.is_find_way:
            click_map_wnd_pos(wk, x, y)
        lib.msleep(1000)
    if is_talk_open(wk):  # 若对话打开
        ret = click_talk_specify_item(wk, item_text)
    return ret


# 跑去找任务问号NPC
def goto_task_question_npc(wk: Worker, npc_name=""):
    if npc_name == "九黎大盗":
        font = "九"
    elif npc_name == "护送交付":
        font = "当|戏|隐|门|青"

    open_map(wk)
    if wk.find_pic(*RECT_FULL, "寻路目的点标志.bmp"):
        ret = True
    else:
        x, y = wk.get_str_pos(*RECT_FULL, font, COLOR_MAP_NPC)
        if x > 0:
            ret = wk.find_pic_click(x + 10, y - 10, x + 40, y + 25, "Npc问号.bmp", order=rnd(0, 3))
            if not ret:
                ret = wk.find_pic_click(*RECT_FULL, "Npc问号.bmp", order=rnd(0, 3))
        else:
            wk.record(f"未找到npc {npc_name}")
            ret = wk.find_pic_click(*RECT_FULL, "Npc问号.bmp", order=rnd(0, 3))
    close_map(wk)
    return ret


# 调整当前任务栏字体
def adjust_cur_task_bar_font(wk: Worker):
    for i in range(2):
        if wk.find_pic(*RECT_CUR_TASK, "中字二.bmp|中字三.bmp|中字四.bmp|大字二.bmp|大字三.bmp|大字四.bmp",
                       delta_color="222222", sim=0.9):
            wk.record("发现 当前任务栏字体较大, 正在自动调整...")
            wk.find_pic_click(*RECT_FULL, "调整字体.bmp")
            lib.msleep(500)
        else:
            break


# 是否任务在当前任务栏
def is_task_on_cur_task_bar(wk: Worker):
    if not wk.find_str(*RECT_FULL, "前任务", COLOR_WHITE):
        close_all_sub_wnd(wk)
    adjust_cur_task_bar_font(wk)  # 检查字体
    if wk.cur_task == "[边境]":
        cur_task = "[任务]"
    elif wk.cur_task in ("[玄武]", "[青龙]"):
        cur_task = "[帮派]"
    else:
        cur_task = wk.cur_task
    x, y = wk.get_str_pos(*RECT_FULL, "前任务", COLOR_WHITE)
    if x > 0:
        ret = wk.find_str(*RECT_CUR_TASK, cur_task, COLOR_YELLOW, zk=ZK_TASK_TYPE)
    else:
        ret = False
        wk.record("未找到当前任务栏")
    return ret


# 任务界面勾选当前任务
def task_ui_check_cur_task(wk: Worker):
    if wk.cur_task == "[边境]":
        cur_task = "[任务]"
    elif wk.cur_task in {"[玄武]", "[青龙]"}:
        cur_task = "[帮派]"
    else:
        cur_task = wk.cur_task
    task_name = cur_task.strip("[|]")  # "运镖"
    x, y = wk.get_pic_pos(*RECT_FULL, f"任务_{task_name}A.bmp|任务_{task_name}B.bmp")
    if x < 0:  # 没找到该任务
        return False
    if not wk.find_pic_click(x + 140, y - 10, x + 230, y + 30, "单任务追踪0.bmp"):
        x2, y2 = wk.get_pic_pos(x + 140, y - 10, x + 230, y + 30, "单任务追踪1.bmp")
        if x2 > 0:
            wk.move_click(x2 + rnd(1, 3), y2 + rnd(1, 3), False)
            lib.msleep(300, 500)
            wk.move_click(x2 + rnd(1, 3), y2 + rnd(1, 3))
        else:
            return False  # 没点击成功
    return True


# 任务界面放弃官职任务
def task_ui_abondon_guan_zhi(wk: Worker):
    if not wk.find_pic_click(*RECT_FULL, "任务_官职A.bmp|任务_官职B.bmp"):
        return False
    lib.msleep(400, 600)
    if not wk.find_pic_click(*RECT_FULL, "放弃1.bmp|放弃2.bmp"):
        return False
    lib.msleep(400, 600)
    if not click_confirm(wk):
        return False
    return True


# 遍历任务界面, 执行函数
def foreach_task_ui_exec_fn(wk: Worker, fn):
    open_task_ui(wk)
    x, y = wk.get_pic_pos(*RECT_FULL, "界_任务.bmp|界_任务2.bmp")
    if x == -1:
        wk.record("任务界面未打开")
        return False
    if wk.find_pic_click(*RECT_FULL, "当前任务.bmp"):  # 切换到已接任务
        lib.msleep(1000)
    s_x, s_y = wk.get_pic_pos(x + 240, y + 10, x + 276, y + 320, "任务滚动条.bmp")
    if s_x > 0:  # 如果找到滚动条,则拖动到顶部
        wk.move_drag_to(s_x + rnd(2, 4), s_y + rnd(2, 4), 374 + rnd(-100, 100), 6 + rnd(-2, 8))
        for i in range(5):
            if fn(wk):  # 任务界面勾选当前任务
                close_task_ui(wk)
                return True
            # 若未找到当前任务, 则往下翻
            d_x, d_y = wk.get_pic_pos(x + 240, y + 10, x + 300, y + 320, "下箭头.bmp")
            if d_x > 0:
                wk.move_wheel_down(d_x + rnd(2, 5), d_y + rnd(2, 5), 20)
            if wk.find_pic(x + 240, y + 10, x + 300, y + 320, "滚动条至底.bmp"):
                wk.record(f"已遍历整个任务界面, 未找到 {wk.cur_task}")
                break
    ret = fn(wk)
    close_task_ui(wk)
    return ret


# 设置任务到当前任务栏
def set_task_to_cur_task_bar(wk: Worker):
    if is_fight(wk):
        fight_operation(wk)
    if not wk.find_str(*RECT_FULL, "前任务", COLOR_WHITE):
        close_all_sub_wnd(wk)
    adjust_cur_task_bar_font(wk)  # 检查字体
    x, y = get_cur_task_pos(wk)
    if 0 < y < CENTER_Y:  # 若任务在上半截, 直接返回真
        return True
    open_task_track(wk, False)  # 复位当前任务追踪栏
    ret = foreach_task_ui_exec_fn(wk, task_ui_check_cur_task)
    return ret


# 是否任务结束(次数已达上限 或 其它特殊情况导致不能做)
def is_task_over(wk: Worker, t=0, specify_count=0):
    if not is_talk_open(wk, t):
        return False
    flag = False
    if not specify_count:
        specify_count = get_cur_task_specify_count(wk)
    if wk.cur_task == "[师门]":
        if wk.find_pic(*RECT_TALK_CONTENT_SMALL, "师门满次.bmp") and specify_count <= 20:
            flag = True
    else:
        task_content_dict = {"[运镖]": "运镖满次|运镖未考核|运镖活跃不足|运镖等级不足",
                             "[宝图]": "宝图满次",
                             "[修炼]": "修炼满次",
                             "[边境]": "边境满次",
                             "[官职]": "官职满次",
                             "[玄武]": "玄武满次",
                             "[青龙]": "青龙满次",
                             "[任务链]": "任务链满次"}
        content = task_content_dict.get(wk.cur_task)
        if content and is_talk_have_content(wk, content):
            flag = True
    if flag:
        wk.done_count = specify_count
        wk.record(f"已完成 {specify_count}/{specify_count}")
        wk.record("任务满次")
        return True
    return False


# 放弃任务
def abondon_task(wk: Worker, task: str):
    ret = False
    if task == "官职":
        ret = foreach_task_ui_exec_fn(wk, task_ui_abondon_guan_zhi)
    return ret


# 关闭邮件
def close_mail(wk: Worker):
    if wk.find_pic_click(*RECT_CUR_TASK, "邮件框.bmp"):
        lib.msleep(500)
        close_all_sub_wnd(wk)


# 是否仓库界面打开
def is_depot_ui_open(wk: Worker, t=0):
    ret = wk.find_pic(*RECT_FULL, "界_仓库.bmp|界_仓库2.bmp", timeout=t)
    return ret


# 是否仓库空间不足
def is_depot_space_lack(wk: Worker):
    ret = wk.find_pic(*RECT_TIP_TOP, "仓库空间不足.bmp")
    return ret


# 切换下一个仓库页
def switch_next_depot_page(wk: Worker):
    x, y = wk.get_color_pos(*RECT_DEPOT_PAGE, COLOR_CUR_DEPOT_PAGE)
    if x < 0:
        return
    if y < Y_DEPOT_PAGE:
        if x < X_DEPOT_PAGE1:  # 当前在1,切到2
            wk.move_click(X_DEPOT_PAGE1 + rnd(20, 30), Y_DEPOT_PAGE - rnd(10, 15))
        elif x < X_DEPOT_PAGE2:
            wk.move_click(X_DEPOT_PAGE2 + rnd(20, 30), Y_DEPOT_PAGE - rnd(10, 15))
        elif x < X_DEPOT_PAGE3:
            wk.move_click(X_DEPOT_PAGE3 + rnd(20, 30), Y_DEPOT_PAGE - rnd(10, 15))
        elif x < X_DEPOT_PAGE4:
            wk.move_click(X_DEPOT_PAGE4 + rnd(20, 30), Y_DEPOT_PAGE - rnd(10, 15))
        elif x < X_DEPOT_PAGE5:  # 5 切 6
            wk.move_click(X_DEPOT_PAGE1 - rnd(20, 30), Y_DEPOT_PAGE + rnd(10, 15))
    else:
        if x < X_DEPOT_PAGE1:  # 当前在6,切到7
            wk.move_click(X_DEPOT_PAGE1 + rnd(20, 30), Y_DEPOT_PAGE + rnd(10, 15))
        elif x < X_DEPOT_PAGE2:  # 7 切 8
            wk.move_click(X_DEPOT_PAGE2 + rnd(20, 30), Y_DEPOT_PAGE + rnd(10, 15))
        elif x < X_DEPOT_PAGE2:  # 8 切 9
            wk.move_click(X_DEPOT_PAGE3 + rnd(20, 30), Y_DEPOT_PAGE + rnd(10, 15))
        elif x < X_DEPOT_PAGE2:  # 9 切 10
            wk.move_click(X_DEPOT_PAGE4 + rnd(20, 30), Y_DEPOT_PAGE + rnd(10, 15))
    lib.msleep(1000)  # 等待仓库物品页刷新


# 存本背包页物品
def put_bag_page_goods(wk: Worker, pic: str):
    x, y = wk.get_pic_pos(*RECT_FULL, "行囊页.bmp|行囊页2.bmp")
    if x < 0:
        return
    for i in range(30):
        if not wk.find_pic_r_click(x - 259, y - 40, x, y + 355, pic, timeout=300):
            break
        lib.msleep(100, 200)
        if is_depot_space_lack(wk):
            wk.record("本仓库页空间不足, 自动切换至下一页")
            switch_next_depot_page(wk)


# 物品存放到仓库
def goods_put_depot(wk: Worker, pic: str):
    # 飞到仓库
    if not fly_to_map(wk, "长安当铺"):
        return
    # 打开仓库界面
    for i in range(5):
        if is_depot_ui_open(wk):
            break
        around_list_click_npc(wk, "周围_仓库管理员.bmp")
        click_talk_specify_item(wk, "进入物品仓库", 400)
        lib.msleep(800)
    # 仓库界面打开后的操作
    if is_depot_ui_open(wk, 400):
        put_bag_page_goods(wk, pic)
        wk.record("第一页背包物品放入完毕")
        bag_change_page(wk)
        put_bag_page_goods(wk, pic)
        wk.record("第二页背包物品放入完毕")
    close_all_sub_wnd(wk)


# 是否化龙鼎界面打开
def is_hld_ui_open(wk: Worker, t=0):
    ret = wk.find_pic(*RECT_FULL, "界_化龙鼎.bmp|界_化龙鼎2.bmp", timeout=t)
    return ret


# 打开化龙鼎界面
def open_hld_ui(wk: Worker):
    if is_hld_ui_open(wk):
        return True
    open_bag(wk)
    if is_bag_open(wk):
        for i in range(3):
            wk.find_pic_click(*RECT_FULL, "化龙鼎.bmp")
            lib.msleep(400)
            if is_hld_ui_open(wk, 300):
                return True
    return False


# 制作家具庭院
def make_jia_ju_ting_yuan(wk: Worker, goods_name: str):
    wk.record(f"自制家具庭院: {goods_name}")
    if not wk.find_pic_r_click(*RECT_QUICK_BAR, "技_巧匠.bmp", timeout=200):
        wk.record("右侧快捷面板未找到'巧匠'技能")
        return
    lib.msleep(500)
    if not wk.find_pic(*RECT_FULL, "界_制作.bmp|界_制作2.bmp", timeout=300):
        return
    if goods_name in JIA_JU:
        wk.move_click(*POS_JIA_JU)
    else:
        wk.move_click(*POS_TING_YUAN)
    # 先移到最顶端
    wk.move_wheel_up(POS_JJTY_SCORLL[0] + rnd(-10, 10), POS_JJTY_SCORLL[1] + rnd(-10, 10), 50)
    flag = False  # 标志位
    for i in range(7):
        if wk.find_pic_click(*RECT_MAKE_GOODS, "需.bmp", timeout=300):
            wk.move_click(POS_JJTY_QDZZ[0] + rnd(-2, 2), POS_JJTY_QDZZ[1] + rnd(-2, 2))  # 确定制作
            wk.record("制作成功")
            flag = True
            break
        wk.move_wheel_down(POS_JJTY_SCORLL[0] + rnd(-10, 10), POS_JJTY_SCORLL[1] + rnd(-10, 10), 7)
        lib.msleep(300)
    close_all_sub_wnd(wk)
    if not flag:
        return
    lib.msleep(1000)
    for i in range(2):
        bag_use_goods(wk, "物_装饰设计图.bmp|物_家具设计图.bmp")
        lib.msleep(300)
    close_bag(wk)
    lib.msleep(300)


# 是否日程界面打开
def is_schedule_ui_open(wk: Worker):
    ret = wk.find_pic(*RECT_FULL, "界_日程.bmp|界_日程2.bmp")
    return ret


# 打开日程界面
def open_schedule_ui(wk: Worker):
    close_talk(wk)
    for i in range(4):
        if is_schedule_ui_open(wk):
            break
        else:
            wk.key_press_combo(VK_ALT, VK_Y)
            # wk.move_click(POS_UI_SCHEDULE[0] + rnd(0, 10), POS_UI_SCHEDULE[1] + rnd(0, 10))
        lib.msleep(800)


# 关闭日程界面
def close_schedule_ui(wk: Worker):
    close_talk(wk)
    for i in range(4):
        if is_schedule_ui_open(wk):
            wk.key_press_combo(VK_ALT, VK_Y)
            # wk.move_click(POS_UI_SCHEDULE[0] + rnd(0, 10), POS_UI_SCHEDULE[1] + rnd(0, 10))
        else:
            break
        lib.msleep(800)


# 日程查询当前任务完成次数, 已完成返回真, 否则返回假
def schedule_query_cur_task_done_count(wk: Worker, specify_count: int):
    if wk.cur_task not in ("[灵狐]", "[旗包]", "[祈福]", "[修炼宝箱]"):
        return False
    task_name = wk.cur_task.strip("[|]")
    pic = f"rc_{task_name}A.bmp"
    pic_full = f"rc_{task_name}B.bmp"
    open_schedule_ui(wk)
    lib.msleep(300)
    if wk.find_pic(*RECT_FULL, pic_full, timeout=400):
        wk.done_count = specify_count
    else:
        x, y = wk.get_pic_pos(*RECT_FULL, pic)
        if x > 0:
            ret = wk.ocr(x, y + 20, x + 25, y + 40, COLOR_SCHEDULE_DIGIT, sim=0.85, zk=ZK_DIGIT_BLUR)
            if ret.isdigit():
                wk.done_count = int(ret)
    wk.record(f"已完成 {wk.done_count}/{specify_count}")
    close_schedule_ui(wk)
    if wk.done_count == specify_count:
        return True
    return False


# 是否队伍界面打开
def is_team_ui_open(wk: Worker):
    ret = wk.find_pic(*RECT_FULL, "界_队伍.bmp|界_队伍2.bmp")
    return ret


# 打开队伍界面
def open_team_ui(wk: Worker):
    close_talk(wk)
    for i in range(3):
        if is_team_ui_open(wk):
            break
        else:
            wk.key_press_combo(VK_ALT, VK_V)
            # wk.move_click(POS_UI_TEAM[0] + rnd(0, 10), POS_UI_TEAM[1] + rnd(0, 10))
        lib.msleep(500)


# 关闭队伍界面
def close_team_ui(wk: Worker):
    for i in range(3):
        if is_team_ui_open(wk):
            wk.key_press_combo(VK_ALT, VK_V)
            # wk.move_click(POS_UI_TEAM[0] + rnd(0, 10), POS_UI_TEAM[1] + rnd(0, 10))
        else:
            break
        lib.msleep(500)


# 离开队伍
def exit_team(wk: Worker):
    # 若正在匹配,则退出匹配
    wk.find_str_click(*RECT_FULL, "退出队列", COLOR_CYAN)
    wk.record("离开队伍...")
    open_team_ui(wk)
    lib.msleep(300)
    wk.find_pic_click(*RECT_FULL, "退出队伍.bmp|退出队伍2.bmp", timeout=300)
    wk.find_pic_click(*RECT_FULL, "退出队伍.bmp|退出队伍2.bmp", timeout=300)
    close_team_ui(wk)


# 暂时离开队伍
def temporary_exit_team(wk: Worker):
    wk.record("暂离队伍...")
    open_team_ui(wk)
    wk.find_pic_click(*RECT_FULL, "暂离队伍.bmp|暂离队伍2.bmp", timeout=400)
    close_team_ui(wk)


# 回归队伍
def back_to_team(wk: Worker):
    wk.record("回归队伍...")
    if wk.find_pic_click(*RECT_FULL, "队长旗.bmp"):
        lib.msleep(1000)


# 申请入队
def request_join_team(wk: Worker):
    for i in range(5):
        open_around_list(wk)
        idx_pos_list = wk.find_pic_ex(*RECT_AROUND_LIST, "加入.bmp")
        if not idx_pos_list:
            return
        wk.record("申请入队...") if i == 0 else ...
        for idx_pos in idx_pos_list:
            idx, x, y = idx_pos
            wk.move_click(x, y)
            lib.msleep(50, 200)
        scroll_x, scroll_y = POS_AROUND_SCROLL
        wk.move_wheel_down(scroll_x + rnd(-5, 5), scroll_y + rnd(-2, 2), rnd(5, 8))
        lib.msleep(300)


# 鱼批量换积分
def fish_batch_exchange_score(wk: Worker):
    if wk.find_str_click(*RECT_TALK_CONTENT_BIG, "批量兑换", COLOR_TALK_ITEM, sim=0.85, zk=ZK_TALK):
        lib.msleep(1200, 1500)
        # 全部选中
        wk.move_click(POS_GOODS_SEL_LBTN[0] + rnd(-5, 5), POS_GOODS_SEL_LBTN[1] + rnd(-2, 2), False)
        lib.msleep(500, 600)
        # 确定
        wk.move_click(POS_GOODS_SEL_RBTN[0] + rnd(-5, 5), POS_GOODS_SEL_RBTN[1] + rnd(-2, 2))
        lib.msleep(500, 600)
    elif wk.find_str_click(*RECT_TALK_CONTENT_BIG, "换家园积分", COLOR_TALK_ITEM, sim=0.85, zk=ZK_TALK):
        lib.msleep(1200, 1500)
        # 全部选中
        wk.move_click(POS_GOODS_SEL_LBTN[0] + rnd(-5, 5), POS_GOODS_SEL_LBTN[1] + rnd(-2, 2), False)
        lib.msleep(500, 600)
        # 确定
        wk.move_click(POS_GOODS_SEL_RBTN[0] + rnd(-5, 5), POS_GOODS_SEL_RBTN[1] + rnd(-2, 2))
        lib.msleep(500, 600)


# 是否装备界面打开
def is_zhuang_bei_ui_open(wk: Worker, t=0):
    if wk.find_pic(*RECT_FULL, "界_装备.bmp|界_装备2.bmp", timeout=t):
        return True
    return False


# 打开装备界面
def open_zhuang_bei_ui(wk: Worker):
    close_talk(wk)
    for i in range(3):
        if is_zhuang_bei_ui_open(wk):
            break
        else:
            wk.key_press_combo(VK_ALT, VK_N)
            # wk.move_click(POS_UI_ZB[0] + rnd(0, 10), POS_UI_ZB[1] + rnd(0, 10))
        lib.msleep(500)


# 获取当前任务设定次数
def get_cur_task_specify_count(wk: Worker):
    count = lib.task_count_dict.get(wk.cur_task)
    if count is None:
        return 0
    return count


# 任务Npc寻路
def task_npc_find_way(wk: Worker):
    if is_chuan_song_fu_ui_open(wk):  # 若传送符界面已开, 则先关掉, 否则会走不动
        close_all_sub_wnd(wk)
    close_talk(wk)
    close_map(wk)
    close_mail(wk)
    x, y = get_cur_task_pos(wk, 300)
    if x < 0:
        set_task_to_cur_task_bar(wk)
        x, y = get_cur_task_pos(wk, 300)
        if x < 0:
            return False
    for i in range(3):
        if wk.cur_task == "[任务链]":
            x, y = wk.get_pic_pos(x, y, x + 190, y + 85, "寻路颜色条.bmp")
        else:
            x, y = wk.get_pic_pos(x, y, x + 190, y + 41, "寻路颜色条.bmp")
        if x < 0:
            return False
        wk.move_click(x + rnd(5, 10), y - rnd(1, 5))
        lib.msleep(400, 1000)
        if wk.is_find_way or wk.find_pic(*RECT_FULL, "自动寻路中.bmp"):
            wk.record("自动寻路中...")
            return True
        if is_talk_open(wk):
            return True
    return False


# 捡天降宝箱
def pick_tj_box(wk: Worker):
    if wk.find_pic_r_click(*RECT_FULL, "赐福宝箱2.bmp"):
        return True
    x, y = wk.get_pic_pos(*RECT_FULL, "赐福宝箱.bmp")
    if x > 0:
        wk.move_r_click(x + 30, y - 30, False)
        return True
    return False


# 捡修炼宝箱
def pick_xl_box(wk: Worker):
    if wk.find_pic_r_click(*RECT_FULL, "修炼宝箱2.bmp"):
        return True
    x, y = wk.get_pic_pos(*RECT_FULL, "修炼宝箱.bmp")
    if x > 0:
        wk.move_r_click(x + 30, y - 30, False)
        return True
    return False


# 更新修炼宝箱次数
def update_xl_box_count(wk: Worker):
    lib.msleep(800)
    if wk.find_pic(*RECT_FULL, "确橙1.bmp|确橙2.bmp", timeout=300):
        wk.record("已打开宝箱")
        wk.key_press(VK_ESC)
        wk.done_count += 1
        wk.record(f"已完成: {wk.done_count}/10")


def goto_next_map_have_welcome_npc(wk: Worker, src_map: str, now_map: str, npc_name: str):  # 有接引人, 返回最终到达的地图
    x, y = WELCOME_NPC[npc_name]
    pic = f"周围_{npc_name}.bmp"
    while now_map == src_map:  # 若地图未切换
        if not click_talk_specify_item(wk, "送我过去吧|进入上古战场", 500):
            if is_fight(wk):
                fight_operation(wk)
            if wk.cur_task == "[运镖]" and not is_task_on_cur_task_bar(wk):  # 判断运镖任务是否在任务栏
                break
            elif wk.cur_task == "[修炼宝箱]" and pick_xl_box(wk):  # 顺路捡宝箱
                update_xl_box_count(wk)
            if not wk.is_find_way:
                click_map_wnd_pos(wk, x, y)
            around_list_click_npc(wk, pic)
        lib.msleep(900)
        now_map = cur_map(wk)
    close_around_list(wk)
    return now_map


def goto_next_map_without_welcome_npc(wk: Worker, src_map: str, now_map: str, x: int, y: int):  # 无接引人, 返回最终到达的地图
    while now_map == src_map:  # 若地图未切换
        if not wk.is_find_way:
            click_map_wnd_pos(wk, x, y)
        if is_fight(wk):
            fight_operation(wk)
        if wk.cur_task == "[运镖]" and not is_task_on_cur_task_bar(wk):  # 判断运镖任务是否在任务栏
            break
        elif wk.cur_task == "[修炼宝箱]" and pick_xl_box(wk):  # 顺路捡宝箱
            update_xl_box_count(wk)
        lib.msleep(900)
        now_map = cur_map(wk)
    close_map(wk)
    return now_map


# 去下一地图
def goto_next_map(wk: Worker, src_map: str, dst_map: str):
    now_map = cur_map(wk)
    # 若 当前地图 != 开始地图 多等一会, 或 当前地图 == 目标地图
    if now_map != src_map or now_map == dst_map:
        return True
    path = f"{src_map}-{dst_map}"  # 长安城-长安城外
    try:
        pos = PATH_POS[path]
    except:
        wk.record(f"路径不存在:{path}")
        return False
    wk.is_find_way = False  # 至少寻路一次
    if pos[0] == -1:  # 有接引人
        reach_map = goto_next_map_have_welcome_npc(wk, src_map, now_map, pos[1])
    else:
        reach_map = goto_next_map_without_welcome_npc(wk, src_map, now_map, pos[0], pos[1])
    if reach_map == dst_map:
        wk.record(f"抵达 {reach_map}")
        return True
    return False


# 飞到npc处
def fly_to_npc(wk: Worker, map_name: str, npc_name: str):
    wk.record(f"飞到 {map_name} {npc_name}")
    if map_name == "长安城":
        if npc_name in {"柳乘风", "包夫人", "李员外"}:
            use_fei_xing_qi(wk, "长安城", FLAG_RECT["柳乘风"])
        elif npc_name in {"吴朴智", "如意"}:
            use_fei_xing_qi(wk, "长安城", FLAG_RECT["吴朴智"])
        elif npc_name in {"钱夫人", "雪瑶", "凤瑶"}:
            use_fei_xing_qi(wk, "长安城", FLAG_RECT["钱夫人"])
        elif npc_name in {"如花", "百合", "郑妈妈"}:
            use_fei_xing_qi(wk, "长安城", FLAG_RECT["金悦院"])
        elif npc_name == "周大婶":
            use_fei_xing_qi(wk, "长安城", FLAG_RECT["交易中心"])
        elif npc_name == "李将军":
            use_fei_xing_qi(wk, "长安城", FLAG_RECT["金銮殿"])
        else:
            fly_to_map(wk, map_name)
    elif map_name == "傲来国":
        if npc_name == "神秘人":
            use_fei_xing_qi(wk, "傲来国", FLAG_RECT["天魔里"])
        else:
            fly_to_map(wk, map_name)
    elif map_name == "青河镇":
        if npc_name in {"村长", "小石头", "周夫人"}:
            use_fei_xing_qi(wk, "青河镇", FLAG_RECT["青河村长"])
        else:
            fly_to_map(wk, map_name)
    else:
        fly_to_map(wk, map_name)


# 飞图
def fly_to_map(wk: Worker, map_name: str):
    if cur_map(wk) == map_name or map_name == "":
        return True
    if map_name in ("长安城", "傲来国", "青河镇", "临仙镇", "女儿国"):
        use_chuan_song_fu(wk, map_name)
    else:
        switch = {
            "长安城外": lambda: {
                use_fei_xing_qi(wk, "长安城", FLAG_RECT["长安城外"]),
                goto_next_map(wk, "长安城", "长安城外")
            },
            "大唐国境": lambda: {
                use_fei_xing_qi(wk, "长安城", FLAG_RECT["长安驿站"]),
                goto_next_map(wk, "长安城", "大唐国境")
            },
            "青河镇外": lambda: {
                fly_to_map(wk, "傲来国"),
                goto_next_map(wk, "傲来国", "青河镇外")
            },
            "青河村长家": lambda: {
                use_fei_xing_qi(wk, "青河镇", FLAG_RECT["青河村长"]),
                goto_next_map(wk, "青河镇", "青河村长家")
            },
            "神秘洞窟": lambda: {
                fly_to_map(wk, "青河镇外"),
                goto_next_map(wk, "青河镇外", "神秘洞窟")
            },
            "东海龙宫": lambda: {
                fly_to_map(wk, "青河镇外"),
                goto_next_map(wk, "青河镇外", "东海龙宫")
            },
            "水晶宫": lambda: {
                fly_to_map(wk, "东海龙宫"),
                goto_next_map(wk, "东海龙宫", "水晶宫")
            },
            "天魔里": lambda: {
                fly_to_map(wk, "傲来国"),
                goto_next_map(wk, "傲来国", "天魔里")
            },
            "云隐阁": lambda: {
                fly_to_map(wk, "天魔里"),
                goto_next_map(wk, "天魔里", "云隐阁")
            },
            "天策": lambda: {
                use_fei_xing_qi(wk, "长安城", FLAG_RECT["天策"]),
                goto_next_map(wk, "长安城", "天策")
            },
            "程府": lambda: {
                fly_to_map(wk, "天策"),
                goto_next_map(wk, "天策", "程府")
            },
            "佛门": lambda: {
                use_fei_xing_qi(wk, "长安城", FLAG_RECT["佛门"]),
                goto_next_map(wk, "长安城", "佛门")
            },
            "大雄宝殿": lambda: {
                fly_to_map(wk, "佛门"),
                goto_next_map(wk, "佛门", "大雄宝殿")
            },
            "金銮殿": lambda: {
                use_fei_xing_qi(wk, "长安城", FLAG_RECT["金銮殿"]),
                goto_next_map(wk, "长安城", "金銮殿")
            },
            "金悦院": lambda: {
                use_fei_xing_qi(wk, "长安城", FLAG_RECT["金悦院"]),
                goto_next_map(wk, "长安城", "金悦院")
            },
            "南海普陀": lambda: {
                fly_to_map(wk, "大唐国境"),
                goto_next_map(wk, "大唐国境", "南海普陀")
            },
            "大唐境外": lambda: {
                use_fei_xing_qi(wk, "女儿国", FLAG_RECT["大唐境外"]),
                goto_next_map(wk, "女儿国", "大唐境外")
            },
            "无名谷": lambda: {
                fly_to_map(wk, "大唐境外"),
                goto_next_map(wk, "大唐境外", "无名谷")
            },
            "盘丝岭": lambda: {
                fly_to_map(wk, "大唐境外"),
                goto_next_map(wk, "大唐境外", "盘丝岭")
            },
            "盘丝洞": lambda: {
                fly_to_map(wk, "盘丝岭"),
                goto_next_map(wk, "盘丝岭", "盘丝洞")
            },
            "幽冥地府": lambda: {
                fly_to_map(wk, "大唐境外"),
                goto_next_map(wk, "大唐境外", "幽冥地府")
            },
            "森罗殿": lambda: {
                fly_to_map(wk, "幽冥地府"),
                goto_next_map(wk, "幽冥地府", "森罗殿")
            },
            "乌斯藏": lambda: {
                use_fei_xing_qi(wk, "临仙镇", FLAG_RECT["乌斯藏"]),
                goto_next_map(wk, "临仙镇", "乌斯藏")
            },
            "魔王山": lambda: {
                fly_to_map(wk, "乌斯藏"),
                goto_next_map(wk, "乌斯藏", "魔王山")
            },
            "镇元五庄": lambda: {
                fly_to_map(wk, "乌斯藏"),
                goto_next_map(wk, "乌斯藏", "镇元五庄")
            },
            "乾坤殿": lambda: {
                fly_to_map(wk, "镇元五庄"),
                goto_next_map(wk, "镇元五庄", "乾坤殿")
            },
            "万兽岭": lambda: {
                fly_to_map(wk, "乌斯藏"),
                goto_next_map(wk, "乌斯藏", "万兽岭")
            },
            "狮王洞": lambda: {
                fly_to_map(wk, "万兽岭"),
                goto_next_map(wk, "万兽岭", "狮王洞")
            },
            "平顶山": lambda: {
                fly_to_map(wk, "万兽岭"),
                goto_next_map(wk, "万兽岭", "平顶山")
            },
            "七星方寸": lambda: {
                use_fei_xing_qi(wk, "临仙镇", FLAG_RECT["七星方寸"]),
                goto_next_map(wk, "临仙镇", "七星方寸")
            },
            "灵台宫": lambda: {
                fly_to_map(wk, "七星方寸"),
                goto_next_map(wk, "七星方寸", "灵台宫")
            },
            "昆仑山": lambda: {
                use_fei_xing_qi(wk, "临仙镇", FLAG_RECT["昆仑山"]),
                goto_next_map(wk, "临仙镇", "昆仑山")
            },
            "北冥": lambda: {
                fly_to_map(wk, "昆仑山"),
                goto_next_map(wk, "昆仑山", "北冥")
            },
            "凌霄天宫": lambda: {
                fly_to_map(wk, "昆仑山"),
                goto_next_map(wk, "昆仑山", "凌霄天宫")
            },
            "凌霄殿": lambda: {
                fly_to_map(wk, "凌霄天宫"),
                goto_next_map(wk, "凌霄天宫", "凌霄殿")
            },
            "花果山": lambda: {
                fly_to_map(wk, "傲来国"),
                goto_next_map(wk, "傲来国", "花果山")
            },
            "大雁塔一层": lambda: {
                use_fei_xing_qi(wk, "长安城", FLAG_RECT["大雁塔"]),
                goto_next_map(wk, "长安城", "大雁塔一层")
            },
            "大雁塔二层": lambda: {
                fly_to_map(wk, "大雁塔一层"),
                goto_next_map(wk, "大雁塔一层", "大雁塔二层")
            },
            "大雁塔三层": lambda: {
                fly_to_map(wk, "大雁塔二层"),
                goto_next_map(wk, "大雁塔二层", "大雁塔三层")
            },
            "大雁塔四层": lambda: {
                fly_to_map(wk, "大雁塔三层"),
                goto_next_map(wk, "大雁塔三层", "大雁塔四层")
            },
            "大雁塔五层": lambda: {
                fly_to_map(wk, "大雁塔四层"),
                goto_next_map(wk, "大雁塔四层", "大雁塔五层")
            },
            "大雁塔六层": lambda: {
                fly_to_map(wk, "大雁塔五层"),
                goto_next_map(wk, "大雁塔五层", "大雁塔六层")
            },
            "东海迷宫一层": lambda: {
                fly_to_map(wk, "东海龙宫"),
                goto_next_map(wk, "东海龙宫", "东海迷宫一层")
            },
            "东海迷宫二层": lambda: {
                fly_to_map(wk, "东海迷宫一层"),
                goto_next_map(wk, "东海迷宫一层", "东海迷宫二层")
            },
            "东海迷宫三层": lambda: {
                fly_to_map(wk, "东海迷宫二层"),
                goto_next_map(wk, "东海迷宫二层", "东海迷宫三层")
            },
            "地狱迷宫一层": lambda: {
                fly_to_map(wk, "幽冥地府"),
                goto_next_map(wk, "幽冥地府", "地狱迷宫一层")
            },
            "地狱迷宫二层": lambda: {
                fly_to_map(wk, "地狱迷宫一层"),
                goto_next_map(wk, "地狱迷宫一层", "地狱迷宫二层")
            },
            "地狱迷宫三层": lambda: {
                fly_to_map(wk, "地狱迷宫二层"),
                goto_next_map(wk, "地狱迷宫二层", "地狱迷宫三层")
            },
            "琉璃多宝塔一层": lambda: {
                fly_to_map(wk, "北冥"),
                goto_next_map(wk, "北冥", "琉璃多宝塔一层")
            },
            "琉璃多宝塔二层": lambda: {
                fly_to_map(wk, "琉璃多宝塔一层"),
                goto_next_map(wk, "琉璃多宝塔一层", "琉璃多宝塔二层")
            },
            "琉璃多宝塔三层": lambda: {
                fly_to_map(wk, "琉璃多宝塔二层"),
                goto_next_map(wk, "琉璃多宝塔二层", "琉璃多宝塔三层")
            },
            "寒冰宫一层": lambda: {
                fly_to_map(wk, "大唐境外"),
                goto_next_map(wk, "大唐境外", "寒冰宫一层")
            },
            "寒冰宫二层": lambda: {
                fly_to_map(wk, "寒冰宫一层"),
                goto_next_map(wk, "寒冰宫一层", "寒冰宫二层")
            },
            "寒冰宫三层": lambda: {
                fly_to_map(wk, "寒冰宫二层"),
                goto_next_map(wk, "寒冰宫二层", "寒冰宫三层")
            },
            "水帘洞": lambda: {
                fly_to_map(wk, "花果山"),
                goto_next_map(wk, "花果山", "水帘洞")
            },
            "神弃平原": lambda: {
                fly_to_map(wk, "水帘洞"),
                goto_next_map(wk, "水帘洞", "神弃平原")
            },
            "东海幻境": lambda: {
                fly_to_map(wk, "东海龙宫"),
                goto_next_map(wk, "东海龙宫", "东海幻境")
            },
            "广寒宫": lambda: {
                fly_to_map(wk, "凌霄天宫"),
                goto_next_map(wk, "凌霄天宫", "广寒宫")
            },
            "子母河畔": lambda: {
                fly_to_map(wk, "女儿国"),
                goto_next_map(wk, "女儿国", "子母河畔")
            },
            "桃花岛": lambda: {
                fly_to_map(wk, "子母河畔"),
                goto_next_map(wk, "子母河畔", "桃花岛")
            },
            "上古战场": lambda: {
                fly_to_map(wk, "昆仑山"),
                goto_next_map(wk, "昆仑山", "上古战场")
            },
            "长安当铺": lambda: {
                use_fei_xing_qi(wk, "长安城", FLAG_RECT["长安药店"]),
                goto_next_map(wk, "长安城", "长安当铺")
            },
            "长安药店": lambda: {
                use_fei_xing_qi(wk, "长安城", FLAG_RECT["长安药店"]),
                goto_next_map(wk, "长安城", "长安药店")
            },
            "长安服饰店": lambda: {
                use_fei_xing_qi(wk, "长安城", FLAG_RECT["长安药店"]),
                goto_next_map(wk, "长安城", "长安服饰店")
            },
            "长安杂货店": lambda: {
                use_fei_xing_qi(wk, "长安城", FLAG_RECT["长安药店"]),
                goto_next_map(wk, "长安城", "长安杂货店")
            },
            "长安武器店": lambda: {
                use_fei_xing_qi(wk, "长安城", FLAG_RECT["长安药店"]),
                goto_next_map(wk, "长安城", "长安武器店")
            },
            "傲来服饰店": lambda: {
                fly_to_map(wk, "傲来国"),
                goto_next_map(wk, "傲来国", "傲来服饰店")
            },
            "傲来武器店": lambda: {
                fly_to_map(wk, "傲来国"),
                goto_next_map(wk, "傲来国", "傲来武器店")
            },
            "青河服饰店": lambda: {
                fly_to_map(wk, "青河镇"),
                goto_next_map(wk, "青河镇", "青河服饰店")
            },
            "青河武器店": lambda: {
                fly_to_map(wk, "青河镇"),
                goto_next_map(wk, "青河镇", "青河武器店")
            },
            "临仙服饰店": lambda: {
                fly_to_map(wk, "临仙镇"),
                goto_next_map(wk, "临仙镇", "临仙服饰店")
            },
            "临仙武器店": lambda: {
                fly_to_map(wk, "临仙镇"),
                goto_next_map(wk, "临仙镇", "临仙武器店")
            }
        }
        func = switch.get(map_name)
        if func:
            func()
    for i in range(4):
        if cur_map(wk) == map_name:
            return True
        lib.msleep(600)
    return False


# 右下角使用
def right_down_use(wk: Worker):
    wk.find_pic_click(*RECT_RIGHT_DOWN, "右下角使用.bmp")


# 右下角快捷操作
def right_down_quick_operation(wk: Worker):
    # 右下角回门派
    wk.find_pic_click(*RECT_RIGHT_DOWN, "右下角回门派.bmp|右下角回门派2.bmp")
    # 右下角领双
    if lib.cfg_main["跟随队长领双"]:
        wk.find_pic_click(*RECT_RIGHT_DOWN, "右下角领双.bmp")
    # 右下角使用
    if wk.find_pic(*RECT_RIGHT_DOWN, "右下角驱魔香.bmp"):
        if lib.cfg_main["自动购买驱魔香"] and wk.cur_task != "[打野]":
            right_down_use(wk)
        else:
            wk.find_pic_click(*RECT_RIGHT_DOWN, "界_关闭1.bmp|界_关闭2.bmp|界_关闭3.bmp|界_关闭4.bmp")
    else:
        right_down_use(wk)
    # 右下角活动追踪
    wk.find_pic_click(*RECT_RIGHT_DOWN, "隐藏活动追踪.bmp")


# 获取角色门派
def get_role_school(wk: Worker):
    if wk.school != "":
        return
    pic_name = wk.get_pic_name(*RECT_QUICK_BAR, "技_东海龙宫.bmp|技_天魔里.bmp|技_佛门.bmp|技_天策.bmp|技_南海普陀.bmp|"
                                                "技_盘丝岭.bmp|技_幽冥地府.bmp|技_无名谷.bmp|技_魔王山.bmp|技_镇元五庄.bmp|"
                                                "技_七星方寸.bmp|技_万兽岭.bmp|技_凌霄天宫.bmp")
    wk.school = pic_name.lstrip("技_") if pic_name != "" else ""
    wk.write_tbe_console(lib.COL_SCHOOL, wk.school)


# 开宝箱
def open_treasure_box(wk: Worker):
    if not wk.find_pic(*RECT_FULL, "选择一个宝箱.bmp"):
        return
    which = lib.cfg_main["开宝箱"]
    if which == "左":
        wk.move_click(X_TREASURE_BOX_LEFT + rnd(-5, 5), Y_TREASURE_BOX + rnd(-5, 5))
    elif which == "中":
        wk.move_click(X_TREASURE_BOX_CENTER + rnd(-5, 5), Y_TREASURE_BOX + rnd(-5, 5))
    else:
        wk.move_click(X_TREASURE_BOX_RIGHT + rnd(-5, 5), Y_TREASURE_BOX + rnd(-5, 5))
    wk.record("已打开 宝箱")
    lib.msleep(500)
    if wk.find_pic_click(*RECT_FULL, "宝箱.bmp"):
        wk.record("已随机打开 宝箱")
    # 关闭宝箱框
    wk.find_pic_click(*RECT_FULL, "界_关闭1.bmp|界_关闭2.bmp|界_关闭3.bmp|界_关闭4.bmp", order=ORDER_RLUD)


# 点继续游戏
def click_continue_game(wk: Worker):
    for i in range(5):
        if not wk.find_pic(*RECT_FULL, "继续游戏.bmp|继续游戏2.bmp|继续游戏3.bmp"):
            break
        wk.key_press(VK_ESC)
        lib.msleep(300)


# 关闭任务描述框
def close_describe_box(wk: Worker):
    if rnd(1, 60) == 10:  # 只有1/60的概率去关闭任务描述框
        if wk.find_pic_r_click(*RECT_RIGHT, "描述框1.bmp|描述框2.bmp", delta_color="000000", sim=1.0):
            wk.record("发现 描述框, 已自动关闭")


# 排队回原服
def queue_back_server(wk: Worker):
    if not lib.cfg_main["自动排队回到原服"]:
        return
    if wk.find_pic_click(*RECT_QUQUE_BACK, "排队回到原服.bmp"):
        wk.record("已点击排队回原服, 等待中...")
        wk.mutex.lock()  # 挂起执行线程
        lib.msleep(8000)
        wk.record("排队回原服完成")
        wk.mutex.unlock()


# 掷骰子
def throw_dice(wk: Worker):
    if wk.find_pic_click(*RECT_FULL, "骰子1.bmp|骰子2.bmp"):
        wk.record("已自动掷骰子")
        lib.msleep(500)
    if wk.find_pic(*RECT_FULL, "骰子3.bmp"):
        wk.key_press(VK_ESC)


# 关闭小昕提示
def close_xiao_xin_tip(wk: Worker):
    wk.find_pic_click(*RECT_RIGHT_DOWN, "右下角领双.bmp")
    if wk.find_pic_click(*RECT_FULL, "我不需要.bmp|我知道.bmp|小昕提示.bmp|大昕提示.bmp|大昕提示2.bmp"):
        wk.record("发现小昕提示,已自动关闭")
    x, y = wk.get_pic_pos(*RECT_FULL, "大昕提示3.bmp")
    if x > 0:
        wk.move_click(x - rnd(50, 60), y + rnd(10, 20))


# 关闭弹窗
def close_popup_wnd(wk: Worker):
    if wk.find_pic_click(*RECT_FULL, "恭喜获得关闭.bmp"):
        wk.record("发现[恭喜获得],已点击关闭")
    if wk.cur_task in ("[修炼宝箱]", "[天降宝箱]"):
        click_cancel(wk)  # 点击取消


# 检测在线状态
def check_online_state(wk: Worker):
    if wk.find_pic_click(*RECT_TIP_CENTER, "重新登录.bmp|重新登录2.bmp"):
        wk.record("检测到游戏掉线, 自动暂停执行, 请重新登录...")
        wk.write_tbe_console(lib.COL_PAUSE, lib.SELECTED)


# 检测剧情
def check_ju_qing(wk: Worker):
    if wk.cur_task != "[剧情]":
        return
    # 等级礼包
    if wk.find_pic_click(*RECT_RIGHT_DOWN, "右下角领取.bmp"):
        lib.msleep(300)
        wk.find_pic_click(*RECT_FULL, "领取奖励.bmp", 300)
    # 关闭奖励中心
    if wk.find_pic(*RECT_FULL, "界_奖励中心.bmp"):
        wk.key_press(VK_ESC)
        lib.msleep(300)
    # 关闭属性点提示
    if wk.find_pic_click(*RECT_BUFF, "属性点提示.bmp"):
        wk.record("发现属性点提示, 已自动关闭")


# -------------------------------- 过游戏检测 ---------------------------------------
def auth_type(wk: Worker):
    if wk.find_pic(*RECT_FULL, "检测_拼图框.bmp"):
        return "拼图"
    if wk.find_pic(*RECT_FULL, "检测_滑块框.bmp"):
        return "滑块"
    if wk.find_pic(*RECT_AUTH_LONG_TITLE, "检测_旋转框.bmp"):
        return "旋转长"
    if wk.find_pic(*RECT_AUTH_SQUA_TITLE, "检测_旋转框.bmp"):
        return "旋转方"
    if wk.find_pic(*RECT_AUTH_LONG_TITLE, "检测_清晰框.bmp"):
        return "清晰长"
    if wk.find_pic(*RECT_AUTH_SQUA_TITLE, "检测_清晰框.bmp"):
        return "清晰方"
    if wk.find_pic(*RECT_FULL, "检测_换位框.bmp"):
        return "换位"
    if wk.find_pic(*RECT_FULL, "检测_成语框.bmp"):
        return "成语"
    if wk.find_pic(*RECT_FULL, "检测_语序框.bmp"):
        return "语序"
    if wk.find_pic(*RECT_FULL, "检测_时.bmp|检测_分.bmp|检测_秒.bmp"):
        return "时钟"
    if wk.find_pic(*RECT_FULL, "检测_力度框.bmp"):
        return "力度"
    if wk.find_pic(*RECT_FULL, "检测_方块框.bmp"):
        return "方块"
    return "无"


# 过所有检测
def pass_all_auth(wk: Worker):
    tp = auth_type(wk)
    if tp == "无":
        return

    wk.is_find_way = False
    wk.mutex.lock()  # 挂起执行线程
    func_dict = {
        "拼图": pass_pin_tu, "旋转长": pass_rotate_long, "旋转方": pass_rotate_squa,
        "清晰长": pass_clear_long, "清晰方": pass_clear_squa, "换位": pass_huan_wei,
        "力度": pass_li_du, "方块": pass_fang_kuai,
        # 需要换绑定
        "滑块": pass_slider, "时钟": pass_clock, "成语": pass_cy_yx, "语序": pass_cy_yx,
    }
    pass_func = func_dict[tp]
    pass_func(wk)
    wk.mutex.unlock()

    lib.msleep(800)
    if auth_type(wk) != "无":  # 再判断一次检测类型
        wk.record("过检测失败")
        return
    wk.record("检测已过")
    wk.last_word = ""
    wk.last_idx = -1


# 过拼图
def pass_pin_tu(wk: Worker):
    wk.record("出现 拼图")
    pic_pt = wk.match_pic("*.bmp", lib.DIR_PT)
    pic_name = wk.get_pic_name(*RECT_AUTH_PT_Q, pic_pt, dir=lib.DIR_PT, delta_color="151515", sim=0.85,
                               timeout=300)  # "雪精灵2"
    if pic_name == "":
        wk.record("未识别出该拼图序号")
        wk.move_click(321 + rnd(0, 5), 321 + rnd(0, 5))  # 点选项A
        return
    name = pic_name.rstrip("1|2|3|4")  # "雪精灵"
    # "pt\\雪精灵1.bmp|pt\\雪精灵2.bmp|pt\\雪精灵3.bmp|pt\\雪精灵4.bmp"
    names = f"pt\\{name}1.bmp|pt\\{name}2.bmp|pt\\{name}3.bmp|pt\\{name}4.bmp"
    if not wk.find_pic_click(*RECT_AUTH_PT_A, names, delta_color="151515", sim=0.90):
        wk.record("在拼图选项中未找到指定图片")
        wk.move_click(321 + rnd(0, 5), 321 + rnd(0, 5))  # 点选项A


# 点击刷新验证
def click_refresh_auth(wk: Worker):
    wk.move_click(POS_AUTH_REFRESH[0] + rnd(-3, 3), POS_AUTH_REFRESH[1] + rnd(-3, 3))


# 旋转获取正确索引
def rotate_get_true_idx(keyword: str, all_pic_ocr_list: str):
    if not keyword:
        return -1
    # all_pic_ocr_list = ["m0w2m0w3", "m1w2m7w4", "m2w3m6w5", ...]
    # 整理成["m0m1m2m3m4m5", "w2w2w3w3w4w4", "m0m7m6m5m4m3", "w3w4w5w6w7w0"]
    sex_speed_list = ["", "", "", ""]
    for pic_ocr_ret in all_pic_ocr_list:
        # pic_ocr_ret = "m0w2m0w3"
        sex_speed_list[0] += pic_ocr_ret[0:2]
        sex_speed_list[1] += pic_ocr_ret[2:4]
        sex_speed_list[2] += pic_ocr_ret[4:6]
        sex_speed_list[3] += pic_ocr_ret[6:8]
    # 整理成[("m", 5), ("w", 3), ("m", -5), ("w", 5)]
    for i in range(4):
        sex_str = sex_speed_list[i][0::2]  # "mmmmmm"
        dire_str = sex_speed_list[i][1::2]  # "012345"  或  "345670"
        sex = "m" if sex_str.count("m") >= 3 else "w"
        last_dire = dire_str[0]
        speed = 0
        for cur_dire in dire_str:
            if cur_dire == last_dire:
                continue
            if (last_dire, cur_dire) == ("7", "0"):
                speed += 1  # 逆为正数
            elif (last_dire, cur_dire) == ("0", "7"):
                speed -= 1  # 顺为负数
            else:
                if last_dire < cur_dire:
                    speed += 1  # 逆为正数
                else:
                    speed -= 1  # 顺为负数
            last_dire = cur_dire
        sex_speed_list[i] = (sex, speed)
    # 开始排除答案
    m_speed = 0 if "快" in keyword else 6  # 最大速度 或 最小速度
    m_idx = -1  # 最快或最慢对应的人物索引
    ret_idx = -1  # 最终返回的索引
    candidate_list = [0, 1, 2, 3]  # 候选列表
    for i, (sex, speed) in enumerate(sex_speed_list):
        # 排除 性别不符
        if (sex == "w" and "男" in keyword) or (sex == "m" and "女" in keyword):
            candidate_list.remove(i)
            continue
        # 排除 顺逆不符
        if (speed < 0 and "逆" in keyword) or (speed > 0 and "顺" in keyword):
            candidate_list.remove(i)
            continue
        # 排除 快慢不符
        if "快" in keyword:
            if abs(speed) > abs(m_speed):
                if m_idx != -1:
                    candidate_list.remove(m_idx)  # 移除之前最快的
                m_speed = speed
                m_idx = i
            else:
                candidate_list.remove(i)
        elif "慢" in keyword:
            if abs(speed) < abs(m_speed):
                if m_idx != -1:
                    candidate_list.remove(m_idx)  # 移除之前最慢的
                m_speed = speed
                m_idx = i
            else:
                candidate_list.remove(i)
    if candidate_list:
        ret_idx = candidate_list[0]
    return ret_idx


# 过旋转长
def pass_rotate_long(wk: Worker):
    wk.key_press(VK_ESC)  # 关闭可能阻塞的窗口
    keyword = wk.ocr(*RECT_AUTH_LONG_TITLE, COLOR_AUTH_ROTATE_KEYWORD, sim=0.8, zk=ZK_AUTH_OTHER)
    wk.record(f"正在过旋转验证(长型), 关键词:{keyword}")
    idx = wk.last_idx
    if keyword != wk.last_word or idx == -1:
        lib.msleep(1000)  # 等待浮动提示消失
        for i in range(NUM_ROTATE_FRAME):  # 连续截图
            wk.capture(*RECT_AUTH_LONG_ITEM, f"{lib.DIR_TEMP}\\xzc_{wk.row}-{i}.bmp")
            lib.msleep(60)
        tr = create_dispatch_obj(wk, lib.COM_NAME_TR)
        tr.Lib_Load(f"{lib.DIR_DLL}\\rtt.lib")
        all_pic_ocr_list = []
        for i in range(NUM_ROTATE_FRAME):  # 逐个识别
            tr.Pixel_FromPicture(f"{lib.DIR_TEMP}\\xzc_{wk.row}-{i}.bmp")
            tr.Filter_Binaryzation("0-80")
            tr.Incise_ScopeAisle(6, 6, "20-110", "40-160", 0)
            ocr_ret = tr.ocr()
            # wk.record(f"第{i}张, 识别结果:{ocr_ret}")
            if len(ocr_ret) != 8:
                break
            all_pic_ocr_list.append(ocr_ret)
        else:
            idx = rotate_get_true_idx(keyword, all_pic_ocr_list)
    if idx == -1:  # 答案无效
        # for i in range(NUM_ROTATE_FRAME):  # 重命名这几张截图,方便后续更新字库
        #     lib.file_rename(lib.DIR_TEMP, f"xzc_{wk.row}-{i}.bmp", f"xzc_{lib.cur_time_stamp}-{i}.bmp")
        wk.record("答案不确定, 将随机选择")
        idx = rnd(0, 3)
    else:  # 答案有效,记录下来
        wk.last_word = keyword
        wk.last_idx = idx
    # 根据 答案索引 计算 应点击的坐标
    idx_pos_list = [(215, 340), (342, 340), (467, 340), (596, 340)]
    x, y = idx_pos_list[idx]
    wk.record(f"关键词:{keyword}, 答案:{x, y}")
    close_talk(wk)
    wk.move_click(x + rnd(-3, 3), y + rnd(-5, 5))


# 过旋转方
def pass_rotate_squa(wk: Worker):
    wk.key_press(VK_ESC)  # 关闭可能阻塞的窗口
    keyword = wk.ocr(*RECT_AUTH_SQUA_TITLE, COLOR_AUTH_ROTATE_KEYWORD, sim=0.8, zk=ZK_AUTH_OTHER)
    wk.record(f"正在过旋转验证(方型), 关键词:{keyword}")
    idx = wk.last_idx
    if keyword != wk.last_word or idx == -1:
        lib.msleep(1000)  # 等待浮动提示消失
        for i in range(NUM_ROTATE_FRAME):  # 连续截图
            wk.capture(*RECT_AUTH_SQUA_ITEM, f"{lib.DIR_TEMP}\\xzf_{wk.row}-{i}.bmp")
            lib.msleep(60)
        tr = create_dispatch_obj(wk, lib.COM_NAME_TR)
        tr.Lib_Load(f"{lib.DIR_DLL}\\rtt.lib")
        all_pic_ocr_list = []
        for i in range(NUM_ROTATE_FRAME):  # 逐个识别
            tr.Pixel_FromPicture(f"{lib.DIR_TEMP}\\xzf_{wk.row}-{i}.bmp")
            tr.Filter_Binaryzation("0-80")
            tr.Incise_ScopeAisle(6, 6, "20-110", "40-160", 0)
            ocr_ret = tr.ocr()
            # wk.record(f"第{i}张, 识别结果:{ocr_ret}")
            if len(ocr_ret) != 8:
                break
            all_pic_ocr_list.append(ocr_ret)
        else:
            idx = rotate_get_true_idx(keyword, all_pic_ocr_list)
    if idx == -1:  # 答案无效
        # for i in range(NUM_ROTATE_FRAME):  # 重命名这几张截图,方便后续更新字库
        #     lib.file_rename(lib.DIR_TEMP, f"xzf_{wk.row}-{i}.bmp", f"xzf_{lib.cur_time_stamp}-{i}.bmp")
        wk.record("答案不确定, 将随机选择")
        idx = rnd(0, 3)
    else:  # 答案有效,记录下来
        wk.last_word = keyword
        wk.last_idx = idx
    # 根据 答案索引 计算 应点击的坐标
    idx_pos_list = [(320, 270), (492, 270), (320, 430), (492, 430)]
    x, y = idx_pos_list[idx]
    wk.record(f"关键词:{keyword}, 答案:{x, y}")
    close_talk(wk)
    wk.move_click(x + rnd(-3, 3), y + rnd(-5, 5))


# 清晰获取正确索引
def clear_get_true_idx(wk: Worker, keyword: str):
    var_list = []
    tr = create_dispatch_obj(wk, lib.COM_NAME_TR)
    for i in range(1, 5):
        path_pic = f"{lib.DIR_TEMP}\\qx_{wk.row}-{i}.bmp"
        tr.Pixel_FromPicture(path_pic)
        tr.Filter_Posterization(2)  # 色调分离排除背景色
        v = tr.EvalVariance()
        print(i, v)
        var_list.append(v)
    if keyword == "清晰":  # 找方差最小的
        idx = var_list.index(min(var_list))
    else:  # 最不清晰, 找方差最大的
        idx = var_list.index(max(var_list))
    return idx


# 过清晰长
def pass_clear_long(wk: Worker):
    wk.key_press(VK_ESC)  # 关闭可能阻塞的窗口
    keyword = wk.ocr(*RECT_AUTH_LONG_TITLE, COLOR_AUTH_ROTATE_KEYWORD, sim=0.8, zk=ZK_AUTH_OTHER)
    wk.record(f"正在过清晰验证(长型), 关键词:{keyword}")
    wk.capture(*RECT_AUTH_LONG_CAP1, f"{lib.DIR_TEMP}\\qx_{wk.row}-1.bmp")
    wk.capture(*RECT_AUTH_LONG_CAP2, f"{lib.DIR_TEMP}\\qx_{wk.row}-2.bmp")
    wk.capture(*RECT_AUTH_LONG_CAP3, f"{lib.DIR_TEMP}\\qx_{wk.row}-3.bmp")
    wk.capture(*RECT_AUTH_LONG_CAP4, f"{lib.DIR_TEMP}\\qx_{wk.row}-4.bmp")
    idx = clear_get_true_idx(wk, keyword)
    # 根据 答案索引 计算 应点击的坐标
    idx_pos_list = [(215, 340), (342, 340), (467, 340), (596, 340)]
    x, y = idx_pos_list[idx]
    wk.record(f"关键词:{keyword}, 答案:{x, y}")
    close_talk(wk)
    wk.move_click(x + rnd(-10, 10), y + rnd(-5, 5))


# 过清晰方
def pass_clear_squa(wk: Worker):
    wk.key_press(VK_ESC)  # 关闭可能阻塞的窗口
    keyword = wk.ocr(*RECT_AUTH_SQUA_TITLE, COLOR_AUTH_ROTATE_KEYWORD, sim=0.8, zk=ZK_AUTH_OTHER)
    wk.record(f"正在过清晰验证(方型), 关键词:{keyword}")
    wk.capture(*RECT_AUTH_SQUA_CAP1, f"{lib.DIR_TEMP}\\qx_{wk.row}-1.bmp")
    wk.capture(*RECT_AUTH_SQUA_CAP2, f"{lib.DIR_TEMP}\\qx_{wk.row}-2.bmp")
    wk.capture(*RECT_AUTH_SQUA_CAP3, f"{lib.DIR_TEMP}\\qx_{wk.row}-3.bmp")
    wk.capture(*RECT_AUTH_SQUA_CAP4, f"{lib.DIR_TEMP}\\qx_{wk.row}-4.bmp")
    idx = clear_get_true_idx(wk, keyword)
    # 根据 答案索引 计算 应点击的坐标
    idx_pos_list = [(320, 270), (492, 270), (320, 430), (492, 430)]
    x, y = idx_pos_list[idx]
    wk.record(f"关键词:{keyword}, 答案:{x, y}")
    close_talk(wk)
    wk.move_click(x + rnd(-10, 10), y + rnd(-5, 5))


# 提取边缘像素
def extract_edge_px(tr, path_pic: str):
    # 加载图片, 背景色BBGGRR="9B9B7C" (155, 155, 124)
    tr.Pixel_FromPicture(path_pic)
    # 提取图片的像素到列表中
    px_list = []
    data = tr.GetImageData()[0]
    print(data)
    w, h, img_data = data.split("|")
    w, h = int(w), int(h)
    img_data = img_data.split(",")
    i = 0
    edge_top, edge_bottom = [], []
    edge_left, edge_right = [], []
    for x in range(w):
        for y in range(h):
            # BBGGRR
            px = (int(img_data[i]), int(img_data[i + 1]), int(img_data[i + 2]))
            if px == AUTH_HW_BGR_BACK:
                px = 0
            if x == 0:  # 左边界
                edge_left.append(px)
            if y == 0:  # 上边界
                edge_top.append(px)
            if x == w - 1:  # 右边界
                edge_right.append(px)
            if y == h - 1:  # 下边界
                edge_bottom.append(px)
            i += 4
    return edge_top, edge_bottom, edge_left, edge_right


# 是否边缘匹配, 匹配则返回True,相似度,  不匹配返回False, 0
def is_edge_match(i1: int, i2: int, edge1: list, edge2: list):
    if i1 == i2:  # 只和其他边比较
        return False, 0
    edge1_effect = len(edge1) - edge1.count(0)
    edge2_effect = len(edge2) - edge2.count(0)
    if edge1_effect < 15 or edge2_effect < 15:
        return False, 0
    print("edge1_effect:", edge1_effect, " edge2_effect:", edge2_effect)
    if abs(edge2_effect - edge1_effect) > 10:  # 若有效点数相差超过10个
        return False, 0
    i, n = 0, 0  # 相似点数, 有效点数 (edge1_effect + edge2_effect) // 2
    for edge1_px, edge2_px in zip(edge1, edge2):
        if edge1_px == 0 or edge2_px == 0:  # 若像素点是背景色, 则直接匹配下两个点
            continue
        n += 1
        b1, g1, r1 = edge1_px
        b2, g2, r2 = edge2_px
        if (b1 - b2) ** 2 + (g1 - g2) ** 2 + (r1 - r2) ** 2 < 0x60 ** 2:
            i += 1  # 颜色相似, 则相似点数+1
    if n < 10:
        return False, 0
    pct = i / n
    print("pct:", pct, " i:", i, " n:", n)
    if pct >= 0.80:
        return True, pct
    return False, 0


def get_true_pos(relative_pos: list):
    ori_pos = [0, 1, 2, 3]  # 初始位置
    true_pos = [None, None, None, None]  # 真实位置
    # 获取左上角正确的小拼图序号(参考点)
    for idx in ori_pos:
        for k, v, flag in relative_pos:
            if idx == v:
                break
        else:
            true_pos[0] = idx
            break
    # 遍历 参考点和相对位置列表, 获取其它位置
    for i in range(3):
        for k, v, flag in relative_pos:
            if k == true_pos[0]:
                if flag == "右":
                    true_pos[1] = v
                elif flag == "下":
                    true_pos[2] = v
            elif k == true_pos[1]:
                if flag == "右":
                    true_pos[2] = v
                elif flag == "下":
                    true_pos[3] = v
            elif k == true_pos[2]:
                if flag == "右":
                    true_pos[3] = v
    return true_pos


def exchange_pos_click(wk: Worker, i1: int, i2: int):
    x1, y1 = AUTH_HW_POS[i1]
    x2, y2 = AUTH_HW_POS[i2]
    wk.move_click(x1 + rnd(-3, 3), y1 + rnd(-3, 3), False)
    lib.msleep(400, 600)
    wk.move_click(x2 + rnd(-3, 3), y2 + rnd(-3, 3))


# 过换位
def pass_huan_wei(wk: Worker):
    wk.record("正在过换位验证...")
    tr = create_dispatch_obj(wk, lib.COM_NAME_TR)
    rect0 = (AUTH_HW_X, AUTH_HW_Y, AUTH_HW_X + AUTH_HW_W, AUTH_HW_Y + AUTH_HW_H)
    rect1 = (AUTH_HW_X + AUTH_HW_W, AUTH_HW_Y, AUTH_HW_X + AUTH_HW_W * 2, AUTH_HW_Y + AUTH_HW_H)
    rect2 = (AUTH_HW_X, AUTH_HW_Y + AUTH_HW_H, AUTH_HW_X + AUTH_HW_W, AUTH_HW_Y + AUTH_HW_H * 2)
    rect3 = (AUTH_HW_X + AUTH_HW_W, AUTH_HW_Y + AUTH_HW_H, AUTH_HW_X + AUTH_HW_W * 2, AUTH_HW_Y + AUTH_HW_H * 2)
    # 先截图4块
    pic0 = f"{lib.DIR_TEMP}\\hw_{wk.row}-0.bmp"
    pic1 = f"{lib.DIR_TEMP}\\hw_{wk.row}-1.bmp"
    pic2 = f"{lib.DIR_TEMP}\\hw_{wk.row}-2.bmp"
    pic3 = f"{lib.DIR_TEMP}\\hw_{wk.row}-3.bmp"
    wk.capture(*rect0, pic0)
    wk.capture(*rect1, pic1)
    wk.capture(*rect2, pic2)
    wk.capture(*rect3, pic3)
    # -------------------------- 提取所有边缘像素 --------------------------
    edge_top0, edge_bottom0, edge_left0, edge_right0 = extract_edge_px(tr, pic0)
    edge_top1, edge_bottom1, edge_left1, edge_right1 = extract_edge_px(tr, pic1)
    edge_top2, edge_bottom2, edge_left2, edge_right2 = extract_edge_px(tr, pic2)
    edge_top3, edge_bottom3, edge_left3, edge_right3 = extract_edge_px(tr, pic3)
    all_edge_top = [edge_top0, edge_top1, edge_top2, edge_top3]
    all_edge_bottom = [edge_bottom0, edge_bottom1, edge_bottom2, edge_bottom3]
    all_edge_left = [edge_left0, edge_left1, edge_left2, edge_left3]
    all_edge_right = [edge_right0, edge_right1, edge_right2, edge_right3]
    # -------------------------- 获取相对关系 --------------------------
    relative_pos_sim = []  # 相对关系(带相似度)
    # 底和顶对比
    for i1, edge_bottom in enumerate(all_edge_bottom):
        for i2, edge_top in enumerate(all_edge_top):
            ret, pct = is_edge_match(i1, i2, edge_bottom, edge_top)
            if ret:
                print(f"{i1}下边是{i2}", f"{i1} >> {i2}")
                relative_pos_sim.append((i1, i2, "下", format(pct, ".3f")))
    # 右和左对比
    for i1, edge_right in enumerate(all_edge_right):
        for i2, edge_left in enumerate(all_edge_left):
            ret, pct = is_edge_match(i1, i2, edge_right, edge_left)
            if ret:
                print(f"{i1}右边是{i2}", f"{i1} > {i2}")
                relative_pos_sim.append((i1, i2, "右", format(pct, ".3f")))
    print("relative_pos_sim:", relative_pos_sim)
    # 若边缘相似的超过4个, 移除相似度低的
    if len(relative_pos_sim) > 4:
        relative_pos_sim.sort(key=lambda x: x[3], reverse=True)  # 按相似度从高到低排
        relative_pos_sim = relative_pos[:4]
    # 再移除相似度参数
    relative_pos = []  # 相对关系(不带相似度)
    for i1, i2, pos, pct in relative_pos_sim:
        relative_pos.append((i1, i2, pos))
    print("relative_pos:", relative_pos)  # [(0, 2, '下'), (1, 3, '下'), (1, 0, '右'), (3, 2, '右')]
    # -------------------------- 获取真实位置 --------------------------
    true_pos = get_true_pos(relative_pos)
    print("true_pos:", true_pos)  # [1, 2, 3, 0]
    # -------------------------- 鼠标点击换位 --------------------------
    ori_pos = [0, 1, 2, 3]  # 初始位置
    i1 = 0
    for ori, true in zip(ori_pos, true_pos):
        if ori != true:
            i2 = ori_pos.index(true)
            print(f"{i1}和{i2}互换位置")
            exchange_pos_click(wk, i1, i2)
            ori_pos[i1], ori_pos[i2] = ori_pos[i2], ori_pos[i1]
        i1 += 1
    print("ori_pos:", ori_pos)


def proc_li_du(wk: Worker):
    # 移到确定处
    x, y = POS_AUTH_LD_CONFIRM
    wk.move_to(x + rnd(-5, 5), y + rnd(-2, 2))
    # 找到力度条黄区左边位置
    left_x, _ = wk.get_color_pos(*RECT_FORCE_BAR, COLOR_FORCE_BAR)  # 力度条黄区左边
    right_x = left_x + 15
    # 循环判断游标位置, 若在中心, 立刻点击
    for i in range(200):
        ldx, ldy = wk.get_pic_pos(*RECT_FORCE_BAR, "力度条滑块.bmp")  # 力度条滑块左上角
        cx = ldx + 8
        if left_x < cx < right_x:
            wk.left_click(False)
            lib.msleep(200)
            break
        lib.msleep(10)
    wk.re_move()


# 过力度
def pass_li_du(wk: Worker):
    wk.record("正在过力度验证...")
    proc_li_du(wk)


# 过方块
def pass_fang_kuai(wk: Worker):
    wk.record("正在过方块验证...")
    pic_name = f"fk_{wk.row}"
    wk.capture(*RECT_FULL, f"{lib.DIR_TEMP}\\{pic_name}.bmp")
    wk.capture(*RECT_AUTH_FK_SEL, f"{lib.DIR_TEMP}\\{pic_name}-0.bmp")
    wk.capture(*RECT_AUTH_FK_POS, f"{lib.DIR_TEMP}\\{pic_name}-1.bmp")
    tr = create_dispatch_obj(wk, lib.COM_NAME_TR)
    fk_sel_objs = get_fk_sel_objs(tr, pic_name)
    fk_all_pos = get_fk_all_pos(tr, pic_name)
    get_all_match_pos(fk_sel_objs, fk_all_pos)
    confirmed = filter_answer(fk_sel_objs, fk_all_pos)
    fk_move_in_turn(wk, confirmed, fk_sel_objs)
    lib.msleep(5000)  # 点完后等待5秒


# -------------------------- 需要换绑定的验证 ---------------------------

# 获取验证背景图
def get_auth_bg_pic_idx(wk: Worker) -> str:
    idx = wk.get_pic_idx(*RECT_AUTH_FULL, "bg0top.bmp|bg1top.bmp|bg2top.bmp|bg3top.bmp|bg4top.bmp")
    return idx


# 获取滑块缺口中心坐标X
def get_slider_breach_center_x(wk: Worker, idx: int) -> int:
    if idx == -1:
        return -1

    # 截图所在路径
    cap_pic_path = f"{lib.DIR_TEMP}\\hk_{wk.row}.bmp"
    wk.capture(*RECT_AUTH_PIC, cap_pic_path)
    # 加载图片
    tr = create_dispatch_obj(wk, lib.COM_NAME_TR)
    tr.LoadImageData(PIC_BACKGROUND[idx])
    tr.Draw_Backups(1)
    tr.Pixel_FromPicture(cap_pic_path)
    tr.Draw_Backups(2)
    # 开始对比差异
    tr.Filter_DiffeExtract(1, 2, 0.85)
    # 去除杂点
    tr.Filter_Despeckle(20)
    # 范围投影切割, 返回的是切割数量的最大下标, 若为1, 说明切割出2个, 若为2, 说明切割出3个
    num = tr.Incise_ScopeAisle(3, 3, "20-60", "20-60", 1)[0]  # 从左到右
    wk.record(f"检测到目标个数: {num+1}")
    # 获取切割字符数据(左,上,宽,高)
    ret = tr.Incise_GetCharData(2)[0]
    pos_list = ret.split("|")  # ['7,87,50,43', '166,90,45,39']
    print("pos_list:", pos_list)
    ret_x, t0, w0, h0 = -1, -1, -1, -1
    ret_x_list = []
    for idx, pos in enumerate(pos_list):
        if pos == "":
            break
        left, top, width, height = [int(i) for i in pos.split(",")]
        if idx == 0:  # 原滑块位置
            t0, w0, h0 = top, width, height
        else:
            if left > 100 and abs(width-w0) < 6 and abs(height-h0) < 6 and abs(top - t0) < 6:
                ret_x = RECT_AUTH_PIC[0] + left + round(width / 2)
                ret_x_list.append(ret_x)
    print("ret_x_list:", ret_x_list)
    if len(ret_x_list) == 1:
        return ret_x_list[0]
    else:
        return -1


# 过程-过滑块
def proc_pass_slider(wk: Worker):
    wk.record("正在过滑块验证...")
    idx = get_auth_bg_pic_idx(wk)
    cx = get_slider_breach_center_x(wk, idx)
    if cx < 0:
        wk.record("获取滑块缺口坐标失败")
        return False
    sx = 60 + rnd(-5, 5)  # 60 对应于滑块初始中心
    wk.move_to(sx, 290 + rnd(-5, 5))
    wk.left_down()
    # 生成滑动轨迹
    delta_px = cx - sx
    track_list = generate_slider_tracks(delta_px)
    forward_list = track_list["forward"]
    backward_list = track_list["backward"]
    for rx in forward_list:
        wk.move_relative(rx, rnd(-1, 1))
        lib.msleep(10, 20)
    for rx in backward_list:
        wk.move_relative(rx, rnd(-1, 1))
        lib.msleep(20, 40)
    lib.msleep(100, 300)  # 等一会再松开
    wk.left_up()
    return True


# 过滑块
def pass_slider(wk: Worker):
    hwnd = wk.get_son_hwnd(wk.hwnd)
    if hwnd == 0:
        return
    wk.switch_bind_detect_window(hwnd)
    for i in range(10):
        if wk.get_son_hwnd(wk.hwnd) == 0:
            break
        if not proc_pass_slider(wk):
            click_refresh_auth(wk)
        lib.msleep(2000, 2200)
    wk.switch_bind_game_window(wk.hwnd)


# 生成黑色点列表
def generate_black_point_list(wk: Worker):
    pt_list = []
    flag = False
    for x, y in CLOCK_POS_LIST_L30:
        if not flag and is_around_pixel_black(wk, x, y):
            pt_list.append((x, y))
            flag = True  # 若这次遍历添加过, 则下一个点就算是黑的也不添加了
        else:
            flag = False
    return pt_list


# 是否周围像素黑色
def is_around_pixel_black(wk: Worker, pos_x: int, pos_y: int):
    color1 = wk.get_pos_color(pos_x, pos_y)
    color2 = wk.get_pos_color(pos_x - 1, pos_y)
    color3 = wk.get_pos_color(pos_x, pos_y - 1)
    for color in (color1, color2, color3):
        r = int(color[0:2], base=16)
        g = int(color[2:4], base=16)
        b = int(color[4:6], base=16)
        if r < 0x20 and g < 0x20 and b < 0x20:
            return True
    return False


# 生成滑块轨迹
def generate_slider_tracks(dist: int):
    dist += 20  # 先加上20的距离然后在生成轨迹中再减去20，达到超过缺口在回滑的效果
    v = 0
    t = 0.2  # 时间间隔0.2s
    forward_tracks = []
    threshold = dist * 0.6  # 开始减速的阈值
    cur = 0  # 当前相对原点的位置
    while cur < dist:
        a = 4 if cur < threshold else -6
        ds = round(v * t + 0.5 * a * t * t)  # 在时间间隔内走过的距离
        forward_tracks.append(ds)
        cur += ds
        v = v + a * t  # 经时间间隔后达到的瞬时速度
    backward_tracks = [-4, -4, -2, -3, -3, -2, -2]
    return {"forward": forward_tracks, "backward": backward_tracks}


# 过程-过时钟
def proc_pass_clock(wk: Worker):
    # 若是移动时钟, 则直接返回
    if wk.find_pic(*RECT_AUTH_FULL, "检测_时.bmp"):
        wk.record("不支持移动时针")
        return False
    wk.record("正在过时钟验证...")
    # 识别要移动到的分秒数
    digit_str = wk.ocr(*RECT_AUTH_CLOCK, COLOR_AUTH_CLOCK_TIME, zk=ZK_AUTH_CLOCK, sim=0.8, timeout=300)
    if not digit_str.isdigit():
        return False
    number = int(digit_str)
    # 计算应移动到的角度和位置
    angle = number if number < 60 else 0
    pos_x, pos_y = CLOCK_POS_LIST_L30[angle]
    print(f"angle: {angle}, pos: {pos_x, pos_y}")
    # 若刚开始就满足时钟题目,说明是其它指针在该位,直接换图
    if is_around_pixel_black(wk, pos_x, pos_y):
        return False
    # 初始阶段, 识别60个固定点位, 把黑色的点存放到list1中
    list1 = generate_black_point_list(wk)  # [(193, 136), (217, 153), (169, 188)]
    print("list1:", list1)
    if len(list1) != 3:
        return False
    # 开始拖动滑块, 并向右移动
    small_offset = rnd(-5, 5)
    wk.move_to(POS_AUTH_SLIDER_START[0] + small_offset, POS_AUTH_SLIDER_START[1] + rnd(-5, 5))
    wk.left_down()
    for i in range(3):
        big_offset = rnd(60, 100)
        wk.move_to(POS_AUTH_SLIDER_START[0] + small_offset + big_offset, POS_AUTH_SLIDER_START[1] + rnd(-5, 5))
        lib.msleep(800, 1000)  # 等待画面更新
        # 第二阶段, 移动big_offset后, 继续识别60个点位, 把黑色的点存放到list2中
        list2 = generate_black_point_list(wk)  # [(217, 153), (219, 165), (169, 188)]
        print("list2:", list2)
        if len(list2) == 3:
            break
    else:
        return False
    # 移动回按下时的点位
    wk.move_to(POS_AUTH_SLIDER_START[0] + small_offset, POS_AUTH_SLIDER_START[1] + rnd(-5, 5))
    lib.msleep(300, 500)  # 等待画面更新
    # 找到 变化的两个点
    list3 = [pt for pt in list1 if pt not in list2]  # 找出所有在列表1但不在列表2中的元素
    list4 = [pt for pt in list2 if pt not in list1]  # 找出所有在列表2但不在列表1中的元素
    if len(list3) != 1 or len(list4) != 1:
        return False
    x1, y1 = list3[0]
    x2, y2 = list4[0]
    # 计算顺时针移动的角度数
    angle1 = CLOCK_POS_LIST_L30.index((x1, y1))
    angle2 = CLOCK_POS_LIST_L30.index((x2, y2))
    delta_angle = angle2 - angle1 if angle2 > angle1 else 60 + angle2 - angle1
    # 计算平均每像素移动的角度数
    angle_per_px = delta_angle / big_offset
    print("angle_per_px:", angle_per_px)
    # 根据题目要求, 计算需移动多少角度
    delta_angle = angle - angle1 if angle > angle1 else 60 + angle - angle1
    print("delta_angle:", delta_angle)
    # 计算需移动多少像素
    delta_px = round(delta_angle / angle_per_px)
    print("delta_px:", delta_px)
    # 生成滑动轨迹
    track_list = generate_slider_tracks(delta_px)
    forward_list = track_list["forward"]
    backward_list = track_list["backward"]
    for rx in forward_list:
        wk.move_relative(rx, rnd(-1, 1))
        lib.msleep(20, 50)
    for rx in backward_list:
        wk.move_relative(rx, rnd(-1, 1))
        lib.msleep(20, 50)
    lib.msleep(200, 400)  # 等一会再松开
    return True


# 过时钟
def pass_clock(wk: Worker):
    hwnd = wk.get_son_hwnd(wk.hwnd)
    if hwnd == 0:
        return
    wk.switch_bind_detect_window(hwnd)
    for i in range(10):
        if wk.get_son_hwnd(wk.hwnd) == 0:
            break
        ret = proc_pass_clock(wk)
        wk.left_up()  # 确保左键抬起
        if ret:
            lib.msleep(1000)  # 成功后多等一会, 确保服务器判定完成
        else:
            click_refresh_auth(wk)
        lib.msleep(1500, 2000)
    wk.switch_bind_game_window(wk.hwnd)


# 获取成语位置列表
def get_cheng_yu_pos_list(wk: Worker):
    idx = get_auth_bg_pic_idx(wk)
    if idx == -1:
        return []
    cap_pic_path = f"{lib.DIR_TEMP}\\cy_{wk.row}.bmp"
    wk.capture(*RECT_AUTH_PIC, cap_pic_path)

    tr = create_dispatch_obj(wk, lib.COM_NAME_TR)
    print(tr.version())
    tr.Lib_Load(f"{lib.DIR_DLL}\\phr.lib")
    # 加载原图数据
    tr.LoadImageData(PIC_BACKGROUND[idx])
    tr.Draw_Backups(1)
    # 截图所在路径
    tr.Pixel_FromPicture(cap_pic_path)
    tr.Draw_Backups(2)
    # 差异提取
    tr.Filter_DiffeExtract(1, 2, 0.80)
    # 去除杂点
    tr.Filter_Despeckle(6)
    tr.Filter_DespeckleEx(30)

    # 范围投影切割
    max_idx = tr.Incise_ScopeAisle(8, 8, "10-50", "5-50")[0]
    print("max_idx:", max_idx)
    # 获取切割字符数据(左,上,宽,高)  ret = "23,23,29,38|266,28,29,27|20,148,41,32|85,149,31,28"
    ret = tr.Incise_GetCharData(2)[0]
    pos_list = ret.split("|")
    print("pos_list =", pos_list)
    char_num = max_idx + 1
    for i in range(char_num):
        # 设置 当前图像 为 切割后的第i个字符图像
        tr.Pixel_SetImageDataCut(i)
        # 备份切割字符的图像
        tr.Draw_Backups(3 + i)
    for i in range(char_num):
        # ------------------------ 2 字符数据规格化, 并识别 ------------------------
        # 恢复图像数据
        tr.Draw_Recover(3 + i)
        # 旋转纠正处理
        tr.Filter_RotateCorrect(45, 1)
        # 统一字符图像大小
        tr.Filter_ZoomOne(36, 36)
        # 对整个图像切割, 切割后才能识别
        tr.Incise_FixedLocation(0, 0, 36, 36)
        # 识别
        ocr_ret = tr.Ocr()
        print("ocr_ret:", ocr_ret)
        pos_list[i] += f",{ocr_ret}"
    # ['206,25,30,32,色', '203,86,30,32,六', '23,146,36,34,五', '137,139,42,42,颜']
    pos_list = [pos.split(",") for pos in pos_list]
    if len(pos_list) < 3:
        return []

    for idx, xywhf in enumerate(pos_list):
        x, y, w, h, f = xywhf
        x, y, w, h = int(x), int(y), int(w), int(h)
        pos_list[idx] = (x, y, w, h, f)
    # [(206, 25, 30, 32, '色'), (203, 86, 30, 32, '六'), (23, 146, 36, 34, '五'), (137, 139, 42, 42, '颜')]
    print("pos_list =", pos_list)
    return pos_list


# 过程-过成语语序
def proc_pass_cy_yx(wk: Worker):
    wk.record("正在过成语验证...")
    # [(23,23,29,38,"出"), (266,28,29,27,"望"), ("20,148,41,32,"喜"), (85,149,31,28,"外")]
    pos_list = get_cheng_yu_pos_list(wk)
    print("pos_list:", pos_list)
    if len(pos_list) < 3:
        return False
    # 把识别出的字提取到列表中
    word_list = []
    for xywhf in pos_list:
        word_list.append(xywhf[-1])
    print("word_list:", word_list)  # ["出", "望", "喜", "外"]
    if "" in word_list:
        return False
    # 筛选成语库中有这几个字的成语
    answer = ""
    for phrase in PHRASE_SET:
        idx_list = []
        for word in word_list:
            idx = phrase.find(word)
            idx_list.append(idx)
            if idx_list.count(-1) >= 2:  # 若列表中有两个以上没找到, 则跳出, 尝试匹配下一个成语
                break
        err_count = idx_list.count(-1)  # 识别出错的字数
        if err_count <= 1:
            answer = phrase
            if err_count == 0:  # [1,2,0,3]
                break
            # [1,-1,0,3]
            err_idx = idx_list.index(-1)  # 识别错的字在索引列表中的位置
            idx_list[err_idx] = [i for i in range(len(idx_list)) if i not in idx_list][0]
            bool_list = [i in idx_list for i in range(len(idx_list))]
            print("idx_list0:", idx_list)
            print("bool_list:", bool_list)
            if False not in bool_list:  # 避免[1, 0, 3]这种情况
                break
    else:
        return False
    print("idx_list1:", idx_list)
    # 初始化点击顺序列表
    click_order_list = [(0, 0) for _ in pos_list]
    # 根据顺序, 更新点击顺序列表
    for i, order in enumerate(idx_list):
        x, y, w, h = pos_list[i][:4]
        pos_x, pos_y = RECT_AUTH_PIC[0] + x + w // 2, RECT_AUTH_PIC[1] + y + h // 2
        click_order_list[order] = (pos_x, pos_y)
    print(f"成语:{answer}, 答案:{click_order_list}")
    wk.record(f"成语:{answer}, 答案:{click_order_list}")

    wk.enable_real_mouse(True, step=20)
    for pos_x, pos_y in click_order_list:  # 依次点击字
        wk.move_click(pos_x, pos_y)
        lib.msleep(500, 800)
    wk.simulate_real_mouse()  # 恢复之前
    return True


# 过成语语序
def pass_cy_yx(wk: Worker):
    hwnd = wk.get_son_hwnd(wk.hwnd)
    if hwnd == 0:
        return
    wk.switch_bind_detect_window(hwnd)
    for i in range(20):
        if wk.get_son_hwnd(wk.hwnd) == 0:
            break
        if proc_pass_cy_yx(wk):
            lib.msleep(1000)  # 成功后多等一会, 确保服务器判定完成
        else:
            click_refresh_auth(wk)
        lib.msleep(1500, 2000)
    wk.switch_bind_game_window(wk.hwnd)


# ------------------------ 过方块 --------------------------------

# 俄罗斯方块类
class ElsSquare():
    def __init__(self, x: int, y: int, feature: list):
        self.x = x
        self.y = y
        self.mat = feature
        self.h = len(self.mat)
        self.w = len(self.mat[0])
        self.mat_list = []  # 存放矩阵的几种不同形态
        self.match_list = []  # 存放匹配的位置 (行, 列, 旋转次数)
        self.rtt_count = 0  # 旋转次数

    def __str__(self):
        ret = "x:{},y:{},w:{},h:{},mat:{}".format(self.x, self.y, self.w, self.h, self.mat)
        return ret

    # 顺时针旋转90度
    def rotate_90(self):
        self.rtt_count += 1
        if self.rtt_count >= 4:
            self.rtt_count = 0
        # 先反转
        self.mat = self.mat[::-1]
        # 再转置
        self.transpose()
        # 重新计算宽高
        self.w = len(self.mat[0])
        self.h = len(self.mat)

    # 转置
    def transpose(self):
        ret = []
        for line in zip(*self.mat):
            ret.append(list(line))
        self.mat = ret


# 矩阵转置
def mat_transpose(mat: list):
    ret = []
    for line in zip(*mat):
        ret.append(list(line))
    mat = ret
    return mat


# 获取方块选择列表
def get_fk_sel_objs(tr, pic_name: str):
    fk_sel_objs = []
    pic = f"{lib.DIR_TEMP}\\{pic_name}-0.bmp"
    tr.Pixel_FromPicture(pic)
    # 二值化
    tr.Filter_Binaryzation(COLOR_AUTH_FK_SEL)
    # 对白色膨胀, 以填充空隙至W_FK_SINGLE
    tr.Filter_DilationErosion()
    tr.Filter_DilationErosion()

    num = tr.Incise_ScopeAisle(3, 3, "10-80", "10-80")[0]
    ret = tr.Incise_GetCharData()[0]
    for char_data in ret.split("|"):
        x, y, w, h, mat = char_data.split(",")
        # 33 10 16 70 111111111111111100111111111111111100111111111111111100...
        print(x, y, w, h, mat)
        x, y, w, h = int(x), int(y), int(w), int(h)
        col = w // W_FK_SINGLE  # 列数1
        row = h // W_FK_SINGLE  # 行数4
        feature_list = []  # 每W_FK_SINGLE个像素收集最左上角的像素作为特征
        for i in range(col):  # i代表第几列 = 0
            col_feature = []  # 收集第i列的特征
            for j in range(row):  # j代表第几行 = 0, 1, 2, 3
                idx = (i * row * W_FK_SINGLE + j) * W_FK_SINGLE
                px = int(mat[idx])
                col_feature.append(px)
            feature_list.append(col_feature)
        feature_list = mat_transpose(feature_list)
        els = ElsSquare(x, y, feature_list)
        print(els)
        fk_sel_objs.append(els)
    return fk_sel_objs


# 获取方块位置列表
def get_fk_all_pos(tr, pic_name: str):
    fk_all_pos = []
    pic = f"{lib.DIR_TEMP}\\{pic_name}-1.bmp"
    tr.Pixel_FromPicture(pic)
    # 二值化
    tr.Filter_Binaryzation(COLOR_AUTH_FK_POS)
    # 对整张图片进行切割
    tr.Incise_FixedLocation(0, 0, W_FK_POS_FULL, W_FK_POS_FULL, 0, 1, 0, 1)
    # 获取切割字符数据
    ret = tr.Incise_GetCharData()[0]
    for char_data in ret.split("|"):
        print(char_data)
        l, t, w, h, mat = char_data.split(",")
        l, t, w, h = int(l), int(t), int(w), int(h)
        col = w // W_FK_SINGLE  # 列数
        row = h // W_FK_SINGLE  # 行数
        print("col:", col)
        print("row:", row)
        for i in range(col):  # i代表第几列 = 0, 1, ..., 15
            col_feature = []  # 收集第i列的特征
            for j in range(row):  # j代表第几行 = 0, 1, ..., 15
                # 每W_FK_SINGLE个像素收集最左上角的像素作为特征
                idx = (i * row * W_FK_SINGLE + j) * W_FK_SINGLE
                px = int(mat[idx])
                col_feature.append(px)
            fk_all_pos.append(col_feature)
    fk_all_pos = mat_transpose(fk_all_pos)
    return fk_all_pos


# 其它边连通数目
def other_side_conn_num(fk_all_pos: [[int]], traversed: [(int, int)], row: int, col: int, exclude: str, num=0):
    # 此点位不通, 或已经遍历过, 则直接返回
    if fk_all_pos[row][col] == 0 or (row, col) in traversed:
        return num
    num += 1
    traversed.append((row, col))
    # 遍历相邻边点位
    include = {"上", "下", "左", "右"}
    include.remove(exclude)
    if "上" in include and row - 1 >= 0:
        num = other_side_conn_num(fk_all_pos, traversed, row - 1, col, "下", num)
    if "下" in include and row + 1 < NUM_FK:
        num = other_side_conn_num(fk_all_pos, traversed, row + 1, col, "上", num)
    if "左" in include and col - 1 >= 0:
        num = other_side_conn_num(fk_all_pos, traversed, row, col - 1, "右", num)
    if "右" in include and col + 1 < NUM_FK:
        num = other_side_conn_num(fk_all_pos, traversed, row, col + 1, "左", num)
    return num


# 是否位置有效(上下左右全是0 或 上下左右相连的1个数要大于3)
def is_pos_effect(els: ElsSquare, fk_all_pos: [[int]], row: int, col: int):
    w = els.w
    h = els.h
    # 把方块摆上去
    temp_fk_all = copy.deepcopy(fk_all_pos)
    for i in range(h):
        for j in range(w):
            if els.mat[i][j] == 1:
                temp_fk_all[row + i][col + j] = 0
    # 上边界
    for j in range(col, col + w):
        i = row - 1  # 默认从第一行的前一行递归搜索
        for _ in range(h):  # 尽可能从最下边一个空位开始计算
            if i + 1 < row + h and temp_fk_all[i + 1][j] == 1:
                i += 1
            else:
                break
        if i < 0:
            continue
        traversed = []  # 已经遍历过的点位
        if temp_fk_all[i][j] == 1:
            xxx = other_side_conn_num(temp_fk_all, traversed, i, j, "下")
            if xxx < 4:
                return False
    # 下边界
    for j in range(col, col + w):
        i = row + h  # 默认从最后一行的后一行递归搜索
        for _ in range(h):  # 尽可能从最上边一个空位开始计算
            if i - 1 >= row and temp_fk_all[i - 1][j] == 1:
                i -= 1
            else:
                break
        if i >= NUM_FK:
            continue
        traversed = []  # 已经遍历过的点位
        if temp_fk_all[i][j] == 1:
            xxx = other_side_conn_num(temp_fk_all, traversed, i, j, "上")
            if xxx < 4:
                return False
    # 左边界
    for i in range(row, row + h):
        j = col - 1  # 默认从第一列的前一列递归搜索
        for _ in range(w):  # 尽可能从最右边一个空位开始计算
            if j + 1 < col + w and temp_fk_all[i][j + 1] == 1:
                j += 1
            else:
                break
        if j < 0:
            continue
        traversed = []  # 已经遍历过的点位
        if temp_fk_all[i][j] == 1:
            xxx = other_side_conn_num(temp_fk_all, traversed, i, j, "右")
            if xxx < 4:
                return False
    # 右边界, 若方块最后一列有空位, 就从最后一列递归搜索, 否则从最后一列的下一列递归搜索
    for i in range(row, row + h):
        j = col + w
        for _ in range(w):  # 尽可能从最左边一个空位开始计算
            if j - 1 >= col and temp_fk_all[i][j - 1] == 1:
                j -= 1
            else:
                break
        if j >= NUM_FK:
            continue
        traversed = []  # 已经遍历过的点位
        if temp_fk_all[i][j] == 1:
            xxx = other_side_conn_num(temp_fk_all, traversed, i, j, "左")
            if xxx < 4:
                return False
    # 4个边界都没有堵死其它方块
    return True


# 获取单个俄罗斯方块位置
def get_single_match_pos(els: ElsSquare, fk_all_pos: [[int]]):
    print("els.mat:", els.mat)
    full_match_num = els.w * els.h  # 全匹配数
    cmp_w = NUM_FK - els.w + 1
    cmp_h = NUM_FK - els.h + 1
    print("cmp_w:", cmp_w)
    print("cmp_h:", cmp_h)
    # 逐个遍历摆放区域, 判断是否与方块匹配
    for row in range(cmp_h):
        for col in range(cmp_w):
            match_num = 0  # 当前匹配数
            # 逐个遍历方块的每个特征点
            for i in range(els.h):
                for j in range(els.w):
                    a = fk_all_pos[row + i][col + j]
                    b = els.mat[i][j]
                    if a == 1 or a == b:
                        match_num += 1
                        if match_num == full_match_num:  # 全匹配
                            # 周围被0包围的1个数要大于3才记录
                            if is_pos_effect(els, fk_all_pos, row, col):
                                els.match_list.append((row, col, els.rtt_count))
                            break  # 匹配完成, 跳出
                    else:
                        break  # 只要有一个点不匹配, 就跳出
                # 下面3行实现只要上面跳出, 就会同时跳出两层for循环, 开始匹配下一个摆放点
                else:
                    continue
                break


# 获取所有匹配位置, 放在每一个方块类对象的实例属性match_list里
def get_all_match_pos(fk_sel_objs: [ElsSquare], fk_all_pos: [[int]]):
    print("找出匹配位置")
    for els in fk_sel_objs:
        mat0 = els.mat
        els.mat_list.append(mat0)
        get_single_match_pos(els, fk_all_pos)  # 0

        els.rotate_90()
        mat1 = els.mat
        if mat1 != mat0:
            els.mat_list.append(mat1)
            get_single_match_pos(els, fk_all_pos)  # 90

        els.rotate_90()
        mat2 = els.mat
        if mat2 != mat0 and mat2 != mat1:
            els.mat_list.append(mat2)
            get_single_match_pos(els, fk_all_pos)  # 180

        els.rotate_90()
        mat3 = els.mat
        if mat3 != mat0 and mat3 != mat1:
            els.mat_list.append(mat3)
            get_single_match_pos(els, fk_all_pos)  # 270

        els.rotate_90()  # 最后旋转一次, 复位


# 筛选答案
def filter_answer(fk_sel_objs: [ElsSquare], fk_all_pos: [[int]]) -> dict:
    # 未占据集合
    unoccupied = {(i, j) for i in range(NUM_FK) for j in range(NUM_FK) if fk_all_pos[i][j] == 1}
    # 已占据集合
    occupied = set()
    # 未确定字典 {索引号: [(摆放的行号, 摆放的列号, 旋转的次数),(摆放的行号, 摆放的列号, 旋转的次数),...]}
    unconfirmed = {idx: els.match_list for idx, els in enumerate(fk_sel_objs)}
    # 已确定字典 {索引号: (摆放的行号, 摆放的列号, 旋转的次数), ...}
    confirmed = {}

    def only_sol():
        row, col, rtt = els.match_list[0]
        # 已确定字典添加元素, 未确定字典弹出元素
        confirmed[idx] = (row, col, rtt)
        unconfirmed.pop(idx)
        # 已占据集合添加元素, 未占据集合弹出元素
        mat = els.mat_list[rtt]
        h = len(mat)
        w = len(mat[0])
        for i in range(h):
            for j in range(w):
                if mat[i][j] == 1:
                    occupied.add((row + i, col + j))
                    unoccupied.remove((row + i, col + j))

    def multi_sol():
        for row, col, rtt in els.match_list:
            mat = els.mat_list[rtt]
            h = len(mat)
            w = len(mat[0])
            for i in range(h):
                for j in range(w):
                    if mat[i][j] == 1 and (row + i, col + j) in occupied:
                        els.match_list.remove((row, col, rtt))
                        break
                else:
                    continue
                break

    def is_comb_perfect():
        for idx, (row, col, rtt) in enumerate(comb):
            idx = list(unconfirmed.keys())[idx]
            els = fk_sel_objs[idx]
            mat = els.mat_list[rtt]
            h = len(mat)
            w = len(mat[0])
            for i in range(h):
                for j in range(w):
                    if mat[i][j] == 0:
                        continue
                    if (row + i, col + j) in temp_occupied:  # 若点位已被占
                        return False
                    else:
                        temp_occupied.add((row + i, col + j))
                        temp_unoccupied.remove((row + i, col + j))
            # 已确定字典添加元素
            temp_confirmed[idx] = (row, col, rtt)
        return True

    # 第一轮: 放入有唯一解的, 根据被占据的点位, 排除一些多解, 重复多次
    for _ in range(4):
        for idx, els in enumerate(fk_sel_objs):
            if idx in confirmed:
                continue
            num_sol = len(els.match_list)
            if num_sol == 0:  # 无解
                return {}
            if num_sol == 1:  # 有唯一解
                only_sol()
            if num_sol > 1:  # 有多解
                multi_sol()

    # 第二轮: 对未确定字典排列组合, 依次尝试
    combinations = list(itertools.product(*unconfirmed.values()))
    for comb in combinations:
        # 恢复全部不确定方块未放置时的状态
        temp_unoccupied = copy.deepcopy(unoccupied)
        temp_occupied = copy.deepcopy(occupied)
        temp_confirmed = copy.deepcopy(confirmed)
        # 依次假设放到摆放区, 若中途发生冲突, 则直接跳出, 判断下一种组合
        if is_comb_perfect():
            confirmed = temp_confirmed
            break
    else:
        return {}
    return confirmed


# 方块按顺序移动
def fk_move_in_turn(wk: Worker, confirmed: dict, fk_sel_objs: [ElsSquare]):
    # {4: (1, 1, 2), 5: (12, 9, 3), 7: (3, 6, 1), 1: (2, 7, 0),
    # 2: (10, 4, 2), 3: (2, 10, 1), 6: (9, 6, 1), 0: (7, 6, 2)}
    if not confirmed:
        wk.record("无解")
        return
    wk.record(f"唯一解:{confirmed}")
    wk.enable_real_mouse(True, step=20)
    for idx, (row, col, rtt) in confirmed.items():
        els = fk_sel_objs[idx]
        mat = els.mat_list[rtt]
        h = len(mat)
        w = len(mat[0])
        # 方块选择区起始位置
        ori_x, ori_y = POS_AUTH_FK_SEL
        # 抓起方块(这里要用初始时的宽高)
        ctr_x = ori_x + els.x + round(W_FK_SINGLE * els.w / 2)
        ctr_y = ori_y + els.y + round(W_FK_SINGLE * els.h / 2)
        wk.move_click(ctr_x, ctr_y, False)
        lib.msleep(500, 800)
        # 旋转rtt次
        for _ in range(rtt):
            wk.key_press(VK_SPACE)
            lib.msleep(400, 600)
        # 放置方块(这里要用旋转后的宽高)
        pos_x, pos_y = POS_AUTH_FK_POS
        des_x = pos_x + col * W_FK_SINGLE + round(W_FK_SINGLE * w / 2)
        des_y = pos_y + row * W_FK_SINGLE + round(W_FK_SINGLE * h / 2)
        offsets = [(-6, -6), (-6, 6), (6, -6), (6, 6),
                   (-12, -12), (-12, 12), (12, -12), (12, 12)]
        for off_x, off_y in offsets:  # 尝试多个位置放置方块
            plc_x, plc_y = des_x + off_x, des_y + off_y
            wk.move_click(plc_x, plc_y, False)
            lib.msleep(200)
            if wk.find_color(plc_x - 5, plc_y - 5, plc_x + 5, plc_y + 5, COLOR_AUTH_FK_SUC, timeout=200):
                break
            elif wk.find_pic(*RECT_FULL, "方块完成.bmp"):
                break
        lib.msleep(500, 800)
    wk.simulate_real_mouse()  # 恢复之前


# -------------------------- 全局变量 -----------------------------
team = Team()

# -------------------------- 字库 -----------------------------
ZK_ALL = 0  # 全部
ZK_DIGIT_BLUR = 1  # 数字模糊(坐标, 日程数字)
ZK_DIGIT_CLEAR = 2  # 数字清晰(价格, 挖宝索引)
ZK_TALK = 3  # 对话内容
ZK_TASK_TYPE = 4  # 任务类型
ZK_SUB_TASK = 5  # 子任务
ZK_AUTH_CLOCK = 6  # 时钟验证
ZK_AUTH_OTHER = 7  # 其它验证

# --------------------------- 业务逻辑相关全局变量 ---------------------------
ORDER_LRUD, ORDER_LRDU, ORDER_RLUD, ORDER_RLDU = 0, 1, 2, 3
VK_BACK, VK_TAB, VK_ENTER, VK_ESC = 8, 9, 13, 27
VK_LEFT, VK_RIGHT = 37, 39
VK_SPACE = 32
VK_SHIFT, VK_CTRL, VK_ALT = 16, 17, 18
VK_F1, VK_F2, VK_F3, VK_F4, VK_F5 = 112, 113, 114, 115, 116
VK_F6, VK_F7, VK_F8, VK_F9 = 117, 118, 119, 120
VK_1, VK_2, VK_3, VK_4, VK_5 = 49, 50, 51, 52, 53
VK_A, VK_E, VK_F, VK_J, VK_N, VK_O = 65, 69, 70, 74, 78, 79
VK_Q, VK_T, VK_V, VK_Y = 81, 84, 86, 89

COLOR_WHITE = "ffffff-010101"  # 白色
COLOR_BLACK = "000000-010101"  # 黑色
COLOR_CYAN = "00ffff-000101"  # 青色
COLOR_YELLOW = "ffff00-010100"  # 黄色
COLOR_GREEN = "00ff00-000100"  # 绿色
COLOR_RED = "ff0000-010000"  # 红色

COLOR_HOVER = "fff225-000000"  # 对话项鼠标悬浮颜色
COLOR_UI = "157187-222222|713206-222222"  # 界面颜色
COLOR_CUR_POS = "ffffff-444444|76ff8d-333333"  # 当前坐标 字体颜色
COLOR_TALK_ITEM = "00ffff-222222|fff225-222222"  # 对话框选项 字体颜色
COLOR_WHITE_BLUR = "ffffff-222222"  # 对话框内容 字体颜色, 宠物温饱度 数字颜色
COLOR_PET_LOYAL = "efcc41-000000"  # 宠物忠诚条颜色
COLOR_MAP_NPC = "65df49-000000"  # 地图NPC名字颜色
COLOR_TREASURE = "00eaff-000000"  # 藏宝图地图名颜色
COLOR_TREASURE_IDX = "944600-000000"  # 藏宝点索引颜色
COLOR_CUR_DEPOT_PAGE = "f2d375-111111"  # 当前仓库页颜色
COLOR_FU_BEN_LINE = "ff6539-050505"  # 副本已做次数橙色线
COLOR_FIGHT_UNIT = "56df6d-050505"  # 战斗中所有单位下方字体的颜色
COLOR_LH_COUNT = "00ff00-333333"  # 灵狐剩余次数颜色
COLOR_SCHEDULE_DIGIT = "524744-222222"  # 日程数字颜色, SW币物品售价颜色
COLOR_TALK_BACK = "184a4a-050505"  # 对话框透明背景色
COLOR_FORCE_BAR = "f8fc50-101010"  # 钓鱼力度条颜色
COLOR_ZI_NV_WB = "708989-050505"  # 子女温饱度进度条灰色

GAME_W = 800
GAME_H = 600
CENTER_X = GAME_W // 2
CENTER_Y = GAME_H // 2

Y_DEPOT_PAGE = 468
X_DEPOT_PAGE1 = 159
X_DEPOT_PAGE2 = 208
X_DEPOT_PAGE3 = 256
X_DEPOT_PAGE4 = 303
X_DEPOT_PAGE5 = 360
X_TREASURE_BOX_LEFT = 250
X_TREASURE_BOX_CENTER = 390
X_TREASURE_BOX_RIGHT = 530
X_LIMIT_ADD_LOYAL = 660
Y_TREASURE_BOX = 300

POS_ZI_DONG_ZHAN_DOU = (70, 395)  # 自动战斗框位置
POS_CUR_TASK_BAR = (569, 119)  # 当前任务栏位置
POS_TALK_BLANK = (380, 288)  # 对话空白区
POS_CENTER = (CENTER_X, CENTER_Y)  # 窗口中心
POS_ROLE_HP = (762, 7)  # 人物加血
POS_ROLE_MP = (762, 18)  # 人物加蓝
POS_PET_HP = (642, 8)  # 宠物加血
POS_PET_MP = (642, 19)  # 宠物加蓝
POS_PET_LOYAL = (642, 41)  # 宠物加忠诚
POS_JIA_JU = (736, 117)  # 房屋家具
POS_TING_YUAN = (736, 204)  # 庭院装饰
POS_HTD_FC = (615, 175)  # 还童丹-放入宠物
POS_HTD_CWJY = (500, 495)  # 还童丹-宠物交易中心
POS_JJTY_SCORLL = (620, 424)  # 制作家具庭院-可滚动区域
POS_JJTY_QDZZ = (617, 258)  # 制作家具庭院-确定制作
POS_LOGO_LEADER = (621, 508)  # 队长标识中心点
POS_LOGO_BOSS = (409, 508)  # 首领怪标识中心点
POS_AROUND_SCROLL = (155, 180)  # 周围列表-可滚动区域的点位
POS_FIGHT_BUFF = (545, 13)  # 展开战斗buff的位置
POS_UI_PET = (588, 27)  # 点开宠物界面的位置
POS_SWB_BUY = (471, 470)  # SWB购买按钮位置
POS_SWB_BUY_ONE = (468, 214)  # SWB购买一个按钮位置
POS_MAKE_ZB = (454, 480)  # 制作装备按钮位置
POS_DONATE_SELL_ZB = (176, 490)  # 装备捐献与出售的位置
POS_DONATE_ZB = (214, 415)  # 装备捐献的位置
POS_GOODS_SEL_LBTN = (355, 503)  # 物品选择界面左按钮_选择(快速选中)
POS_GOODS_SEL_RBTN = (438, 503)  # 物品选择界面右按钮_确定
POS_ZHUAN_LE = (131, 526)  # 转转乐左下角小鸡吉祥位置
POS_JS_CONFIRM = (314, 506)  # 经商选择角色时的确认按钮位置
POS_QHXBW = (194, 181)  # 剧情青河小霸王位置
POS_SHEN_MO_LX = (449, 404)  # 神魔副本灵心位置
POS_SHEN_MO_GC = (266, 198)  # 神魔副本鬼车位置
POS_SWB_PRICE = (399, 93)  # 识别SW币物品的价格起始点
POS_SWB_SMS = (257, 215)  # SW币商城的神秘石位置
POS_FACTION_AVOID = (600, 480)  # 帮派找总管位置防挡字位置
POS_MAP_LEFT_UP = (230, 160)  # 地图左上角窗口坐标(边境, 封妖)
POS_MAP_LEFT_DOWN = (230, 440)  # 地图左下角窗口坐标(边境, 封妖)
POS_MAP_RIGHT_DOWN = (570, 440)  # 地图右下角窗口坐标(边境, 封妖)
POS_MAP_RIGHT_UP = (570, 160)  # 地图右上角窗口坐标(边境, 封妖)
POS_JI_SHOU_PRICE_LT = (209, 123)  # 寄售价格左上角位置
POS_QF_START_STOP = (291, 275)  # 祈福开始停止按钮位置
POS_HLD_DUI_HUAN = (393, 417)  # 化龙鼎兑换龙魂的位置

POS_UI_Y = 589
POS_UI_TASK = (577, POS_UI_Y)  # 点开任务界面的位置
POS_UI_FRIEND = (660, POS_UI_Y)  # 点开好友界面的位置
POS_UI_BAG = (458, POS_UI_Y)  # 点开背包界面的位置
POS_UI_TEAM = (537, POS_UI_Y)  # 点开队伍界面的位置
POS_UI_ZB = (497, POS_UI_Y)  # 点开装备界面的位置

POS_UI_JI_SHOU = (7, 237)  # 点开寄售中心界面的位置
POS_UI_SWB = (7, 211)  # 点开SW币交易中心界面的位置
POS_UI_SCHEDULE = (7, 83)  # 点开日程界面的位置

RECT_FULL = (0, 0, GAME_W, GAME_H)  # 全屏
RECT_RIGHT = (CENTER_X, 0, GAME_W, GAME_H)  # 右半屏
RECT_CUR_MAP = (45, 0, 173, 20)  # 当前地图
RECT_CUR_POS = (55, 23, 142, 42)  # 当前坐标
RECT_CLOSE_TALK = (680, 278, 719, 320)  # 关闭对话框的叉所在区域
RECT_TALK_CONTENT_SMALL = (261, 280, 538, 447)  # 对话内容小
RECT_TALK_CONTENT_BIG = (162, 283, 617, 464)  # 对话内容大
RECT_TIP_CENTER = (230, 190, 554, 384)  # 中心提示框
RECT_TIP_TOP = (227, 0, 557, 137)  # 上提示框
RECT_TIP_BOTTOM = (273, 534, 525, 567)  # 下提示区
RECT_TIP_DETAIL = (24, 75, 174, 234)  # 副本或活动详情提示区
RECT_AROUND_LIST = (50, 160, 260, 500)  # 周围列表范围
RECT_FIGHT = (391, 462, 800, 600)  # 战斗判定
RECT_BUFF = (659, 52, 796, 114)  # buff范围
RECT_QUICK_BAR = (761, 111, 799, 431)  # 快捷栏
RECT_PET_LOYAL = (613, 36, 667, 46)  # 宠物忠诚栏
RECT_GOODS = (204, 68, 472, 443)  # 商品区域
RECT_CUR_TASK = (530, 133, 760, 430)  # 当前任务区
RECT_CUR_ACTIVITY = (530, 143, 760, 600)  # 当前活动区
RECT_RIGHT_UP = (525, 0, 800, 120)  # 右上角
RECT_RIGHT_DOWN = (540, 400, 800, 600)  # 右下角
RECT_LEFT_ICON = (0, 56, 31, 381)  # 左边图标
RECT_DEPOT_PAGE = (109, 441, 354, 497)  # 仓库页
RECT_PET_BRING = (208, 232, 373, 465)  # 宠物携带区
RECT_MAKE_GOODS = (81, 282, 253, 541)  # 制作物品区
RECT_ENEMY = (0, 0, 520, 373)  # 战斗敌方区域
RECT_LOGO_ENEMY = (337, 492, 482, 551)  # 敌方标识区
RECT_LOGO_FRIEND = (551, 492, 693, 551)  # 友方标识区
RECT_LOGO_BOSS = (396, 492, 425, 523)  # 首领怪标识区

RECT_FIGHT_BUFF = (400, 0, 550, 55)  # 战斗buff区
RECT_JS_CARD = (412, 485, 798, 537)  # 经商卡片区
RECT_TALK_BACK = (500, 300, 510, 310)  # 对话框背景颜色区
RECT_DIAO_YU = (55, 45, 747, 533)  # 钓鱼界面区
RECT_FORCE_BAR = (315, 210, 497, 340)  # 钓鱼力度条区
RECT_SKIP_ANIMATION = (715, 0, 800, 30)  # 剧情跳过动画范围
RECT_QUQUE_BACK = (45, 45, 140, 80)  # 排队回原服范围, 是否屏蔽范围

# NPC位置(窗口坐标)
NPC_POS_WND = {
    "李少镖头": (399, 366), "江湖密探": (421, 378), "邮差": (534, 138),
    "说书先生": (224, 280), "交易中心": (422, 450), "玄修": (255, 205),
    "小狐仙": (290, 237), "钟馗": (264, 224), "帮派总管": (483, 314),
    "帮派车夫": (656, 436), "幸运小昕": (321, 304), "楚千机": (193, 250),
    "昭武校尉": (280, 234), "领双人": (226, 245), "边境将领": (221, 190),
    "玄义": (303, 246), "祈福僧人": (329, 169), "林惊羽": (503, 351),
}

# NPC位置(真实坐标)
NPC_POS_TRUE = {
    "李少镖头": (272, 104),
}

# 师父坐标
TUTOR_POS = {
    "大雄宝殿": (441, 302), "程府": (346, 314), "水晶宫": (274, 253), "云隐阁": (501, 288),
    "南海普陀": (509, 190), "森罗殿": (315, 282), "盘丝洞": (399, 308), "无名谷": (218, 167),
    "魔王山": (233, 195), "乾坤殿": (294, 265), "狮王洞": (332, 307), "灵台宫": (351, 297),
    "凌霄殿": (368, 304)
}

# 飞行旗范围(窗口坐标)
FLAG_RECT = {
    "运镖宝图": (354, 334, 466, 399), "长安驿站": (308, 392, 382, 440), "交易中心": (398, 412, 483, 474),
    "帮派": (453, 280, 526, 335), "说书先生": (201, 237, 279, 290), "捉鬼": (250, 195, 314, 247),
    "长安药店": (582, 352, 644, 401), "长安城外": (688, 443, 751, 495), "柳乘风": (79, 375, 187, 475),
    "吴朴智": (181, 293, 358, 354), "钱夫人": (347, 215, 432, 278), "金悦院": (655, 268, 750, 337),
    "天策": (59, 313, 129, 373), "佛门": (469, 71, 549, 131), "大雁塔": (553, 89, 646, 154),
    "金銮殿": (108, 154, 182, 226), "房屋车夫": (662, 155, 722, 211), "天魔里": (527, 70, 690, 155),
    "乌斯藏": (586, 412, 694, 485), "昆仑山": (572, 108, 677, 177), "七星方寸": (86, 104, 197, 191),
    "大唐境外": (604, 404, 682, 488), "青河村长": (137, 100, 295, 253),
}

# 接引人位置
WELCOME_NPC = {
    "青河镇外船夫": (638, 380), "傲来国船夫": (600, 400), "傲来国驿站老板": (244, 269),
    "鱼精": (604, 172), "长安城驿站老板": (329, 427), "国境驿站老板": (577, 187),
    "仙女": (585, 109), "女儿国驿使": (298, 150), "乌斯藏驿站老板": (300, 247),
    "猴精": (392, 210), "土地公公": (551, 334), "月宫侍女": (627, 375),
    "护剑弟子": (547, 178), "轩辕剑灵": (367, 250), "张校尉": (163, 479),
    "月盈": (120, 191),
    "引路蚌精": (413, 306), "传送使": (433, 207), "接引仙女": (562, 267),
    "引路小妖": (572, 187), "传送小鬼": (279, 179), "引路雪舞": (199, 197),
    "引路狐精": (201, 241), "传送道童": (439, 382), "传送道士": (315, 255),
    "引路山精": (193, 190), "传送仙子": (560, 162), "引路灵猿": (654, 453)
}

# 地图比例 (窗口起始X, 窗口起始Y, 比例X, 比例Y)
MAP_RATIO = {
    "帮派地图": (79, 511, 3.395, -3.384), "长安城": (73, 492, 1.191, -1.185),
    "傲来国": (123, 507, 3.469, -3.458), "青河镇": (142, 493, 3.231, -3.225),
    "临仙镇": (102, 478, 2.985, -2.975), "女儿国": (143, 492, 3.219, -3.208),
}

# 路径终点坐标
PATH_POS = {"长安城-长安城外": (724, 488), "长安城-佛门": (502, 110),
            "长安城-天策": (76, 352), "长安城-大唐国境": (-1, "长安城驿站老板"),
            "长安城-金銮殿": (110, 162), "长安城-金悦院": (712, 294),
            "长安城-长安当铺": (626, 399), "长安城-长安药店": (597, 384),
            "长安城-长安武器店": (660, 358), "长安城-长安服饰店": (675, 424),
            "长安城-长安杂货店": (650, 411), "长安城-大雁塔一层": (594, 123),
            "长安城外-长安城": (76, 123), "长安城外-青河镇": (716, 121),
            "青河镇-长安城外": (-1, "张校尉"), "青河镇-青河镇外": (612, 125),
            "青河镇-青河药店": (452, 397), "青河镇-青河武器店": (462, 122),
            "青河镇-青河服饰店": (562, 335), "青河镇-青河村长家": (272, 132),
            "青河镇外-青河镇": (129, 101), "青河镇外-傲来国": (-1, "青河镇外船夫"),
            "青河镇外-东海龙宫": (-1, "鱼精"), "青河镇外-神秘洞窟": (506, 141),
            "东海龙宫-水晶宫": (350, 286), "东海龙宫-长安城": (-1, "引路蚌精"),
            "东海龙宫-东海幻境": (175, 469), "东海龙宫-东海迷宫一层": (691, 205),
            "水晶宫-东海龙宫": (613, 433),
            "傲来国-天魔里": (667, 105), "傲来国-花果山": (132, 499),
            "傲来国-青河镇外": (-1, "傲来国船夫"), "傲来国-长安城": (-1, "傲来国驿站老板"),
            "傲来国-傲来武器店": (623, 241), "傲来国-傲来服饰店": (460, 165),
            "天魔里-傲来国": (495, 510), "天魔里-云隐阁": (487, 164), "天魔里-长安城": (-1, "传送使"),
            "云隐阁-天魔里": (217, 432),
            "佛门-长安城": (96, 479), "佛门-大雄宝殿": (418, 276),
            "大雄宝殿-佛门": (204, 440),
            "天策-程府": (231, 188), "天策-长安城": (666, 502),
            "程府-天策": (609, 454),
            "大唐国境-南海普陀": (-1, "仙女"), "大唐国境-大唐境外": (158, 83),
            "大唐国境-长安城": (-1, "国境驿站老板"),
            "南海普陀-大唐国境": (163, 475), "南海普陀-长安城": (-1, "接引仙女"),
            "大唐境外-女儿国": (-1, "女儿国驿使"), "大唐境外-幽冥地府": (283, 409),
            "大唐境外-乌斯藏": (107, 438), "大唐境外-大唐国境": (690, 458),
            "大唐境外-盘丝岭": (691, 164), "大唐境外-无名谷": (-1, "月盈"),
            "大唐境外-寒冰宫一层": (108, 140),
            "女儿国-大唐境外": (649, 457), "女儿国-子母河畔": (155, 464),
            "盘丝岭-盘丝洞": (588, 129), "盘丝岭-大唐境外": (161, 477),
            "盘丝岭-长安城": (-1, "引路小妖"), "盘丝洞-盘丝岭": (200, 447),
            "幽冥地府-森罗殿": (211, 147), "幽冥地府-大唐境外": (591, 514),
            "幽冥地府-长安城": (-1, "传送小鬼"), "幽冥地府-地狱迷宫一层": (596, 147),
            "森罗殿-幽冥地府": (602, 448),
            "无名谷-大唐境外": (643, 460), "无名谷-长安城": (-1, "引路雪舞"),
            "乌斯藏-魔王山": (132, 172), "乌斯藏-大唐境外": (674, 154),
            "乌斯藏-镇元五庄": (427, 162), "乌斯藏-长安城": (-1, "乌斯藏驿站老板"),
            "乌斯藏-万兽岭": (105, 425), "乌斯藏-临仙镇": (106, 347),
            "魔王山-乌斯藏": (630, 471), "魔王山-长安城": (-1, "引路狐精"),
            "镇元五庄-乾坤殿": (398, 323), "镇元五庄-乌斯藏": (691, 516),
            "镇元五庄-长安城": (-1, "传送道童"),
            "乾坤殿-镇元五庄": (603, 449),
            "临仙镇-乌斯藏": (635, 464), "临仙镇-七星方寸": (131, 125),
            "临仙镇-昆仑山": (634, 127), "临仙镇-临仙武器店": (285, 407),
            "临仙镇-临仙服饰店": (150, 326),
            "七星方寸-长安城": (-1, "传送道士"), "七星方寸-临仙镇": (597, 481),
            "七星方寸-灵台宫": (314, 203), "七星方寸-灵剑峰": (-1, "护剑弟子"),
            "灵台宫-七星方寸": (605, 437),
            "万兽岭-乌斯藏": (691, 194), "万兽岭-长安城": (-1, "引路山精"),
            "万兽岭-狮王洞": (128, 180), "万兽岭-平顶山": (-1, "引路灵猿"),
            "狮王洞-万兽岭": (600, 446),
            "昆仑山-北冥": (241, 103), "昆仑山-临仙镇": (215, 500),
            "昆仑山-花果山": (-1, "土地公公"), "昆仑山-凌霄天宫": (590, 96),
            "昆仑山-上古战场": (-1, "轩辕剑灵"),
            "北冥-昆仑山": (525, 469), "北冥-琉璃多宝塔一层": (236, 399),
            "凌霄天宫-昆仑山": (135, 494), "凌霄天宫-凌霄殿": (620, 138),
            "凌霄天宫-长安城": (-1, "传送仙子"), "凌霄天宫-广寒宫": (-1, "月宫侍女"),
            "凌霄殿-凌霄天宫": (200, 440),
            "花果山-傲来国": (686, 133), "花果山-昆仑山": (-1, "猴精"), "花果山-水帘洞": (417, 294),
            "水帘洞-神弃平原": (561, 209),
            "神弃平原-水帘洞": (180, 397),
            "大雁塔一层-大雁塔二层": (226, 254), "大雁塔二层-大雁塔三层": (469, 143),
            "大雁塔三层-大雁塔四层": (222, 332), "大雁塔四层-大雁塔五层": (560, 172),
            "大雁塔五层-大雁塔六层": (222, 349),
            "东海迷宫一层-东海迷宫二层": (638, 476), "东海迷宫二层-东海迷宫三层": (673, 451),
            "地狱迷宫一层-地狱迷宫二层": (567, 98), "地狱迷宫二层-地狱迷宫三层": (566, 117),
            "琉璃多宝塔一层-琉璃多宝塔二层": (207, 195), "琉璃多宝塔二层-琉璃多宝塔三层": (166, 181),
            "寒冰宫一层-寒冰宫二层": (111, 112), "寒冰宫二层-寒冰宫三层": (113, 515),
            "子母河畔-桃花岛": (637, 439),
            "镖局-长安城": (793, 553),
            "民居-大唐国境": (400, 540)}

# 图片_地图
PIC_MAP = "七星方寸.bmp|万兽岭.bmp|上古战场.bmp|东宫.bmp|东海幻境.bmp|东海迷宫一层.bmp|东海迷宫三层.bmp|东海迷宫二层.bmp|" \
          "东海龙宫.bmp|临仙服饰店.bmp|临仙武器店.bmp|临仙镇.bmp|乌斯藏.bmp|乾坤殿.bmp|云隐阁.bmp|佛门.bmp|傲来国.bmp|" \
          "傲来服饰店.bmp|傲来武器店.bmp|傲来神殿.bmp|其它阵.bmp|农产区.bmp|准备厅.bmp|凌霄天宫.bmp|凌霄殿.bmp|北冥.bmp|" \
          "南海普陀.bmp|后备营地.bmp|圣火城.bmp|地狱迷宫一层.bmp|地狱迷宫三层.bmp|地狱迷宫二层.bmp|地藏王府.bmp|大唐国境.bmp|" \
          "大唐境外.bmp|大雁塔一层.bmp|大雁塔三层.bmp|大雁塔二层.bmp|大雁塔五层.bmp|大雁塔六层.bmp|大雁塔四层.bmp|大雄宝殿.bmp|" \
          "天策.bmp|天魔里.bmp|太极殿.bmp|女儿国.bmp|子母河畔.bmp|寒冰宫一层.bmp|寒冰宫三层.bmp|寒冰宫二层.bmp|山寨大厅.bmp|" \
          "山巅神殿.bmp|帮派地图.bmp|帮派庭院.bmp|平顶山.bmp|幽冥地府.bmp|广寒宫.bmp|心之阵.bmp|无名村落.bmp|无名谷.bmp|" \
          "昆仑山.bmp|桃花岛.bmp|森罗殿.bmp|水帘洞.bmp|水晶宫.bmp|海底迷宫.bmp|火魂先锋营.bmp|灵剑峰.bmp|灵台宫.bmp|" \
          "灵狐乐园.bmp|燧明大帐.bmp|狮王洞.bmp|琉璃多宝塔一层.bmp|琉璃多宝塔三层.bmp|琉璃多宝塔二层.bmp|白骨岭.bmp|白骨洞.bmp|" \
          "盘丝岭.bmp|盘丝洞.bmp|神弃平原.bmp|神秘洞窟.bmp|神秘谷地.bmp|秦王府.bmp|程府.bmp|经商之路.bmp|花果山.bmp|" \
          "蛮荒山.bmp|血吼深渊.bmp|辎重库.bmp|边境秘营.bmp|酆都城.bmp|金悦院.bmp|金銮殿.bmp|铸剑坊.bmp|镇元五庄.bmp|镖局.bmp|" \
          "长安.bmp|长安3.bmp|长安10.bmp|长安城.bmp|长安城外.bmp|长安当铺.bmp|长安服饰店.bmp|长安杂货店.bmp|长安武器店.bmp|" \
          "长安药店.bmp|隐蔽溪谷.bmp|青河服饰店.bmp|青河村长家.bmp|青河武器店.bmp|青河药店.bmp|青河镇.bmp|青河镇外.bmp|" \
          "风牧荒原.bmp|高老庄.bmp|魍魉栈道.bmp|魔王山.bmp|龙宫副本.bmp|龙宫副本1.bmp|民居.bmp|民房.bmp"

# 图片_装备灵
PIC_ZB_LING = "物_swb_短棒之灵.bmp|物_swb_法珠之灵.bmp|物_swb_利剑之灵.bmp|物_swb_男帽之灵.bmp|物_swb_男鞋之灵.bmp|" \
              "物_swb_男衣之灵.bmp|物_swb_女帽之灵.bmp|物_swb_女鞋之灵.bmp|物_swb_女衣之灵.bmp|物_swb_朴刀之灵.bmp|" \
              "物_swb_枪戟之灵.bmp|物_swb_双环之灵.bmp|物_swb_唐刀之灵.bmp|物_swb_项链之灵.bmp|物_swb_腰带之灵.bmp|" \
              "物_swb_长鞭之灵.bmp|物_swb_折扇之灵.bmp"

# 图片_鱼
PIC_FISH = "可收藏.bmp|物_Fish_01.bmp|物_Fish_02.bmp|物_Fish_03.bmp|物_Fish_04.bmp|物_Fish_05.bmp|物_Fish_06.bmp|" \
           "物_Fish_07.bmp|物_Fish_08.bmp|物_Fish_09.bmp|物_Fish_10.bmp|物_Fish_11.bmp|物_Fish_12.bmp|物_Fish_13.bmp|" \
           "物_Fish_14.bmp|物_Fish_15.bmp"

# 副本地图
MAP_FU_BEN = {
    "高老庄", "山寨大厅", "龙宫副本", "龙宫副本1", "海底迷宫", "地藏王府", "酆都城", "白骨岭", "白骨洞", "长安", "长安3",
    "长安10", "东宫", "太极殿", "秦王府", "血吼深渊", "圣火城", "其它阵", "心之阵", "后备营地", "燧明大帐",
    "隐蔽溪谷", "辎重库", "风牧荒原", "农产区", "火魂先锋营", "魍魉栈道", "山巅神殿", "无名村落", "神秘谷地", "铸剑坊"
}

# 运镖地图
MAP_YUN_BIAO = {
    "东海龙宫", "天魔里", "佛门", "天策", "南海普陀", "盘丝岭", "幽冥地府", "无名谷", "魔王山", "镇元五庄",
    "七星方寸", "万兽岭", "凌霄天宫", "水晶宫", "云隐阁", "大雄宝殿", "程府", "乾坤殿", "盘丝洞", "森罗殿",
    "灵台宫", "狮王洞", "凌霄殿", "女儿国", "长安城外", "青河镇", "青河镇外", "傲来国", "大唐国境", "昆仑山",
    "北冥", "花果山", "临仙镇", "乌斯藏", "大唐境外", "长安城", "镖局", "民居",
}

# 药品
YAO_PIN = {"豆腐", "五加皮", "金疮药", "升丹", "归魂露", "金银花", "金钱草", "土当归",
           "苦地丁", "锦灯笼", "车前草", "款冬花", "过路黄", "吕宋果"}
# 杂货
ZA_HUO = {"高级宠物口粮", "驱魔香", "传送符", "萤光草", "梅花镖", "宠物口粮", "摄魂石"}
# 0,20级服饰
FU_SHI_0_20 = {"粗布帽", "虹布巾", "虹布衣", "花布衣", "布靴", "虹布鞋", "燧石项链", "帆布腰带",
               "绫罗衣", "熊皮帽", "熊皮甲", "桃木簪", "熊皮靴", "巾帼靴", "牛骨项链", "熊皮腰带"}
# 0,20级武器
WU_QI_0_20 = {"粗制唐刀", "寒铁唐刀", "玄铁刀", "青铜剑", "红缨枪", "檀木扇", "粗制藤鞭", "软木棒", "玄铁法珠",
              "护手双环", "雀尾扇", "寒犀刀", "青冥剑", "破甲枪", "翠竹鞭", "蛇形棒", "赤金法珠", "尖刺双环"}
# 10级服饰
FU_SHI_10 = {"虎皮帽", "淑芳巾", "虎皮甲", "紫岚衣", "虎皮靴", "绣花鞋", "狼牙项链", "虎皮腰带"}
# 10级武器
WU_QI_10 = {"精炼唐刀", "斩马刀", "诛雀剑", "白杆枪", "幻蝶扇", "精制皮鞭", "青藤棒", "黄玉法珠", "青铜双环"}
# 30级服饰
FU_SHI_30 = {"檀木簪", "刺钢盔", "铁锁环甲", "霜月衣", "破冰履", "凌风靴", "琉璃项链", "烙牙腰带"}
# 30级武器
WU_QI_30 = {"青铜唐刀", "贯心刀", "穿心剑", "岚风枪", "铁鸳鸯", "蝠翼双环", "九节钢鞭", "盘龙棒", "碧波法珠"}
# 40级服饰
FU_SHI_40 = {"白驹履", "羽麟帽", "银光簪", "墨麒胸甲", "霓裳衣", "霓虹鞋", "孔雀石链", "鳄鳞腰带"}
# 40级武器
WU_QI_40 = {"银光唐刀", "碧水刀", "星魂剑", "雷鸣枪", "象牙红", "蛇形骨鞭", "墨玉棒", "飞燕法珠", "狼牙双环"}
# 二级药
ER_JI_YAO = {"也白头", "松节", "灵芝", "龙尾骨", "药神花", "贝母花", "紫冥果", "麻黄", "绿莲散", "赤石脂",
             "七星草", "紫花兰", "蛇胆", "长寿果", "血玛瑙", "山长青", "奇异果", "月月花", "叶上珠"}
# 三级药
SAN_JI_YAO = {"血还丹", "还灵散", "济生丸", "逍遥散", "乾坤丹", "玉蟾丸", "驱魔丹", "灵心丸", "聚元丹",
              "九转还魂丹"}
# 烹饪
PENG_REN = {"珍露酒", "蛇胆酒", "百味酒", "醉生梦死", "女儿红", "叫花鸡", "五味羹", "玉琼浆", "佛跳墙",
            "长寿面", "踏雪燕窝", "玉蓉糕", "香辣蟹", "八宝粥", "珍珠丸子", "脆皮乳猪"}
# 食品
SHI_PIN = {"霞光宝塔", "八仙过海", "海外仙山", "凉拌杂丝", "美味拼盘", "狮子头"}
# 古董
GU_DONG = {"玉凤形佩", "千佛像", "杜虎符", "金臂钏", "乐府钟", "长明灯", "碧玉戈", "莲鹤方壶", "七弦古琴",
           "四羊方尊"}
# 家具
JIA_JU = {"蒲草席", "青竹凳", "漆花竹桌", "雕花屏风", "孔雀姬", "君子兰", "水仙", "金钱树", "青山绿水图",
          "桦木床", "红釉描金瓶", "太极无忧榻", "云中莲", "毛皮地毯", "铜制仕女宫灯", "红木雕花椅",
          "红木瓷面八仙桌", "檀木玉面桌", "猛虎下山图", "檀香立柜", "仕女图屏风", "流云地毯", "仙鹤图屏风",
          "沐光笼", "八骏图", "香木凳", "橡木地板", "青瓷竹叶瓶", "鸾凤和鸣灯", "银质立式烛台", "双色软绸帘",
          "双鲤戏珠柜", "桐木立柜", "皂缎流苏帘", "仙鹤扶摇帘"}
# 庭院装饰
TING_YUAN = {"大理石桌", "青砂盆", "银杏盆景", "金雀盆景", "石制影壁", "关山白", "珊瑚草", "秋木蕨", "石桌",
             "石凳", "小水池", "牵机藤", "仙人掌", "石制院灯", "大理石影壁", "紫丁香", "篱笆花圃", "紫金菊",
             "酒葫芦", "普通盆栽", "竹制宠屋", "灯笼花", "铁算盘", "映山红", "金边莲", "翠云竹", "三叶菊",
             "珍珠梅", "七星海", "红云桂", "青石凳", "天竺兰", "小池塘", "棕榈", "掌中峰", "木制院门"}

# 人机验证相关
PIC_PIN_TU = """\
pt000a.bmp|pt000b.bmp|pt000c.bmp|pt000d.bmp|pt001a.bmp|pt001b.bmp|pt001c.bmp|pt001d.bmp|pt002a.bmp|pt002b.bmp|pt002c.bmp|pt002d.bmp|pt003a.bmp|pt003b.bmp|pt003c.bmp|pt003d.bmp|pt004a.bmp|pt004b.bmp|pt004c.bmp|pt004d.bmp|pt005a.bmp|pt005b.bmp|pt005c.bmp|pt005d.bmp|pt006a.bmp|pt006b.bmp|pt006c.bmp|pt006d.bmp|pt007a.bmp|pt007b.bmp|pt007c.bmp|pt007d.bmp|pt008a.bmp|pt008b.bmp|pt008c.bmp|pt008d.bmp|pt009a.bmp|pt009b.bmp|pt009c.bmp|pt009d.bmp|\
pt010a.bmp|pt010b.bmp|pt010c.bmp|pt010d.bmp|pt011a.bmp|pt011b.bmp|pt011c.bmp|pt011d.bmp|pt012a.bmp|pt012b.bmp|pt012c.bmp|pt012d.bmp|pt013a.bmp|pt013b.bmp|pt013c.bmp|pt013d.bmp|pt014a.bmp|pt014b.bmp|pt014c.bmp|pt014d.bmp|pt015a.bmp|pt015b.bmp|pt015c.bmp|pt015d.bmp|pt016a.bmp|pt016b.bmp|pt016c.bmp|pt016d.bmp|pt017a.bmp|pt017b.bmp|pt017c.bmp|pt017d.bmp|pt018a.bmp|pt018b.bmp|pt018c.bmp|pt018d.bmp|pt019a.bmp|pt019b.bmp|pt019c.bmp|pt019d.bmp|\
pt020a.bmp|pt020b.bmp|pt020c.bmp|pt020d.bmp|pt021a.bmp|pt021b.bmp|pt021c.bmp|pt021d.bmp|pt022a.bmp|pt022b.bmp|pt022c.bmp|pt022d.bmp|pt023a.bmp|pt023b.bmp|pt023c.bmp|pt023d.bmp|pt024a.bmp|pt024b.bmp|pt024c.bmp|pt024d.bmp|pt025a.bmp|pt025b.bmp|pt025c.bmp|pt025d.bmp|pt026a.bmp|pt026b.bmp|pt026c.bmp|pt026d.bmp|pt027a.bmp|pt027b.bmp|pt027c.bmp|pt027d.bmp|pt028a.bmp|pt028b.bmp|pt028c.bmp|pt028d.bmp|pt029a.bmp|pt029b.bmp|pt029c.bmp|pt029d.bmp|\
pt030a.bmp|pt030b.bmp|pt030c.bmp|pt030d.bmp|pt031a.bmp|pt031b.bmp|pt031c.bmp|pt031d.bmp|pt032a.bmp|pt032b.bmp|pt032c.bmp|pt032d.bmp|pt033a.bmp|pt033b.bmp|pt033c.bmp|pt033d.bmp|pt034a.bmp|pt034b.bmp|pt034c.bmp|pt034d.bmp|pt035a.bmp|pt035b.bmp|pt035c.bmp|pt035d.bmp|pt036a.bmp|pt036b.bmp|pt036c.bmp|pt036d.bmp|pt037a.bmp|pt037b.bmp|pt037c.bmp|pt037d.bmp|pt038a.bmp|pt038b.bmp|pt038c.bmp|pt038d.bmp|pt039a.bmp|pt039b.bmp|pt039c.bmp|pt039d.bmp|\
pt040a.bmp|pt040b.bmp|pt040c.bmp|pt040d.bmp|pt041a.bmp|pt041b.bmp|pt041c.bmp|pt041d.bmp|pt042a.bmp|pt042b.bmp|pt042c.bmp|pt042d.bmp|pt043a.bmp|pt043b.bmp|pt043c.bmp|pt043d.bmp|pt044a.bmp|pt044b.bmp|pt044c.bmp|pt044d.bmp|pt045a.bmp|pt045b.bmp|pt045c.bmp|pt045d.bmp|pt046a.bmp|pt046b.bmp|pt046c.bmp|pt046d.bmp|pt047a.bmp|pt047b.bmp|pt047c.bmp|pt047d.bmp|pt048a.bmp|pt048b.bmp|pt048c.bmp|pt048d.bmp|pt049a.bmp|pt049b.bmp|pt049c.bmp|pt049d.bmp|\
pt050a.bmp|pt050b.bmp|pt050c.bmp|pt050d.bmp|pt051a.bmp|pt051b.bmp|pt051c.bmp|pt051d.bmp|pt052a.bmp|pt052b.bmp|pt052c.bmp|pt052d.bmp|pt053a.bmp|pt053b.bmp|pt053c.bmp|pt053d.bmp|pt054a.bmp|pt054b.bmp|pt054c.bmp|pt054d.bmp|pt055a.bmp|pt055b.bmp|pt055c.bmp|pt055d.bmp|pt056a.bmp|pt056b.bmp|pt056c.bmp|pt056d.bmp|pt057a.bmp|pt057b.bmp|pt057c.bmp|pt057d.bmp|pt058a.bmp|pt058b.bmp|pt058c.bmp|pt058d.bmp|pt059a.bmp|pt059b.bmp|pt059c.bmp|pt059d.bmp|\
pt060a.bmp|pt060b.bmp|pt060c.bmp|pt060d.bmp|pt061a.bmp|pt061b.bmp|pt061c.bmp|pt061d.bmp|pt062a.bmp|pt062b.bmp|pt062c.bmp|pt062d.bmp|pt063a.bmp|pt063b.bmp|pt063c.bmp|pt063d.bmp|pt064a.bmp|pt064b.bmp|pt064c.bmp|pt064d.bmp|pt065a.bmp|pt065b.bmp|pt065c.bmp|pt065d.bmp|pt066a.bmp|pt066b.bmp|pt066c.bmp|pt066d.bmp|pt067a.bmp|pt067b.bmp|pt067c.bmp|pt067d.bmp|pt068a.bmp|pt068b.bmp|pt068c.bmp|pt068d.bmp|pt069a.bmp|pt069b.bmp|pt069c.bmp|pt069d.bmp|\
pt070a.bmp|pt070b.bmp|pt070c.bmp|pt070d.bmp|pt071a.bmp|pt071b.bmp|pt071c.bmp|pt071d.bmp|pt072a.bmp|pt072b.bmp|pt072c.bmp|pt072d.bmp|pt073a.bmp|pt073b.bmp|pt073c.bmp|pt073d.bmp|pt074a.bmp|pt074b.bmp|pt074c.bmp|pt074d.bmp|pt075a.bmp|pt075b.bmp|pt075c.bmp|pt075d.bmp|pt076a.bmp|pt076b.bmp|pt076c.bmp|pt076d.bmp|pt077a.bmp|pt077b.bmp|pt077c.bmp|pt077d.bmp|pt078a.bmp|pt078b.bmp|pt078c.bmp|pt078d.bmp|pt079a.bmp|pt079b.bmp|pt079c.bmp|pt079d.bmp|\
pt080a.bmp|pt080b.bmp|pt080c.bmp|pt080d.bmp|pt081a.bmp|pt081b.bmp|pt081c.bmp|pt081d.bmp|pt082a.bmp|pt082b.bmp|pt082c.bmp|pt082d.bmp|pt083a.bmp|pt083b.bmp|pt083c.bmp|pt083d.bmp|pt084a.bmp|pt084b.bmp|pt084c.bmp|pt084d.bmp|pt085a.bmp|pt085b.bmp|pt085c.bmp|pt085d.bmp|pt086a.bmp|pt086b.bmp|pt086c.bmp|pt086d.bmp|pt087a.bmp|pt087b.bmp|pt087c.bmp|pt087d.bmp|pt088a.bmp|pt088b.bmp|pt088c.bmp|pt088d.bmp|pt089a.bmp|pt089b.bmp|pt089c.bmp|pt089d.bmp|\
pt090a.bmp|pt090b.bmp|pt090c.bmp|pt090d.bmp|pt091a.bmp|pt091b.bmp|pt091c.bmp|pt091d.bmp|pt092a.bmp|pt092b.bmp|pt092c.bmp|pt092d.bmp|pt093a.bmp|pt093b.bmp|pt093c.bmp|pt093d.bmp|pt094a.bmp|pt094b.bmp|pt094c.bmp|pt094d.bmp|pt095a.bmp|pt095b.bmp|pt095c.bmp|pt095d.bmp|pt096a.bmp|pt096b.bmp|pt096c.bmp|pt096d.bmp|pt097a.bmp|pt097b.bmp|pt097c.bmp|pt097d.bmp|pt098a.bmp|pt098b.bmp|pt098c.bmp|pt098d.bmp|pt099a.bmp|pt099b.bmp|pt099c.bmp|pt099d.bmp|\
pt100a.bmp|pt100b.bmp|pt100c.bmp|pt100d.bmp|pt101a.bmp|pt101b.bmp|pt101c.bmp|pt101d.bmp|pt102a.bmp|pt102b.bmp|pt102c.bmp|pt102d.bmp|pt103a.bmp|pt103b.bmp|pt103c.bmp|pt103d.bmp|pt104a.bmp|pt104b.bmp|pt104c.bmp|pt104d.bmp|pt105a.bmp|pt105b.bmp|pt105c.bmp|pt105d.bmp|pt106a.bmp|pt106b.bmp|pt106c.bmp|pt106d.bmp|pt107a.bmp|pt107b.bmp|pt107c.bmp|pt107d.bmp|pt108a.bmp|pt108b.bmp|pt108c.bmp|pt108d.bmp|pt109a.bmp|pt109b.bmp|pt109c.bmp|pt109d.bmp|\
pt110a.bmp|pt110b.bmp|pt110c.bmp|pt110d.bmp|pt111a.bmp|pt111b.bmp|pt111c.bmp|pt111d.bmp|pt112a.bmp|pt112b.bmp|pt112c.bmp|pt112d.bmp|pt113a.bmp|pt113b.bmp|pt113c.bmp|pt113d.bmp|pt114a.bmp|pt114b.bmp|pt114c.bmp|pt114d.bmp|pt115a.bmp|pt115b.bmp|pt115c.bmp|pt115d.bmp|pt116a.bmp|pt116b.bmp|pt116c.bmp|pt116d.bmp|pt117a.bmp|pt117b.bmp|pt117c.bmp|pt117d.bmp|pt118a.bmp|pt118b.bmp|pt118c.bmp|pt118d.bmp|pt119a.bmp|pt119b.bmp|pt119c.bmp|pt119d.bmp|\
pt120a.bmp|pt120b.bmp|pt120c.bmp|pt120d.bmp|pt121a.bmp|pt121b.bmp|pt121c.bmp|pt121d.bmp|pt122a.bmp|pt122b.bmp|pt122c.bmp|pt122d.bmp|pt123a.bmp|pt123b.bmp|pt123c.bmp|pt123d.bmp\
"""

# 验证背景图
PIC_BACKGROUND = []
for idx in range(5):
    with open(f"{lib.DIR_DLL}\\{idx}.bin", "rb") as f:
        com_bytes = f.read()
        decom_bytes = zlib.decompress(com_bytes)
        PIC_BACKGROUND.append(decom_bytes.decode("utf-8"))

PI = 3.14159
LENGTH_AUTH_CLOCK = 30
NUM_ROTATE_FRAME = 6
AUTH_HW_X = 201  # 换位验证_左上角起始点X
AUTH_HW_Y = 266  # 换位验证_左上角起始点Y
AUTH_HW_W = 180  # 换位验证_每幅图宽
AUTH_HW_H = 50  # 换位验证_每幅图高

COLOR_AUTH_CLOCK_TIME = "202020-222222"
COLOR_AUTH_ROTATE_KEYWORD = "ffff00-333333"

POS_AUTH_REFRESH = (330, 35)
POS_AUTH_CLOCK_CENTER = (189.5, 165.5)
POS_AUTH_SLIDER_START = (56, 333)
POS_AUTH_LD_CONFIRM = (394, 326)

RECT_AUTH_LONG = (132, 208, 671, 237)
RECT_AUTH_LONG_TITLE = (172, 207, 630, 270)
RECT_AUTH_LONG_ITEM = (164, 263, 641, 389)
RECT_AUTH_SQUA = (209, 118, 594, 153)
RECT_AUTH_SQUA_TITLE = (223, 120, 575, 190)
RECT_AUTH_SQUA_ITEM = (276, 201, 543, 483)
RECT_AUTH_LONG_CAP1 = (162, 234, 262, 399)
RECT_AUTH_LONG_CAP2 = (282, 234, 382, 399)
RECT_AUTH_LONG_CAP3 = (408, 234, 508, 399)
RECT_AUTH_LONG_CAP4 = (540, 234, 640, 399)
RECT_AUTH_SQUA_CAP1 = (276, 165, 376, 320)
RECT_AUTH_SQUA_CAP2 = (436, 165, 536, 320)
RECT_AUTH_SQUA_CAP3 = (276, 330, 376, 485)
RECT_AUTH_SQUA_CAP4 = (436, 330, 536, 485)
RECT_AUTH_PT_Q = (342, 185, 489, 278)
RECT_AUTH_PT_A = (260, 291, 543, 432)
RECT_AUTH_FULL = (0, 0, 380, 354)
RECT_AUTH_CLOCK = (197, 269, 255, 291)
RECT_AUTH_PIC = (30, 66, 350, 266)  # 背景图片

CLOCK_POS_LIST_L30 = [(190, 136), (193, 136), (196, 136), (199, 137), (202, 138), (204, 140), (207, 141), (210, 143),
                      (212, 145), (214, 148), (215, 150), (217, 153), (218, 156), (219, 159), (219, 162), (219, 165),
                      (219, 169), (219, 172), (218, 175), (217, 178), (215, 180), (214, 183), (212, 186), (210, 188),
                      (207, 190), (205, 191), (202, 193), (199, 194), (196, 195), (193, 195), (190, 195), (186, 195),
                      (183, 195), (180, 194), (177, 193), (175, 191), (172, 190), (169, 188), (167, 186), (165, 183),
                      (164, 181), (162, 178), (161, 175), (160, 172), (160, 169), (160, 166), (160, 162), (160, 159),
                      (161, 156), (162, 153), (164, 151), (165, 148), (167, 145), (169, 143), (172, 141), (174, 140),
                      (177, 138), (180, 137), (183, 136), (186, 136)]

# 成语集
PHRASE_SET = {
    "喜出望外", "自强不息", "别有用心", "承前启后", "承上启下", "足不出户", "无与伦比", "疑难杂症", "莫名其妙", "举足轻重", "显而易见", "旗帜鲜明", "以身作则",
    "扬长而去", "手足无措", "急急如律令", "独立自主", "振奋人心", "不可思议", "不知所措", "家常便饭", "别出心裁", "志同道合", "喜闻乐见", "身无分文", "日新月异",
    "四通八达", "卷土重来", "勇往直前", "货真价实", "刮目相看", "人不可貌相", "机不可失", "枪打出头鸟", "见义勇为", "不厌其烦", "山清水秀", "无可争辩", "并肩作战",
    "绞尽脑汁", "如愿以偿", "雨后春笋", "毫不动摇", "时势造英雄", "无微不至", "博大精深", "德才兼备", "风云变幻", "取长补短", "雨霖铃", "改头换面", "遍地开花",
    "迫在眉睫", "何乐而不为", "畅通无阻", "安居乐业", "出谋划策", "不约而同", "排忧解难", "因地制宜", "吃力不讨好", "独善其身", "虞美人", "坚持不懈", "截然不同",
    "情不自禁", "浣溪沙", "无人问津", "心中有数", "总而言之", "救死扶伤", "老大徒伤悲", "自食其力", "水落石出", "势在必行", "春暖花开", "成千上万", "掉以轻心",
    "天下无双", "难能可贵", "赞不绝口", "井然有序", "乱七八糟", "风雨无阻", "日久见人心", "蒙混过关", "微不足道", "水调歌头", "四海皆兄弟", "持之以恒", "流连忘返",
    "错落有致", "连锁反应", "欲速则不达", "不辱使命", "水土不服", "沁园春", "不亦乐乎", "满江红", "绳之以法", "循序渐进", "天翻地覆", "品学兼优", "五颜六色",
    "在所难免", "来龙去脉", "不可多得", "千丝万缕", "八九不离十", "量力而行", "迫不及待", "史无前例", "素不相识", "寸步难行", "蛮不讲理", "人满为患", "归根结底",
    "深思熟虑", "未雨绸缪", "千家万户", "首当其冲", "有生之年", "与日俱増", "长途跋涉", "大同小异", "近在咫尺", "蛛丝马迹", "名师出高徒", "先下手为强", "五花八门",
    "马不停蹄", "浪淘沙", "叹为观止", "前车之鉴", "昏迷不醒", "屈指可数", "天经地义", "出乎意料", "计以万数", "艰苦奋斗", "身临其境", "十八般武艺", "衣食住行",
    "大惊小怪", "顾名思义", "朽木不可雕", "不言而喻", "不甘示弱", "前所未有", "脱口而出", "助人为乐", "起早贪黑", "拾金不昧", "普天同庆", "取而代之", "记忆犹新",
    "重建家园", "随心所欲", "打草惊蛇", "引人注目", "推陈出新", "街头巷尾", "他乡遇故知", "恨铁不成钢", "物以稀为贵", "车水马龙", "顺理成章", "物美价廉", "自始至终",
    "学而时习之", "面目全非", "热情洋溢", "说三道四", "少年游", "大江南北", "无中生有", "变幻风云", "名不虚传", "接踵而至", "必由之路", "供不应求", "刻骨铭心",
    "名列前茅", "源远流长", "习以为常", "曾几何时", "无可厚非", "深入浅出", "燃眉之急", "不绝于耳", "指日可待", "猝不及防", "坐山观虎斗", "纷至沓来", "早出晚归",
    "世外桃源", "如梦令", "与众不同", "独木不成林", "畅所欲言", "热火朝天", "无独有偶", "慕名而来", "据为己有", "醉花阴", "从头到尾", "四面八方", "应运而生",
    "大张旗鼓", "大相径庭", "分秒争夺", "天壤之别", "聚精会神", "铿锵有力", "不可估量", "雪中送炭", "亡羊补牢", "与日俱增", "琳琅满目", "学以致用", "水到渠成",
    "恰到好处", "哭笑不得", "明目张胆", "拒之门外", "信以为真", "乐此不疲", "拭目以待", "有条不紊", "不谋而合", "不计其数", "惨不忍睹", "语重心长", "奋不顾身",
    "根深蒂固", "当务之急", "锲而不舍", "直言不讳", "潜移默化", "拳打脚踢", "难以置信", "图文并茂", "陷入僵局", "爱不释手", "自力更生", "不相上下", "络绎不绝",
    "无风不起浪", "新陈代谢", "雷厉风行", "精打细算", "直截了当", "了如指掌", "明察暗访", "当之无愧", "铺天盖地", "意味深长", "顺藤摸瓜", "不以为然", "视而不见",
    "建功立业", "瑞雪兆丰年", "大开眼界", "证据确凿", "入不敷出", "轻描淡写", "吃苦耐劳", "屡见不鲜", "相提并论", "得天独厚", "迎刃而解", "人去楼空", "众所周知",
    "无所适从", "朝气蓬勃", "名副其实", "轻而易举", "声声慢", "长此以往", "丰富多彩", "泣不成声", "惊心动魄", "梦寐以求", "脱颖而出", "西江月", "五湖四海",
    "真人不露相", "此起彼伏", "理直气壮", "有目共睹", "溃不成军", "目瞪口呆", "协心同力", "望江南", "司空见惯", "竭尽全力", "因人而异", "望而却步", "喜怒哀乐",
    "无能为力", "事半功倍", "义不容辞", "淋漓尽致", "不遗余力", "通俗易懂", "开门见山", "争先恐后", "座无虚席", "真相大白", "炙手可热", "趋之若鹜", "防患于未燃",
    "针锋相对", "落地生根", "快刀斩乱麻", "责无旁贷", "埋头苦干", "从天而降", "不失时机", "十万八千里", "清平调", "数以万计", "义无反顾", "坚定不移", "归根到底",
    "鲜为人知", "同心协力", "翻天覆地", "鹧鸪天", "水泄不通", "黄金时代", "不由自主"
}

AUTH_HW_X = 201  # 换位验证_左上角起始点X
AUTH_HW_Y = 266  # 换位验证_左上角起始点Y
AUTH_HW_W = 180  # 换位验证_每幅图宽
AUTH_HW_H = 50  # 换位验证_每幅图高
AUTH_HW_BGR_BACK = (155, 155, 124)  # 换位验证_背景颜色
AUTH_HW_POS = [
    (AUTH_HW_X + AUTH_HW_W // 2, AUTH_HW_Y + AUTH_HW_H // 2),
    (AUTH_HW_X + AUTH_HW_W + AUTH_HW_W // 2, AUTH_HW_Y + AUTH_HW_H // 2),
    (AUTH_HW_X + AUTH_HW_W // 2, AUTH_HW_Y + AUTH_HW_H + AUTH_HW_H // 2),
    (AUTH_HW_X + AUTH_HW_W + AUTH_HW_W // 2, AUTH_HW_Y + AUTH_HW_H + AUTH_HW_H // 2)
]

W_FK_SINGLE = 18  # 单个方块的像素宽度
W_FK_POS_FULL = 270  # 整个方块摆放区的宽高
NUM_FK = W_FK_POS_FULL // W_FK_SINGLE  # 方块摆放区每条边的方块数
POS_AUTH_FK_SEL = (120, 215)  # 方块选择区-左上角坐标
POS_AUTH_FK_POS = (392, 226)  # 方块摆放区-左上角坐标
RECT_AUTH_FK_SEL = (*POS_AUTH_FK_SEL, 385, 455)  # 方块选择区
RECT_AUTH_FK_POS = (*POS_AUTH_FK_POS, 662, 496)  # 方块摆放区
COLOR_AUTH_FK_SEL = "2E668A-202020"  # 方块选择区有效颜色
COLOR_AUTH_FK_POS = "47442E-101010"  # 方块摆放区有效颜色
COLOR_AUTH_FK_SUC = "b6a07d-000000"  # 方块摆放区摆放成功高亮颜色
