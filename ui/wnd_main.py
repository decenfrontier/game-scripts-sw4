# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'wnd_main.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import wnd_main_rc

class Ui_WndMain(object):
    def setupUi(self, WndMain):
        if not WndMain.objectName():
            WndMain.setObjectName(u"WndMain")
        WndMain.resize(808, 472)
        WndMain.setMinimumSize(QSize(0, 0))
        WndMain.setMaximumSize(QSize(3000, 2000))
        icon = QIcon()
        icon.addFile(u":/rbt1.png", QSize(), QIcon.Normal, QIcon.Off)
        WndMain.setWindowIcon(icon)
        WndMain.setWindowOpacity(0.980000000000000)
        WndMain.setStyleSheet(u"* {\n"
"    font-size: 12px;\n"
"    font-family: \"Microsoft YaHei\";\n"
"}\n"
"QTableView {\n"
"    background: white;\n"
"    selection-color: #000000; \n"
"    gridline-color: rgb(213, 213, 213); \n"
"	selection-background-color: #a1b1c9;\n"
"    alternate-background-color: rgb(243, 246, 249);\n"
"}\n"
"QTableView::item:hover	{\n"
"    background-color: #a1b1c9;\n"
"}")
        self.action_console = QAction(WndMain)
        self.action_console.setObjectName(u"action_console")
        self.action_console.setCheckable(False)
        icon1 = QIcon()
        icon1.addFile(u":/control8.png", QSize(), QIcon.Normal, QIcon.Off)
        self.action_console.setIcon(icon1)
        self.action_plan = QAction(WndMain)
        self.action_plan.setObjectName(u"action_plan")
        self.action_plan.setCheckable(False)
        icon2 = QIcon()
        icon2.addFile(u":/plan7.png", QSize(), QIcon.Normal, QIcon.Off)
        self.action_plan.setIcon(icon2)
        self.action_setting = QAction(WndMain)
        self.action_setting.setObjectName(u"action_setting")
        self.action_setting.setCheckable(False)
        icon3 = QIcon()
        icon3.addFile(u":/gnrl7.png", QSize(), QIcon.Normal, QIcon.Off)
        self.action_setting.setIcon(icon3)
        self.centralwidget = QWidget(WndMain)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_3 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(2, 2, 2, 2)
        self.stack_widget = QStackedWidget(self.centralwidget)
        self.stack_widget.setObjectName(u"stack_widget")
        self.stack_widget.setFrameShape(QFrame.NoFrame)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.gridLayout_14 = QGridLayout(self.page)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.gridLayout_14.setContentsMargins(2, 2, 2, 2)
        self.tbe_console = QTableWidget(self.page)
        if (self.tbe_console.columnCount() < 6):
            self.tbe_console.setColumnCount(6)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setTextAlignment(Qt.AlignCenter);
        self.tbe_console.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setTextAlignment(Qt.AlignCenter);
        self.tbe_console.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setTextAlignment(Qt.AlignCenter);
        self.tbe_console.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setTextAlignment(Qt.AlignCenter);
        self.tbe_console.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setTextAlignment(Qt.AlignCenter);
        self.tbe_console.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        __qtablewidgetitem5.setTextAlignment(Qt.AlignCenter);
        self.tbe_console.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        if (self.tbe_console.rowCount() < 15):
            self.tbe_console.setRowCount(15)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tbe_console.setVerticalHeaderItem(0, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tbe_console.setVerticalHeaderItem(1, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tbe_console.setVerticalHeaderItem(2, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tbe_console.setVerticalHeaderItem(3, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tbe_console.setVerticalHeaderItem(4, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tbe_console.setVerticalHeaderItem(5, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tbe_console.setVerticalHeaderItem(6, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        __qtablewidgetitem13.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.tbe_console.setVerticalHeaderItem(7, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tbe_console.setVerticalHeaderItem(8, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tbe_console.setVerticalHeaderItem(9, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tbe_console.setVerticalHeaderItem(10, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tbe_console.setVerticalHeaderItem(11, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tbe_console.setVerticalHeaderItem(12, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.tbe_console.setVerticalHeaderItem(13, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.tbe_console.setVerticalHeaderItem(14, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.tbe_console.setItem(0, 0, __qtablewidgetitem21)
        self.tbe_console.setObjectName(u"tbe_console")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tbe_console.sizePolicy().hasHeightForWidth())
        self.tbe_console.setSizePolicy(sizePolicy)
        self.tbe_console.setMaximumSize(QSize(16777215, 16777215))
        self.tbe_console.setFrameShadow(QFrame.Raised)
        self.tbe_console.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.tbe_console.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tbe_console.setAlternatingRowColors(False)
        self.tbe_console.setShowGrid(True)
        self.tbe_console.setGridStyle(Qt.SolidLine)
        self.tbe_console.setCornerButtonEnabled(False)
        self.tbe_console.setRowCount(15)
        self.tbe_console.horizontalHeader().setCascadingSectionResizes(True)
        self.tbe_console.horizontalHeader().setMinimumSectionSize(30)
        self.tbe_console.horizontalHeader().setStretchLastSection(True)
        self.tbe_console.verticalHeader().setVisible(False)
        self.tbe_console.verticalHeader().setMinimumSectionSize(27)
        self.tbe_console.verticalHeader().setDefaultSectionSize(27)
        self.tbe_console.verticalHeader().setStretchLastSection(False)

        self.gridLayout_14.addWidget(self.tbe_console, 0, 0, 1, 1)

        self.stack_widget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.horizontalLayout_4 = QHBoxLayout(self.page_2)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(2, 2, 2, 2)
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_4)

        self.label_49 = QLabel(self.page_2)
        self.label_49.setObjectName(u"label_49")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_49.sizePolicy().hasHeightForWidth())
        self.label_49.setSizePolicy(sizePolicy1)
        self.label_49.setMinimumSize(QSize(55, 17))
        self.label_49.setMaximumSize(QSize(55, 17))
        self.label_49.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_49)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_5)


        self.verticalLayout_4.addLayout(self.horizontalLayout_2)

        self.tre_all = QTreeWidget(self.page_2)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setTextAlignment(0, Qt.AlignCenter);
        self.tre_all.setHeaderItem(__qtreewidgetitem)
        __qtreewidgetitem1 = QTreeWidgetItem(self.tre_all)
        QTreeWidgetItem(__qtreewidgetitem1)
        QTreeWidgetItem(__qtreewidgetitem1)
        __qtreewidgetitem2 = QTreeWidgetItem(self.tre_all)
        QTreeWidgetItem(__qtreewidgetitem2)
        QTreeWidgetItem(__qtreewidgetitem2)
        QTreeWidgetItem(__qtreewidgetitem2)
        QTreeWidgetItem(__qtreewidgetitem2)
        QTreeWidgetItem(__qtreewidgetitem2)
        QTreeWidgetItem(__qtreewidgetitem2)
        __qtreewidgetitem3 = QTreeWidgetItem(self.tre_all)
        QTreeWidgetItem(__qtreewidgetitem3)
        QTreeWidgetItem(__qtreewidgetitem3)
        QTreeWidgetItem(__qtreewidgetitem3)
        QTreeWidgetItem(__qtreewidgetitem3)
        self.tre_all.setObjectName(u"tre_all")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.tre_all.sizePolicy().hasHeightForWidth())
        self.tre_all.setSizePolicy(sizePolicy2)
        self.tre_all.setMinimumSize(QSize(100, 200))
        self.tre_all.setMaximumSize(QSize(100, 16777215))
        self.tre_all.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tre_all.setAutoExpandDelay(0)
        self.tre_all.setIndentation(7)
        self.tre_all.setAnimated(True)
        self.tre_all.header().setVisible(False)

        self.verticalLayout_4.addWidget(self.tre_all)


        self.horizontalLayout_4.addLayout(self.verticalLayout_4)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_2 = QSpacerItem(18, 17, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.label_52 = QLabel(self.page_2)
        self.label_52.setObjectName(u"label_52")
        sizePolicy1.setHeightForWidth(self.label_52.sizePolicy().hasHeightForWidth())
        self.label_52.setSizePolicy(sizePolicy1)
        self.label_52.setMinimumSize(QSize(55, 17))
        self.label_52.setMaximumSize(QSize(55, 17))
        self.label_52.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label_52)

        self.horizontalSpacer_3 = QSpacerItem(18, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.lst_exec = QListWidget(self.page_2)
        self.lst_exec.setObjectName(u"lst_exec")
        sizePolicy2.setHeightForWidth(self.lst_exec.sizePolicy().hasHeightForWidth())
        self.lst_exec.setSizePolicy(sizePolicy2)
        self.lst_exec.setMinimumSize(QSize(95, 200))
        self.lst_exec.setMaximumSize(QSize(95, 16777215))
        self.lst_exec.setDragEnabled(True)
        self.lst_exec.setDragDropMode(QAbstractItemView.DragDrop)
        self.lst_exec.setDefaultDropAction(Qt.MoveAction)

        self.verticalLayout_2.addWidget(self.lst_exec)


        self.horizontalLayout_4.addLayout(self.verticalLayout_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_2)

        self.btn_plan_save = QPushButton(self.page_2)
        self.btn_plan_save.setObjectName(u"btn_plan_save")
        sizePolicy1.setHeightForWidth(self.btn_plan_save.sizePolicy().hasHeightForWidth())
        self.btn_plan_save.setSizePolicy(sizePolicy1)
        self.btn_plan_save.setMinimumSize(QSize(100, 25))
        self.btn_plan_save.setMaximumSize(QSize(16777215, 16777215))

        self.verticalLayout_3.addWidget(self.btn_plan_save)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_3)


        self.horizontalLayout_4.addLayout(self.verticalLayout_3)

        self.gridLayout_10 = QGridLayout()
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.gridLayout_10.setVerticalSpacing(2)
        self.edt_plan_new_name = QLineEdit(self.page_2)
        self.edt_plan_new_name.setObjectName(u"edt_plan_new_name")
        sizePolicy1.setHeightForWidth(self.edt_plan_new_name.sizePolicy().hasHeightForWidth())
        self.edt_plan_new_name.setSizePolicy(sizePolicy1)
        self.edt_plan_new_name.setMinimumSize(QSize(0, 0))
        self.edt_plan_new_name.setMaximumSize(QSize(110, 16777215))
        self.edt_plan_new_name.setAlignment(Qt.AlignCenter)

        self.gridLayout_10.addWidget(self.edt_plan_new_name, 3, 0, 1, 2)

        self.label_53 = QLabel(self.page_2)
        self.label_53.setObjectName(u"label_53")
        sizePolicy1.setHeightForWidth(self.label_53.sizePolicy().hasHeightForWidth())
        self.label_53.setSizePolicy(sizePolicy1)
        self.label_53.setMinimumSize(QSize(0, 0))
        self.label_53.setMaximumSize(QSize(110, 16777215))
        self.label_53.setAlignment(Qt.AlignCenter)

        self.gridLayout_10.addWidget(self.label_53, 0, 0, 1, 2)

        self.lst_plan = QListWidget(self.page_2)
        self.lst_plan.setObjectName(u"lst_plan")
        sizePolicy2.setHeightForWidth(self.lst_plan.sizePolicy().hasHeightForWidth())
        self.lst_plan.setSizePolicy(sizePolicy2)
        self.lst_plan.setMinimumSize(QSize(0, 0))
        self.lst_plan.setMaximumSize(QSize(110, 16777215))

        self.gridLayout_10.addWidget(self.lst_plan, 1, 0, 1, 2)

        self.btn_plan_create = QPushButton(self.page_2)
        self.btn_plan_create.setObjectName(u"btn_plan_create")
        sizePolicy1.setHeightForWidth(self.btn_plan_create.sizePolicy().hasHeightForWidth())
        self.btn_plan_create.setSizePolicy(sizePolicy1)
        self.btn_plan_create.setMinimumSize(QSize(0, 0))
        self.btn_plan_create.setMaximumSize(QSize(50, 16777215))

        self.gridLayout_10.addWidget(self.btn_plan_create, 4, 0, 1, 1)

        self.btn_plan_rename = QPushButton(self.page_2)
        self.btn_plan_rename.setObjectName(u"btn_plan_rename")
        sizePolicy1.setHeightForWidth(self.btn_plan_rename.sizePolicy().hasHeightForWidth())
        self.btn_plan_rename.setSizePolicy(sizePolicy1)
        self.btn_plan_rename.setMinimumSize(QSize(0, 0))
        self.btn_plan_rename.setMaximumSize(QSize(50, 16777215))

        self.gridLayout_10.addWidget(self.btn_plan_rename, 4, 1, 1, 1)

        self.label_54 = QLabel(self.page_2)
        self.label_54.setObjectName(u"label_54")

        self.gridLayout_10.addWidget(self.label_54, 2, 0, 1, 1)


        self.horizontalLayout_4.addLayout(self.gridLayout_10)

        self.groupBox_2 = QGroupBox(self.page_2)
        self.groupBox_2.setObjectName(u"groupBox_2")
        sizePolicy1.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy1)
        self.groupBox_2.setMinimumSize(QSize(300, 0))

        self.horizontalLayout_4.addWidget(self.groupBox_2)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalSpacer = QSpacerItem(20, 158, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer)

        self.horizontalSpacer_6 = QSpacerItem(28, 18, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.verticalLayout_5.addItem(self.horizontalSpacer_6)

        self.verticalSpacer_4 = QSpacerItem(20, 188, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_4)


        self.horizontalLayout_4.addLayout(self.verticalLayout_5)

        self.stack_widget.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.gridLayout_16 = QGridLayout(self.page_3)
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.gridLayout_16.setContentsMargins(2, 2, 2, 2)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tab_set = QTabWidget(self.page_3)
        self.tab_set.setObjectName(u"tab_set")
        self.tab_set.setTabPosition(QTabWidget.North)
        self.tab_set.setTabShape(QTabWidget.Rounded)
        self.tab_set.setIconSize(QSize(32, 32))
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        self.tab_set.addTab(self.tab_5, "")
        self.tab_6 = QWidget()
        self.tab_6.setObjectName(u"tab_6")
        self.groupBox_7 = QGroupBox(self.tab_6)
        self.groupBox_7.setObjectName(u"groupBox_7")
        self.groupBox_7.setGeometry(QRect(10, 110, 141, 171))
        self.gridLayout_8 = QGridLayout(self.groupBox_7)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_8.setContentsMargins(6, 6, 6, 6)
        self.chk_duiyuan_ls = QCheckBox(self.groupBox_7)
        self.chk_duiyuan_ls.setObjectName(u"chk_duiyuan_ls")
        self.chk_duiyuan_ls.setMinimumSize(QSize(0, 20))
        self.chk_duiyuan_ls.setMaximumSize(QSize(16777215, 16777215))
        self.chk_duiyuan_ls.setChecked(True)

        self.gridLayout_8.addWidget(self.chk_duiyuan_ls, 0, 0, 1, 1)

        self.chk_duiyuan_td = QCheckBox(self.groupBox_7)
        self.chk_duiyuan_td.setObjectName(u"chk_duiyuan_td")
        self.chk_duiyuan_td.setMinimumSize(QSize(0, 20))
        self.chk_duiyuan_td.setMaximumSize(QSize(16777215, 16777215))
        self.chk_duiyuan_td.setChecked(True)

        self.gridLayout_8.addWidget(self.chk_duiyuan_td, 3, 0, 1, 1)

        self.chk_duiyuan_closetalk = QCheckBox(self.groupBox_7)
        self.chk_duiyuan_closetalk.setObjectName(u"chk_duiyuan_closetalk")
        self.chk_duiyuan_closetalk.setMinimumSize(QSize(0, 20))
        self.chk_duiyuan_closetalk.setMaximumSize(QSize(16777215, 16777215))
        self.chk_duiyuan_closetalk.setChecked(True)

        self.gridLayout_8.addWidget(self.chk_duiyuan_closetalk, 4, 0, 1, 1)

        self.chk_duiyuan_js = QCheckBox(self.groupBox_7)
        self.chk_duiyuan_js.setObjectName(u"chk_duiyuan_js")
        self.chk_duiyuan_js.setMinimumSize(QSize(0, 20))
        self.chk_duiyuan_js.setMaximumSize(QSize(16777215, 16777215))
        self.chk_duiyuan_js.setChecked(True)

        self.gridLayout_8.addWidget(self.chk_duiyuan_js, 1, 0, 1, 1)

        self.chk_duiyuan_ds = QCheckBox(self.groupBox_7)
        self.chk_duiyuan_ds.setObjectName(u"chk_duiyuan_ds")
        self.chk_duiyuan_ds.setMinimumSize(QSize(0, 20))
        self.chk_duiyuan_ds.setMaximumSize(QSize(16777215, 16777215))
        self.chk_duiyuan_ds.setChecked(True)

        self.gridLayout_8.addWidget(self.chk_duiyuan_ds, 2, 0, 1, 1)

        self.groupBox_6 = QGroupBox(self.tab_6)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.groupBox_6.setGeometry(QRect(180, 20, 101, 61))
        self.gridLayout_9 = QGridLayout(self.groupBox_6)
        self.gridLayout_9.setSpacing(4)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_9.setContentsMargins(4, 4, 4, 4)
        self.label_17 = QLabel(self.groupBox_6)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_9.addWidget(self.label_17, 0, 0, 1, 1)

        self.cmb_double_time = QComboBox(self.groupBox_6)
        self.cmb_double_time.addItem("")
        self.cmb_double_time.addItem("")
        self.cmb_double_time.addItem("")
        self.cmb_double_time.setObjectName(u"cmb_double_time")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.cmb_double_time.sizePolicy().hasHeightForWidth())
        self.cmb_double_time.setSizePolicy(sizePolicy3)
        self.cmb_double_time.setMinimumSize(QSize(60, 20))
        self.cmb_double_time.setMaximumSize(QSize(16777215, 20))

        self.gridLayout_9.addWidget(self.cmb_double_time, 0, 1, 1, 1)

        self.groupBox = QGroupBox(self.tab_6)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(10, 11, 151, 81))
        self.gridLayout_2 = QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(6, 6, 6, 6)
        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_2.addWidget(self.label_4, 0, 0, 1, 1)

        self.cmb_daye_map = QComboBox(self.groupBox)
        self.cmb_daye_map.addItem("")
        self.cmb_daye_map.addItem("")
        self.cmb_daye_map.addItem("")
        self.cmb_daye_map.addItem("")
        self.cmb_daye_map.addItem("")
        self.cmb_daye_map.addItem("")
        self.cmb_daye_map.addItem("")
        self.cmb_daye_map.addItem("")
        self.cmb_daye_map.addItem("")
        self.cmb_daye_map.addItem("")
        self.cmb_daye_map.setObjectName(u"cmb_daye_map")
        self.cmb_daye_map.setMinimumSize(QSize(0, 20))
        self.cmb_daye_map.setMaximumSize(QSize(16777215, 20))

        self.gridLayout_2.addWidget(self.cmb_daye_map, 0, 1, 1, 2)

        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_2.addWidget(self.label_5, 1, 0, 1, 1)

        self.edt_daye_time = QLineEdit(self.groupBox)
        self.edt_daye_time.setObjectName(u"edt_daye_time")
        self.edt_daye_time.setMinimumSize(QSize(0, 20))
        self.edt_daye_time.setMaximumSize(QSize(16777215, 20))
        self.edt_daye_time.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.edt_daye_time, 1, 1, 1, 1)

        self.label_6 = QLabel(self.groupBox)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_2.addWidget(self.label_6, 1, 2, 1, 1)

        self.tab_set.addTab(self.tab_6, "")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.chk_on_time = QGroupBox(self.tab)
        self.chk_on_time.setObjectName(u"chk_on_time")
        self.chk_on_time.setGeometry(QRect(160, 20, 191, 91))
        self.chk_on_time.setCheckable(True)
        self.chk_on_time.setChecked(False)
        self.gridLayout_18 = QGridLayout(self.chk_on_time)
        self.gridLayout_18.setObjectName(u"gridLayout_18")
        self.chk_on_time_run_all = QCheckBox(self.chk_on_time)
        self.chk_on_time_run_all.setObjectName(u"chk_on_time_run_all")
        self.chk_on_time_run_all.setChecked(True)

        self.gridLayout_18.addWidget(self.chk_on_time_run_all, 0, 0, 1, 1)

        self.tmedt_on_time_run_all = QTimeEdit(self.chk_on_time)
        self.tmedt_on_time_run_all.setObjectName(u"tmedt_on_time_run_all")
        self.tmedt_on_time_run_all.setMinimumSize(QSize(0, 22))
        self.tmedt_on_time_run_all.setMaximumSize(QSize(16777215, 22))

        self.gridLayout_18.addWidget(self.tmedt_on_time_run_all, 0, 1, 1, 1)

        self.chk_on_time_shut_down = QCheckBox(self.chk_on_time)
        self.chk_on_time_shut_down.setObjectName(u"chk_on_time_shut_down")
        self.chk_on_time_shut_down.setChecked(True)

        self.gridLayout_18.addWidget(self.chk_on_time_shut_down, 1, 0, 1, 1)

        self.tmedt_on_time_shut_down = QTimeEdit(self.chk_on_time)
        self.tmedt_on_time_shut_down.setObjectName(u"tmedt_on_time_shut_down")
        self.tmedt_on_time_shut_down.setMinimumSize(QSize(0, 22))
        self.tmedt_on_time_shut_down.setMaximumSize(QSize(16777215, 22))
        self.tmedt_on_time_shut_down.setTime(QTime(3, 0, 0))

        self.gridLayout_18.addWidget(self.tmedt_on_time_shut_down, 1, 1, 1, 1)

        self.groupBox_15 = QGroupBox(self.tab)
        self.groupBox_15.setObjectName(u"groupBox_15")
        self.groupBox_15.setGeometry(QRect(10, 20, 131, 91))
        self.gridLayout_12 = QGridLayout(self.groupBox_15)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.chk_ban_screen_protect = QCheckBox(self.groupBox_15)
        self.chk_ban_screen_protect.setObjectName(u"chk_ban_screen_protect")

        self.gridLayout_12.addWidget(self.chk_ban_screen_protect, 2, 0, 1, 1)

        self.chk_ban_sys_sleep = QCheckBox(self.groupBox_15)
        self.chk_ban_sys_sleep.setObjectName(u"chk_ban_sys_sleep")

        self.gridLayout_12.addWidget(self.chk_ban_sys_sleep, 0, 0, 1, 1)

        self.groupBox_18 = QGroupBox(self.tab)
        self.groupBox_18.setObjectName(u"groupBox_18")
        self.groupBox_18.setGeometry(QRect(360, 20, 181, 118))
        self.gridLayout_17 = QGridLayout(self.groupBox_18)
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.label_22 = QLabel(self.groupBox_18)
        self.label_22.setObjectName(u"label_22")

        self.gridLayout_17.addWidget(self.label_22, 0, 0, 1, 1)

        self.cmb_arrange_get_wnd = QComboBox(self.groupBox_18)
        self.cmb_arrange_get_wnd.addItem("")
        self.cmb_arrange_get_wnd.addItem("")
        self.cmb_arrange_get_wnd.addItem("")
        self.cmb_arrange_get_wnd.addItem("")
        self.cmb_arrange_get_wnd.setObjectName(u"cmb_arrange_get_wnd")
        self.cmb_arrange_get_wnd.setMinimumSize(QSize(0, 20))
        self.cmb_arrange_get_wnd.setMaximumSize(QSize(16777215, 20))

        self.gridLayout_17.addWidget(self.cmb_arrange_get_wnd, 0, 1, 1, 1)

        self.label_48 = QLabel(self.groupBox_18)
        self.label_48.setObjectName(u"label_48")

        self.gridLayout_17.addWidget(self.label_48, 1, 0, 1, 1)

        self.cmb_set_plan_get_wnd = QComboBox(self.groupBox_18)
        self.cmb_set_plan_get_wnd.addItem("")
        self.cmb_set_plan_get_wnd.addItem("")
        self.cmb_set_plan_get_wnd.addItem("")
        self.cmb_set_plan_get_wnd.addItem("")
        self.cmb_set_plan_get_wnd.setObjectName(u"cmb_set_plan_get_wnd")
        self.cmb_set_plan_get_wnd.setMinimumSize(QSize(0, 20))
        self.cmb_set_plan_get_wnd.setMaximumSize(QSize(16777215, 20))

        self.gridLayout_17.addWidget(self.cmb_set_plan_get_wnd, 1, 1, 1, 1)

        self.label_55 = QLabel(self.groupBox_18)
        self.label_55.setObjectName(u"label_55")

        self.gridLayout_17.addWidget(self.label_55, 2, 0, 1, 1)

        self.cmb_set_plan_db_col = QComboBox(self.groupBox_18)
        self.cmb_set_plan_db_col.addItem("")
        self.cmb_set_plan_db_col.addItem("")
        self.cmb_set_plan_db_col.addItem("")
        self.cmb_set_plan_db_col.setObjectName(u"cmb_set_plan_db_col")
        self.cmb_set_plan_db_col.setMinimumSize(QSize(0, 20))
        self.cmb_set_plan_db_col.setMaximumSize(QSize(16777215, 20))

        self.gridLayout_17.addWidget(self.cmb_set_plan_db_col, 2, 1, 1, 1)

        self.tab_set.addTab(self.tab, "")

        self.verticalLayout.addWidget(self.tab_set)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setSpacing(4)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer)

        self.btn_main_read = QPushButton(self.page_3)
        self.btn_main_read.setObjectName(u"btn_main_read")

        self.horizontalLayout_15.addWidget(self.btn_main_read)

        self.btn_main_save = QPushButton(self.page_3)
        self.btn_main_save.setObjectName(u"btn_main_save")
        sizePolicy1.setHeightForWidth(self.btn_main_save.sizePolicy().hasHeightForWidth())
        self.btn_main_save.setSizePolicy(sizePolicy1)
        self.btn_main_save.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_15.addWidget(self.btn_main_save)


        self.verticalLayout.addLayout(self.horizontalLayout_15)


        self.gridLayout_16.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.stack_widget.addWidget(self.page_3)

        self.horizontalLayout_3.addWidget(self.stack_widget)

        WndMain.setCentralWidget(self.centralwidget)
        self.status_bar = QStatusBar(WndMain)
        self.status_bar.setObjectName(u"status_bar")
        self.status_bar.setSizeGripEnabled(False)
        WndMain.setStatusBar(self.status_bar)
        self.tool_bar = QToolBar(WndMain)
        self.tool_bar.setObjectName(u"tool_bar")
        sizePolicy4 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.tool_bar.sizePolicy().hasHeightForWidth())
        self.tool_bar.setSizePolicy(sizePolicy4)
        self.tool_bar.setMaximumSize(QSize(16777215, 16777215))
        self.tool_bar.setAutoFillBackground(True)
        self.tool_bar.setStyleSheet(u"* {\n"
"    font-size: 12px;\n"
"    font-family: \"Microsoft YaHei\";\n"
"}\n"
"QTableView {\n"
"    background: white;\n"
"    selection-color: #000000; \n"
"    gridline-color: rgb(213, 213, 213); \n"
"	selection-background-color: #a1b1c9;\n"
"    alternate-background-color: rgb(243, 246, 249);\n"
"}\n"
"QTableView::item:hover	{\n"
"    background-color: #a1b1c9;\n"
"}\n"
"")
        self.tool_bar.setIconSize(QSize(28, 36))
        self.tool_bar.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.tool_bar.setFloatable(True)
        WndMain.addToolBar(Qt.LeftToolBarArea, self.tool_bar)

        self.tool_bar.addAction(self.action_console)
        self.tool_bar.addAction(self.action_plan)
        self.tool_bar.addAction(self.action_setting)

        self.retranslateUi(WndMain)

        self.stack_widget.setCurrentIndex(1)
        self.tab_set.setCurrentIndex(0)
        self.cmb_double_time.setCurrentIndex(1)
        self.cmb_daye_map.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(WndMain)
    # setupUi

    def retranslateUi(self, WndMain):
        WndMain.setWindowTitle(QCoreApplication.translate("WndMain", u"Robot", None))
        self.action_console.setText(QCoreApplication.translate("WndMain", u"\u63a7 \u5236", None))
#if QT_CONFIG(shortcut)
        self.action_console.setShortcut(QCoreApplication.translate("WndMain", u"Alt+1", None))
#endif // QT_CONFIG(shortcut)
        self.action_plan.setText(QCoreApplication.translate("WndMain", u"\u65b9 \u6848", None))
#if QT_CONFIG(shortcut)
        self.action_plan.setShortcut(QCoreApplication.translate("WndMain", u"Alt+2", None))
#endif // QT_CONFIG(shortcut)
        self.action_setting.setText(QCoreApplication.translate("WndMain", u"\u914d \u7f6e", None))
#if QT_CONFIG(shortcut)
        self.action_setting.setShortcut(QCoreApplication.translate("WndMain", u"Alt+3", None))
#endif // QT_CONFIG(shortcut)
        ___qtablewidgetitem = self.tbe_console.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("WndMain", u"\u7a97\u53e3", None));
#if QT_CONFIG(tooltip)
        ___qtablewidgetitem.setToolTip(QCoreApplication.translate("WndMain", u"\u53cc\u51fb\u8868\u5934\u83b7\u53d6\u5168\u90e8\u6e38\u620f\u7a97\u53e3\u53e5\u67c4, \u53cc\u51fb\u672c\u5217\u4e0b\u7684\u8868\u9879\u53ef\u663e\u793a\u6fc0\u6d3b\u8be5\u7a97\u53e3", None));
#endif // QT_CONFIG(tooltip)
        ___qtablewidgetitem1 = self.tbe_console.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("WndMain", u"\u65b9\u6848", None));
#if QT_CONFIG(tooltip)
        ___qtablewidgetitem1.setToolTip(QCoreApplication.translate("WndMain", u"\u53cc\u51fb\u8868\u5934\u53ef\u5168\u90e8\u8bbe\u7f6e\u65b9\u6848", None));
#endif // QT_CONFIG(tooltip)
        ___qtablewidgetitem2 = self.tbe_console.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("WndMain", u"\u8fd0\u884c", None));
#if QT_CONFIG(tooltip)
        ___qtablewidgetitem2.setToolTip(QCoreApplication.translate("WndMain", u"\u53cc\u51fb\u8868\u5934\u53ef\u5168\u90e8\u8fd0\u884c, \u53cc\u51fb\u672c\u5217\u4e0b\u7684\u8868\u9879\u53ef\u8fd0\u884c\u5355\u4e2a\u7a97\u53e3", None));
#endif // QT_CONFIG(tooltip)
        ___qtablewidgetitem3 = self.tbe_console.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("WndMain", u"\u6682\u505c", None));
