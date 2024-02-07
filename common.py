from biz.constants.constants import ZK_ALL
import lib


class Worker(lib.PluginSDK):
    def __init__(self, hwnd: int, obj, row: int):
        # 初始化Com类
        super().__init__(obj)
        # 设置图片和字库
        self.set_pic_pwd(lib.pwd_pic)
        self.set_dict_pwd(lib.pwd_zk)
        self.set_path(lib.DIR_RES)
        self.set_dict(ZK_ALL, "0全部.txt")
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
        info = f"{lib.cur_time_fmt} [{self.cur_task}] {info}"
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
