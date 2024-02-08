# 标准库
from ctypes import util
from threading import Thread
import time
import copy

# 第三方库
from PySide2.QtWidgets import QMainWindow, QLabel, QComboBox, QMenu, QTableWidgetItem, \
    QDialog, QTextBrowser, QHBoxLayout, QMessageBox, QSystemTrayIcon, QAction
from PySide2.QtGui import QCursor, QIcon, QTextCursor, QCloseEvent, QColor
from PySide2.QtCore import Signal, QTimer, Qt, QEvent

# 本地库
from ui.wnd_main import Ui_WndMain
import common
from call import ThreadExec
import utils
from utils.wnd import arrange_all_wnd, get_main_screen_wh
from utils.file import json_file_to_dict
from utils.msg_box import MyMsgBox, TimeMsgBox
from const import const
from utils.log import log
import settings


class WndMain(QMainWindow, Ui_WndMain):
    sig_info = Signal(int, int, str)
    sig_close = Signal()

    def __init__(self):
        super().__init__()
        # 安装界面
        self.setupUi(self)
        # 初始化自定义信号槽
        self.init_custom_sig_slot()
        # 初始化实例属性
        self.init_instance_field()
        # 初始化 界面控件
        self.init_widgets()
        # 初始化 菜单
        self.init_menus()
        # 初始化信号槽
        self.init_sig_slot()
        # 读取 主窗口配置
        self.cfg_read()
        # 设置为首页
        self.stack_widget.setCurrentIndex(0)
        # 显示欢迎信息
        self.show_info("初始化完成, 欢迎使用!")
        # 开启心跳线程
        # Thread(target=self.thd_heart_beat, daemon=True).start()

    def closeEvent(self, event: QCloseEvent):
        self.diag.close()
        # self.send_recv_offline()

    # 最小化到托盘区
    def changeEvent(self, event: QEvent):
        if event.type() == QEvent.WindowStateChange and self.isMinimized():
            self.hide()
            event.ignore()

    # 读取配置
    def cfg_read(self):
        settings.cfg_common = json_file_to_dict(
            const.PATH_SOFTWARE_COMMON, settings.cfg_common)
        # 通用设置
        self.cmb_mode.setCurrentText(settings.cfg_common.get("绑定模式", "模式0"))
        self.chk_ban_sys_sleep.setChecked(
            settings.cfg_common.get("禁用系统休眠", False))
        self.chk_ban_screen_protect.setChecked(
            settings.cfg_common.get("禁用屏幕保护", False))
        self.cmb_arrange_get_wnd.setCurrentText(
            settings.cfg_common.get("获取窗口后排列方式", "0"))
        self.cmb_set_plan_get_wnd.setCurrentText(
            settings.cfg_common.get("获取窗口后设置方案", "0"))
        self.cmb_set_plan_db_col.setCurrentText(
            settings.cfg_common.get("双击方案列设置方案", "0"))
        # 方案配置
        settings.cfg_plan_dict = json_file_to_dict(
            const.PATH_SOFTWARE_PLAN, settings.cfg_plan_dict)
        print("settings.cfg_plan_dict:", settings.cfg_plan_dict)
        for plan_name, cfg_plan_load in settings.cfg_plan_dict.items():
            # 逐个方案更新, 否则会直接替换整个cfg_plan
            if not settings.cfg_plan_dict.get(plan_name):  # 用户自定义的方案
                settings.cfg_plan_dict[plan_name] = copy.deepcopy(
                    settings.cfg_plan)  # 先读取默认方案
                self.lst_plan.addItem(plan_name)  # 添加到方案列表中
            # 用配置文件更新
            settings.cfg_plan_dict[plan_name].update(cfg_plan_load)
        else:  # 如果没有任何方案配置，则加入 ‘0内置默认’
            self.lst_plan.addItem('0内置默认')
            self.lst_plan.setCurrentRow(0)
            settings.cfg_plan_dict['0内置默认'] = self.get_plan_setting_dict()
        cur_plan = self.lst_plan.currentItem().text()
        cur_plan_dict = settings.cfg_plan_dict.get(cur_plan)
        self.set_plan_setting_dict(cur_plan_dict)

    # 保存配置
    def cfg_save(self):
        # 界面设置
        settings.cfg_common["绑定模式"] = self.cmb_mode.currentText()
        # 基本设置
        settings.cfg_common["禁用系统睡眠"] = self.chk_ban_sys_sleep.isChecked()
        settings.cfg_common["禁用屏幕保护"] = self.chk_ban_screen_protect.isChecked()
        settings.cfg_common["获取窗口后排列方式"] = self.cmb_arrange_get_wnd.currentText()
        settings.cfg_common["获取窗口后设置方案"] = self.cmb_set_plan_get_wnd.currentText()
        settings.cfg_common["双击方案列设置方案"] = self.cmb_set_plan_db_col.currentText()
        utils.dict_to_json_file(settings.cfg_common, const.PATH_SOFTWARE_COMMON)

    def init_custom_sig_slot(self):
        self.sig_info.connect(
            lambda row, col, info: self.tbe_console.item(
                row, col).setText(info)
        )
        self.sig_close.connect(lambda: self.close())

    def init_instance_field(self):
        # 定时器
        self.timer_cur = QTimer()  # 每隔1秒获取当前时间格式串
        self.timer_info = QTimer()  # 每隔10秒刷新小贴士信息
        self.timer_ds = QTimer()  # 每隔60秒检查是否到启动或定时的时间
        # info标签
        self.lbe_1 = QLabel("<提示> : ")
        self.lbe_info = QLabel("窗口初始化完成")
        # mode组合框
        self.lbe_2 = QLabel("绑定模式:")
        self.cmb_mode = QComboBox()
        # 日志窗口
        self.diag = QDialog(self)
        self.tbr_log = QTextBrowser(self.diag)
        self.form_lot = QHBoxLayout(self.diag)

    def init_widgets(self):
        # ------------------------- 窗口 -------------------------
        w, h = get_main_screen_wh()
        pos_x, pos_y = w - self.width() - 10, h - self.height() - 80
        self.move(pos_x, pos_y)
        self.setWindowTitle(f"版本号: {const.client_ver}")
        # ------------------------- 日志窗口 -------------------------
        self.diag.resize(460, 480)
        self.form_lot.addWidget(self.tbr_log)
        self.form_lot.setMargin(4)
        # ------------------------- 树列表 -------------------------
        self.tre_all.expandAll()
        # ------------------------- 状态栏 -------------------------
        self.status_bar.addWidget(self.lbe_1)
        self.status_bar.addWidget(self.lbe_info)
        self.status_bar.addPermanentWidget(self.lbe_2)
        self.status_bar.addPermanentWidget(self.cmb_mode)
        self.cmb_mode.addItem("模式0")  # [f"模式{i}" for i in range(5)]
        # ------------------------- 托盘区 -------------------------
        self.tray_icon = QSystemTrayIcon(self)
        self.tray_icon.setIcon(QIcon(":/rbt1.png"))
        self.tray_icon.show()
        # ------------------------- 表 格 -------------------------
        tbe_console = self.tbe_console
        h_header = tbe_console.horizontalHeader()
        v_header = tbe_console.verticalHeader()
        # 显示表头
        h_header.setVisible(True)
        v_header.setVisible(True)
        # 设置表格各列宽度
        h_header.resizeSection(const.COL_HWND, 80)
        h_header.resizeSection(const.COL_PLAN, 95)
        h_header.resizeSection(const.COL_RUN, 32)
        h_header.resizeSection(const.COL_PAUSE, 32)
        h_header.resizeSection(const.COL_END, 32)
        h_header.resizeSection(const.COL_LOG, 300)
        # 逐行添加项
        for row in range(const.TBE_CONSOLE_ROW):
            # 窗口句柄
            item = QTableWidgetItem()
            tbe_console.setItem(row, const.COL_HWND, item)
            tbe_console.item(row, const.COL_HWND).setTextAlignment(
                Qt.AlignHCenter | Qt.AlignVCenter)
            # 方案选择
            item = QTableWidgetItem()
            tbe_console.setItem(row, const.COL_PLAN, item)
            tbe_console.item(row, const.COL_PLAN).setTextAlignment(
                Qt.AlignHCenter | Qt.AlignVCenter)
            cmb_plan = QComboBox()
            settings.cmb_plan_list[row] = cmb_plan
            tbe_console.setCellWidget(row, const.COL_PLAN, cmb_plan)
            cmb_plan.setEnabled(False)
            # 运行
            item = QTableWidgetItem()
            tbe_console.setItem(row, const.COL_RUN, item)
            tbe_console.item(row, const.COL_RUN).setTextAlignment(
                Qt.AlignHCenter | Qt.AlignVCenter)
            # 暂停
            item = QTableWidgetItem()
            tbe_console.setItem(row, const.COL_PAUSE, item)
            tbe_console.item(row, const.COL_PAUSE).setTextAlignment(
                Qt.AlignHCenter | Qt.AlignVCenter)
            # 终止
            item = QTableWidgetItem()
            tbe_console.setItem(row, const.COL_END, item)
            tbe_console.item(row, const.COL_END).setTextAlignment(
                Qt.AlignHCenter | Qt.AlignVCenter)
            # 日志
            item = QTableWidgetItem()
            tbe_console.setItem(row, const.COL_LOG, item)
            tbe_console.item(row, const.COL_LOG).setTextAlignment(
                Qt.AlignHCenter | Qt.AlignVCenter)
            # 设置颜色
            if row in range(0, 5):
                color = QColor(243, 255, 246)
            elif row in range(5, 10):
                color = QColor(243, 246, 255)
            else:
                color = QColor(255, 246, 243)
            for col in range(const.TBE_CONSOLE_COL):
                tbe_console.item(row, col).setBackgroundColor(color)
        # ------------------------- 下拉框 -------------------------
        plan_list = settings.cfg_plan_dict.keys()
        for cmb_plan in settings.cmb_plan_list:
            cmb_plan.addItems(plan_list)
            cmb_plan.setCurrentIndex(-1)

    def init_menus(self):
        # ------------------- tbe_console设置右键菜单 -------------------
        self.tbe_console.setContextMenuPolicy(Qt.CustomContextMenu)
        self.menu_tbe_console = QMenu()
        self.action_get_all_wnd = QAction("获取所有窗口")
        self.action_clear_sel_wnd = QAction("清除选中窗口")
        self.action_hide_show_sel_wnd = QAction("隐藏/显示选中窗口")
        self.action_lock_unlock_sel_wnd = QAction("锁定/解锁选中窗口")
        self.action_force_exit_sel_wnd = QAction("强制退出选中窗口")
        self.action_all_set_plan = QAction("全部设为方案")  # 二级菜单
        self.action_arrange_all_wnd = QAction("排列所有窗口")  # 二级菜单
        self.menu_tbe_console.addAction(self.action_get_all_wnd)
        self.menu_tbe_console.addSeparator()
        self.menu_tbe_console.addAction(self.action_clear_sel_wnd)
        self.menu_tbe_console.addAction(self.action_hide_show_sel_wnd)
        self.menu_tbe_console.addAction(self.action_lock_unlock_sel_wnd)
        self.menu_tbe_console.addAction(self.action_force_exit_sel_wnd)
        self.menu_tbe_console.addSeparator()
        self.menu_tbe_console.addAction(self.action_all_set_plan)
        self.menu_tbe_console.addAction(self.action_arrange_all_wnd)
        # 二级菜单
        self.sub_menu_set_plan = QMenu()
        self.sub_action_plan0 = QAction("方案0")
        self.sub_action_plan1 = QAction("方案1")
        self.sub_action_plan2 = QAction("方案2")
        self.sub_action_plan3 = QAction("方案3")
        self.sub_menu_set_plan.addActions([self.sub_action_plan0,
                                           self.sub_action_plan1,
                                           self.sub_action_plan2,
                                           self.sub_action_plan3])
        self.sub_menu_arrange_wnd = QMenu()
        self.sub_action_method1 = QAction("方式1")
        self.sub_action_method2 = QAction("方式2")
        self.sub_action_method3 = QAction("方式3")
        self.sub_menu_arrange_wnd.addActions([self.sub_action_method1,
                                              self.sub_action_method2,
                                              self.sub_action_method3])
        self.action_all_set_plan.setMenu(self.sub_menu_set_plan)
        self.action_arrange_all_wnd.setMenu(self.sub_menu_arrange_wnd)
        self.tbe_console.customContextMenuRequested.connect(
            lambda: self.menu_tbe_console.exec_(QCursor.pos())
        )
        # 连接信号槽
        self.action_get_all_wnd.triggered.connect(
            self.on_action_get_all_wnd_triggered)
        self.action_clear_sel_wnd.triggered.connect(
            self.on_action_clear_sel_wnd_triggered)
        self.action_hide_show_sel_wnd.triggered.connect(
            self.on_action_hide_show_sel_wnd_triggered)
        self.action_lock_unlock_sel_wnd.triggered.connect(
            self.on_action_lock_unlock_sel_wnd_triggered)
        self.action_force_exit_sel_wnd.triggered.connect(
            self.on_action_force_exit_sel_wnd_triggered)
        self.sub_action_plan0.triggered.connect(
            lambda: self.one_key_set_plan(0))
        self.sub_action_plan1.triggered.connect(
            lambda: self.one_key_set_plan(1))
        self.sub_action_plan2.triggered.connect(
            lambda: self.one_key_set_plan(2))
        self.sub_action_plan3.triggered.connect(
            lambda: self.one_key_set_plan(3))
        self.sub_action_method1.triggered.connect(
            lambda: arrange_all_wnd(1))
        self.sub_action_method2.triggered.connect(
            lambda: arrange_all_wnd(2))
        self.sub_action_method3.triggered.connect(
            lambda: arrange_all_wnd(3))

        # ------------------- lst_exec设置右键菜单 -------------------
        self.lst_exec.setContextMenuPolicy(Qt.CustomContextMenu)
        self.menu_lst_exec = QMenu()
        self.action_lst_exec_clear = QAction("清空执行列表(&C)")
        # 添加菜单项
        self.menu_lst_exec.addAction(self.action_lst_exec_clear)
        # 连接信号槽
        self.lst_exec.customContextMenuRequested.connect(
            lambda: self.menu_lst_exec.exec_(QCursor.pos())
        )
        self.action_lst_exec_clear.triggered.connect(
            lambda: self.lst_exec.clear()
        )

        # ------------------- tray_icon设置右键菜单 -------------------
        self.menu_tray_icon = QMenu()
        # 创建菜单项
        self.action_kill_all_wnd = QAction("强制退出所有游戏窗口(&K)")
        self.action_hide_show_all_wnd = QAction("隐藏/显示所有游戏窗口(&H)")
        self.action_lock_unlock_all_wnd = QAction("锁定/解锁所有游戏窗口(&L)")
        self.action_quit = QAction("退出本软件(&Q)")
        # 添加菜单项
        self.menu_tray_icon.addAction(self.action_kill_all_wnd)
        self.menu_tray_icon.addSeparator()
        self.menu_tray_icon.addAction(self.action_hide_show_all_wnd)
        self.menu_tray_icon.addAction(self.action_lock_unlock_all_wnd)
        self.menu_tray_icon.addSeparator()
        self.menu_tray_icon.addAction(self.action_quit)
        # 为图标设置菜单
        self.tray_icon.setContextMenu(self.menu_tray_icon)
        # 连接信号槽
        self.tray_icon.activated.connect(self.on_tray_icon_activated)
        self.action_kill_all_wnd.triggered.connect(
            self.on_action_kill_all_wnd_triggered)
        self.action_hide_show_all_wnd.triggered.connect(
            self.on_action_hide_show_all_wnd_triggered)
        self.action_lock_unlock_all_wnd.triggered.connect(
            self.on_action_lock_unlock_all_wnd_triggered)
        self.action_quit.triggered.connect(self.on_action_quit_triggered)

        # ------------------- lst_plan设置右键菜单 -------------------
        self.lst_plan.setContextMenuPolicy(Qt.CustomContextMenu)
        self.menu_lst_plan = QMenu()
        self.action_lst_plan_del = QAction("删除此方案(&D)")
        self.action_lst_plan_cancel = QAction("取消选中")
        # 添加菜单项
        self.menu_lst_plan.addAction(self.action_lst_plan_del)
        self.menu_lst_plan.addAction(self.action_lst_plan_cancel)
        self.lst_plan.customContextMenuRequested.connect(
            lambda: self.menu_lst_plan.exec_(QCursor.pos())
        )
        self.action_lst_plan_del.triggered.connect(
            self.on_action_lst_plan_del_triggered)
        self.action_lst_plan_cancel.triggered.connect(
            lambda: self.lst_plan.setCurrentItem(None))

    def init_sig_slot(self):
        # ------------------- 时钟 -------------------
        self.timer_cur.timeout.connect(self.on_timer_cur_timeout)
        self.timer_cur.start(1000)
        self.timer_info.timeout.connect(self.on_timer_info_timeout)
        self.timer_info.start(1000*10)
        self.timer_ds.timeout.connect(self.on_timer_ds_timeout)
        self.timer_ds.start(1000*60)
        # ------------------- 工具栏 -------------------
        self.tool_bar.actionTriggered.connect(self.on_tool_bar_actionTriggered)
        self.tool_bar.orientationChanged.connect(
            self.on_tool_bar_orientationChanged)
        # ------------------- 中控台表格 -------------------
        h_header = self.tbe_console.horizontalHeader()
        v_header = self.tbe_console.verticalHeader()
        h_header.sectionDoubleClicked.connect(self.on_h_header_double_clicked)
        v_header.sectionDoubleClicked.connect(self.on_v_header_double_clicked)
        self.tbe_console.cellDoubleClicked.connect(
            self.on_tbe_console_cellDoubleClicked)
        self.tbe_console.itemChanged.connect(self.on_tbe_console_itemChanged)
        # cmb_plan添加currentTextChanged信号槽
        for idx in range(len(settings.cmb_plan_list)):
            cmb_plan = settings.cmb_plan_list[idx]
            cmb_plan.currentTextChanged.connect(
                self.on_cmb_plan_cur_text_changed)
        # ------------------- 选项卡-设置 -------------------
        self.tab_set.currentChanged.connect(self.on_tab_set_currentChanged)
        # ------------------- 方案设置 -------------------
        # tre_all双击添加
        self.tre_all.itemDoubleClicked.connect(
            self.on_tre_all_item_double_clicked)
        # lst_exec双击删除
        self.lst_exec.itemDoubleClicked.connect(
            self.on_lst_exec_item_double_clicked)
        # 保存方案
        self.btn_plan_save.clicked.connect(self.on_btn_plan_save_clicked)
        # lst_plan双击读取配置
        self.lst_plan.itemDoubleClicked.connect(
            self.on_lst_plan_item_double_clicked)
        # lst_plan当前项改变时设置编辑框内容
        self.lst_plan.currentTextChanged.connect(
            self.on_lst_plan_currentTextChanged)
        # btn_plan_create点击新建配置文件
        self.btn_plan_create.clicked.connect(self.on_btn_plan_create_clicked)
        # btn_plan_rename点击重命名配置文件
        self.btn_plan_rename.clicked.connect(self.on_btn_plan_rename_clicked)
        # ------------------- 通用设置 -------------------
        self.btn_main_read.clicked.connect(self.on_btn_main_read_clicked)
        self.btn_main_save.clicked.connect(self.on_btn_main_save_clicked)
        self.chk_ban_sys_sleep.stateChanged.connect(
            self.on_chk_ban_sys_sleep_stateChanged)
        self.chk_ban_screen_protect.stateChanged.connect(
            self.on_chk_ban_screen_protect_stateChanged)

    def show_info(self, info: str):
        self.lbe_info.setText(info)
        log.info(info)

    def show_tip(self, tip: str):
        self.lbe_info.setText(tip)

    def get_plan_setting_dict(self):
        items_text = [self.lst_exec.item(idx).text() for idx in range(self.lst_exec.count())]
        return {
            '执行列表': items_text,
            '人物战斗': utils.get_checked_radio_text_in_groupbox(self.groupBox_people),
            '宠物战斗': utils.get_checked_radio_text_in_groupbox(self.groupBox_pet),
            '出城': utils.get_checked_radio_text_in_groupbox(self.groupBox_go),
            '回城': utils.get_checked_radio_text_in_groupbox(self.groupBox_back),
        }
    
    def set_plan_setting_dict(self, plan_setting_dict: dict):
        if plan_setting_dict is None:
            return
        self.lst_exec.clear()
        self.lst_exec.addItems(plan_setting_dict.get('执行列表', []))
        utils.set_checked_radio_text_in_groupbox(self.groupBox_people, plan_setting_dict.get('人物战斗', ''))
        utils.set_checked_radio_text_in_groupbox(self.groupBox_pet, plan_setting_dict.get('宠物战斗', ''))
        utils.set_checked_radio_text_in_groupbox(self.groupBox_go, plan_setting_dict.get('出城', ''))
        utils.set_checked_radio_text_in_groupbox(self.groupBox_back, plan_setting_dict.get('回城', ''))

    # def thd_heart_beat(self):
    #     while True:
    #         # 每一轮循环错误次数+1, 失败则每隔20秒连接一次
    #         self.fail_count += 1
    #         sleep_time = 20
    #         # settings.is_user_dangerous()
    #         # 尝试连接服务端
    #         tcp_socket = settings.connect_server_tcp()
    #         if not tcp_socket:  # 连接失败
    #             log.info("与服务器连接异常...")
    #         else:  # 连接成功, 发送心跳包
    #             client_info_dict = {"消息类型": "心跳",
    #                                 "内容": {"账号": settings.user_account, "机器码": settings.machine_code, "用户行为": settings.action_code}}
    #             settings.send_to_server(tcp_socket, client_info_dict)
    #             msg_type, server_content_dict = settings.recv_from_server(
    #                 tcp_socket)
    #             if msg_type == "心跳":
    #                 heart_ret = server_content_dict["结果"]
    #                 if heart_ret == "正常":
    #                     self.fail_count = 0  # 正常则清零失败错误
    #                     self.last_heart_stamp = settings.cur_time_stamp
    #                     sleep_time = 60*9  # 正常通信, 下次隔9分钟发一次心跳包
    #                 elif heart_ret == "下线":
    #                     self.fail_count = 10
    #                     self.show_info(server_content_dict["详情"])
    #             tcp_socket.close()  # 发送接收完立刻断开
    #         # 超过5次没连上, 跳出心跳循环, 关闭窗口
    #         if self.fail_count > 5:
    #             break
    #         print("等待时间:", sleep_time)
    #         time.sleep(sleep_time)
    #     self.show_info("与服务器断开连接1...")
    #     self.sig_close.emit()

    def send_recv_offline(self):
        # settings.is_user_dangerous()
        tcp_socket = settings.connect_server_tcp()
        if not tcp_socket:
            log.info("服务器繁忙, 请稍后再试")
            return
        client_info_dict = {"消息类型": "离线",
                            "内容": {"账号": settings.user_account, "用户行为": settings.action_code}}
        settings.send_to_server(tcp_socket, client_info_dict)
        msg_type, server_content_dict = settings.recv_from_server(tcp_socket)
        tcp_socket.close()
        if msg_type == "离线":
            log.info("------- 客户端正常退出 -------")
        else:
            log.info("------- 客户端异常退出 -------")

    def one_key_get_wnd(self):
        hwnd_list = settings.com_obj.enum_window()

        if hwnd_list == []:
            self.show_info("未发现游戏窗口,请打开游戏后再试")
            return
        log.info(f"获取到的窗口句柄:{hwnd_list}")
        # 获取 用户设定的方案索引
        plan_idx = int(settings.cfg_common["获取窗口后设置方案"])
        for hwnd in hwnd_list:
            # 若窗口已经存在, 则跳过下面步骤
            if settings.is_wnd_in_list(hwnd):
                continue
            # 找一个空位填充
            row = settings.worker_list.index(None)
            self.tbe_console.item(row, settings.COL_HWND).setText(str(hwnd))
            # 创建com对象
            obj = settings.create_com_obj(settings.COM_NAME)
            if settings.is_custom:
                obj = settings.BaseObj(obj)
            # 创建worker对象
            wk = common.Worker(hwnd, obj, row)
            # 把wk添加到列表中
            settings.worker_list[row] = wk
            # 清空之前的日志内容
            row_num = row + 1
            settings.file_clear_content(f"{settings.DIR_LOG}\\{row_num}.txt")
            # 激活cmb_plan,  并设置方案
            cmb_plan = settings.cmb_plan_list[row]
            cmb_plan.setEnabled(True)
            cmb_plan.setCurrentIndex(plan_idx)
            # 获取窗口位置
            x, y = settings.get_wnd_pos(hwnd)
            if x != settings.HIDE_X:
                wk.x, wk.y = x, y
            wk.record(f"窗口{row_num}获取成功, 并自动设置为{plan_idx}号方案")
        # 排列所有窗口
        mode = int(settings.cfg_common["获取窗口后排列方式"])
        arrange_all_wnd(mode)
        self.show_info(f"获取所有游戏窗口成功, 并按方式{mode}排列")

    def one_key_set_plan(self, idx):
        for wk in settings.worker_list:
            if wk is None:
                continue
            cmb_plan = settings.cmb_plan_list[wk.row]
            if cmb_plan.isEnabled() and cmb_plan.count() >= idx:
                cmb_plan.setCurrentIndex(idx)

    def rmv_wnd_from_console(self, wk: common.Worker):
        row = wk.row
        # 移除此工人
        settings.worker_list[row] = None
        wk = None
        # 清空此行内容
        for col in range(settings.TBE_CONSOLE_COL):
            item = self.tbe_console.item(row, col)
            if item:
                item.setText("")
        # 禁用cmb_plan
        cmb_plan = settings.cmb_plan_list[row]
        cmb_plan.setEnabled(False)
        cmb_plan.setCurrentIndex(-1)

    def update_cmb_plan_tooltip(self, row):
        wk = settings.worker_list[row]
        cmb_plan = settings.cmb_plan_list[row]
        tooltip = "-".join(wk.cfg_plan["执行列表"])
        cmb_plan.setToolTip(tooltip)

    # ---------------------- 自定义槽函数 -----------------------
    def on_tray_icon_activated(self, reason):
        if reason == QSystemTrayIcon.Trigger:
            if self.isHidden():
                self.showNormal()
                self.activateWindow()
            else:
                self.hide()

    def on_action_kill_all_wnd_triggered(self):
        ret = QMessageBox.warning(
            self, "警告", "是否要强制结束所有游戏窗口?", QMessageBox.Yes | QMessageBox.No)
        if ret != QMessageBox.Yes:
            return
        for wk in settings.worker_list:
            if wk is None:
                continue
            settings.terminate_wnd(wk.hwnd)
            self.rmv_wnd_from_console(wk)

    def on_action_hide_show_all_wnd_triggered(self):
        for wk in settings.worker_list:
            if wk is None:
                continue
            x, y = settings.get_wnd_pos(wk.hwnd)
            if x != settings.HIDE_X:  # 在显示则隐藏
                wk.hide_wnd(x, y)
            else:  # 在隐藏则显示
                wk.show_wnd()

    def on_action_lock_unlock_all_wnd_triggered(self):
        for wk in settings.worker_list:
            if wk is None:
                continue
            if wk.is_lock:
                wk.lock_input("关闭锁定")
                wk.record("锁定键鼠 已关闭")
                wk.is_lock = False
            else:
                wk.lock_input("锁定键鼠")
                wk.record("锁定键鼠 已开启")
                wk.is_lock = True

    def on_action_quit_triggered(self):
        ret = QMessageBox.warning(
            self, "警告", "是否要退出本软件?", QMessageBox.Yes | QMessageBox.No)
        if ret != QMessageBox.Yes:
            return
        self.sig_close.emit()

    def on_timer_cur_timeout(self):
        settings.cur_time_fmt = time.strftime("%H:%M:%S")
        settings.cur_time_stamp += 1

    def on_timer_info_timeout(self):
        self.show_tip("低调使用科技, 守护游戏公平!")

    def on_timer_ds_timeout(self):
        # # 若距离上次心跳过去15分钟, 则退出软件
        # # 防止心跳线程被干掉
        # if settings.delta_minute(self.last_heart_stamp, settings.cur_time_stamp) >= 15:
        #     self.show_info("与服务器断开连接2...")
        #     self.sig_close.emit()
        if not settings.cfg_common.get("定时"):
            return
        if settings.cfg_common.get("定时运行全部窗口") and settings.cur_time_fmt[:5] == settings.cfg_common.get("定时运行全部窗口时间"):
            self.show_info("定时运行开始执行!")
            # 依次运行
            for wk in settings.worker_list:
                if wk:
                    wk.write_tbe_console(settings.COL_RUN, settings.SELECTED)
        if settings.cfg_common.get("定时关闭计算机") and settings.cur_time_fmt[:5] == settings.cfg_common.get("定时关闭计算机时间"):
            self.show_info("定时关机开始执行!")
            # 依次终止
            for wk in settings.worker_list:
                if wk:
                    wk.write_tbe_console(settings.COL_END, settings.SELECTED)
            # 弹框提示
            msg_box = TimeMsgBox("提示", "定时关机时间到, 是否关机?")
            msg_box.exec_()
            if msg_box.clickedButton() != msg_box.btn_accept:
                self.show_info("已取消关机")
                return
            # 确定关机
            settings.com_obj.exit_os()

    def on_tre_all_item_double_clicked(self, item, col):
        item_text = item.text(col)
        if item_text in ("单人", "组队", "其它"):
            return
        self.lst_exec.addItem(item_text)

    def on_lst_exec_item_double_clicked(self, item):
        row = self.lst_exec.row(item)
        self.lst_exec.takeItem(row)

    # 保存方案
    def on_btn_plan_save_clicked(self):
        curItem = self.lst_plan.currentItem()
        plan_name = "0内置默认" if curItem is None else curItem.text()
        # 弹框提示
        msg_box = MyMsgBox("提示", f"将左边的控件配置保存至方案 \n{plan_name}?", self)
        msg_box.exec_()
        if msg_box.clickedButton() != msg_box.btn_accept:
            self.show_info("保存方案 操作已取消")
            return
        cfg_plan = settings.cfg_plan_dict.get(plan_name, {})
        # 保存方案配置
        cfg_plan["执行列表"] = [self.lst_exec.item(
            i).text() for i in range(self.lst_exec.count())]
        utils.dict_to_json_file(settings.cfg_plan_dict, const.PATH_SOFTWARE_PLAN)
        # 刷新所有cmb_plan的toolTip
        for cmb_plan in settings.cmb_plan_list:
            if cmb_plan.currentText() == plan_name:
                idx = settings.cmb_plan_list.index(cmb_plan)
                self.update_cmb_plan_tooltip(idx)
        self.show_info(f"方案配置-{plan_name}, 保存完成")

    # 读取方案
    def on_lst_plan_item_double_clicked(self):
        curItem = self.lst_plan.currentItem()
        if curItem is None:
            self.show_info("失败,请选择要读取的配置文件!")
            return
        plan_name = curItem.text()
        cfg_plan = settings.cfg_plan_dict.get(plan_name, {})
        # 读取方案配置
        self.lst_exec.clear()
        self.lst_exec.addItems(cfg_plan.get("执行列表", []))
        self.show_info(f"方案配置-{plan_name}, 读取完成")

    def on_lst_plan_currentTextChanged(self, cur_text):
        self.edt_plan_new_name.setText(cur_text)

    # 新建方案
    def on_btn_plan_create_clicked(self):
        plan_name = self.edt_plan_new_name.text()
        if plan_name == "":
            self.show_info("失败, 请先输入新方案名")
            return
        if plan_name in settings.cfg_plan_dict:
            self.show_info("失败, 方案名已存在")
            return
        # 这时要读取所有控件状态，保存
        settings.cfg_plan_dict[plan_name] = self.get_plan_setting_dict()
        # 在lst_plan里添加方案名, 并排序
        self.lst_plan.addItem(plan_name)
        self.lst_plan.sortItems()
        # 在每个cmb_plan里添加方案名的选项
        for cmb_plan in settings.cmb_plan_list:
            cmb_plan.addItem(plan_name)
        # 保存到json文件
        utils.dict_to_json_file(settings.cfg_plan_dict, const.PATH_SOFTWARE_PLAN)
        self.show_info("新建方案成功!")

    # 重命名方案
    def on_btn_plan_rename_clicked(self):
        curItem = self.lst_plan.currentItem()
        if curItem is None:
            self.show_info("失败, 请先选择要重命名哪个方案!")
            return
        old_plan_name = curItem.text()
        new_plan_name = self.edt_plan_new_name.text()
        if new_plan_name == "":
            self.show_info("请先输入新方案名")
            return
        # 重命名key
        settings.cfg_plan_dict[new_plan_name] = settings.cfg_plan_dict.pop(
            old_plan_name)
        utils.dict_to_json_file(settings.cfg_plan_dict, const.PATH_SOFTWARE_PLAN)
        # 在lst_plan里修改方案名
        self.lst_plan.takeItem(self.lst_plan.row(curItem))
        self.lst_plan.addItem(new_plan_name)
        self.lst_plan.sortItems()  # 重新排序
        # 在cmb_plan里修改方案名
        for cmb_plan in settings.cmb_plan_list:
            idx = cmb_plan.findText(old_plan_name)
            if idx != -1:
                cmb_plan.setItemText(idx, new_plan_name)
        self.show_info("重命名方案成功!")

    def on_btn_main_read_clicked(self):
        self.cfg_read()

        self.show_info("配置文件 -> 控件, 保存完成")

    def on_btn_main_save_clicked(self):
        self.cfg_save()
        self.show_info("控件 -> 配置文件, 保存完成")

    def on_chk_ban_sys_sleep_stateChanged(self, state):
        if state == 2:  # 变为选中
            settings.com_obj.ban_sys_sleep()
            self.show_info("已成功禁用系统睡眠, 关机后自动失效")

    def on_chk_ban_screen_protect_stateChanged(self, state):
        if state == 2:  # 变为选中
            settings.com_obj.ban_screen_protect()
            self.show_info("已成功禁用屏幕保护, 关机后自动失效")

    def on_h_header_double_clicked(self, col):
        log.info(f"第{col}列双击了")
        if col == const.COL_HWND:
            self.show_info("双击 [窗口句柄] 表头, 一键获取所有窗口")
            self.one_key_get_wnd()

        elif col == const.COL_PLAN:
            plan_idx = int(settings.cfg_common["双击方案列设置方案"])
            self.show_info(f"双击 [方案选择] 表头, 一键设置为{plan_idx}号方案")
            self.one_key_set_plan(plan_idx)

        elif col == const.COL_RUN:
            self.show_info("双击 [运行] 表头, 一键运行表格上的所有窗口")
            for wk in settings.worker_list:
                if wk is None:
                    continue
                self.tbe_console.item(wk.row, col).setText(settings.SELECTED)

        elif col == const.COL_PAUSE:
            self.show_info("双击 [暂停] 表头, 一键暂停表格上的所有窗口")
            for wk in settings.worker_list:
                if wk is None:
                    continue
                if self.tbe_console.item(wk.row, settings.COL_RUN).text():
                    self.tbe_console.item(
                        wk.row, col).setText(settings.SELECTED)

        elif col == const.COL_END:
            self.show_info("双击 [终止] 表头, 一键终止表格上的所有窗口")
            for wk in settings.worker_list:
                if wk is None:
                    continue
                if self.tbe_console.item(wk.row, settings.COL_RUN).text() or \
                        self.tbe_console.item(wk.row, settings.COL_PAUSE).text():
                    self.tbe_console.item(
                        wk.row, col).setText(settings.SELECTED)

        elif col == const.COL_LOG:
            self.show_info("双击 [日志] 表头, 获取软件日志记录")
            # 读取内容, 设置内容
            content = settings.file_read_content(settings.PATH_CLIENT_LOG)
            self.tbr_log.setText(content)
            # 设置标题, 将光标移到文档末, 显示
            self.diag.setWindowTitle(f"日志-本软件")
            self.tbr_log.moveCursor(QTextCursor.End)
            self.diag.show()
            self.diag.activateWindow()

    def on_v_header_double_clicked(self, row):
        log.info(f"第{row}行双击了")
        wk = settings.worker_list[row]
        if not wk:
            return
        self.show_info("双击 垂直 表头, 显示/隐藏该窗口")
        x, y = settings.get_wnd_pos(wk.hwnd)
        if x != settings.HIDE_X:
            wk.hide_wnd(x, y)
        else:
            wk.show_wnd()
            settings.activate_wnd(wk.hwnd)

    def on_tbe_console_cellDoubleClicked(self, row, col):
        # 若双击的列不是日志列, 且还没获取窗口
        if col != settings.COL_LOG and not self.tbe_console.item(row, settings.COL_HWND).text():
            self.show_info("无效操作, 请先双击 [窗口句柄] 表头获取游戏窗口")
            return
        log.info(f"第{row}行, 第{col}列单元格被双击!")
        row_num = row + 1

        if col == settings.COL_HWND:  # 若双击"窗口句柄"列
            self.show_info(f"双击 [窗口句柄] 列,第{row_num}行, 显示并激活该窗口")
            wk = settings.worker_list[row]
            wk.show_wnd()
            settings.activate_wnd(wk.hwnd)

        elif col == settings.COL_RUN:  # 若双击"运行"列
            self.show_info(f"双击 [运行] 列,第{row_num}行, 运行该窗口")
            self.tbe_console.currentItem().setText(settings.SELECTED)

        elif col == settings.COL_PAUSE:  # 若双击"暂停"列
            if self.tbe_console.item(row, settings.COL_RUN).text():
                self.show_info(f"双击 [暂停] 列,第{row_num}行, 暂停该窗口")
                self.tbe_console.currentItem().setText(settings.SELECTED)

        elif col == settings.COL_END:  # 若双击"终止"列
            if self.tbe_console.item(row, settings.COL_RUN).text() or \
                    self.tbe_console.item(row, settings.COL_PAUSE).text():
                self.show_info(f"双击 [终止] 列,第{row_num}行, 终止该窗口")
                self.tbe_console.currentItem().setText(settings.SELECTED)

        elif col == settings.COL_LOG:  # 若双击"日志"列
            self.show_info(f"双击 [日志] 列,第{row_num}行, 显示该窗口的执行日志")
            # 先清除当前tbr日志的内容
            self.tbr_log.clear()
            # 读取内容, 设置内容
            content = settings.file_read_content(
                f"{settings.DIR_LOG}\\{row_num}.txt")
            self.tbr_log.setText(content)
            # 设置标题, 将光标移到文档末, 显示
            self.diag.setWindowTitle(f"日志-窗口{row_num}")
            self.tbr_log.moveCursor(QTextCursor.End)
            self.diag.show()
            self.diag.activateWindow()

    def on_tbe_console_itemChanged(self, item):
        col = item.column()
        if col > settings.COL_END or col < settings.COL_RUN or item.text() == "":
            return
        row = item.row()
        wk = settings.worker_list[row]
        if col == settings.COL_RUN:
            self.tbe_console.item(row, settings.COL_PAUSE).setText("")
            self.tbe_console.item(row, settings.COL_END).setText("")
            Thread(target=self.thread_run, args=(wk,), daemon=True).start()

        elif col == settings.COL_PAUSE:
            self.tbe_console.item(row, settings.COL_RUN).setText("")
            self.tbe_console.item(row, settings.COL_END).setText("")
            Thread(target=self.thread_pause, args=(wk,), daemon=True).start()

        elif col == settings.COL_END:
            self.tbe_console.item(row, settings.COL_RUN).setText("")
            self.tbe_console.item(row, settings.COL_PAUSE).setText("")
            Thread(target=self.thread_end, args=(wk,), daemon=True).start()

    # 方案改变
    def on_cmb_plan_cur_text_changed(self, plan_name):
        cmb_plan = self.sender()
        row = settings.cmb_plan_list.index(cmb_plan)
        wk = settings.worker_list[row]
        if wk is None:
            return
        wk.cfg_plan = settings.cfg_plan_dict[plan_name]
        wk.record(f"窗口已更换为方案{plan_name}")
        # 刷新cmb_plan的toolTip
        self.update_cmb_plan_tooltip(row)

    def on_tab_set_currentChanged(self, idx):
        map_dict = {0: "基本设置", 1: "单人相关", 2: "组队相关"}
        self.show_tip(f"切换到 {map_dict[idx]} 窗口")

    def on_tool_bar_actionTriggered(self, action):
        action_name = action.text()
        self.show_tip(f"切换到 {action_name} 窗口")
        if action_name == "窗口控制":
            self.stack_widget.setCurrentIndex(0)
        elif action_name == "方案配置":
            self.stack_widget.setCurrentIndex(1)
        elif action_name == "通用配置":
            self.stack_widget.setCurrentIndex(2)

    def on_tool_bar_orientationChanged(self, orientation):
        if orientation == Qt.Horizontal:
            self.tool_bar.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        else:
            self.tool_bar.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

    # 删除方案
    def on_action_lst_plan_del_triggered(self):
        cur_item = self.lst_plan.currentItem()
        if cur_item is None:
            self.show_info("请先选中你要删除的方案")
            return
        plan_name = cur_item.text()
        # 从 方案配置字典中移除该方案
        settings.cfg_plan_dict.pop(plan_name)
        utils.dict_to_json_file(settings.cfg_plan_dict, settings.PATH_JSON_PLAN)
        # 删除 方案列表中的对应项
        row = self.lst_plan.row(cur_item)
        self.lst_plan.takeItem(row)
        # 删除 所有方案选择下拉框中的对应项
        for cmb_plan in settings.cmb_plan_list:
            cur_idx = cmb_plan.findText(plan_name)
            if cur_idx >= 0:  # 找到才删
                cmb_plan.removeItem(cur_idx)
        self.show_info("方案删除成功")

    def on_action_get_all_wnd_triggered(self):
        self.one_key_get_wnd()

    def on_action_clear_sel_wnd_triggered(self):
        items = self.tbe_console.selectedItems()
        row_list = [item.row() for item in items if item.column()
                    == 0 and item.text() != ""]
        for row in row_list:
            wk = settings.worker_list[row]
            if wk.is_end:
                self.rmv_wnd_from_console(wk)
            else:
                wk.record("清除窗口前请先终止此窗口")

    def on_action_hide_show_sel_wnd_triggered(self):
        items = self.tbe_console.selectedItems()
        row_list = [item.row() for item in items if item.column()
                    == 0 and item.text() != ""]
        for row in row_list:
            wk = settings.worker_list[row]
            x, y = settings.get_wnd_pos(wk.hwnd)
            if x != settings.HIDE_X:
                wk.hide_wnd(x, y)
            else:
                wk.show_wnd()

    def on_action_lock_unlock_sel_wnd_triggered(self):
        items = self.tbe_console.selectedItems()
        row_list = [item.row() for item in items if item.column()
                    == 0 and item.text() != ""]
        if not row_list:
            return
        for row in row_list:
            wk = settings.worker_list[row]
            if wk.is_lock:
                wk.lock_input("关闭锁定")
                wk.record("锁定键鼠 已关闭")
                wk.is_lock = False
            else:
                wk.lock_input("锁定键鼠")
                wk.record("锁定键鼠 已开启")
                wk.is_lock = True

    def on_action_force_exit_sel_wnd_triggered(self):
        ret = QMessageBox.warning(
            self, "警告", "是否要强制结束选中游戏窗口?", QMessageBox.Yes | QMessageBox.No)
        if ret != QMessageBox.Yes:
            return
        items = self.tbe_console.selectedItems()
        row_list = [item.row() for item in items if item.column()
                    == 0 and item.text() != ""]
        for row in row_list:
            wk = settings.worker_list[row]
            utils.terminate_wnd(wk.hwnd)
            self.rmv_wnd_from_console(wk)

    @staticmethod
    def thread_run(wk: common.Worker):
        if wk.is_pause:  # 若暂停, 则恢复
            if wk.thread:
                wk.thread.resume()
            wk.record("窗口已恢复运行")
        elif wk.is_end:  # 若结束, 才运行
            ret = wk.bind_window(wk.hwnd)
            wk.record(f"窗口绑定结果:{ret}")
            if ret == 1:  # 若绑定成功
                # 禁用cmb_plan
                cmb_plan = settings.cmb_plan_list[wk.row]
                cmb_plan.setEnabled(False)
                # 运行窗口
                wk.record("窗口开始运行")
                wk.thread = ThreadExec(wk)
                wk.thread.start()
            else:  # 若绑定失败, 则把"运行"列重置为空
                wk.record(f"窗口绑定失败, 错误码: {ret}, 请更换绑定模式")
                wk.is_run, wk.is_pause, wk.is_end = False, False, True
                wk.write_tbe_console(settings.COL_RUN, "")

    @staticmethod
    def thread_pause(wk: common.Worker):
        wk.record("窗口即将暂停...")
        if wk.thread:
            wk.thread.pause()
        wk.record("窗口已暂停运行")

    @staticmethod
    def thread_end(wk: common.Worker):
        wk.record("窗口即将终止...")
        if wk.thread:
            wk.thread.end()
        # 启用cmb_plan
        cmb_plan = settings.cmb_plan_list[wk.row]
        cmb_plan.setEnabled(True)
        wk.record("窗口已终止运行")