#if QT_CONFIG(tooltip)
        ___qtablewidgetitem3.setToolTip(QCoreApplication.translate("WndMain", u"\u53cc\u51fb\u8868\u5934\u53ef\u5168\u90e8\u6682\u505c, \u53cc\u51fb\u672c\u5217\u4e0b\u7684\u8868\u9879\u53ef\u6682\u505c\u5355\u4e2a\u7a97\u53e3", None));
#endif // QT_CONFIG(tooltip)
        ___qtablewidgetitem4 = self.tbe_console.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("WndMain", u"\u7ec8\u6b62", None));
#if QT_CONFIG(tooltip)
        ___qtablewidgetitem4.setToolTip(QCoreApplication.translate("WndMain", u"\u53cc\u51fb\u8868\u5934\u53ef\u5168\u90e8\u7ec8\u6b62, \u53cc\u51fb\u672c\u5217\u4e0b\u7684\u8868\u9879\u53ef\u7ec8\u6b62\u5355\u4e2a\u7a97\u53e3", None));
#endif // QT_CONFIG(tooltip)
        ___qtablewidgetitem5 = self.tbe_console.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("WndMain", u"\u65e5\u5fd7", None));
#if QT_CONFIG(tooltip)
        ___qtablewidgetitem5.setToolTip(QCoreApplication.translate("WndMain", u"\u53cc\u51fb\u8868\u5934\u53ef\u663e\u793a\u672c\u8f6f\u4ef6\u65e5\u5fd7, \u53cc\u51fb\u672c\u5217\u4e0b\u7684\u8868\u9879\u53ef\u663e\u793a\u5404\u7a97\u53e3\u6267\u884c\u65e5\u5fd7", None));
#endif // QT_CONFIG(tooltip)
        ___qtablewidgetitem6 = self.tbe_console.verticalHeaderItem(0)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("WndMain", u" 1 ", None));
#if QT_CONFIG(tooltip)
        ___qtablewidgetitem6.setToolTip(QCoreApplication.translate("WndMain", u"\u53cc\u51fb \u5782\u76f4 \u8868\u5934, \u663e\u793a/\u9690\u85cf\u8be5\u7a97\u53e3", None));
#endif // QT_CONFIG(tooltip)
        ___qtablewidgetitem7 = self.tbe_console.verticalHeaderItem(1)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("WndMain", u" 2 ", None));
#if QT_CONFIG(tooltip)
        ___qtablewidgetitem7.setToolTip(QCoreApplication.translate("WndMain", u"\u53cc\u51fb \u5782\u76f4 \u8868\u5934, \u663e\u793a/\u9690\u85cf\u8be5\u7a97\u53e3", None));
#endif // QT_CONFIG(tooltip)
        ___qtablewidgetitem8 = self.tbe_console.verticalHeaderItem(2)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("WndMain", u" 3 ", None));
#if QT_CONFIG(tooltip)
        ___qtablewidgetitem8.setToolTip(QCoreApplication.translate("WndMain", u"\u53cc\u51fb \u5782\u76f4 \u8868\u5934, \u663e\u793a/\u9690\u85cf\u8be5\u7a97\u53e3", None));
#endif // QT_CONFIG(tooltip)
        ___qtablewidgetitem9 = self.tbe_console.verticalHeaderItem(3)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("WndMain", u" 4 ", None));
#if QT_CONFIG(tooltip)
        ___qtablewidgetitem9.setToolTip(QCoreApplication.translate("WndMain", u"\u53cc\u51fb \u5782\u76f4 \u8868\u5934, \u663e\u793a/\u9690\u85cf\u8be5\u7a97\u53e3", None));
#endif // QT_CONFIG(tooltip)
        ___qtablewidgetitem10 = self.tbe_console.verticalHeaderItem(4)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("WndMain", u" 5 ", None));
#if QT_CONFIG(tooltip)
        ___qtablewidgetitem10.setToolTip(QCoreApplication.translate("WndMain", u"\u53cc\u51fb \u5782\u76f4 \u8868\u5934, \u663e\u793a/\u9690\u85cf\u8be5\u7a97\u53e3", None));
#endif // QT_CONFIG(tooltip)
        ___qtablewidgetitem11 = self.tbe_console.verticalHeaderItem(5)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("WndMain", u" 6 ", None));
#if QT_CONFIG(tooltip)
        ___qtablewidgetitem11.setToolTip(QCoreApplication.translate("WndMain", u"\u53cc\u51fb \u5782\u76f4 \u8868\u5934, \u663e\u793a/\u9690\u85cf\u8be5\u7a97\u53e3", None));
#endif // QT_CONFIG(tooltip)
        ___qtablewidgetitem12 = self.tbe_console.verticalHeaderItem(6)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("WndMain", u" 7 ", None));
#if QT_CONFIG(tooltip)
        ___qtablewidgetitem12.setToolTip(QCoreApplication.translate("WndMain", u"\u53cc\u51fb \u5782\u76f4 \u8868\u5934, \u663e\u793a/\u9690\u85cf\u8be5\u7a97\u53e3", None));
#endif // QT_CONFIG(tooltip)
        ___qtablewidgetitem13 = self.tbe_console.verticalHeaderItem(7)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("WndMain", u" 8 ", None));
#if QT_CONFIG(tooltip)
        ___qtablewidgetitem13.setToolTip(QCoreApplication.translate("WndMain", u"\u53cc\u51fb \u5782\u76f4 \u8868\u5934, \u663e\u793a/\u9690\u85cf\u8be5\u7a97\u53e3", None));
#endif // QT_CONFIG(tooltip)
        ___qtablewidgetitem14 = self.tbe_console.verticalHeaderItem(8)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("WndMain", u" 9 ", None));
#if QT_CONFIG(tooltip)
        ___qtablewidgetitem14.setToolTip(QCoreApplication.translate("WndMain", u"\u53cc\u51fb \u5782\u76f4 \u8868\u5934, \u663e\u793a/\u9690\u85cf\u8be5\u7a97\u53e3", None));
#endif // QT_CONFIG(tooltip)
        ___qtablewidgetitem15 = self.tbe_console.verticalHeaderItem(9)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("WndMain", u"10", None));
#if QT_CONFIG(tooltip)
        ___qtablewidgetitem15.setToolTip(QCoreApplication.translate("WndMain", u"\u53cc\u51fb \u5782\u76f4 \u8868\u5934, \u663e\u793a/\u9690\u85cf\u8be5\u7a97\u53e3", None));
#endif // QT_CONFIG(tooltip)
        ___qtablewidgetitem16 = self.tbe_console.verticalHeaderItem(10)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("WndMain", u"11", None));
#if QT_CONFIG(tooltip)
        ___qtablewidgetitem16.setToolTip(QCoreApplication.translate("WndMain", u"\u53cc\u51fb \u5782\u76f4 \u8868\u5934, \u663e\u793a/\u9690\u85cf\u8be5\u7a97\u53e3", None));
#endif // QT_CONFIG(tooltip)
        ___qtablewidgetitem17 = self.tbe_console.verticalHeaderItem(11)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("WndMain", u"12", None));
#if QT_CONFIG(tooltip)
        ___qtablewidgetitem17.setToolTip(QCoreApplication.translate("WndMain", u"\u53cc\u51fb \u5782\u76f4 \u8868\u5934, \u663e\u793a/\u9690\u85cf\u8be5\u7a97\u53e3", None));
#endif // QT_CONFIG(tooltip)
        ___qtablewidgetitem18 = self.tbe_console.verticalHeaderItem(12)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("WndMain", u"13", None));
#if QT_CONFIG(tooltip)
        ___qtablewidgetitem18.setToolTip(QCoreApplication.translate("WndMain", u"\u53cc\u51fb \u5782\u76f4 \u8868\u5934, \u663e\u793a/\u9690\u85cf\u8be5\u7a97\u53e3", None));
#endif // QT_CONFIG(tooltip)
        ___qtablewidgetitem19 = self.tbe_console.verticalHeaderItem(13)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("WndMain", u"14", None));
#if QT_CONFIG(tooltip)
        ___qtablewidgetitem19.setToolTip(QCoreApplication.translate("WndMain", u"\u53cc\u51fb \u5782\u76f4 \u8868\u5934, \u663e\u793a/\u9690\u85cf\u8be5\u7a97\u53e3", None));
#endif // QT_CONFIG(tooltip)
        ___qtablewidgetitem20 = self.tbe_console.verticalHeaderItem(14)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("WndMain", u"15", None));
#if QT_CONFIG(tooltip)
        ___qtablewidgetitem20.setToolTip(QCoreApplication.translate("WndMain", u"\u53cc\u51fb \u5782\u76f4 \u8868\u5934, \u663e\u793a/\u9690\u85cf\u8be5\u7a97\u53e3", None));
#endif // QT_CONFIG(tooltip)

        __sortingEnabled = self.tbe_console.isSortingEnabled()
        self.tbe_console.setSortingEnabled(False)
        self.tbe_console.setSortingEnabled(__sortingEnabled)

        self.label_49.setText(QCoreApplication.translate("WndMain", u"\u529f\u80fd\u5217\u8868", None))
        ___qtreewidgetitem = self.tre_all.headerItem()
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("WndMain", u"\u6240\u6709\u529f\u80fd", None));

        __sortingEnabled1 = self.tre_all.isSortingEnabled()
        self.tre_all.setSortingEnabled(False)
        ___qtreewidgetitem1 = self.tre_all.topLevelItem(0)
        ___qtreewidgetitem1.setText(0, QCoreApplication.translate("WndMain", u"\u5355\u4eba", None));
        ___qtreewidgetitem2 = ___qtreewidgetitem1.child(0)
        ___qtreewidgetitem2.setText(0, QCoreApplication.translate("WndMain", u"\u56db\u8c61\u8dd1\u73af", None));
        ___qtreewidgetitem3 = ___qtreewidgetitem1.child(1)
        ___qtreewidgetitem3.setText(0, QCoreApplication.translate("WndMain", u"\u5e08\u95e8\u8dd1\u73af", None));
        ___qtreewidgetitem4 = self.tre_all.topLevelItem(1)
        ___qtreewidgetitem4.setText(0, QCoreApplication.translate("WndMain", u"\u7ec4\u961f", None));
        ___qtreewidgetitem5 = ___qtreewidgetitem4.child(0)
        ___qtreewidgetitem5.setText(0, QCoreApplication.translate("WndMain", u"\u961f\u5458\u6302\u673a", None));
        ___qtreewidgetitem6 = ___qtreewidgetitem4.child(1)
        ___qtreewidgetitem6.setText(0, QCoreApplication.translate("WndMain", u"\u5e26\u961f\u5237\u91ce", None));
        ___qtreewidgetitem7 = ___qtreewidgetitem4.child(2)
        ___qtreewidgetitem7.setText(0, QCoreApplication.translate("WndMain", u"\u5e26\u961f\u6253\u725b", None));
        ___qtreewidgetitem8 = ___qtreewidgetitem4.child(3)
        ___qtreewidgetitem8.setText(0, QCoreApplication.translate("WndMain", u"\u5e26\u961f\u6253\u864e", None));
        ___qtreewidgetitem9 = ___qtreewidgetitem4.child(4)
        ___qtreewidgetitem9.setText(0, QCoreApplication.translate("WndMain", u"\u5e26\u961f\u5e73\u4e71", None));
        ___qtreewidgetitem10 = ___qtreewidgetitem4.child(5)
        ___qtreewidgetitem10.setText(0, QCoreApplication.translate("WndMain", u"\u5e26\u961f\u5a01\u671b", None));
        ___qtreewidgetitem11 = self.tre_all.topLevelItem(2)
        ___qtreewidgetitem11.setText(0, QCoreApplication.translate("WndMain", u"\u5176\u5b83", None));
        ___qtreewidgetitem12 = ___qtreewidgetitem11.child(0)
        ___qtreewidgetitem12.setText(0, QCoreApplication.translate("WndMain", u"\u9886\u53d6\u53cc\u500d", None));
        ___qtreewidgetitem13 = ___qtreewidgetitem11.child(1)
        ___qtreewidgetitem13.setText(0, QCoreApplication.translate("WndMain", u"\u51bb\u7ed3\u53cc\u500d", None));
        ___qtreewidgetitem14 = ___qtreewidgetitem11.child(2)
        ___qtreewidgetitem14.setText(0, QCoreApplication.translate("WndMain", u"\u9000\u51fa\u961f\u4f0d", None));
        ___qtreewidgetitem15 = ___qtreewidgetitem11.child(3)
        ___qtreewidgetitem15.setText(0, QCoreApplication.translate("WndMain", u"\u6e05\u7406\u80cc\u5305", None));
        self.tre_all.setSortingEnabled(__sortingEnabled1)

#if QT_CONFIG(tooltip)
        self.tre_all.setToolTip(QCoreApplication.translate("WndMain", u"\u53cc\u51fb\u5217\u8868\u9879\u53ef\u6dfb\u52a0\u5230\u6267\u884c\u5217\u8868", None))
#endif // QT_CONFIG(tooltip)
        self.label_52.setText(QCoreApplication.translate("WndMain", u"\u6267\u884c\u5217\u8868", None))
#if QT_CONFIG(tooltip)
        self.lst_exec.setToolTip(QCoreApplication.translate("WndMain", u"\u53cc\u51fb\u9009\u4e2d\u5217\u8868\u9879\u53ef\u4ece\u6267\u884c\u5217\u8868\u4e2d\u5220\u9664, \u6309\u4f4f\u5e76\u62d6\u52a8\u53ef\u8c03\u6574\u4efb\u52a1\u7684\u6267\u884c\u987a\u5e8f", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.btn_plan_save.setToolTip(QCoreApplication.translate("WndMain", u"\u4fdd\u5b58 \u6267\u884c\u5217\u8868\u548c\u6218\u6597\u8bbe\u7f6e \u5230 \u9009\u4e2d\u65b9\u6848, \u672a\u9009\u62e9\u65b9\u6848\u5219\u4fdd\u5b58\u5230\u5185\u7f6e\u9ed8\u8ba4\u65b9\u6848\u4e2d", None))
#endif // QT_CONFIG(tooltip)
        self.btn_plan_save.setText(QCoreApplication.translate("WndMain", u"\u4fdd\u5b58\u5230\u65b9\u6848\u2192", None))
        self.label_53.setText(QCoreApplication.translate("WndMain", u"\u65b9\u6848\u5217\u8868", None))
#if QT_CONFIG(tooltip)
        self.lst_plan.setToolTip(QCoreApplication.translate("WndMain", u"\u53cc\u51fb\u5217\u8868\u9879\u53ef\u8bfb\u53d6\u6307\u5b9a\u65b9\u6848\u5230\u63a7\u4ef6", None))
#endif // QT_CONFIG(tooltip)
        self.btn_plan_create.setText(QCoreApplication.translate("WndMain", u"\u65b0\u5efa", None))
        self.btn_plan_rename.setText(QCoreApplication.translate("WndMain", u"\u91cd\u547d\u540d", None))
        self.label_54.setText(QCoreApplication.translate("WndMain", u"\u65b0\u65b9\u6848\u540d", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("WndMain", u"\u65b9\u6848-\u57fa\u672c\u914d\u7f6e", None))
        self.tab_set.setTabText(self.tab_set.indexOf(self.tab_5), QCoreApplication.translate("WndMain", u"\u5355\u4eba\u76f8\u5173", None))
        self.groupBox_7.setTitle(QCoreApplication.translate("WndMain", u"\u961f\u5458\u6302\u673a", None))
        self.chk_duiyuan_ls.setText(QCoreApplication.translate("WndMain", u"\u8ddf\u968f\u961f\u957f\u9886\u53cc", None))
        self.chk_duiyuan_td.setText(QCoreApplication.translate("WndMain", u"\u8ddf\u968f\u961f\u957f\u9000\u961f", None))
        self.chk_duiyuan_closetalk.setText(QCoreApplication.translate("WndMain", u"\u81ea\u52a8\u5173\u95ed\u5bf9\u8bdd\u6846", None))
        self.chk_duiyuan_js.setText(QCoreApplication.translate("WndMain", u"\u8ddf\u968f\u961f\u957f\u89e3\u51bb\u53cc", None))
        self.chk_duiyuan_ds.setText(QCoreApplication.translate("WndMain", u"\u8ddf\u968f\u961f\u957f\u51bb\u53cc", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("WndMain", u"\u9886\u53d6\u53cc\u500d", None))
        self.label_17.setText(QCoreApplication.translate("WndMain", u"\u65f6\u95f4", None))
        self.cmb_double_time.setItemText(0, QCoreApplication.translate("WndMain", u"1\u5c0f\u65f6", None))
        self.cmb_double_time.setItemText(1, QCoreApplication.translate("WndMain", u"2\u5c0f\u65f6", None))
        self.cmb_double_time.setItemText(2, QCoreApplication.translate("WndMain", u"4\u5c0f\u65f6", None))

        self.groupBox.setTitle(QCoreApplication.translate("WndMain", u"\u5e26\u961f\u6253\u91ce", None))
        self.label_4.setText(QCoreApplication.translate("WndMain", u"\u5730\u56fe", None))
        self.cmb_daye_map.setItemText(0, QCoreApplication.translate("WndMain", u"\u96c1\u95e8\u5173", None))
        self.cmb_daye_map.setItemText(1, QCoreApplication.translate("WndMain", u"\u5937\u6d32\u5c9b", None))
        self.cmb_daye_map.setItemText(2, QCoreApplication.translate("WndMain", u"\u5927\u8349\u539f", None))
        self.cmb_daye_map.setItemText(3, QCoreApplication.translate("WndMain", u"\u79e6\u5cad\u4e00\u5c42", None))
        self.cmb_daye_map.setItemText(4, QCoreApplication.translate("WndMain", u"\u7384\u971c\u6d45\u6ee9", None))
        self.cmb_daye_map.setItemText(5, QCoreApplication.translate("WndMain", u"\u8d64\u971e\u6e21\u53e3", None))
        self.cmb_daye_map.setItemText(6, QCoreApplication.translate("WndMain", u"\u9752\u4e91\u5e7d\u8c37", None))
        self.cmb_daye_map.setItemText(7, QCoreApplication.translate("WndMain", u"\u71d5\u5b50\u575e", None))
        self.cmb_daye_map.setItemText(8, QCoreApplication.translate("WndMain", u"\u697c\u5170\u53e4\u9053", None))
        self.cmb_daye_map.setItemText(9, QCoreApplication.translate("WndMain", u"\u7389\u95e8\u5173", None))

        self.cmb_daye_map.setCurrentText(QCoreApplication.translate("WndMain", u"\u5927\u8349\u539f", None))
        self.label_5.setText(QCoreApplication.translate("WndMain", u"\u65f6\u95f4", None))
#if QT_CONFIG(tooltip)
        self.edt_daye_time.setToolTip(QCoreApplication.translate("WndMain", u"\u8bf7\u8f93\u51650-999\u4e4b\u95f4\u7684\u6570\u5b57", None))
#endif // QT_CONFIG(tooltip)
        self.edt_daye_time.setText(QCoreApplication.translate("WndMain", u"600", None))
        self.label_6.setText(QCoreApplication.translate("WndMain", u"\u5206\u949f", None))
        self.tab_set.setTabText(self.tab_set.indexOf(self.tab_6), QCoreApplication.translate("WndMain", u"\u7ec4\u961f\u76f8\u5173", None))
        self.chk_on_time.setTitle(QCoreApplication.translate("WndMain", u"\u5b9a\u65f6", None))
        self.chk_on_time_run_all.setText(QCoreApplication.translate("WndMain", u"\u8fd0\u884c\u5168\u90e8\u7a97\u53e3", None))
        self.tmedt_on_time_run_all.setDisplayFormat(QCoreApplication.translate("WndMain", u"HH:mm", None))
        self.chk_on_time_shut_down.setText(QCoreApplication.translate("WndMain", u"\u5173\u95ed\u8ba1\u7b97\u673a", None))
        self.tmedt_on_time_shut_down.setDisplayFormat(QCoreApplication.translate("WndMain", u"HH:mm", None))
        self.groupBox_15.setTitle(QCoreApplication.translate("WndMain", u"\u7cfb\u7edf", None))
        self.chk_ban_screen_protect.setText(QCoreApplication.translate("WndMain", u"\u7981\u7528\u5c4f\u5e55\u4fdd\u62a4", None))
        self.chk_ban_sys_sleep.setText(QCoreApplication.translate("WndMain", u"\u7981\u7528\u7cfb\u7edf\u7761\u7720", None))
        self.groupBox_18.setTitle(QCoreApplication.translate("WndMain", u"\u63a7\u5236\u8868", None))
        self.label_22.setText(QCoreApplication.translate("WndMain", u"\u83b7\u53d6\u7a97\u53e3\u540e\u6392\u5217\u65b9\u5f0f", None))
        self.cmb_arrange_get_wnd.setItemText(0, QCoreApplication.translate("WndMain", u"0", None))
        self.cmb_arrange_get_wnd.setItemText(1, QCoreApplication.translate("WndMain", u"1", None))
        self.cmb_arrange_get_wnd.setItemText(2, QCoreApplication.translate("WndMain", u"2", None))
        self.cmb_arrange_get_wnd.setItemText(3, QCoreApplication.translate("WndMain", u"3", None))

        self.label_48.setText(QCoreApplication.translate("WndMain", u"\u83b7\u53d6\u7a97\u53e3\u540e\u8bbe\u7f6e\u65b9\u6848", None))
        self.cmb_set_plan_get_wnd.setItemText(0, QCoreApplication.translate("WndMain", u"0", None))
        self.cmb_set_plan_get_wnd.setItemText(1, QCoreApplication.translate("WndMain", u"1", None))
        self.cmb_set_plan_get_wnd.setItemText(2, QCoreApplication.translate("WndMain", u"2", None))
        self.cmb_set_plan_get_wnd.setItemText(3, QCoreApplication.translate("WndMain", u"3", None))

        self.label_55.setText(QCoreApplication.translate("WndMain", u"\u53cc\u51fb\u65b9\u6848\u5217\u8bbe\u7f6e\u65b9\u6848", None))
        self.cmb_set_plan_db_col.setItemText(0, QCoreApplication.translate("WndMain", u"1", None))
        self.cmb_set_plan_db_col.setItemText(1, QCoreApplication.translate("WndMain", u"2", None))
        self.cmb_set_plan_db_col.setItemText(2, QCoreApplication.translate("WndMain", u"3", None))

        self.tab_set.setTabText(self.tab_set.indexOf(self.tab), QCoreApplication.translate("WndMain", u"\u5176\u5b83\u914d\u7f6e", None))
        self.btn_main_read.setText(QCoreApplication.translate("WndMain", u"\u8bfb \u53d6", None))
        self.btn_main_save.setText(QCoreApplication.translate("WndMain", u"\u4fdd \u5b58", None))
        self.tool_bar.setWindowTitle(QCoreApplication.translate("WndMain", u"toolBar", None))
    # retranslateUi

