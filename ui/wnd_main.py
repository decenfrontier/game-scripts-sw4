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
        WndMain.resize(755, 475)
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
        self.action_gnrl = QAction(WndMain)
        self.action_gnrl.setObjectName(u"action_gnrl")
        self.action_gnrl.setCheckable(False)
        icon3 = QIcon()
        icon3.addFile(u":/gnrl7.png", QSize(), QIcon.Normal, QIcon.Off)
        self.action_gnrl.setIcon(icon3)
        self.centralwidget = QWidget(WndMain)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_13 = QGridLayout(self.centralwidget)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.gridLayout_13.setContentsMargins(2, 2, 2, 2)
        self.stack_widget = QStackedWidget(self.centralwidget)
        self.stack_widget.setObjectName(u"stack_widget")
        self.stack_widget.setFrameShape(QFrame.NoFrame)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.gridLayout_14 = QGridLayout(self.page)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.gridLayout_14.setContentsMargins(2, 2, 2, 2)
        self.tbe_console = QTableWidget(self.page)
        if (self.tbe_console.columnCount() < 7):
            self.tbe_console.setColumnCount(7)
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
        __qtablewidgetitem6 = QTableWidgetItem()
        __qtablewidgetitem6.setTextAlignment(Qt.AlignCenter);
        self.tbe_console.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        if (self.tbe_console.rowCount() < 15):
            self.tbe_console.setRowCount(15)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tbe_console.setVerticalHeaderItem(0, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tbe_console.setVerticalHeaderItem(1, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tbe_console.setVerticalHeaderItem(2, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tbe_console.setVerticalHeaderItem(3, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tbe_console.setVerticalHeaderItem(4, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tbe_console.setVerticalHeaderItem(5, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tbe_console.setVerticalHeaderItem(6, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        __qtablewidgetitem14.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.tbe_console.setVerticalHeaderItem(7, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tbe_console.setVerticalHeaderItem(8, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tbe_console.setVerticalHeaderItem(9, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tbe_console.setVerticalHeaderItem(10, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tbe_console.setVerticalHeaderItem(11, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.tbe_console.setVerticalHeaderItem(12, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.tbe_console.setVerticalHeaderItem(13, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.tbe_console.setVerticalHeaderItem(14, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.tbe_console.setItem(0, 0, __qtablewidgetitem22)
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
        self.gridLayout_15 = QGridLayout(self.page_2)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.gridLayout_15.setContentsMargins(2, 2, 2, 2)
        self.verticalLayout_16 = QVBoxLayout()
        self.verticalLayout_16.setSpacing(2)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.label_52 = QLabel(self.page_2)
        self.label_52.setObjectName(u"label_52")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_52.sizePolicy().hasHeightForWidth())
        self.label_52.setSizePolicy(sizePolicy1)
        self.label_52.setMinimumSize(QSize(0, 15))
        self.label_52.setAlignment(Qt.AlignCenter)

        self.verticalLayout_16.addWidget(self.label_52)

        self.lst_exec = QListWidget(self.page_2)
        self.lst_exec.setObjectName(u"lst_exec")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.lst_exec.sizePolicy().hasHeightForWidth())
        self.lst_exec.setSizePolicy(sizePolicy2)
        self.lst_exec.setMinimumSize(QSize(90, 200))
        self.lst_exec.setMaximumSize(QSize(90, 16777215))
        self.lst_exec.setDragEnabled(True)
        self.lst_exec.setDragDropMode(QAbstractItemView.DragDrop)
        self.lst_exec.setDefaultDropAction(Qt.MoveAction)

        self.verticalLayout_16.addWidget(self.lst_exec)


        self.gridLayout_15.addLayout(self.verticalLayout_16, 0, 1, 3, 1)

        self.gridLayout_10 = QGridLayout()
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.gridLayout_10.setVerticalSpacing(2)
        self.lst_plan = QListWidget(self.page_2)
        self.lst_plan.setObjectName(u"lst_plan")
        sizePolicy2.setHeightForWidth(self.lst_plan.sizePolicy().hasHeightForWidth())
        self.lst_plan.setSizePolicy(sizePolicy2)
        self.lst_plan.setMinimumSize(QSize(0, 0))
        self.lst_plan.setMaximumSize(QSize(110, 16777215))

        self.gridLayout_10.addWidget(self.lst_plan, 1, 0, 1, 2)

        self.label_54 = QLabel(self.page_2)
        self.label_54.setObjectName(u"label_54")

        self.gridLayout_10.addWidget(self.label_54, 2, 0, 1, 1)

        self.edt_plan_new_name = QLineEdit(self.page_2)
        self.edt_plan_new_name.setObjectName(u"edt_plan_new_name")
        sizePolicy1.setHeightForWidth(self.edt_plan_new_name.sizePolicy().hasHeightForWidth())
        self.edt_plan_new_name.setSizePolicy(sizePolicy1)
        self.edt_plan_new_name.setMinimumSize(QSize(0, 0))
        self.edt_plan_new_name.setMaximumSize(QSize(110, 16777215))
        self.edt_plan_new_name.setAlignment(Qt.AlignCenter)

        self.gridLayout_10.addWidget(self.edt_plan_new_name, 3, 0, 1, 2)

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

        self.label_53 = QLabel(self.page_2)
        self.label_53.setObjectName(u"label_53")
        sizePolicy1.setHeightForWidth(self.label_53.sizePolicy().hasHeightForWidth())
        self.label_53.setSizePolicy(sizePolicy1)
        self.label_53.setMinimumSize(QSize(0, 0))
        self.label_53.setMaximumSize(QSize(110, 16777215))
        self.label_53.setAlignment(Qt.AlignCenter)

        self.gridLayout_10.addWidget(self.label_53, 0, 0, 1, 2)


        self.gridLayout_15.addLayout(self.gridLayout_10, 0, 4, 3, 1)

        self.groupBox_3 = QGroupBox(self.page_2)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.verticalLayout_3 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.gridLayout_11 = QGridLayout()
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.label_21 = QLabel(self.groupBox_3)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setMinimumSize(QSize(0, 20))

        self.gridLayout_11.addWidget(self.label_21, 0, 0, 1, 1)

        self.cmb_policy_bb = QComboBox(self.groupBox_3)
        self.cmb_policy_bb.addItem("")
        self.cmb_policy_bb.addItem("")
        self.cmb_policy_bb.addItem("")
        self.cmb_policy_bb.setObjectName(u"cmb_policy_bb")
        sizePolicy1.setHeightForWidth(self.cmb_policy_bb.sizePolicy().hasHeightForWidth())
        self.cmb_policy_bb.setSizePolicy(sizePolicy1)
        self.cmb_policy_bb.setMinimumSize(QSize(55, 20))

        self.gridLayout_11.addWidget(self.cmb_policy_bb, 0, 1, 1, 1)


        self.verticalLayout_3.addLayout(self.gridLayout_11)

        self.chk_fuyu = QCheckBox(self.groupBox_3)
        self.chk_fuyu.setObjectName(u"chk_fuyu")
        sizePolicy1.setHeightForWidth(self.chk_fuyu.sizePolicy().hasHeightForWidth())
        self.chk_fuyu.setSizePolicy(sizePolicy1)
        self.chk_fuyu.setMinimumSize(QSize(85, 20))
        self.chk_fuyu.setChecked(True)

        self.verticalLayout_3.addWidget(self.chk_fuyu)

        self.chk_da_rou_shan = QCheckBox(self.groupBox_3)
        self.chk_da_rou_shan.setObjectName(u"chk_da_rou_shan")
        sizePolicy1.setHeightForWidth(self.chk_da_rou_shan.sizePolicy().hasHeightForWidth())
        self.chk_da_rou_shan.setSizePolicy(sizePolicy1)
        self.chk_da_rou_shan.setMinimumSize(QSize(85, 20))
        self.chk_da_rou_shan.setChecked(True)

        self.verticalLayout_3.addWidget(self.chk_da_rou_shan)

        self.chk_zhao_huan = QCheckBox(self.groupBox_3)
        self.chk_zhao_huan.setObjectName(u"chk_zhao_huan")
        self.chk_zhao_huan.setChecked(True)

        self.verticalLayout_3.addWidget(self.chk_zhao_huan)

        self.chk_df_lahuan = QCheckBox(self.groupBox_3)
        self.chk_df_lahuan.setObjectName(u"chk_df_lahuan")
        self.chk_df_lahuan.setChecked(True)

        self.verticalLayout_3.addWidget(self.chk_df_lahuan)

        self.chk_save_people = QCheckBox(self.groupBox_3)
        self.chk_save_people.setObjectName(u"chk_save_people")
        self.chk_save_people.setChecked(True)

        self.verticalLayout_3.addWidget(self.chk_save_people)

        self.chk_tm_anqi = QCheckBox(self.groupBox_3)
        self.chk_tm_anqi.setObjectName(u"chk_tm_anqi")
        sizePolicy1.setHeightForWidth(self.chk_tm_anqi.sizePolicy().hasHeightForWidth())
        self.chk_tm_anqi.setSizePolicy(sizePolicy1)
        self.chk_tm_anqi.setMinimumSize(QSize(85, 20))
        self.chk_tm_anqi.setChecked(True)

        self.verticalLayout_3.addWidget(self.chk_tm_anqi)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(self.groupBox_3)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(0, 20))

        self.gridLayout.addWidget(self.label, 0, 0, 1, 2)

        self.label_42 = QLabel(self.groupBox_3)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setMinimumSize(QSize(0, 20))

        self.gridLayout.addWidget(self.label_42, 1, 0, 1, 1)

        self.cmb_skill_round1 = QComboBox(self.groupBox_3)
        self.cmb_skill_round1.addItem("")
        self.cmb_skill_round1.addItem("")
        self.cmb_skill_round1.addItem("")
        self.cmb_skill_round1.addItem("")
        self.cmb_skill_round1.addItem("")
        self.cmb_skill_round1.addItem("")
        self.cmb_skill_round1.addItem("")
        self.cmb_skill_round1.addItem("")
        self.cmb_skill_round1.addItem("")
        self.cmb_skill_round1.setObjectName(u"cmb_skill_round1")
        sizePolicy1.setHeightForWidth(self.cmb_skill_round1.sizePolicy().hasHeightForWidth())
        self.cmb_skill_round1.setSizePolicy(sizePolicy1)
        self.cmb_skill_round1.setMinimumSize(QSize(55, 20))

        self.gridLayout.addWidget(self.cmb_skill_round1, 1, 1, 1, 1)

        self.label_43 = QLabel(self.groupBox_3)
        self.label_43.setObjectName(u"label_43")
        self.label_43.setMinimumSize(QSize(0, 20))

        self.gridLayout.addWidget(self.label_43, 2, 0, 1, 1)

        self.cmb_obj_round1 = QComboBox(self.groupBox_3)
        self.cmb_obj_round1.addItem("")
        self.cmb_obj_round1.addItem("")
        self.cmb_obj_round1.setObjectName(u"cmb_obj_round1")
        sizePolicy1.setHeightForWidth(self.cmb_obj_round1.sizePolicy().hasHeightForWidth())
        self.cmb_obj_round1.setSizePolicy(sizePolicy1)
        self.cmb_obj_round1.setMinimumSize(QSize(55, 20))

        self.gridLayout.addWidget(self.cmb_obj_round1, 2, 1, 1, 1)


        self.verticalLayout_3.addLayout(self.gridLayout)

        self.gridLayout_6 = QGridLayout()
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.label_46 = QLabel(self.groupBox_3)
        self.label_46.setObjectName(u"label_46")
        self.label_46.setMinimumSize(QSize(0, 20))

        self.gridLayout_6.addWidget(self.label_46, 0, 0, 1, 2)

        self.label_44 = QLabel(self.groupBox_3)
        self.label_44.setObjectName(u"label_44")
        self.label_44.setMinimumSize(QSize(0, 20))

        self.gridLayout_6.addWidget(self.label_44, 1, 0, 1, 1)

        self.cmb_skill_round2 = QComboBox(self.groupBox_3)
        self.cmb_skill_round2.addItem("")
        self.cmb_skill_round2.addItem("")
        self.cmb_skill_round2.addItem("")
        self.cmb_skill_round2.addItem("")
        self.cmb_skill_round2.addItem("")
        self.cmb_skill_round2.addItem("")
        self.cmb_skill_round2.addItem("")
        self.cmb_skill_round2.addItem("")
        self.cmb_skill_round2.addItem("")
        self.cmb_skill_round2.setObjectName(u"cmb_skill_round2")
        sizePolicy1.setHeightForWidth(self.cmb_skill_round2.sizePolicy().hasHeightForWidth())
        self.cmb_skill_round2.setSizePolicy(sizePolicy1)
        self.cmb_skill_round2.setMinimumSize(QSize(55, 20))

        self.gridLayout_6.addWidget(self.cmb_skill_round2, 1, 1, 1, 1)

        self.label_45 = QLabel(self.groupBox_3)
        self.label_45.setObjectName(u"label_45")
        self.label_45.setMinimumSize(QSize(0, 20))

        self.gridLayout_6.addWidget(self.label_45, 2, 0, 1, 1)

        self.cmb_obj_round2 = QComboBox(self.groupBox_3)
        self.cmb_obj_round2.addItem("")
        self.cmb_obj_round2.addItem("")
        self.cmb_obj_round2.setObjectName(u"cmb_obj_round2")
        sizePolicy1.setHeightForWidth(self.cmb_obj_round2.sizePolicy().hasHeightForWidth())
        self.cmb_obj_round2.setSizePolicy(sizePolicy1)
        self.cmb_obj_round2.setMinimumSize(QSize(55, 20))

        self.gridLayout_6.addWidget(self.cmb_obj_round2, 2, 1, 1, 1)


        self.verticalLayout_3.addLayout(self.gridLayout_6)


        self.gridLayout_15.addWidget(self.groupBox_3, 0, 2, 3, 1)

        self.btn_plan_save = QPushButton(self.page_2)
        self.btn_plan_save.setObjectName(u"btn_plan_save")
        sizePolicy1.setHeightForWidth(self.btn_plan_save.sizePolicy().hasHeightForWidth())
        self.btn_plan_save.setSizePolicy(sizePolicy1)
        self.btn_plan_save.setMinimumSize(QSize(100, 25))
        self.btn_plan_save.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_15.addWidget(self.btn_plan_save, 1, 3, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(126, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_15.addItem(self.horizontalSpacer_2, 1, 5, 1, 1)

        self.verticalLayout_15 = QVBoxLayout()
        self.verticalLayout_15.setSpacing(2)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.label_49 = QLabel(self.page_2)
        self.label_49.setObjectName(u"label_49")
        sizePolicy1.setHeightForWidth(self.label_49.sizePolicy().hasHeightForWidth())
        self.label_49.setSizePolicy(sizePolicy1)
        self.label_49.setMinimumSize(QSize(0, 15))
        self.label_49.setAlignment(Qt.AlignCenter)

        self.verticalLayout_15.addWidget(self.label_49)

        self.tre_all = QTreeWidget(self.page_2)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setTextAlignment(0, Qt.AlignCenter);
        self.tre_all.setHeaderItem(__qtreewidgetitem)
        __qtreewidgetitem1 = QTreeWidgetItem(self.tre_all)
        QTreeWidgetItem(__qtreewidgetitem1)
        QTreeWidgetItem(__qtreewidgetitem1)
        QTreeWidgetItem(__qtreewidgetitem1)
        QTreeWidgetItem(__qtreewidgetitem1)
        QTreeWidgetItem(__qtreewidgetitem1)
        QTreeWidgetItem(__qtreewidgetitem1)
        QTreeWidgetItem(__qtreewidgetitem1)
        QTreeWidgetItem(__qtreewidgetitem1)
        QTreeWidgetItem(__qtreewidgetitem1)
        QTreeWidgetItem(__qtreewidgetitem1)
        QTreeWidgetItem(__qtreewidgetitem1)
        QTreeWidgetItem(__qtreewidgetitem1)
        QTreeWidgetItem(__qtreewidgetitem1)
        QTreeWidgetItem(__qtreewidgetitem1)
        QTreeWidgetItem(__qtreewidgetitem1)
        QTreeWidgetItem(__qtreewidgetitem1)
        QTreeWidgetItem(__qtreewidgetitem1)
        QTreeWidgetItem(__qtreewidgetitem1)
        QTreeWidgetItem(__qtreewidgetitem1)
        QTreeWidgetItem(__qtreewidgetitem1)
        QTreeWidgetItem(__qtreewidgetitem1)
        QTreeWidgetItem(__qtreewidgetitem1)
        __qtreewidgetitem2 = QTreeWidgetItem(self.tre_all)
        QTreeWidgetItem(__qtreewidgetitem2)
        QTreeWidgetItem(__qtreewidgetitem2)
        QTreeWidgetItem(__qtreewidgetitem2)
        QTreeWidgetItem(__qtreewidgetitem2)
        QTreeWidgetItem(__qtreewidgetitem2)
        QTreeWidgetItem(__qtreewidgetitem2)
        QTreeWidgetItem(__qtreewidgetitem2)
        QTreeWidgetItem(__qtreewidgetitem2)
        QTreeWidgetItem(__qtreewidgetitem2)
        QTreeWidgetItem(__qtreewidgetitem2)
        QTreeWidgetItem(__qtreewidgetitem2)
        __qtreewidgetitem3 = QTreeWidgetItem(self.tre_all)
        QTreeWidgetItem(__qtreewidgetitem3)
        QTreeWidgetItem(__qtreewidgetitem3)
        __qtreewidgetitem4 = QTreeWidgetItem(self.tre_all)
        QTreeWidgetItem(__qtreewidgetitem4)
        QTreeWidgetItem(__qtreewidgetitem4)
        QTreeWidgetItem(__qtreewidgetitem4)
        self.tre_all.setObjectName(u"tre_all")
        sizePolicy2.setHeightForWidth(self.tre_all.sizePolicy().hasHeightForWidth())
        self.tre_all.setSizePolicy(sizePolicy2)
        self.tre_all.setMinimumSize(QSize(100, 200))
        self.tre_all.setMaximumSize(QSize(100, 16777215))
        self.tre_all.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tre_all.setAutoExpandDelay(0)
        self.tre_all.setIndentation(7)
        self.tre_all.setAnimated(True)
        self.tre_all.header().setVisible(False)

        self.verticalLayout_15.addWidget(self.tre_all)


        self.gridLayout_15.addLayout(self.verticalLayout_15, 0, 0, 3, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_15.addItem(self.verticalSpacer_2, 0, 3, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_15.addItem(self.verticalSpacer_3, 2, 3, 1, 1)

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
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.chk_auto_buy_drug = QGroupBox(self.tab_4)
        self.chk_auto_buy_drug.setObjectName(u"chk_auto_buy_drug")
        self.chk_auto_buy_drug.setGeometry(QRect(140, 9, 311, 141))
        self.chk_auto_buy_drug.setCheckable(True)
        self.gridLayout_3 = QGridLayout(self.chk_auto_buy_drug)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_7 = QLabel(self.chk_auto_buy_drug)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_3.addWidget(self.label_7, 0, 0, 1, 1)

        self.edt_hp_num = QLineEdit(self.chk_auto_buy_drug)
        self.edt_hp_num.setObjectName(u"edt_hp_num")
        self.edt_hp_num.setMinimumSize(QSize(0, 20))
        self.edt_hp_num.setMaximumSize(QSize(50, 16777215))
        self.edt_hp_num.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.edt_hp_num, 0, 1, 1, 1)

        self.label_990 = QLabel(self.chk_auto_buy_drug)
        self.label_990.setObjectName(u"label_990")

        self.gridLayout_3.addWidget(self.label_990, 0, 2, 1, 1)

        self.cmb_doufu = QComboBox(self.chk_auto_buy_drug)
        self.cmb_doufu.addItem("")
        self.cmb_doufu.addItem("")
        self.cmb_doufu.setObjectName(u"cmb_doufu")
        self.cmb_doufu.setMinimumSize(QSize(76, 20))
        self.cmb_doufu.setMaximumSize(QSize(16777215, 20))

        self.gridLayout_3.addWidget(self.cmb_doufu, 0, 3, 1, 1)

        self.label_11 = QLabel(self.chk_auto_buy_drug)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout_3.addWidget(self.label_11, 0, 4, 1, 1)

        self.label_8 = QLabel(self.chk_auto_buy_drug)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_3.addWidget(self.label_8, 1, 0, 1, 1)

        self.edt_mp_num = QLineEdit(self.chk_auto_buy_drug)
        self.edt_mp_num.setObjectName(u"edt_mp_num")
        self.edt_mp_num.setMinimumSize(QSize(0, 20))
        self.edt_mp_num.setMaximumSize(QSize(50, 16777215))
        self.edt_mp_num.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.edt_mp_num, 1, 1, 1, 1)

        self.label_991 = QLabel(self.chk_auto_buy_drug)
        self.label_991.setObjectName(u"label_991")

        self.gridLayout_3.addWidget(self.label_991, 1, 2, 1, 1)

        self.cmb_wujiapi = QComboBox(self.chk_auto_buy_drug)
        self.cmb_wujiapi.addItem("")
        self.cmb_wujiapi.addItem("")
        self.cmb_wujiapi.setObjectName(u"cmb_wujiapi")
        self.cmb_wujiapi.setMinimumSize(QSize(76, 20))
        self.cmb_wujiapi.setMaximumSize(QSize(16777215, 20))

        self.gridLayout_3.addWidget(self.cmb_wujiapi, 1, 3, 1, 1)

        self.label_12 = QLabel(self.chk_auto_buy_drug)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout_3.addWidget(self.label_12, 1, 4, 1, 1)

        self.label_9 = QLabel(self.chk_auto_buy_drug)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_3.addWidget(self.label_9, 2, 0, 1, 1)

        self.edt_sp_num = QLineEdit(self.chk_auto_buy_drug)
        self.edt_sp_num.setObjectName(u"edt_sp_num")
        self.edt_sp_num.setMinimumSize(QSize(0, 20))
        self.edt_sp_num.setMaximumSize(QSize(50, 16777215))
        self.edt_sp_num.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.edt_sp_num, 2, 1, 1, 1)

        self.label_992 = QLabel(self.chk_auto_buy_drug)
        self.label_992.setObjectName(u"label_992")

        self.gridLayout_3.addWidget(self.label_992, 2, 2, 1, 1)

        self.cmb_shengdan = QComboBox(self.chk_auto_buy_drug)
        self.cmb_shengdan.addItem("")
        self.cmb_shengdan.addItem("")
        self.cmb_shengdan.setObjectName(u"cmb_shengdan")
        self.cmb_shengdan.setMinimumSize(QSize(76, 20))
        self.cmb_shengdan.setMaximumSize(QSize(16777215, 20))

        self.gridLayout_3.addWidget(self.cmb_shengdan, 2, 3, 1, 1)

        self.label_13 = QLabel(self.chk_auto_buy_drug)
        self.label_13.setObjectName(u"label_13")

        self.gridLayout_3.addWidget(self.label_13, 2, 4, 1, 1)

        self.label_10 = QLabel(self.chk_auto_buy_drug)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout_3.addWidget(self.label_10, 3, 0, 1, 1)

        self.edt_gcl_num = QLineEdit(self.chk_auto_buy_drug)
        self.edt_gcl_num.setObjectName(u"edt_gcl_num")
        self.edt_gcl_num.setMinimumSize(QSize(0, 20))
        self.edt_gcl_num.setMaximumSize(QSize(50, 16777215))
        self.edt_gcl_num.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.edt_gcl_num, 3, 1, 1, 1)

        self.label_994 = QLabel(self.chk_auto_buy_drug)
        self.label_994.setObjectName(u"label_994")

        self.gridLayout_3.addWidget(self.label_994, 3, 2, 1, 1)

        self.cmb_gaochong = QComboBox(self.chk_auto_buy_drug)
        self.cmb_gaochong.addItem("")
        self.cmb_gaochong.addItem("")
        self.cmb_gaochong.setObjectName(u"cmb_gaochong")
        self.cmb_gaochong.setEnabled(False)
        self.cmb_gaochong.setMinimumSize(QSize(76, 20))
        self.cmb_gaochong.setMaximumSize(QSize(16777215, 20))

        self.gridLayout_3.addWidget(self.cmb_gaochong, 3, 3, 1, 1)

        self.label_14 = QLabel(self.chk_auto_buy_drug)
        self.label_14.setObjectName(u"label_14")

        self.gridLayout_3.addWidget(self.label_14, 3, 4, 1, 1)

        self.groupBox_4 = QGroupBox(self.tab_4)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setGeometry(QRect(460, 10, 181, 281))
        self.formLayout_4 = QFormLayout(self.groupBox_4)
        self.formLayout_4.setObjectName(u"formLayout_4")
        self.chk_use_qmx = QCheckBox(self.groupBox_4)
        self.chk_use_qmx.setObjectName(u"chk_use_qmx")
        self.chk_use_qmx.setMinimumSize(QSize(130, 20))
        self.chk_use_qmx.setChecked(True)

        self.formLayout_4.setWidget(0, QFormLayout.LabelRole, self.chk_use_qmx)

        self.chk_buy_qmx = QCheckBox(self.groupBox_4)
        self.chk_buy_qmx.setObjectName(u"chk_buy_qmx")
        self.chk_buy_qmx.setMinimumSize(QSize(130, 20))
        self.chk_buy_qmx.setChecked(True)

        self.formLayout_4.setWidget(1, QFormLayout.LabelRole, self.chk_buy_qmx)

        self.chk_supply_qibao = QCheckBox(self.groupBox_4)
        self.chk_supply_qibao.setObjectName(u"chk_supply_qibao")
        self.chk_supply_qibao.setMinimumSize(QSize(130, 20))
        self.chk_supply_qibao.setChecked(True)

        self.formLayout_4.setWidget(3, QFormLayout.LabelRole, self.chk_supply_qibao)

        self.chk_make_jiaju = QCheckBox(self.groupBox_4)
        self.chk_make_jiaju.setObjectName(u"chk_make_jiaju")
        self.chk_make_jiaju.setMinimumSize(QSize(130, 20))
        self.chk_make_jiaju.setChecked(True)

        self.formLayout_4.setWidget(4, QFormLayout.LabelRole, self.chk_make_jiaju)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_15 = QLabel(self.groupBox_4)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setMinimumSize(QSize(75, 20))

        self.horizontalLayout.addWidget(self.label_15)

        self.cmb_buy_style = QComboBox(self.groupBox_4)
        self.cmb_buy_style.addItem("")
        self.cmb_buy_style.addItem("")
        self.cmb_buy_style.setObjectName(u"cmb_buy_style")
        self.cmb_buy_style.setMinimumSize(QSize(50, 20))
        self.cmb_buy_style.setMaximumSize(QSize(16777215, 20))

        self.horizontalLayout.addWidget(self.cmb_buy_style)


        self.formLayout_4.setLayout(7, QFormLayout.LabelRole, self.horizontalLayout)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.label_35 = QLabel(self.groupBox_4)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setMinimumSize(QSize(38, 20))

        self.horizontalLayout_17.addWidget(self.label_35)

        self.cmb_bao_xiang = QComboBox(self.groupBox_4)
        self.cmb_bao_xiang.addItem("")
        self.cmb_bao_xiang.addItem("")
        self.cmb_bao_xiang.addItem("")
        self.cmb_bao_xiang.setObjectName(u"cmb_bao_xiang")
        self.cmb_bao_xiang.setMinimumSize(QSize(50, 20))
        self.cmb_bao_xiang.setMaximumSize(QSize(16777215, 20))

        self.horizontalLayout_17.addWidget(self.cmb_bao_xiang)


        self.formLayout_4.setLayout(8, QFormLayout.LabelRole, self.horizontalLayout_17)

        self.chk_use_htd = QCheckBox(self.groupBox_4)
        self.chk_use_htd.setObjectName(u"chk_use_htd")

        self.formLayout_4.setWidget(5, QFormLayout.LabelRole, self.chk_use_htd)

        self.chk_buy_csf = QCheckBox(self.groupBox_4)
        self.chk_buy_csf.setObjectName(u"chk_buy_csf")
        self.chk_buy_csf.setMinimumSize(QSize(130, 20))
        self.chk_buy_csf.setChecked(True)

        self.formLayout_4.setWidget(2, QFormLayout.LabelRole, self.chk_buy_csf)

        self.chk_queue_back = QCheckBox(self.groupBox_4)
        self.chk_queue_back.setObjectName(u"chk_queue_back")

        self.formLayout_4.setWidget(6, QFormLayout.LabelRole, self.chk_queue_back)

        self.groupBox_2 = QGroupBox(self.tab_4)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(9, 9, 121, 104))
        self.groupBox_2.setFlat(False)
        self.groupBox_2.setCheckable(False)
        self.verticalLayout_13 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.chk_add_hp = QCheckBox(self.groupBox_2)
        self.chk_add_hp.setObjectName(u"chk_add_hp")
        self.chk_add_hp.setEnabled(True)
        self.chk_add_hp.setMinimumSize(QSize(0, 20))
        self.chk_add_hp.setMaximumSize(QSize(16777215, 16777215))
        self.chk_add_hp.setChecked(True)

        self.verticalLayout_13.addWidget(self.chk_add_hp)

        self.chk_add_mp = QCheckBox(self.groupBox_2)
        self.chk_add_mp.setObjectName(u"chk_add_mp")
        self.chk_add_mp.setEnabled(True)
        self.chk_add_mp.setMinimumSize(QSize(0, 20))
        self.chk_add_mp.setMaximumSize(QSize(16777215, 16777215))
        self.chk_add_mp.setChecked(True)

        self.verticalLayout_13.addWidget(self.chk_add_mp)

        self.chk_add_loyal = QCheckBox(self.groupBox_2)
        self.chk_add_loyal.setObjectName(u"chk_add_loyal")
        self.chk_add_loyal.setEnabled(True)
        self.chk_add_loyal.setMinimumSize(QSize(0, 20))
        self.chk_add_loyal.setMaximumSize(QSize(16777215, 16777215))
        self.chk_add_loyal.setChecked(True)

        self.verticalLayout_13.addWidget(self.chk_add_loyal)

        self.groupBox_15 = QGroupBox(self.tab_4)
        self.groupBox_15.setObjectName(u"groupBox_15")
        self.groupBox_15.setGeometry(QRect(10, 152, 131, 91))
        self.gridLayout_12 = QGridLayout(self.groupBox_15)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.chk_ban_screen_protect = QCheckBox(self.groupBox_15)
        self.chk_ban_screen_protect.setObjectName(u"chk_ban_screen_protect")

        self.gridLayout_12.addWidget(self.chk_ban_screen_protect, 2, 0, 1, 1)

        self.chk_ban_sys_sleep = QCheckBox(self.groupBox_15)
        self.chk_ban_sys_sleep.setObjectName(u"chk_ban_sys_sleep")

        self.gridLayout_12.addWidget(self.chk_ban_sys_sleep, 0, 0, 1, 1)

        self.groupBox_18 = QGroupBox(self.tab_4)
        self.groupBox_18.setObjectName(u"groupBox_18")
        self.groupBox_18.setGeometry(QRect(10, 251, 181, 118))
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

        self.chk_on_time = QGroupBox(self.tab_4)
        self.chk_on_time.setObjectName(u"chk_on_time")
        self.chk_on_time.setGeometry(QRect(158, 153, 191, 91))
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

        self.tab_set.addTab(self.tab_4, "")
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        self.groupBox_13 = QGroupBox(self.tab_5)
        self.groupBox_13.setObjectName(u"groupBox_13")
        self.groupBox_13.setGeometry(QRect(440, 154, 171, 211))
        self.formLayout_5 = QFormLayout(self.groupBox_13)
        self.formLayout_5.setObjectName(u"formLayout_5")
        self.label_31 = QLabel(self.groupBox_13)
        self.label_31.setObjectName(u"label_31")

        self.formLayout_5.setWidget(0, QFormLayout.LabelRole, self.label_31)

        self.label_32 = QLabel(self.groupBox_13)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setMinimumSize(QSize(0, 20))
        self.label_32.setMaximumSize(QSize(16777215, 20))

        self.formLayout_5.setWidget(0, QFormLayout.FieldRole, self.label_32)

        self.label_29 = QLabel(self.groupBox_13)
        self.label_29.setObjectName(u"label_29")

        self.formLayout_5.setWidget(1, QFormLayout.LabelRole, self.label_29)

        self.label_30 = QLabel(self.groupBox_13)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setMinimumSize(QSize(0, 20))
        self.label_30.setMaximumSize(QSize(16777215, 20))

        self.formLayout_5.setWidget(1, QFormLayout.FieldRole, self.label_30)

        self.label_2 = QLabel(self.groupBox_13)
        self.label_2.setObjectName(u"label_2")

        self.formLayout_5.setWidget(2, QFormLayout.LabelRole, self.label_2)

        self.label_26 = QLabel(self.groupBox_13)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setMinimumSize(QSize(0, 20))
        self.label_26.setMaximumSize(QSize(16777215, 20))

        self.formLayout_5.setWidget(2, QFormLayout.FieldRole, self.label_26)

        self.label_3 = QLabel(self.groupBox_13)
        self.label_3.setObjectName(u"label_3")

        self.formLayout_5.setWidget(3, QFormLayout.LabelRole, self.label_3)

        self.cmb_qingbao_cbt = QComboBox(self.groupBox_13)
        self.cmb_qingbao_cbt.addItem("")
        self.cmb_qingbao_cbt.addItem("")
        self.cmb_qingbao_cbt.setObjectName(u"cmb_qingbao_cbt")
        self.cmb_qingbao_cbt.setMinimumSize(QSize(75, 20))
        self.cmb_qingbao_cbt.setMaximumSize(QSize(16777215, 20))

        self.formLayout_5.setWidget(3, QFormLayout.FieldRole, self.cmb_qingbao_cbt)

        self.label_28 = QLabel(self.groupBox_13)
        self.label_28.setObjectName(u"label_28")

        self.formLayout_5.setWidget(4, QFormLayout.LabelRole, self.label_28)

        self.cmb_qingbao_xj = QComboBox(self.groupBox_13)
        self.cmb_qingbao_xj.addItem("")
        self.cmb_qingbao_xj.addItem("")
        self.cmb_qingbao_xj.setObjectName(u"cmb_qingbao_xj")
        self.cmb_qingbao_xj.setMinimumSize(QSize(75, 20))
        self.cmb_qingbao_xj.setMaximumSize(QSize(16777215, 20))

        self.formLayout_5.setWidget(4, QFormLayout.FieldRole, self.cmb_qingbao_xj)

        self.label_27 = QLabel(self.groupBox_13)
        self.label_27.setObjectName(u"label_27")

        self.formLayout_5.setWidget(5, QFormLayout.LabelRole, self.label_27)

        self.cmb_qingbao_swb = QComboBox(self.groupBox_13)
        self.cmb_qingbao_swb.addItem("")
        self.cmb_qingbao_swb.addItem("")
        self.cmb_qingbao_swb.setObjectName(u"cmb_qingbao_swb")
        self.cmb_qingbao_swb.setMinimumSize(QSize(75, 20))
        self.cmb_qingbao_swb.setMaximumSize(QSize(16777215, 20))

        self.formLayout_5.setWidget(5, QFormLayout.FieldRole, self.cmb_qingbao_swb)

        self.label_34 = QLabel(self.groupBox_13)
        self.label_34.setObjectName(u"label_34")

        self.formLayout_5.setWidget(6, QFormLayout.LabelRole, self.label_34)

        self.label_33 = QLabel(self.groupBox_13)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setMinimumSize(QSize(0, 20))
        self.label_33.setMaximumSize(QSize(16777215, 20))

        self.formLayout_5.setWidget(6, QFormLayout.FieldRole, self.label_33)

        self.groupBox_17 = QGroupBox(self.tab_5)
        self.groupBox_17.setObjectName(u"groupBox_17")
        self.groupBox_17.setGeometry(QRect(300, 154, 121, 121))
        self.gridLayout_4 = QGridLayout(self.groupBox_17)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.cmb_js_role = QComboBox(self.groupBox_17)
        self.cmb_js_role.addItem("")
        self.cmb_js_role.addItem("")
        self.cmb_js_role.addItem("")
        self.cmb_js_role.addItem("")
        self.cmb_js_role.addItem("")
        self.cmb_js_role.addItem("")
        self.cmb_js_role.setObjectName(u"cmb_js_role")
        self.cmb_js_role.setMinimumSize(QSize(50, 20))
        self.cmb_js_role.setMaximumSize(QSize(16777215, 20))

        self.gridLayout_4.addWidget(self.cmb_js_role, 2, 1, 1, 1)

        self.label_41 = QLabel(self.groupBox_17)
        self.label_41.setObjectName(u"label_41")

        self.gridLayout_4.addWidget(self.label_41, 3, 0, 1, 1)

        self.cmb_js_difficulty = QComboBox(self.groupBox_17)
        self.cmb_js_difficulty.addItem("")
        self.cmb_js_difficulty.addItem("")
        self.cmb_js_difficulty.addItem("")
        self.cmb_js_difficulty.setObjectName(u"cmb_js_difficulty")
        self.cmb_js_difficulty.setMinimumSize(QSize(50, 20))
        self.cmb_js_difficulty.setMaximumSize(QSize(16777215, 20))

        self.gridLayout_4.addWidget(self.cmb_js_difficulty, 3, 1, 1, 1)

        self.label_40 = QLabel(self.groupBox_17)
        self.label_40.setObjectName(u"label_40")

        self.gridLayout_4.addWidget(self.label_40, 2, 0, 1, 1)

        self.edt_jingshang_num = QLineEdit(self.groupBox_17)
        self.edt_jingshang_num.setObjectName(u"edt_jingshang_num")
        self.edt_jingshang_num.setMinimumSize(QSize(0, 20))
        self.edt_jingshang_num.setMaximumSize(QSize(16777215, 20))
        self.edt_jingshang_num.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.edt_jingshang_num, 0, 1, 1, 1)

        self.label_57 = QLabel(self.groupBox_17)
        self.label_57.setObjectName(u"label_57")
        self.label_57.setMaximumSize(QSize(60, 20))

        self.gridLayout_4.addWidget(self.label_57, 0, 0, 1, 1)

        self.groupBox_14 = QGroupBox(self.tab_5)
        self.groupBox_14.setObjectName(u"groupBox_14")
        self.groupBox_14.setGeometry(QRect(160, 154, 121, 141))
        self.verticalLayout_6 = QVBoxLayout(self.groupBox_14)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_36 = QLabel(self.groupBox_14)
        self.label_36.setObjectName(u"label_36")

        self.horizontalLayout_11.addWidget(self.label_36)

        self.cmb_jzb_level = QComboBox(self.groupBox_14)
        self.cmb_jzb_level.addItem("")
        self.cmb_jzb_level.addItem("")
        self.cmb_jzb_level.addItem("")
        self.cmb_jzb_level.addItem("")
        self.cmb_jzb_level.setObjectName(u"cmb_jzb_level")
        self.cmb_jzb_level.setMinimumSize(QSize(50, 20))
        self.cmb_jzb_level.setMaximumSize(QSize(16777215, 20))

        self.horizontalLayout_11.addWidget(self.cmb_jzb_level)


        self.verticalLayout_6.addLayout(self.horizontalLayout_11)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_38 = QLabel(self.groupBox_14)
        self.label_38.setObjectName(u"label_38")

        self.horizontalLayout_13.addWidget(self.label_38)

        self.cmb_jzb_num = QComboBox(self.groupBox_14)
        self.cmb_jzb_num.addItem("")
        self.cmb_jzb_num.addItem("")
        self.cmb_jzb_num.addItem("")
        self.cmb_jzb_num.addItem("")
        self.cmb_jzb_num.addItem("")
        self.cmb_jzb_num.addItem("")
        self.cmb_jzb_num.addItem("")
        self.cmb_jzb_num.addItem("")
        self.cmb_jzb_num.addItem("")
        self.cmb_jzb_num.setObjectName(u"cmb_jzb_num")
        self.cmb_jzb_num.setMinimumSize(QSize(50, 20))
        self.cmb_jzb_num.setMaximumSize(QSize(16777215, 20))

        self.horizontalLayout_13.addWidget(self.cmb_jzb_num)


        self.verticalLayout_6.addLayout(self.horizontalLayout_13)

        self.label_56 = QLabel(self.groupBox_14)
        self.label_56.setObjectName(u"label_56")

        self.verticalLayout_6.addWidget(self.label_56)

        self.chk_jzb_gz = QCheckBox(self.groupBox_14)
        self.chk_jzb_gz.setObjectName(u"chk_jzb_gz")
        self.chk_jzb_gz.setMinimumSize(QSize(0, 20))
        self.chk_jzb_gz.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout_6.addWidget(self.chk_jzb_gz)

        self.groupBox_16 = QGroupBox(self.tab_5)
        self.groupBox_16.setObjectName(u"groupBox_16")
        self.groupBox_16.setGeometry(QRect(10, 154, 131, 111))
        self.verticalLayout_9 = QVBoxLayout(self.groupBox_16)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.label_39 = QLabel(self.groupBox_16)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setMaximumSize(QSize(60, 20))

        self.horizontalLayout_14.addWidget(self.label_39)

        self.edt_xiulian_num = QLineEdit(self.groupBox_16)
        self.edt_xiulian_num.setObjectName(u"edt_xiulian_num")
        self.edt_xiulian_num.setMinimumSize(QSize(0, 20))
        self.edt_xiulian_num.setMaximumSize(QSize(16777215, 20))
        self.edt_xiulian_num.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_14.addWidget(self.edt_xiulian_num)


        self.verticalLayout_9.addLayout(self.horizontalLayout_14)

        self.chk_xiulian_fdr = QCheckBox(self.groupBox_16)
        self.chk_xiulian_fdr.setObjectName(u"chk_xiulian_fdr")
        self.chk_xiulian_fdr.setMinimumSize(QSize(0, 20))
        self.chk_xiulian_fdr.setMaximumSize(QSize(16777215, 20))
        self.chk_xiulian_fdr.setChecked(True)

        self.verticalLayout_9.addWidget(self.chk_xiulian_fdr)

        self.chk_bang_gong = QCheckBox(self.groupBox_16)
        self.chk_bang_gong.setObjectName(u"chk_bang_gong")
        self.chk_bang_gong.setMinimumSize(QSize(0, 20))
        self.chk_bang_gong.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout_9.addWidget(self.chk_bang_gong)

        self.layoutWidget = QWidget(self.tab_5)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 10, 661, 61))
        self.horizontalLayout_3 = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.groupBox_10 = QGroupBox(self.layoutWidget)
        self.groupBox_10.setObjectName(u"groupBox_10")
        self.horizontalLayout_7 = QHBoxLayout(self.groupBox_10)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(6, 6, 6, 6)
        self.label_20 = QLabel(self.groupBox_10)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setMaximumSize(QSize(60, 20))

        self.horizontalLayout_7.addWidget(self.label_20)

        self.edt_shimen_num = QLineEdit(self.groupBox_10)
        self.edt_shimen_num.setObjectName(u"edt_shimen_num")
        self.edt_shimen_num.setMinimumSize(QSize(0, 20))
        self.edt_shimen_num.setMaximumSize(QSize(16777215, 20))
        self.edt_shimen_num.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_7.addWidget(self.edt_shimen_num)


        self.horizontalLayout_3.addWidget(self.groupBox_10)

        self.groupBox_9 = QGroupBox(self.layoutWidget)
        self.groupBox_9.setObjectName(u"groupBox_9")
        self.horizontalLayout_5 = QHBoxLayout(self.groupBox_9)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(6, 6, 6, 6)
        self.label_19 = QLabel(self.groupBox_9)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setMaximumSize(QSize(60, 20))

        self.horizontalLayout_5.addWidget(self.label_19)

        self.edt_baotu_num = QLineEdit(self.groupBox_9)
        self.edt_baotu_num.setObjectName(u"edt_baotu_num")
        self.edt_baotu_num.setMinimumSize(QSize(0, 20))
        self.edt_baotu_num.setMaximumSize(QSize(16777215, 20))
        self.edt_baotu_num.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.edt_baotu_num)


        self.horizontalLayout_3.addWidget(self.groupBox_9)

        self.groupBox_8 = QGroupBox(self.layoutWidget)
        self.groupBox_8.setObjectName(u"groupBox_8")
        self.horizontalLayout_4 = QHBoxLayout(self.groupBox_8)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(6, 6, 6, 6)
        self.label_18 = QLabel(self.groupBox_8)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setMaximumSize(QSize(60, 20))

        self.horizontalLayout_4.addWidget(self.label_18)

        self.edt_yunbiao_num = QLineEdit(self.groupBox_8)
        self.edt_yunbiao_num.setObjectName(u"edt_yunbiao_num")
        self.edt_yunbiao_num.setMinimumSize(QSize(0, 20))
        self.edt_yunbiao_num.setMaximumSize(QSize(16777215, 20))
        self.edt_yunbiao_num.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.edt_yunbiao_num)


        self.horizontalLayout_3.addWidget(self.groupBox_8)

        self.groupBox_19 = QGroupBox(self.layoutWidget)
        self.groupBox_19.setObjectName(u"groupBox_19")
        self.horizontalLayout_8 = QHBoxLayout(self.groupBox_19)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(6, 6, 6, 6)
        self.label_37 = QLabel(self.groupBox_19)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setMaximumSize(QSize(60, 20))

        self.horizontalLayout_8.addWidget(self.label_37)

        self.edt_renwulian_num = QLineEdit(self.groupBox_19)
        self.edt_renwulian_num.setObjectName(u"edt_renwulian_num")
        self.edt_renwulian_num.setMinimumSize(QSize(0, 20))
        self.edt_renwulian_num.setMaximumSize(QSize(16777215, 20))
        self.edt_renwulian_num.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_8.addWidget(self.edt_renwulian_num)


        self.horizontalLayout_3.addWidget(self.groupBox_19)

        self.groupBox_20 = QGroupBox(self.layoutWidget)
        self.groupBox_20.setObjectName(u"groupBox_20")
        self.horizontalLayout_6 = QHBoxLayout(self.groupBox_20)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(6, 6, 6, 6)
        self.label_60 = QLabel(self.groupBox_20)
        self.label_60.setObjectName(u"label_60")
        self.label_60.setMaximumSize(QSize(60, 20))

        self.horizontalLayout_6.addWidget(self.label_60)

        self.edt_xuanwu_num = QLineEdit(self.groupBox_20)
        self.edt_xuanwu_num.setObjectName(u"edt_xuanwu_num")
        self.edt_xuanwu_num.setMinimumSize(QSize(0, 20))
        self.edt_xuanwu_num.setMaximumSize(QSize(16777215, 20))
        self.edt_xuanwu_num.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_6.addWidget(self.edt_xuanwu_num)


        self.horizontalLayout_3.addWidget(self.groupBox_20)

        self.groupBox_22 = QGroupBox(self.layoutWidget)
        self.groupBox_22.setObjectName(u"groupBox_22")
        self.horizontalLayout_10 = QHBoxLayout(self.groupBox_22)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(6, 6, 6, 6)
        self.label_59 = QLabel(self.groupBox_22)
        self.label_59.setObjectName(u"label_59")
        self.label_59.setMaximumSize(QSize(60, 20))

        self.horizontalLayout_10.addWidget(self.label_59)

        self.edt_qinglong_num = QLineEdit(self.groupBox_22)
        self.edt_qinglong_num.setObjectName(u"edt_qinglong_num")
        self.edt_qinglong_num.setMinimumSize(QSize(0, 20))
        self.edt_qinglong_num.setMaximumSize(QSize(16777215, 20))
        self.edt_qinglong_num.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_10.addWidget(self.edt_qinglong_num)


        self.horizontalLayout_3.addWidget(self.groupBox_22)

        self.layoutWidget1 = QWidget(self.tab_5)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(10, 80, 661, 61))
        self.horizontalLayout_23 = QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.groupBox_24 = QGroupBox(self.layoutWidget1)
        self.groupBox_24.setObjectName(u"groupBox_24")
        self.horizontalLayout_12 = QHBoxLayout(self.groupBox_24)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(6, 6, 6, 6)
        self.label_63 = QLabel(self.groupBox_24)
        self.label_63.setObjectName(u"label_63")
        self.label_63.setMaximumSize(QSize(60, 20))

        self.horizontalLayout_12.addWidget(self.label_63)

        self.edt_guanzhi_num = QLineEdit(self.groupBox_24)
        self.edt_guanzhi_num.setObjectName(u"edt_guanzhi_num")
        self.edt_guanzhi_num.setMinimumSize(QSize(0, 20))
        self.edt_guanzhi_num.setMaximumSize(QSize(16777215, 20))
        self.edt_guanzhi_num.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_12.addWidget(self.edt_guanzhi_num)


        self.horizontalLayout_23.addWidget(self.groupBox_24)

        self.groupBox_25 = QGroupBox(self.layoutWidget1)
        self.groupBox_25.setObjectName(u"groupBox_25")
        self.horizontalLayout_18 = QHBoxLayout(self.groupBox_25)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(6, 6, 6, 6)
        self.label_64 = QLabel(self.groupBox_25)
        self.label_64.setObjectName(u"label_64")
        self.label_64.setMaximumSize(QSize(60, 20))

        self.horizontalLayout_18.addWidget(self.label_64)

        self.edt_pengren_num = QLineEdit(self.groupBox_25)
        self.edt_pengren_num.setObjectName(u"edt_pengren_num")
        self.edt_pengren_num.setMinimumSize(QSize(0, 20))
        self.edt_pengren_num.setMaximumSize(QSize(16777215, 20))
        self.edt_pengren_num.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_18.addWidget(self.edt_pengren_num)


        self.horizontalLayout_23.addWidget(self.groupBox_25)

        self.groupBox_26 = QGroupBox(self.layoutWidget1)
        self.groupBox_26.setObjectName(u"groupBox_26")
        self.horizontalLayout_19 = QHBoxLayout(self.groupBox_26)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(6, 6, 6, 6)
        self.chk_hld_addition = QCheckBox(self.groupBox_26)
        self.chk_hld_addition.setObjectName(u"chk_hld_addition")

        self.horizontalLayout_19.addWidget(self.chk_hld_addition)

        self.chk_hld_longhun = QCheckBox(self.groupBox_26)
        self.chk_hld_longhun.setObjectName(u"chk_hld_longhun")

        self.horizontalLayout_19.addWidget(self.chk_hld_longhun)


        self.horizontalLayout_23.addWidget(self.groupBox_26)

        self.groupBox_28 = QGroupBox(self.layoutWidget1)
        self.groupBox_28.setObjectName(u"groupBox_28")
        self.horizontalLayout_21 = QHBoxLayout(self.groupBox_28)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.label_66 = QLabel(self.groupBox_28)
        self.label_66.setObjectName(u"label_66")

        self.horizontalLayout_21.addWidget(self.label_66)

        self.cmb_xnbx_map = QComboBox(self.groupBox_28)
        self.cmb_xnbx_map.addItem("")
        self.cmb_xnbx_map.addItem("")
        self.cmb_xnbx_map.addItem("")
        self.cmb_xnbx_map.addItem("")
        self.cmb_xnbx_map.addItem("")
        self.cmb_xnbx_map.addItem("")
        self.cmb_xnbx_map.addItem("")
        self.cmb_xnbx_map.addItem("")
        self.cmb_xnbx_map.addItem("")
        self.cmb_xnbx_map.addItem("")
        self.cmb_xnbx_map.addItem("")
        self.cmb_xnbx_map.addItem("")
        self.cmb_xnbx_map.addItem("")
        self.cmb_xnbx_map.addItem("")
        self.cmb_xnbx_map.addItem("")
        self.cmb_xnbx_map.addItem("")
        self.cmb_xnbx_map.addItem("")
        self.cmb_xnbx_map.setObjectName(u"cmb_xnbx_map")
        self.cmb_xnbx_map.setMinimumSize(QSize(90, 20))
        self.cmb_xnbx_map.setMaximumSize(QSize(16777215, 20))

        self.horizontalLayout_21.addWidget(self.cmb_xnbx_map)


        self.horizontalLayout_23.addWidget(self.groupBox_28)

        self.groupBox_29 = QGroupBox(self.layoutWidget1)
        self.groupBox_29.setObjectName(u"groupBox_29")
        self.horizontalLayout_22 = QHBoxLayout(self.groupBox_29)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.label_67 = QLabel(self.groupBox_29)
        self.label_67.setObjectName(u"label_67")

        self.horizontalLayout_22.addWidget(self.label_67)

        self.cmb_tjbx_map = QComboBox(self.groupBox_29)
        self.cmb_tjbx_map.addItem("")
        self.cmb_tjbx_map.addItem("")
        self.cmb_tjbx_map.addItem("")
        self.cmb_tjbx_map.addItem("")
        self.cmb_tjbx_map.addItem("")
        self.cmb_tjbx_map.setObjectName(u"cmb_tjbx_map")
        self.cmb_tjbx_map.setMinimumSize(QSize(90, 20))
        self.cmb_tjbx_map.setMaximumSize(QSize(16777215, 20))

        self.horizontalLayout_22.addWidget(self.cmb_tjbx_map)


        self.horizontalLayout_23.addWidget(self.groupBox_29)

        self.tab_set.addTab(self.tab_5, "")
        self.tab_6 = QWidget()
        self.tab_6.setObjectName(u"tab_6")
        self.groupBox_12 = QGroupBox(self.tab_6)
        self.groupBox_12.setObjectName(u"groupBox_12")
        self.groupBox_12.setGeometry(QRect(162, 110, 141, 161))
        self.gridLayout_7 = QGridLayout(self.groupBox_12)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.label_24 = QLabel(self.groupBox_12)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_7.addWidget(self.label_24, 1, 0, 1, 1)

        self.label_23 = QLabel(self.groupBox_12)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_7.addWidget(self.label_23, 0, 0, 1, 1)

        self.cmb_diaoyu_num = QComboBox(self.groupBox_12)
        self.cmb_diaoyu_num.addItem("")
        self.cmb_diaoyu_num.addItem("")
        self.cmb_diaoyu_num.addItem("")
        self.cmb_diaoyu_num.addItem("")
        self.cmb_diaoyu_num.addItem("")
        self.cmb_diaoyu_num.setObjectName(u"cmb_diaoyu_num")
        self.cmb_diaoyu_num.setMinimumSize(QSize(0, 20))
        self.cmb_diaoyu_num.setMaximumSize(QSize(16777215, 20))

        self.gridLayout_7.addWidget(self.cmb_diaoyu_num, 1, 1, 1, 1)

        self.label_25 = QLabel(self.groupBox_12)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_7.addWidget(self.label_25, 3, 0, 1, 1)

        self.cmb_diaoyu_deal = QComboBox(self.groupBox_12)
        self.cmb_diaoyu_deal.addItem("")
        self.cmb_diaoyu_deal.addItem("")
        self.cmb_diaoyu_deal.setObjectName(u"cmb_diaoyu_deal")
        self.cmb_diaoyu_deal.setMinimumSize(QSize(0, 20))
        self.cmb_diaoyu_deal.setMaximumSize(QSize(16777215, 20))

        self.gridLayout_7.addWidget(self.cmb_diaoyu_deal, 5, 1, 1, 1)

        self.cmb_diaoyu_map = QComboBox(self.groupBox_12)
        self.cmb_diaoyu_map.addItem("")
        self.cmb_diaoyu_map.addItem("")
        self.cmb_diaoyu_map.addItem("")
        self.cmb_diaoyu_map.addItem("")
        self.cmb_diaoyu_map.addItem("")
        self.cmb_diaoyu_map.setObjectName(u"cmb_diaoyu_map")
        self.cmb_diaoyu_map.setMinimumSize(QSize(80, 20))
        self.cmb_diaoyu_map.setMaximumSize(QSize(16777215, 20))

        self.gridLayout_7.addWidget(self.cmb_diaoyu_map, 0, 1, 1, 1)

        self.cmb_diaoyu_paogan = QComboBox(self.groupBox_12)
        self.cmb_diaoyu_paogan.addItem("")
        self.cmb_diaoyu_paogan.addItem("")
        self.cmb_diaoyu_paogan.setObjectName(u"cmb_diaoyu_paogan")
        self.cmb_diaoyu_paogan.setMinimumSize(QSize(0, 20))
        self.cmb_diaoyu_paogan.setMaximumSize(QSize(16777215, 20))

        self.gridLayout_7.addWidget(self.cmb_diaoyu_paogan, 3, 1, 1, 1)

        self.label_47 = QLabel(self.groupBox_12)
        self.label_47.setObjectName(u"label_47")
        self.label_47.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_7.addWidget(self.label_47, 5, 0, 1, 1)

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
        self.groupBox_6.setGeometry(QRect(315, 110, 101, 61))
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

        self.groupBox_21 = QGroupBox(self.tab_6)
        self.groupBox_21.setObjectName(u"groupBox_21")
        self.groupBox_21.setGeometry(QRect(426, 110, 101, 61))
        self.horizontalLayout_9 = QHBoxLayout(self.groupBox_21)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(6, 6, 6, 6)
        self.label_58 = QLabel(self.groupBox_21)
        self.label_58.setObjectName(u"label_58")
        self.label_58.setMaximumSize(QSize(60, 20))

        self.horizontalLayout_9.addWidget(self.label_58)

        self.edt_bianjing_num = QLineEdit(self.groupBox_21)
        self.edt_bianjing_num.setObjectName(u"edt_bianjing_num")
        self.edt_bianjing_num.setMinimumSize(QSize(0, 20))
        self.edt_bianjing_num.setMaximumSize(QSize(16777215, 20))
        self.edt_bianjing_num.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_9.addWidget(self.edt_bianjing_num)

        self.layoutWidget2 = QWidget(self.tab_6)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(9, 10, 671, 86))
        self.horizontalLayout_16 = QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_16.setSpacing(10)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.groupBox = QGroupBox(self.layoutWidget2)
        self.groupBox.setObjectName(u"groupBox")
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


        self.horizontalLayout_16.addWidget(self.groupBox)

        self.groupBox_5 = QGroupBox(self.layoutWidget2)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.verticalLayout_12 = QVBoxLayout(self.groupBox_5)
        self.verticalLayout_12.setSpacing(5)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_16 = QLabel(self.groupBox_5)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setMaximumSize(QSize(60, 20))

        self.horizontalLayout_2.addWidget(self.label_16)

        self.edt_zhuogui_num = QLineEdit(self.groupBox_5)
        self.edt_zhuogui_num.setObjectName(u"edt_zhuogui_num")
        self.edt_zhuogui_num.setMinimumSize(QSize(0, 20))
        self.edt_zhuogui_num.setMaximumSize(QSize(16777215, 20))
        self.edt_zhuogui_num.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.edt_zhuogui_num)


        self.verticalLayout_12.addLayout(self.horizontalLayout_2)

        self.chk_zhuogui_qn = QCheckBox(self.groupBox_5)
        self.chk_zhuogui_qn.setObjectName(u"chk_zhuogui_qn")
        self.chk_zhuogui_qn.setMinimumSize(QSize(0, 20))
        self.chk_zhuogui_qn.setMaximumSize(QSize(16777215, 20))
        self.chk_zhuogui_qn.setChecked(True)

        self.verticalLayout_12.addWidget(self.chk_zhuogui_qn)


        self.horizontalLayout_16.addWidget(self.groupBox_5)

        self.groupBox_23 = QGroupBox(self.layoutWidget2)
        self.groupBox_23.setObjectName(u"groupBox_23")
        self.gridLayout_19 = QGridLayout(self.groupBox_23)
        self.gridLayout_19.setObjectName(u"gridLayout_19")
        self.label_61 = QLabel(self.groupBox_23)
        self.label_61.setObjectName(u"label_61")

        self.gridLayout_19.addWidget(self.label_61, 0, 0, 1, 1)

        self.cmb_fengyao_map = QComboBox(self.groupBox_23)
        self.cmb_fengyao_map.addItem("")
        self.cmb_fengyao_map.addItem("")
        self.cmb_fengyao_map.addItem("")
        self.cmb_fengyao_map.addItem("")
        self.cmb_fengyao_map.addItem("")
        self.cmb_fengyao_map.addItem("")
        self.cmb_fengyao_map.addItem("")
        self.cmb_fengyao_map.addItem("")
        self.cmb_fengyao_map.addItem("")
        self.cmb_fengyao_map.addItem("")
        self.cmb_fengyao_map.addItem("")
        self.cmb_fengyao_map.addItem("")
        self.cmb_fengyao_map.addItem("")
        self.cmb_fengyao_map.setObjectName(u"cmb_fengyao_map")
        self.cmb_fengyao_map.setMinimumSize(QSize(0, 20))
        self.cmb_fengyao_map.setMaximumSize(QSize(16777215, 20))

        self.gridLayout_19.addWidget(self.cmb_fengyao_map, 0, 1, 1, 1)

        self.label_62 = QLabel(self.groupBox_23)
        self.label_62.setObjectName(u"label_62")
        self.label_62.setMaximumSize(QSize(60, 20))

        self.gridLayout_19.addWidget(self.label_62, 1, 0, 1, 1)

        self.edt_fengyao_num = QLineEdit(self.groupBox_23)
        self.edt_fengyao_num.setObjectName(u"edt_fengyao_num")
        self.edt_fengyao_num.setMinimumSize(QSize(0, 20))
        self.edt_fengyao_num.setMaximumSize(QSize(16777215, 20))
        self.edt_fengyao_num.setAlignment(Qt.AlignCenter)

        self.gridLayout_19.addWidget(self.edt_fengyao_num, 1, 1, 1, 1)


        self.horizontalLayout_16.addWidget(self.groupBox_23)

        self.groupBox_11 = QGroupBox(self.layoutWidget2)
        self.groupBox_11.setObjectName(u"groupBox_11")
        self.gridLayout_5 = QGridLayout(self.groupBox_11)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setHorizontalSpacing(6)
        self.gridLayout_5.setContentsMargins(4, 4, 4, 4)
        self.label_50 = QLabel(self.groupBox_11)
        self.label_50.setObjectName(u"label_50")
        self.label_50.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_5.addWidget(self.label_50, 0, 0, 1, 1)

        self.cmb_fb1 = QComboBox(self.groupBox_11)
        self.cmb_fb1.addItem("")
        self.cmb_fb1.addItem("")
        self.cmb_fb1.addItem("")
        self.cmb_fb1.addItem("")
        self.cmb_fb1.addItem("")
        self.cmb_fb1.addItem("")
        self.cmb_fb1.addItem("")
        self.cmb_fb1.addItem("")
        self.cmb_fb1.addItem("")
        self.cmb_fb1.setObjectName(u"cmb_fb1")
        self.cmb_fb1.setMinimumSize(QSize(90, 20))
        self.cmb_fb1.setMaximumSize(QSize(90, 20))

        self.gridLayout_5.addWidget(self.cmb_fb1, 0, 1, 1, 1)

        self.cmb_fb1_num = QComboBox(self.groupBox_11)
        self.cmb_fb1_num.addItem("")
        self.cmb_fb1_num.addItem("")
        self.cmb_fb1_num.addItem("")
        self.cmb_fb1_num.addItem("")
        self.cmb_fb1_num.addItem("")
        self.cmb_fb1_num.setObjectName(u"cmb_fb1_num")
        self.cmb_fb1_num.setMinimumSize(QSize(40, 20))
        self.cmb_fb1_num.setMaximumSize(QSize(40, 20))

        self.gridLayout_5.addWidget(self.cmb_fb1_num, 0, 2, 1, 1)

        self.label_51 = QLabel(self.groupBox_11)
        self.label_51.setObjectName(u"label_51")
        self.label_51.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_5.addWidget(self.label_51, 1, 0, 1, 1)

        self.cmb_fb2 = QComboBox(self.groupBox_11)
        self.cmb_fb2.addItem("")
        self.cmb_fb2.addItem("")
        self.cmb_fb2.addItem("")
        self.cmb_fb2.addItem("")
        self.cmb_fb2.addItem("")
        self.cmb_fb2.addItem("")
        self.cmb_fb2.addItem("")
        self.cmb_fb2.addItem("")
        self.cmb_fb2.addItem("")
        self.cmb_fb2.setObjectName(u"cmb_fb2")
        self.cmb_fb2.setMinimumSize(QSize(90, 20))
        self.cmb_fb2.setMaximumSize(QSize(16777215, 20))

        self.gridLayout_5.addWidget(self.cmb_fb2, 1, 1, 1, 1)

        self.cmb_fb2_num = QComboBox(self.groupBox_11)
        self.cmb_fb2_num.addItem("")
        self.cmb_fb2_num.addItem("")
        self.cmb_fb2_num.addItem("")
        self.cmb_fb2_num.addItem("")
        self.cmb_fb2_num.addItem("")
        self.cmb_fb2_num.setObjectName(u"cmb_fb2_num")
        self.cmb_fb2_num.setMinimumSize(QSize(35, 20))
        self.cmb_fb2_num.setMaximumSize(QSize(40, 20))

        self.gridLayout_5.addWidget(self.cmb_fb2_num, 1, 2, 1, 1)


        self.horizontalLayout_16.addWidget(self.groupBox_11)

        self.groupBox_27 = QGroupBox(self.tab_6)
        self.groupBox_27.setObjectName(u"groupBox_27")
        self.groupBox_27.setGeometry(QRect(537, 110, 101, 61))
        self.horizontalLayout_20 = QHBoxLayout(self.groupBox_27)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(6, 6, 6, 6)
        self.label_65 = QLabel(self.groupBox_27)
        self.label_65.setObjectName(u"label_65")
        self.label_65.setMaximumSize(QSize(60, 20))

        self.horizontalLayout_20.addWidget(self.label_65)

        self.edt_mandong_num = QLineEdit(self.groupBox_27)
        self.edt_mandong_num.setObjectName(u"edt_mandong_num")
        self.edt_mandong_num.setMinimumSize(QSize(0, 20))
        self.edt_mandong_num.setMaximumSize(QSize(16777215, 20))
        self.edt_mandong_num.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_20.addWidget(self.edt_mandong_num)

        self.tab_set.addTab(self.tab_6, "")

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

        self.gridLayout_13.addWidget(self.stack_widget, 0, 0, 1, 1)

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
        self.tool_bar.addAction(self.action_gnrl)

        self.retranslateUi(WndMain)

        self.stack_widget.setCurrentIndex(2)
        self.tab_set.setCurrentIndex(1)
        self.cmb_jzb_level.setCurrentIndex(2)
        self.cmb_jzb_num.setCurrentIndex(0)
        self.cmb_xnbx_map.setCurrentIndex(0)
        self.cmb_tjbx_map.setCurrentIndex(0)
        self.cmb_diaoyu_map.setCurrentIndex(2)
        self.cmb_diaoyu_paogan.setCurrentIndex(1)
        self.cmb_double_time.setCurrentIndex(1)
        self.cmb_daye_map.setCurrentIndex(0)
        self.cmb_fengyao_map.setCurrentIndex(0)
        self.cmb_fb1.setCurrentIndex(3)
        self.cmb_fb1_num.setCurrentIndex(4)
        self.cmb_fb2.setCurrentIndex(4)
        self.cmb_fb2_num.setCurrentIndex(4)


        QMetaObject.connectSlotsByName(WndMain)
    # setupUi

    def retranslateUi(self, WndMain):
        WndMain.setWindowTitle(QCoreApplication.translate("WndMain", u"WeWork", None))
        self.action_console.setText(QCoreApplication.translate("WndMain", u"\u63a7 \u5236", None))
#if QT_CONFIG(shortcut)
        self.action_console.setShortcut(QCoreApplication.translate("WndMain", u"Alt+1", None))
#endif // QT_CONFIG(shortcut)
        self.action_plan.setText(QCoreApplication.translate("WndMain", u"\u65b9 \u6848", None))
#if QT_CONFIG(shortcut)
        self.action_plan.setShortcut(QCoreApplication.translate("WndMain", u"Alt+2", None))
#endif // QT_CONFIG(shortcut)
        self.action_gnrl.setText(QCoreApplication.translate("WndMain", u"\u901a \u7528", None))
#if QT_CONFIG(shortcut)
        self.action_gnrl.setShortcut(QCoreApplication.translate("WndMain", u"Alt+3", None))
#endif // QT_CONFIG(shortcut)
        ___qtablewidgetitem = self.tbe_console.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("WndMain", u"\u7a97\u53e3\u53e5\u67c4", None));
#if QT_CONFIG(tooltip)
        ___qtablewidgetitem.setToolTip(QCoreApplication.translate("WndMain", u"\u53cc\u51fb\u8868\u5934\u83b7\u53d6\u5168\u90e8\u6e38\u620f\u7a97\u53e3\u53e5\u67c4, \u53cc\u51fb\u672c\u5217\u4e0b\u7684\u8868\u9879\u53ef\u663e\u793a\u6fc0\u6d3b\u8be5\u7a97\u53e3", None));
#endif // QT_CONFIG(tooltip)
        ___qtablewidgetitem1 = self.tbe_console.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("WndMain", u"\u65b9\u6848\u9009\u62e9", None));
#if QT_CONFIG(tooltip)
        ___qtablewidgetitem1.setToolTip(QCoreApplication.translate("WndMain", u"\u53cc\u51fb\u8868\u5934\u53ef\u5168\u90e8\u8bbe\u7f6e\u65b9\u6848", None));
#endif // QT_CONFIG(tooltip)
        ___qtablewidgetitem2 = self.tbe_console.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("WndMain", u"\u95e8\u6d3e", None));
        ___qtablewidgetitem3 = self.tbe_console.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("WndMain", u"\u8fd0\u884c", None));
#if QT_CONFIG(tooltip)
        ___qtablewidgetitem3.setToolTip(QCoreApplication.translate("WndMain", u"\u53cc\u51fb\u8868\u5934\u53ef\u5168\u90e8\u8fd0\u884c, \u53cc\u51fb\u672c\u5217\u4e0b\u7684\u8868\u9879\u53ef\u8fd0\u884c\u5355\u4e2a\u7a97\u53e3", None));
#endif // QT_CONFIG(tooltip)
        ___qtablewidgetitem4 = self.tbe_console.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("WndMain", u"\u6682\u505c", None));
#if QT_CONFIG(tooltip)
        ___qtablewidgetitem4.setToolTip(QCoreApplication.translate("WndMain", u"\u53cc\u51fb\u8868\u5934\u53ef\u5168\u90e8\u6682\u505c, \u53cc\u51fb\u672c\u5217\u4e0b\u7684\u8868\u9879\u53ef\u6682\u505c\u5355\u4e2a\u7a97\u53e3", None));
#endif // QT_CONFIG(tooltip)
        ___qtablewidgetitem5 = self.tbe_console.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("WndMain", u"\u7ec8\u6b62", None));
#if QT_CONFIG(tooltip)
        ___qtablewidgetitem5.setToolTip(QCoreApplication.translate("WndMain", u"\u53cc\u51fb\u8868\u5934\u53ef\u5168\u90e8\u7ec8\u6b62, \u53cc\u51fb\u672c\u5217\u4e0b\u7684\u8868\u9879\u53ef\u7ec8\u6b62\u5355\u4e2a\u7a97\u53e3", None));
#endif // QT_CONFIG(tooltip)
        ___qtablewidgetitem6 = self.tbe_console.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("WndMain", u"\u65e5\u5fd7", None));
#if QT_CONFIG(tooltip)
        ___qtablewidgetitem6.setToolTip(QCoreApplication.translate("WndMain", u"\u53cc\u51fb\u8868\u5934\u53ef\u663e\u793a\u672c\u8f6f\u4ef6\u65e5\u5fd7, \u53cc\u51fb\u672c\u5217\u4e0b\u7684\u8868\u9879\u53ef\u663e\u793a\u5404\u7a97\u53e3\u6267\u884c\u65e5\u5fd7", None));
#endif // QT_CONFIG(tooltip)
        ___qtablewidgetitem7 = self.tbe_console.verticalHeaderItem(0)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("WndMain", u" 1 ", None));
#if QT_CONFIG(tooltip)
        ___qtablewidgetitem7.setToolTip(QCoreApplication.translate("WndMain", u"\u53cc\u51fb \u5782\u76f4 \u8868\u5934, \u663e\u793a/\u9690\u85cf\u8be5\u7a97\u53e3", None));
#endif // QT_CONFIG(tooltip)
        ___qtablewidgetitem8 = self.tbe_console.verticalHeaderItem(1)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("WndMain", u" 2 ", None));
#if QT_CONFIG(tooltip)
        ___qtablewidgetitem8.setToolTip(QCoreApplication.translate("WndMain", u"\u53cc\u51fb \u5782\u76f4 \u8868\u5934, \u663e\u793a/\u9690\u85cf\u8be5\u7a97\u53e3", None));
#endif // QT_CONFIG(tooltip)
        ___qtablewidgetitem9 = self.tbe_console.verticalHeaderItem(2)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("WndMain", u" 3 ", None));
#if QT_CONFIG(tooltip)
        ___qtablewidgetitem9.setToolTip(QCoreApplication.translate("WndMain", u"\u53cc\u51fb \u5782\u76f4 \u8868\u5934, \u663e\u793a/\u9690\u85cf\u8be5\u7a97\u53e3", None));
#endif // QT_CONFIG(tooltip)
        ___qtablewidgetitem10 = self.tbe_console.verticalHeaderItem(3)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("WndMain", u" 4 ", None));
#if QT_CONFIG(tooltip)
        ___qtablewidgetitem10.setToolTip(QCoreApplication.translate("WndMain", u"\u53cc\u51fb \u5782\u76f4 \u8868\u5934, \u663e\u793a/\u9690\u85cf\u8be5\u7a97\u53e3", None));
#endif // QT_CONFIG(tooltip)
        ___qtablewidgetitem11 = self.tbe_console.verticalHeaderItem(4)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("WndMain", u" 5 ", None));
#if QT_CONFIG(tooltip)
        ___qtablewidgetitem11.setToolTip(QCoreApplication.translate("WndMain", u"\u53cc\u51fb \u5782\u76f4 \u8868\u5934, \u663e\u793a/\u9690\u85cf\u8be5\u7a97\u53e3", None));
#endif // QT_CONFIG(tooltip)
        ___qtablewidgetitem12 = self.tbe_console.verticalHeaderItem(5)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("WndMain", u" 6 ", None));
#if QT_CONFIG(tooltip)
        ___qtablewidgetitem12.setToolTip(QCoreApplication.translate("WndMain", u"\u53cc\u51fb \u5782\u76f4 \u8868\u5934, \u663e\u793a/\u9690\u85cf\u8be5\u7a97\u53e3", None));
#endif // QT_CONFIG(tooltip)
        ___qtablewidgetitem13 = self.tbe_console.verticalHeaderItem(6)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("WndMain", u" 7 ", None));
#if QT_CONFIG(tooltip)
        ___qtablewidgetitem13.setToolTip(QCoreApplication.translate("WndMain", u"\u53cc\u51fb \u5782\u76f4 \u8868\u5934, \u663e\u793a/\u9690\u85cf\u8be5\u7a97\u53e3", None));
#endif // QT_CONFIG(tooltip)
        ___qtablewidgetitem14 = self.tbe_console.verticalHeaderItem(7)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("WndMain", u" 8 ", None));
#if QT_CONFIG(tooltip)
        ___qtablewidgetitem14.setToolTip(QCoreApplication.translate("WndMain", u"\u53cc\u51fb \u5782\u76f4 \u8868\u5934, \u663e\u793a/\u9690\u85cf\u8be5\u7a97\u53e3", None));
#endif // QT_CONFIG(tooltip)
        ___qtablewidgetitem15 = self.tbe_console.verticalHeaderItem(8)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("WndMain", u" 9 ", None));
#if QT_CONFIG(tooltip)
        ___qtablewidgetitem15.setToolTip(QCoreApplication.translate("WndMain", u"\u53cc\u51fb \u5782\u76f4 \u8868\u5934, \u663e\u793a/\u9690\u85cf\u8be5\u7a97\u53e3", None));
#endif // QT_CONFIG(tooltip)
        ___qtablewidgetitem16 = self.tbe_console.verticalHeaderItem(9)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("WndMain", u"10", None));
#if QT_CONFIG(tooltip)
        ___qtablewidgetitem16.setToolTip(QCoreApplication.translate("WndMain", u"\u53cc\u51fb \u5782\u76f4 \u8868\u5934, \u663e\u793a/\u9690\u85cf\u8be5\u7a97\u53e3", None));
#endif // QT_CONFIG(tooltip)
        ___qtablewidgetitem17 = self.tbe_console.verticalHeaderItem(10)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("WndMain", u"11", None));
#if QT_CONFIG(tooltip)
        ___qtablewidgetitem17.setToolTip(QCoreApplication.translate("WndMain", u"\u53cc\u51fb \u5782\u76f4 \u8868\u5934, \u663e\u793a/\u9690\u85cf\u8be5\u7a97\u53e3", None));
#endif // QT_CONFIG(tooltip)
        ___qtablewidgetitem18 = self.tbe_console.verticalHeaderItem(11)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("WndMain", u"12", None));
#if QT_CONFIG(tooltip)
        ___qtablewidgetitem18.setToolTip(QCoreApplication.translate("WndMain", u"\u53cc\u51fb \u5782\u76f4 \u8868\u5934, \u663e\u793a/\u9690\u85cf\u8be5\u7a97\u53e3", None));
#endif // QT_CONFIG(tooltip)
        ___qtablewidgetitem19 = self.tbe_console.verticalHeaderItem(12)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("WndMain", u"13", None));
#if QT_CONFIG(tooltip)
        ___qtablewidgetitem19.setToolTip(QCoreApplication.translate("WndMain", u"\u53cc\u51fb \u5782\u76f4 \u8868\u5934, \u663e\u793a/\u9690\u85cf\u8be5\u7a97\u53e3", None));
#endif // QT_CONFIG(tooltip)
        ___qtablewidgetitem20 = self.tbe_console.verticalHeaderItem(13)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("WndMain", u"14", None));
#if QT_CONFIG(tooltip)
        ___qtablewidgetitem20.setToolTip(QCoreApplication.translate("WndMain", u"\u53cc\u51fb \u5782\u76f4 \u8868\u5934, \u663e\u793a/\u9690\u85cf\u8be5\u7a97\u53e3", None));
#endif // QT_CONFIG(tooltip)
        ___qtablewidgetitem21 = self.tbe_console.verticalHeaderItem(14)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("WndMain", u"15", None));
#if QT_CONFIG(tooltip)
        ___qtablewidgetitem21.setToolTip(QCoreApplication.translate("WndMain", u"\u53cc\u51fb \u5782\u76f4 \u8868\u5934, \u663e\u793a/\u9690\u85cf\u8be5\u7a97\u53e3", None));
#endif // QT_CONFIG(tooltip)

        __sortingEnabled = self.tbe_console.isSortingEnabled()
        self.tbe_console.setSortingEnabled(False)
        self.tbe_console.setSortingEnabled(__sortingEnabled)

        self.label_52.setText(QCoreApplication.translate("WndMain", u"\u6267\u884c\u5217\u8868", None))
#if QT_CONFIG(tooltip)
        self.lst_exec.setToolTip(QCoreApplication.translate("WndMain", u"\u53cc\u51fb\u9009\u4e2d\u5217\u8868\u9879\u53ef\u4ece\u6267\u884c\u5217\u8868\u4e2d\u5220\u9664, \u6309\u4f4f\u5e76\u62d6\u52a8\u53ef\u8c03\u6574\u4efb\u52a1\u7684\u6267\u884c\u987a\u5e8f", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.lst_plan.setToolTip(QCoreApplication.translate("WndMain", u"\u53cc\u51fb\u5217\u8868\u9879\u53ef\u8bfb\u53d6\u6307\u5b9a\u65b9\u6848\u5230\u63a7\u4ef6", None))
#endif // QT_CONFIG(tooltip)
        self.label_54.setText(QCoreApplication.translate("WndMain", u"\u65b0\u65b9\u6848\u540d", None))
        self.btn_plan_create.setText(QCoreApplication.translate("WndMain", u"\u65b0\u5efa", None))
        self.btn_plan_rename.setText(QCoreApplication.translate("WndMain", u"\u91cd\u547d\u540d", None))
        self.label_53.setText(QCoreApplication.translate("WndMain", u"\u65b9\u6848\u5217\u8868", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("WndMain", u"\u6218\u6597\u8bbe\u7f6e", None))
        self.label_21.setText(QCoreApplication.translate("WndMain", u"\u5b9d\u5b9d", None))
        self.cmb_policy_bb.setItemText(0, QCoreApplication.translate("WndMain", u"\u6355\u6349", None))
        self.cmb_policy_bb.setItemText(1, QCoreApplication.translate("WndMain", u"\u9632\u5fa1", None))
        self.cmb_policy_bb.setItemText(2, QCoreApplication.translate("WndMain", u"\u65e0\u89c6", None))

#if QT_CONFIG(tooltip)
        self.chk_fuyu.setToolTip(QCoreApplication.translate("WndMain", u"\u786e\u4fdd\"\u606d\u559c\u53d1\u8d22\"\u653e\u5728\u6218\u6597\u65f6\u7684\u5feb\u6377\u680f\u4e0a", None))
#endif // QT_CONFIG(tooltip)
        self.chk_fuyu.setText(QCoreApplication.translate("WndMain", u"\u5bcc\u88d5\u53d1\u8d22", None))
#if QT_CONFIG(tooltip)
        self.chk_da_rou_shan.setToolTip(QCoreApplication.translate("WndMain", u"110\u7ea7\u4ee5\u4e0a\u5c01\u5996\u5730\u56fe\u6218\u6597\u65f6\u624d\u53ef\u80fd\u89e6\u53d1", None))
#endif // QT_CONFIG(tooltip)
        self.chk_da_rou_shan.setText(QCoreApplication.translate("WndMain", u"\u666e\u653b\u5927\u8089\u5c71", None))
#if QT_CONFIG(tooltip)
        self.chk_zhao_huan.setToolTip(QCoreApplication.translate("WndMain", u"\u5f53\u524d\u5ba0\u7269\u6b7b\u4ea1\u4f1a\u81ea\u52a8\u51fa\u6218\u53e6\u4e00\u53ea", None))
#endif // QT_CONFIG(tooltip)
        self.chk_zhao_huan.setText(QCoreApplication.translate("WndMain", u"\u81ea\u52a8\u53ec\u5524", None))
#if QT_CONFIG(tooltip)
        self.chk_df_lahuan.setToolTip(QCoreApplication.translate("WndMain", u"\u786e\u4fdd\u628a\"\u9ed1\u6697\u5149\u73af\"\u6280\u80fd\u653e\u5230\u53f3\u4fa7\u5feb\u6377\u5217\u8868\u4e2d, \u82e5\u6ca1\u6709\u62c9\u73af\u4ea7\u751f\u7684\u62a4\u76fe, \u4f1a\u81ea\u52a8\u4f7f\u7528\u9ed1\u6697\u5149\u73af\u6280\u80fd", None))
#endif // QT_CONFIG(tooltip)
        self.chk_df_lahuan.setText(QCoreApplication.translate("WndMain", u"\u5730\u5e9c\u62c9\u73af", None))
#if QT_CONFIG(tooltip)
        self.chk_save_people.setToolTip(QCoreApplication.translate("WndMain", u"\u961f\u53cb\u6b7b\u4ea1, DF, FM, PT\u4f7f\u7528\u590d\u6d3b\u6280\u80fd", None))
#endif // QT_CONFIG(tooltip)
        self.chk_save_people.setText(QCoreApplication.translate("WndMain", u"\u8f85\u52a9\u6551\u961f\u53cb", None))
#if QT_CONFIG(tooltip)
        self.chk_tm_anqi.setToolTip(QCoreApplication.translate("WndMain", u"\u786e\u4fdd\"\u96e8\u9732\u5343\u672c\" \u548c \"\u5929\u4ed9\u5e97\u94fa\"\u653e\u5728\u6218\u6597\u65f6\u7684\u5feb\u6377\u680f\u4e0a, \u4f18\u5148\u4e70\u98de\u5200,\u82e5\u6ca1\u6709,\u5219\u4e70\u6885\u82b1\u9556", None))
#endif // QT_CONFIG(tooltip)
        self.chk_tm_anqi.setText(QCoreApplication.translate("WndMain", u"\u5929\u9b54\u4e70\u6697\u5668", None))
        self.label.setText(QCoreApplication.translate("WndMain", u"\u9996\u4e2a\u56de\u5408:", None))
        self.label_42.setText(QCoreApplication.translate("WndMain", u"\u6280\u80fd", None))
        self.cmb_skill_round1.setItemText(0, QCoreApplication.translate("WndMain", u"\u81ea\u52a8", None))
        self.cmb_skill_round1.setItemText(1, QCoreApplication.translate("WndMain", u"F1", None))
        self.cmb_skill_round1.setItemText(2, QCoreApplication.translate("WndMain", u"F2", None))
        self.cmb_skill_round1.setItemText(3, QCoreApplication.translate("WndMain", u"F3", None))
        self.cmb_skill_round1.setItemText(4, QCoreApplication.translate("WndMain", u"F4", None))
        self.cmb_skill_round1.setItemText(5, QCoreApplication.translate("WndMain", u"F5", None))
        self.cmb_skill_round1.setItemText(6, QCoreApplication.translate("WndMain", u"F6", None))
        self.cmb_skill_round1.setItemText(7, QCoreApplication.translate("WndMain", u"F7", None))
        self.cmb_skill_round1.setItemText(8, QCoreApplication.translate("WndMain", u"F8", None))

        self.label_43.setText(QCoreApplication.translate("WndMain", u"\u76ee\u6807", None))
        self.cmb_obj_round1.setItemText(0, QCoreApplication.translate("WndMain", u"\u654c\u65b9", None))
        self.cmb_obj_round1.setItemText(1, QCoreApplication.translate("WndMain", u"\u53cb\u65b9", None))

#if QT_CONFIG(tooltip)
        self.cmb_obj_round1.setToolTip(QCoreApplication.translate("WndMain", u"\u654c\u65b9: \u4f18\u5148\u6253BOSS\u602a, \u82e5BOSS\u602a\u6b7b\u4ea1\u5219\u968f\u673a\u6253\u5176\u5b83\u602a;    \u53cb\u65b9: \u4f18\u5148\u5bf9\u961f\u957f\u5ba0\u7269\u4f7f\u7528, \u82e5\u4e0d\u6210\u529f\u5219\u5bf9\u961f\u957f\u4f7f\u7528, \u82e5\u4ecd\u4e0d\u6210\u529f\u5219\u5bf9\u5176\u5b83\u961f\u53cb\u4f7f\u7528", None))
#endif // QT_CONFIG(tooltip)
        self.label_46.setText(QCoreApplication.translate("WndMain", u"\u5269\u4f59\u56de\u5408:", None))
        self.label_44.setText(QCoreApplication.translate("WndMain", u"\u6280\u80fd", None))
        self.cmb_skill_round2.setItemText(0, QCoreApplication.translate("WndMain", u"\u81ea\u52a8", None))
        self.cmb_skill_round2.setItemText(1, QCoreApplication.translate("WndMain", u"F1", None))
        self.cmb_skill_round2.setItemText(2, QCoreApplication.translate("WndMain", u"F2", None))
        self.cmb_skill_round2.setItemText(3, QCoreApplication.translate("WndMain", u"F3", None))
        self.cmb_skill_round2.setItemText(4, QCoreApplication.translate("WndMain", u"F4", None))
        self.cmb_skill_round2.setItemText(5, QCoreApplication.translate("WndMain", u"F5", None))
        self.cmb_skill_round2.setItemText(6, QCoreApplication.translate("WndMain", u"F6", None))
        self.cmb_skill_round2.setItemText(7, QCoreApplication.translate("WndMain", u"F7", None))
        self.cmb_skill_round2.setItemText(8, QCoreApplication.translate("WndMain", u"F8", None))

        self.label_45.setText(QCoreApplication.translate("WndMain", u"\u76ee\u6807", None))
        self.cmb_obj_round2.setItemText(0, QCoreApplication.translate("WndMain", u"\u654c\u65b9", None))
        self.cmb_obj_round2.setItemText(1, QCoreApplication.translate("WndMain", u"\u53cb\u65b9", None))

#if QT_CONFIG(tooltip)
        self.cmb_obj_round2.setToolTip(QCoreApplication.translate("WndMain", u"\u654c\u65b9: \u4f18\u5148\u6253BOSS\u602a, \u82e5BOSS\u602a\u6b7b\u4ea1\u5219\u968f\u673a\u6253\u5176\u5b83\u602a;    \u53cb\u65b9: \u4f18\u5148\u5bf9\u961f\u957f\u5ba0\u7269\u4f7f\u7528, \u82e5\u4e0d\u6210\u529f\u5219\u5bf9\u961f\u957f\u4f7f\u7528, \u82e5\u4ecd\u4e0d\u6210\u529f\u5219\u5bf9\u5176\u5b83\u961f\u53cb\u4f7f\u7528", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.btn_plan_save.setToolTip(QCoreApplication.translate("WndMain", u"\u4fdd\u5b58 \u6267\u884c\u5217\u8868\u548c\u6218\u6597\u8bbe\u7f6e \u5230 \u9009\u4e2d\u65b9\u6848, \u672a\u9009\u62e9\u65b9\u6848\u5219\u4fdd\u5b58\u5230\u5185\u7f6e\u9ed8\u8ba4\u65b9\u6848\u4e2d", None))
#endif // QT_CONFIG(tooltip)
        self.btn_plan_save.setText(QCoreApplication.translate("WndMain", u"\u4fdd\u5b58\u5230\u65b9\u6848\u2192", None))
        self.label_49.setText(QCoreApplication.translate("WndMain", u"\u529f\u80fd\u5217\u8868", None))
        ___qtreewidgetitem = self.tre_all.headerItem()
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("WndMain", u"\u6240\u6709\u529f\u80fd", None));

        __sortingEnabled1 = self.tre_all.isSortingEnabled()
        self.tre_all.setSortingEnabled(False)
        ___qtreewidgetitem1 = self.tre_all.topLevelItem(0)
        ___qtreewidgetitem1.setText(0, QCoreApplication.translate("WndMain", u"\u5355\u4eba", None));
        ___qtreewidgetitem2 = ___qtreewidgetitem1.child(0)
        ___qtreewidgetitem2.setText(0, QCoreApplication.translate("WndMain", u"\u8fd0\u9556\u4efb\u52a1", None));
        ___qtreewidgetitem3 = ___qtreewidgetitem1.child(1)
        ___qtreewidgetitem3.setText(0, QCoreApplication.translate("WndMain", u"\u5b9d\u56fe\u4efb\u52a1", None));
        ___qtreewidgetitem4 = ___qtreewidgetitem1.child(2)
        ___qtreewidgetitem4.setText(0, QCoreApplication.translate("WndMain", u"\u81ea\u52a8\u6316\u5b9d", None));
        ___qtreewidgetitem5 = ___qtreewidgetitem1.child(3)
        ___qtreewidgetitem5.setText(0, QCoreApplication.translate("WndMain", u"\u4e3b\u7ebf\u5267\u60c5", None));
        ___qtreewidgetitem6 = ___qtreewidgetitem1.child(4)
        ___qtreewidgetitem6.setText(0, QCoreApplication.translate("WndMain", u"\u5e08\u95e8\u4efb\u52a1", None));
        ___qtreewidgetitem7 = ___qtreewidgetitem1.child(5)
        ___qtreewidgetitem7.setText(0, QCoreApplication.translate("WndMain", u"\u6e05\u7406\u80cc\u5305", None));
        ___qtreewidgetitem8 = ___qtreewidgetitem1.child(6)
        ___qtreewidgetitem8.setText(0, QCoreApplication.translate("WndMain", u"\u6350\u732e\u88c5\u5907", None));
        ___qtreewidgetitem9 = ___qtreewidgetitem1.child(7)
        ___qtreewidgetitem9.setText(0, QCoreApplication.translate("WndMain", u"\u4fee\u70bc\u4efb\u52a1", None));
        ___qtreewidgetitem10 = ___qtreewidgetitem1.child(8)
        ___qtreewidgetitem10.setText(0, QCoreApplication.translate("WndMain", u"\u5e2e\u6d3e\u7ecf\u5546", None));
        ___qtreewidgetitem11 = ___qtreewidgetitem1.child(9)
        ___qtreewidgetitem11.setText(0, QCoreApplication.translate("WndMain", u"\u5e2e\u6d3e\u7384\u6b66", None));
        ___qtreewidgetitem12 = ___qtreewidgetitem1.child(10)
        ___qtreewidgetitem12.setText(0, QCoreApplication.translate("WndMain", u"\u5e2e\u6d3e\u9752\u9f99", None));
        ___qtreewidgetitem13 = ___qtreewidgetitem1.child(11)
        ___qtreewidgetitem13.setText(0, QCoreApplication.translate("WndMain", u"\u5b98\u804c\u4efb\u52a1", None));
        ___qtreewidgetitem14 = ___qtreewidgetitem1.child(12)
        ___qtreewidgetitem14.setText(0, QCoreApplication.translate("WndMain", u"\u7ecf\u9a8c\u6362\u4fee", None));
        ___qtreewidgetitem15 = ___qtreewidgetitem1.child(13)
        ___qtreewidgetitem15.setText(0, QCoreApplication.translate("WndMain", u"\u5b50\u5973\u6e29\u9971", None));
        ___qtreewidgetitem16 = ___qtreewidgetitem1.child(14)
        ___qtreewidgetitem16.setText(0, QCoreApplication.translate("WndMain", u"\u5236\u4f5c\u70f9\u996a", None));
        ___qtreewidgetitem17 = ___qtreewidgetitem1.child(15)
        ___qtreewidgetitem17.setText(0, QCoreApplication.translate("WndMain", u"\u4f53\u529b\u6253\u5de5", None));
        ___qtreewidgetitem18 = ___qtreewidgetitem1.child(16)
        ___qtreewidgetitem18.setText(0, QCoreApplication.translate("WndMain", u"\u4fee\u70bc\u5b9d\u7bb1", None));
        ___qtreewidgetitem19 = ___qtreewidgetitem1.child(17)
        ___qtreewidgetitem19.setText(0, QCoreApplication.translate("WndMain", u"\u5e78\u8fd0\u8f6c\u76d8", None));
        ___qtreewidgetitem20 = ___qtreewidgetitem1.child(18)
        ___qtreewidgetitem20.setText(0, QCoreApplication.translate("WndMain", u"\u8f6c\u8f6c\u4e50", None));
        ___qtreewidgetitem21 = ___qtreewidgetitem1.child(19)
        ___qtreewidgetitem21.setText(0, QCoreApplication.translate("WndMain", u"\u4efb\u52a1\u94fe", None));
        ___qtreewidgetitem22 = ___qtreewidgetitem1.child(20)
        ___qtreewidgetitem22.setText(0, QCoreApplication.translate("WndMain", u"\u5316\u9f99\u9f0e", None));
        ___qtreewidgetitem23 = ___qtreewidgetitem1.child(21)
        ___qtreewidgetitem23.setText(0, QCoreApplication.translate("WndMain", u"\u7948\u798f", None));
        ___qtreewidgetitem24 = self.tre_all.topLevelItem(1)
        ___qtreewidgetitem24.setText(0, QCoreApplication.translate("WndMain", u"\u7ec4\u961f", None));
        ___qtreewidgetitem25 = ___qtreewidgetitem24.child(0)
        ___qtreewidgetitem25.setText(0, QCoreApplication.translate("WndMain", u"\u961f\u5458\u6302\u673a", None));
        ___qtreewidgetitem26 = ___qtreewidgetitem24.child(1)
        ___qtreewidgetitem26.setText(0, QCoreApplication.translate("WndMain", u"\u5e26\u961f\u6253\u91ce", None));
        ___qtreewidgetitem27 = ___qtreewidgetitem24.child(2)
        ___qtreewidgetitem27.setText(0, QCoreApplication.translate("WndMain", u"\u5e26\u961f\u6349\u9b3c", None));
        ___qtreewidgetitem28 = ___qtreewidgetitem24.child(3)
        ___qtreewidgetitem28.setText(0, QCoreApplication.translate("WndMain", u"\u5e26\u961f\u5c01\u5996", None));
        ___qtreewidgetitem29 = ___qtreewidgetitem24.child(4)
        ___qtreewidgetitem29.setText(0, QCoreApplication.translate("WndMain", u"\u5e26\u961f\u526f\u672c", None));
        ___qtreewidgetitem30 = ___qtreewidgetitem24.child(5)
        ___qtreewidgetitem30.setText(0, QCoreApplication.translate("WndMain", u"\u6df7\u961f\u526f\u672c", None));
        ___qtreewidgetitem31 = ___qtreewidgetitem24.child(6)
        ___qtreewidgetitem31.setText(0, QCoreApplication.translate("WndMain", u"\u4f11\u95f2\u9493\u9c7c", None));
        ___qtreewidgetitem32 = ___qtreewidgetitem24.child(7)
        ___qtreewidgetitem32.setText(0, QCoreApplication.translate("WndMain", u"\u7075\u72d0\u4e50\u56ed", None));
        ___qtreewidgetitem33 = ___qtreewidgetitem24.child(8)
        ___qtreewidgetitem33.setText(0, QCoreApplication.translate("WndMain", u"\u8fb9\u5883\u6551\u63f4", None));
        ___qtreewidgetitem34 = ___qtreewidgetitem24.child(9)
        ___qtreewidgetitem34.setText(0, QCoreApplication.translate("WndMain", u"\u86ee\u6d1e\u5bc6\u4ee4", None));
        ___qtreewidgetitem35 = ___qtreewidgetitem24.child(10)
        ___qtreewidgetitem35.setText(0, QCoreApplication.translate("WndMain", u"\u65d7\u5305\u4efb\u52a1", None));
        ___qtreewidgetitem36 = self.tre_all.topLevelItem(2)
        ___qtreewidgetitem36.setText(0, QCoreApplication.translate("WndMain", u"\u9650\u65f6", None));
        ___qtreewidgetitem37 = ___qtreewidgetitem36.child(0)
        ___qtreewidgetitem37.setText(0, QCoreApplication.translate("WndMain", u"\u5929\u964d\u5b9d\u7bb1", None));
        ___qtreewidgetitem38 = ___qtreewidgetitem36.child(1)
        ___qtreewidgetitem38.setText(0, QCoreApplication.translate("WndMain", u"\u5e2e\u6d3e\u5f3a\u76d7", None));
        ___qtreewidgetitem39 = self.tre_all.topLevelItem(3)
        ___qtreewidgetitem39.setText(0, QCoreApplication.translate("WndMain", u"\u9644\u52a0", None));
        ___qtreewidgetitem40 = ___qtreewidgetitem39.child(0)
        ___qtreewidgetitem40.setText(0, QCoreApplication.translate("WndMain", u"\u9886\u53d6\u53cc\u500d", None));
        ___qtreewidgetitem41 = ___qtreewidgetitem39.child(1)
        ___qtreewidgetitem41.setText(0, QCoreApplication.translate("WndMain", u"\u51bb\u7ed3\u53cc\u500d", None));
        ___qtreewidgetitem42 = ___qtreewidgetitem39.child(2)
        ___qtreewidgetitem42.setText(0, QCoreApplication.translate("WndMain", u"\u9000\u51fa\u961f\u4f0d", None));
        self.tre_all.setSortingEnabled(__sortingEnabled1)

#if QT_CONFIG(tooltip)
        self.tre_all.setToolTip(QCoreApplication.translate("WndMain", u"\u53cc\u51fb\u5217\u8868\u9879\u53ef\u6dfb\u52a0\u5230\u6267\u884c\u5217\u8868", None))
#endif // QT_CONFIG(tooltip)
        self.chk_auto_buy_drug.setTitle(QCoreApplication.translate("WndMain", u"\u81ea\u52a8\u4e70\u836f", None))
#if QT_CONFIG(tooltip)
        self.label_7.setToolTip(QCoreApplication.translate("WndMain", u"\u9009\u5929\u4ed9\u5e97\u94fa,\u5219\u4e70\u8c46\u8150, \u9009\u5bc4\u552e\u4e2d\u5fc3,\u5219\u4e70\u4e94\u5473\u7fb9. \n"
"\u82e5\u80cc\u5305\u4e2d\u6709\u4e94\u5473\u7fb9,\u5219\u6bcf\u4e2a\u4e94\u5473\u7fb9\u89c6\u4e3a300\u4e2a\u8c46\u8150", None))
#endif // QT_CONFIG(tooltip)
        self.label_7.setText(QCoreApplication.translate("WndMain", u"\u52a0\u8840\u836f\u6570\u91cf <", None))
        self.edt_hp_num.setText(QCoreApplication.translate("WndMain", u"50", None))
        self.label_990.setText(QCoreApplication.translate("WndMain", u"\u4e2a,\u5230", None))
        self.cmb_doufu.setItemText(0, QCoreApplication.translate("WndMain", u"\u5929\u4ed9\u5e97\u94fa", None))
        self.cmb_doufu.setItemText(1, QCoreApplication.translate("WndMain", u"\u5bc4\u552e\u4e2d\u5fc3", None))

        self.label_11.setText(QCoreApplication.translate("WndMain", u"\u8d2d\u4e70", None))
#if QT_CONFIG(tooltip)
        self.label_8.setToolTip(QCoreApplication.translate("WndMain", u"\u9009\u5929\u4ed9\u5e97\u94fa,\u5219\u4e70\u4e94\u52a0\u76ae, \u9009\u5bc4\u552e\u4e2d\u5fc3,\u5219\u4e70\u7389\u743c\u6d46. \n"
"\u82e5\u80cc\u5305\u4e2d\u6709\u7389\u743c\u6d46,\u5219\u6bcf\u4e2a\u7389\u743c\u6d46\u89c6\u4e3a150\u4e2a\u4e94\u52a0\u76ae", None))
#endif // QT_CONFIG(tooltip)
        self.label_8.setText(QCoreApplication.translate("WndMain", u"\u52a0\u84dd\u836f\u6570\u91cf <", None))
        self.edt_mp_num.setText(QCoreApplication.translate("WndMain", u"50", None))
        self.label_991.setText(QCoreApplication.translate("WndMain", u"\u4e2a,\u5230", None))
        self.cmb_wujiapi.setItemText(0, QCoreApplication.translate("WndMain", u"\u5929\u4ed9\u5e97\u94fa", None))
        self.cmb_wujiapi.setItemText(1, QCoreApplication.translate("WndMain", u"\u5bc4\u552e\u4e2d\u5fc3", None))

        self.label_12.setText(QCoreApplication.translate("WndMain", u"\u8d2d\u4e70", None))
#if QT_CONFIG(tooltip)
        self.label_9.setToolTip(QCoreApplication.translate("WndMain", u"\u9009\u5929\u4ed9\u5e97\u94fa,\u5219\u4e70\u5347\u4e39, \u9009\u5bc4\u552e\u4e2d\u5fc3,\u5219\u4e70\u7389\u84c9\u7cd5. \n"
"\u82e5\u80cc\u5305\u4e2d\u6709\u7389\u84c9\u7cd5,\u5219\u6bcf\u4e2a\u7389\u84c9\u7cd5\u89c6\u4e3a500\u4e2a\u5347\u4e39", None))
#endif // QT_CONFIG(tooltip)
        self.label_9.setText(QCoreApplication.translate("WndMain", u"\u4f24\u52bf\u836f\u6570\u91cf <", None))
        self.edt_sp_num.setText(QCoreApplication.translate("WndMain", u"50", None))
        self.label_992.setText(QCoreApplication.translate("WndMain", u"\u4e2a,\u5230", None))
        self.cmb_shengdan.setItemText(0, QCoreApplication.translate("WndMain", u"\u5929\u4ed9\u5e97\u94fa", None))
        self.cmb_shengdan.setItemText(1, QCoreApplication.translate("WndMain", u"\u5bc4\u552e\u4e2d\u5fc3", None))

        self.label_13.setText(QCoreApplication.translate("WndMain", u"\u8d2d\u4e70", None))
#if QT_CONFIG(tooltip)
        self.label_10.setToolTip(QCoreApplication.translate("WndMain", u"\u53ea\u80fd\u8bbe\u7f6e\u5728\u5929\u4ed9\u5e97\u94fa\u4e70\u9ad8\u5ba0\u7cae", None))
#endif // QT_CONFIG(tooltip)
        self.label_10.setText(QCoreApplication.translate("WndMain", u"\u9ad8\u5ba0\u7cae\u6570\u91cf <", None))
        self.edt_gcl_num.setText(QCoreApplication.translate("WndMain", u"50", None))
        self.label_994.setText(QCoreApplication.translate("WndMain", u"\u4e2a,\u5230", None))
        self.cmb_gaochong.setItemText(0, QCoreApplication.translate("WndMain", u"\u5929\u4ed9\u5e97\u94fa", None))
        self.cmb_gaochong.setItemText(1, QCoreApplication.translate("WndMain", u"\u5bc4\u552e\u4e2d\u5fc3", None))

#if QT_CONFIG(tooltip)
        self.cmb_gaochong.setToolTip(QCoreApplication.translate("WndMain", u"\u9ad8\u7ea7\u5ba0\u7269\u53e3\u7cae\u53ea\u80fd\u5728\u5929\u4ed9\u5e97\u94fa\u8d2d\u4e70", None))
#endif // QT_CONFIG(tooltip)
        self.label_14.setText(QCoreApplication.translate("WndMain", u"\u8d2d\u4e70", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("WndMain", u"\u5176\u5b83", None))
        self.chk_use_qmx.setText(QCoreApplication.translate("WndMain", u"\u81ea\u52a8\u4f7f\u7528\u9a71\u9b54\u9999", None))
        self.chk_buy_qmx.setText(QCoreApplication.translate("WndMain", u"\u81ea\u52a8\u8d2d\u4e70\u9a71\u9b54\u9999", None))
        self.chk_supply_qibao.setText(QCoreApplication.translate("WndMain", u"\u81ea\u52a8\u8865\u5145\u98de\u884c\u65d7\u5305", None))
        self.chk_make_jiaju.setText(QCoreApplication.translate("WndMain", u"\u81ea\u5236\u5bb6\u5177\u548c\u5ead\u9662\u88c5\u9970", None))
        self.label_15.setText(QCoreApplication.translate("WndMain", u"\u8d2d\u7269\u4f18\u5148\u4f7f\u7528", None))
        self.cmb_buy_style.setItemText(0, QCoreApplication.translate("WndMain", u"\u4fe1\u8a89", None))
        self.cmb_buy_style.setItemText(1, QCoreApplication.translate("WndMain", u"\u73b0\u91d1", None))

        self.label_35.setText(QCoreApplication.translate("WndMain", u"\u5f00\u5b9d\u7bb1", None))
        self.cmb_bao_xiang.setItemText(0, QCoreApplication.translate("WndMain", u"\u5de6", None))
        self.cmb_bao_xiang.setItemText(1, QCoreApplication.translate("WndMain", u"\u4e2d", None))
        self.cmb_bao_xiang.setItemText(2, QCoreApplication.translate("WndMain", u"\u53f3", None))

        self.chk_use_htd.setText(QCoreApplication.translate("WndMain", u"\u4f18\u5148\u4f7f\u7528\u8fd8\u7ae5\u4e39\u4e70\u5ba0", None))
        self.chk_buy_csf.setText(QCoreApplication.translate("WndMain", u"\u81ea\u52a8\u8d2d\u4e70\u4f20\u9001\u7b26", None))
        self.chk_queue_back.setText(QCoreApplication.translate("WndMain", u"\u81ea\u52a8\u6392\u961f\u56de\u5230\u539f\u670d", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("WndMain", u"\u5b89\u5168", None))
#if QT_CONFIG(tooltip)
        self.chk_add_hp.setToolTip(QCoreApplication.translate("WndMain", u" \u6218\u6597\u5f00\u59cb\u65f6\u81ea\u52a8\u8865\u8840", None))
#endif // QT_CONFIG(tooltip)
        self.chk_add_hp.setText(QCoreApplication.translate("WndMain", u"\u4eba\u5ba0\u81ea\u52a8\u8865\u8840", None))
#if QT_CONFIG(tooltip)
        self.chk_add_mp.setToolTip(QCoreApplication.translate("WndMain", u" \u6218\u6597\u5f00\u59cb\u65f6\u81ea\u52a8\u8865\u84dd", None))
#endif // QT_CONFIG(tooltip)
        self.chk_add_mp.setText(QCoreApplication.translate("WndMain", u"\u4eba\u5ba0\u81ea\u52a8\u8865\u84dd", None))
#if QT_CONFIG(tooltip)
        self.chk_add_loyal.setToolTip(QCoreApplication.translate("WndMain", u" \u6218\u6597\u5f00\u59cb\u65f6\u81ea\u52a8\u8865\u5fe0\u8bda", None))
#endif // QT_CONFIG(tooltip)
        self.chk_add_loyal.setText(QCoreApplication.translate("WndMain", u"\u8865\u5145\u5ba0\u7269\u5fe0\u8bda", None))
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

        self.chk_on_time.setTitle(QCoreApplication.translate("WndMain", u"\u5b9a\u65f6", None))
        self.chk_on_time_run_all.setText(QCoreApplication.translate("WndMain", u"\u8fd0\u884c\u5168\u90e8\u7a97\u53e3", None))
        self.tmedt_on_time_run_all.setDisplayFormat(QCoreApplication.translate("WndMain", u"HH:mm", None))
        self.chk_on_time_shut_down.setText(QCoreApplication.translate("WndMain", u"\u5173\u95ed\u8ba1\u7b97\u673a", None))
        self.tmedt_on_time_shut_down.setDisplayFormat(QCoreApplication.translate("WndMain", u"HH:mm", None))
        self.tab_set.setTabText(self.tab_set.indexOf(self.tab_4), QCoreApplication.translate("WndMain", u"\u57fa\u672c\u8bbe\u7f6e", None))
        self.groupBox_13.setTitle(QCoreApplication.translate("WndMain", u"\u6e05\u7406\u80cc\u5305", None))
        self.label_31.setText(QCoreApplication.translate("WndMain", u"\u90ae\u4ef6", None))
        self.label_32.setText(QCoreApplication.translate("WndMain", u"\u81ea\u52a8\u6536\u53d6", None))
#if QT_CONFIG(tooltip)
        self.label_29.setToolTip(QCoreApplication.translate("WndMain", u"\u5305\u62ec\u5377\u5b97, \u961f\u957f\u793c\u76d2, \u8bb8\u613f\u679c, \u4e09\u754c\u5bc6\u5f55\u7b49", None))
#endif // QT_CONFIG(tooltip)
        self.label_29.setText(QCoreApplication.translate("WndMain", u"\u5377\u5b97\u7b49", None))
        self.label_30.setText(QCoreApplication.translate("WndMain", u"\u53f3\u952e\u4f7f\u7528", None))
        self.label_2.setText(QCoreApplication.translate("WndMain", u"\u9c7c\u7c7b", None))
        self.label_26.setText(QCoreApplication.translate("WndMain", u"\u5151\u6362\u9493\u9c7c\u79ef\u5206", None))
        self.label_3.setText(QCoreApplication.translate("WndMain", u"\u85cf\u5b9d\u56fe", None))
        self.cmb_qingbao_cbt.setItemText(0, QCoreApplication.translate("WndMain", u"\u81ea\u52a8\u6316\u5b9d", None))
        self.cmb_qingbao_cbt.setItemText(1, QCoreApplication.translate("WndMain", u"\u5b58\u5230\u4ed3\u5e93", None))

#if QT_CONFIG(tooltip)
        self.label_28.setToolTip(QCoreApplication.translate("WndMain", u"\u5305\u62ec \u5bb6\u5177, \u5ead\u9662\u88c5\u9970, \u53e4\u8463, \u70f9\u996a\u7b49, \u4f46 \u4e94\u5473\u7fb9, \u7389\u743c\u6d46, \u7389\u84c9\u818f\u4f1a\u4fdd\u7559\u5728\u80cc\u5305\u4e2d", None))
#endif // QT_CONFIG(tooltip)
        self.label_28.setText(QCoreApplication.translate("WndMain", u"\u73b0\u91d1\u7269\u54c1", None))
        self.cmb_qingbao_xj.setItemText(0, QCoreApplication.translate("WndMain", u"\u4e0a\u67b6\u5bc4\u552e", None))
        self.cmb_qingbao_xj.setItemText(1, QCoreApplication.translate("WndMain", u"\u5b58\u5230\u4ed3\u5e93", None))

#if QT_CONFIG(tooltip)
        self.label_27.setToolTip(QCoreApplication.translate("WndMain", u"\u5305\u62ec \u88c5\u5907\u4e4b\u7075, \u5b9d\u77f3, \u5982\u610f\u5b9d\u7389, \u5ba0\u7269\u9970\u7269, \u9b54\u517d\u8981\u8bc0\u7b49", None))
#endif // QT_CONFIG(tooltip)
        self.label_27.setText(QCoreApplication.translate("WndMain", u"\u795e\u6b66\u5e01\u7269\u54c1", None))
        self.cmb_qingbao_swb.setItemText(0, QCoreApplication.translate("WndMain", u"\u5546\u57ce\u51fa\u552e", None))
        self.cmb_qingbao_swb.setItemText(1, QCoreApplication.translate("WndMain", u"\u5b58\u5230\u4ed3\u5e93", None))

#if QT_CONFIG(tooltip)
        self.label_34.setToolTip(QCoreApplication.translate("WndMain", u"\u5305\u62ec \u5ba0\u7269\u7ecf\u9a8c\u5fc3\u5f97(\u7ed1\u5b9a\u4e13\u7528), \u8fd8\u7ae5\u4e39, \u91d1\u9999\u679c, \u6c5f\u6e56\u5fd7, \u70bc\u5316\u7b26, \u5ba0\u7269\u88c5\u5907, \u7cbe\u7075\u4e4b\u5fc3\u7b49", None))
#endif // QT_CONFIG(tooltip)
        self.label_34.setText(QCoreApplication.translate("WndMain", u"\u5176\u5b83", None))
        self.label_33.setText(QCoreApplication.translate("WndMain", u"\u5b58\u5230\u4ed3\u5e93", None))
        self.groupBox_17.setTitle(QCoreApplication.translate("WndMain", u"\u5e2e\u6d3e\u7ecf\u5546", None))
        self.cmb_js_role.setItemText(0, QCoreApplication.translate("WndMain", u"\u59ae\u59ae", None))
        self.cmb_js_role.setItemText(1, QCoreApplication.translate("WndMain", u"\u94b1\u767e\u4e07", None))
        self.cmb_js_role.setItemText(2, QCoreApplication.translate("WndMain", u"\u6556\u5343\u91d1", None))
        self.cmb_js_role.setItemText(3, QCoreApplication.translate("WndMain", u"\u98ce\u4e8c\u90ce", None))
        self.cmb_js_role.setItemText(4, QCoreApplication.translate("WndMain", u"\u5b59\u5c0f\u8d24", None))
        self.cmb_js_role.setItemText(5, QCoreApplication.translate("WndMain", u"\u5f20\u5927\u529b", None))

        self.label_41.setText(QCoreApplication.translate("WndMain", u"\u96be\u5ea6", None))
        self.cmb_js_difficulty.setItemText(0, QCoreApplication.translate("WndMain", u"\u7b80\u5355", None))
        self.cmb_js_difficulty.setItemText(1, QCoreApplication.translate("WndMain", u"\u666e\u901a", None))
        self.cmb_js_difficulty.setItemText(2, QCoreApplication.translate("WndMain", u"\u56f0\u96be", None))

        self.label_40.setText(QCoreApplication.translate("WndMain", u"\u89d2\u8272", None))
#if QT_CONFIG(tooltip)
        self.edt_jingshang_num.setToolTip(QCoreApplication.translate("WndMain", u"\u8bf7\u8f93\u51650-999\u4e4b\u95f4\u7684\u6570\u5b57", None))
#endif // QT_CONFIG(tooltip)
        self.edt_jingshang_num.setText(QCoreApplication.translate("WndMain", u"3", None))
        self.label_57.setText(QCoreApplication.translate("WndMain", u"\u6b21\u6570", None))
#if QT_CONFIG(tooltip)
        self.groupBox_14.setToolTip(QCoreApplication.translate("WndMain", u" \u53ea\u4f1a\u7528\u4f53\u529b\u5236\u9020, \u9700\u5148\u5b66\u591f\u76f8\u5e94\u7b49\u7ea7\u7684\u6253\u9020\u88c1\u7f1d\u70bc\u91d1\u6280\u80fd", None))
#endif // QT_CONFIG(tooltip)
        self.groupBox_14.setTitle(QCoreApplication.translate("WndMain", u"\u6350\u732e\u88c5\u5907", None))
        self.label_36.setText(QCoreApplication.translate("WndMain", u"\u7b49\u7ea7", None))
        self.cmb_jzb_level.setItemText(0, QCoreApplication.translate("WndMain", u"50", None))
        self.cmb_jzb_level.setItemText(1, QCoreApplication.translate("WndMain", u"60", None))
        self.cmb_jzb_level.setItemText(2, QCoreApplication.translate("WndMain", u"70", None))
        self.cmb_jzb_level.setItemText(3, QCoreApplication.translate("WndMain", u"80", None))

        self.label_38.setText(QCoreApplication.translate("WndMain", u"\u6570\u91cf", None))
        self.cmb_jzb_num.setItemText(0, QCoreApplication.translate("WndMain", u"0", None))
        self.cmb_jzb_num.setItemText(1, QCoreApplication.translate("WndMain", u"1", None))
        self.cmb_jzb_num.setItemText(2, QCoreApplication.translate("WndMain", u"2", None))
        self.cmb_jzb_num.setItemText(3, QCoreApplication.translate("WndMain", u"3", None))
        self.cmb_jzb_num.setItemText(4, QCoreApplication.translate("WndMain", u"4", None))
        self.cmb_jzb_num.setItemText(5, QCoreApplication.translate("WndMain", u"5", None))
        self.cmb_jzb_num.setItemText(6, QCoreApplication.translate("WndMain", u"6", None))
        self.cmb_jzb_num.setItemText(7, QCoreApplication.translate("WndMain", u"7", None))
        self.cmb_jzb_num.setItemText(8, QCoreApplication.translate("WndMain", u"8", None))

        self.label_56.setText(QCoreApplication.translate("WndMain", u"\u4e70\u6700\u4f4e\u4ef7\u88c5\u5907\u7075", None))
        self.chk_jzb_gz.setText(QCoreApplication.translate("WndMain", u"\u6350\u732e\u8d35\u91cd\u88c5\u5907", None))
        self.groupBox_16.setTitle(QCoreApplication.translate("WndMain", u"\u4fee\u70bc\u4efb\u52a1", None))
        self.label_39.setText(QCoreApplication.translate("WndMain", u"\u6b21\u6570", None))
#if QT_CONFIG(tooltip)
        self.edt_xiulian_num.setToolTip(QCoreApplication.translate("WndMain", u"\u8bf7\u8f93\u51650-999\u4e4b\u95f4\u7684\u6570\u5b57", None))
#endif // QT_CONFIG(tooltip)
        self.edt_xiulian_num.setText(QCoreApplication.translate("WndMain", u"30", None))
        self.chk_xiulian_fdr.setText(QCoreApplication.translate("WndMain", u"\u75af\u9053\u4eba\u9884\u8a00\u622a\u56fe", None))
        self.chk_bang_gong.setText(QCoreApplication.translate("WndMain", u"\u5bfb\u7269\u7528\u5e2e\u8d21\u5b8c\u6210", None))
        self.groupBox_10.setTitle(QCoreApplication.translate("WndMain", u"\u5e08\u95e8\u4efb\u52a1", None))
        self.label_20.setText(QCoreApplication.translate("WndMain", u"\u6b21\u6570", None))
#if QT_CONFIG(tooltip)
        self.edt_shimen_num.setToolTip(QCoreApplication.translate("WndMain", u"\u8bf7\u8f93\u51650-999\u4e4b\u95f4\u7684\u6570\u5b57", None))
#endif // QT_CONFIG(tooltip)
        self.edt_shimen_num.setText(QCoreApplication.translate("WndMain", u"20", None))
        self.groupBox_9.setTitle(QCoreApplication.translate("WndMain", u"\u5b9d\u56fe\u4efb\u52a1", None))
        self.label_19.setText(QCoreApplication.translate("WndMain", u"\u6b21\u6570", None))
#if QT_CONFIG(tooltip)
        self.edt_baotu_num.setToolTip(QCoreApplication.translate("WndMain", u"\u8bf7\u8f93\u51650-999\u4e4b\u95f4\u7684\u6570\u5b57", None))
#endif // QT_CONFIG(tooltip)
        self.edt_baotu_num.setText(QCoreApplication.translate("WndMain", u"10", None))
        self.groupBox_8.setTitle(QCoreApplication.translate("WndMain", u"\u8fd0\u9556\u4efb\u52a1", None))
        self.label_18.setText(QCoreApplication.translate("WndMain", u"\u6b21\u6570", None))
#if QT_CONFIG(tooltip)
        self.edt_yunbiao_num.setToolTip(QCoreApplication.translate("WndMain", u"\u8bf7\u8f93\u51650-999\u4e4b\u95f4\u7684\u6570\u5b57", None))
#endif // QT_CONFIG(tooltip)
        self.edt_yunbiao_num.setText(QCoreApplication.translate("WndMain", u"20", None))
        self.groupBox_19.setTitle(QCoreApplication.translate("WndMain", u"\u4efb\u52a1\u94fe", None))
        self.label_37.setText(QCoreApplication.translate("WndMain", u"\u73af\u6570", None))
#if QT_CONFIG(tooltip)
        self.edt_renwulian_num.setToolTip(QCoreApplication.translate("WndMain", u"\u8bf7\u8f93\u51650-999\u4e4b\u95f4\u7684\u6570\u5b57", None))
#endif // QT_CONFIG(tooltip)
        self.edt_renwulian_num.setText(QCoreApplication.translate("WndMain", u"60", None))
        self.groupBox_20.setTitle(QCoreApplication.translate("WndMain", u"\u5e2e\u6d3e\u7384\u6b66", None))
        self.label_60.setText(QCoreApplication.translate("WndMain", u"\u6b21\u6570", None))
#if QT_CONFIG(tooltip)
        self.edt_xuanwu_num.setToolTip(QCoreApplication.translate("WndMain", u"\u8bf7\u8f93\u51650-999\u4e4b\u95f4\u7684\u6570\u5b57", None))
#endif // QT_CONFIG(tooltip)
        self.edt_xuanwu_num.setText(QCoreApplication.translate("WndMain", u"40", None))
        self.groupBox_22.setTitle(QCoreApplication.translate("WndMain", u"\u5e2e\u6d3e\u9752\u9f99", None))
        self.label_59.setText(QCoreApplication.translate("WndMain", u"\u6b21\u6570", None))
#if QT_CONFIG(tooltip)
        self.edt_qinglong_num.setToolTip(QCoreApplication.translate("WndMain", u"\u8bf7\u8f93\u51650-999\u4e4b\u95f4\u7684\u6570\u5b57", None))
#endif // QT_CONFIG(tooltip)
        self.edt_qinglong_num.setText(QCoreApplication.translate("WndMain", u"20", None))
        self.groupBox_24.setTitle(QCoreApplication.translate("WndMain", u"\u5b98\u804c\u4efb\u52a1", None))
        self.label_63.setText(QCoreApplication.translate("WndMain", u"\u6b21\u6570", None))
#if QT_CONFIG(tooltip)
        self.edt_guanzhi_num.setToolTip(QCoreApplication.translate("WndMain", u"\u8bf7\u8f93\u51650-999\u4e4b\u95f4\u7684\u6570\u5b57", None))
#endif // QT_CONFIG(tooltip)
        self.edt_guanzhi_num.setText(QCoreApplication.translate("WndMain", u"20", None))
        self.groupBox_25.setTitle(QCoreApplication.translate("WndMain", u"\u5236\u4f5c\u70f9\u996a", None))
        self.label_64.setText(QCoreApplication.translate("WndMain", u"\u6b21\u6570", None))
#if QT_CONFIG(tooltip)
        self.edt_pengren_num.setToolTip(QCoreApplication.translate("WndMain", u"\u8bf7\u8f93\u51650-999\u4e4b\u95f4\u7684\u6570\u5b57", None))
#endif // QT_CONFIG(tooltip)
        self.edt_pengren_num.setText(QCoreApplication.translate("WndMain", u"20", None))
        self.groupBox_26.setTitle(QCoreApplication.translate("WndMain", u"\u5316\u9f99\u9f0e", None))
        self.chk_hld_addition.setText(QCoreApplication.translate("WndMain", u"\u989d\u5916\u4fee\u70bc", None))
        self.chk_hld_longhun.setText(QCoreApplication.translate("WndMain", u"\u5151\u6362\u9f99\u9b42", None))
        self.groupBox_28.setTitle(QCoreApplication.translate("WndMain", u"\u4fee\u70bc\u5b9d\u7bb1", None))
        self.label_66.setText(QCoreApplication.translate("WndMain", u"\u5730\u56fe", None))
        self.cmb_xnbx_map.setItemText(0, QCoreApplication.translate("WndMain", u"\u957f\u5b89\u57ce\u5916", None))
        self.cmb_xnbx_map.setItemText(1, QCoreApplication.translate("WndMain", u"\u5927\u5510\u56fd\u5883", None))
        self.cmb_xnbx_map.setItemText(2, QCoreApplication.translate("WndMain", u"\u4e4c\u65af\u85cf", None))
        self.cmb_xnbx_map.setItemText(3, QCoreApplication.translate("WndMain", u"\u6606\u4ed1\u5c71", None))
        self.cmb_xnbx_map.setItemText(4, QCoreApplication.translate("WndMain", u"\u5730\u72f1\u8ff7\u5bab\u4e00\u5c42", None))
        self.cmb_xnbx_map.setItemText(5, QCoreApplication.translate("WndMain", u"\u5730\u72f1\u8ff7\u5bab\u4e8c\u5c42", None))
        self.cmb_xnbx_map.setItemText(6, QCoreApplication.translate("WndMain", u"\u5730\u72f1\u8ff7\u5bab\u4e09\u5c42", None))
        self.cmb_xnbx_map.setItemText(7, QCoreApplication.translate("WndMain", u"\u5317\u51a5", None))
        self.cmb_xnbx_map.setItemText(8, QCoreApplication.translate("WndMain", u"\u7409\u7483\u591a\u5b9d\u5854\u4e00\u5c42", None))
        self.cmb_xnbx_map.setItemText(9, QCoreApplication.translate("WndMain", u"\u7409\u7483\u591a\u5b9d\u5854\u4e8c\u5c42", None))
        self.cmb_xnbx_map.setItemText(10, QCoreApplication.translate("WndMain", u"\u7409\u7483\u591a\u5b9d\u5854\u4e09\u5c42", None))
        self.cmb_xnbx_map.setItemText(11, QCoreApplication.translate("WndMain", u"\u5bd2\u51b0\u5bab\u4e00\u5c42", None))
        self.cmb_xnbx_map.setItemText(12, QCoreApplication.translate("WndMain", u"\u5bd2\u51b0\u5bab\u4e8c\u5c42", None))
        self.cmb_xnbx_map.setItemText(13, QCoreApplication.translate("WndMain", u"\u5bd2\u51b0\u5bab\u4e09\u5c42", None))
        self.cmb_xnbx_map.setItemText(14, QCoreApplication.translate("WndMain", u"\u795e\u5f03\u5e73\u539f", None))
        self.cmb_xnbx_map.setItemText(15, QCoreApplication.translate("WndMain", u"\u4e1c\u6d77\u5e7b\u5883", None))
        self.cmb_xnbx_map.setItemText(16, QCoreApplication.translate("WndMain", u"\u5b50\u6bcd\u6cb3\u7554", None))

        self.groupBox_29.setTitle(QCoreApplication.translate("WndMain", u"\u5929\u964d\u5b9d\u7bb1", None))
        self.label_67.setText(QCoreApplication.translate("WndMain", u"\u5730\u56fe", None))
        self.cmb_tjbx_map.setItemText(0, QCoreApplication.translate("WndMain", u"\u957f\u5b89\u57ce\u5916", None))
        self.cmb_tjbx_map.setItemText(1, QCoreApplication.translate("WndMain", u"\u5927\u5510\u56fd\u5883", None))
        self.cmb_tjbx_map.setItemText(2, QCoreApplication.translate("WndMain", u"\u5927\u5510\u5883\u5916", None))
        self.cmb_tjbx_map.setItemText(3, QCoreApplication.translate("WndMain", u"\u4e4c\u65af\u85cf", None))
        self.cmb_tjbx_map.setItemText(4, QCoreApplication.translate("WndMain", u"\u6606\u4ed1\u5c71", None))

        self.tab_set.setTabText(self.tab_set.indexOf(self.tab_5), QCoreApplication.translate("WndMain", u"\u5355\u4eba\u76f8\u5173", None))
        self.groupBox_12.setTitle(QCoreApplication.translate("WndMain", u"\u4f11\u95f2\u9493\u9c7c", None))
        self.label_24.setText(QCoreApplication.translate("WndMain", u"\u6b21\u6570", None))
        self.label_23.setText(QCoreApplication.translate("WndMain", u"\u5730\u56fe", None))
        self.cmb_diaoyu_num.setItemText(0, QCoreApplication.translate("WndMain", u"1", None))
        self.cmb_diaoyu_num.setItemText(1, QCoreApplication.translate("WndMain", u"2", None))
        self.cmb_diaoyu_num.setItemText(2, QCoreApplication.translate("WndMain", u"3", None))
        self.cmb_diaoyu_num.setItemText(3, QCoreApplication.translate("WndMain", u"4", None))
        self.cmb_diaoyu_num.setItemText(4, QCoreApplication.translate("WndMain", u"5", None))

        self.label_25.setText(QCoreApplication.translate("WndMain", u"\u629b\u7aff", None))
        self.cmb_diaoyu_deal.setItemText(0, QCoreApplication.translate("WndMain", u"\u5151\u6362\u79ef\u5206", None))
        self.cmb_diaoyu_deal.setItemText(1, QCoreApplication.translate("WndMain", u"\u4f18\u5148\u6536\u85cf", None))

        self.cmb_diaoyu_map.setItemText(0, QCoreApplication.translate("WndMain", u"\u9752\u6cb3\u9547\u5916", None))
        self.cmb_diaoyu_map.setItemText(1, QCoreApplication.translate("WndMain", u"\u957f\u5b89\u57ce\u5916", None))
        self.cmb_diaoyu_map.setItemText(2, QCoreApplication.translate("WndMain", u"\u50b2\u6765\u56fd", None))
        self.cmb_diaoyu_map.setItemText(3, QCoreApplication.translate("WndMain", u"\u82b1\u679c\u5c71", None))
        self.cmb_diaoyu_map.setItemText(4, QCoreApplication.translate("WndMain", u"\u6843\u82b1\u5c9b", None))

        self.cmb_diaoyu_paogan.setItemText(0, QCoreApplication.translate("WndMain", u"\u7acb\u523b\u629b\u7aff", None))
        self.cmb_diaoyu_paogan.setItemText(1, QCoreApplication.translate("WndMain", u"S\u8bc4\u5206", None))

        self.label_47.setText(QCoreApplication.translate("WndMain", u"\u5904\u7406", None))
        self.groupBox_7.setTitle(QCoreApplication.translate("WndMain", u"\u961f\u5458\u6302\u673a", None))
        self.chk_duiyuan_ls.setText(QCoreApplication.translate("WndMain", u"\u8ddf\u968f\u961f\u957f\u9886\u53cc", None))
        self.chk_duiyuan_td.setText(QCoreApplication.translate("WndMain", u"\u8ddf\u968f\u961f\u957f\u9000\u961f", None))
        self.chk_duiyuan_closetalk.setText(QCoreApplication.translate("WndMain", u"\u81ea\u52a8\u5173\u95ed\u5bf9\u8bdd\u6846", None))
        self.chk_duiyuan_js.setText(QCoreApplication.translate("WndMain", u"\u8ddf\u968f\u961f\u957f\u89e3\u53cc", None))
        self.chk_duiyuan_ds.setText(QCoreApplication.translate("WndMain", u"\u8ddf\u968f\u961f\u957f\u51bb\u53cc", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("WndMain", u"\u9886\u53d6\u53cc\u500d", None))
        self.label_17.setText(QCoreApplication.translate("WndMain", u"\u65f6\u95f4", None))
        self.cmb_double_time.setItemText(0, QCoreApplication.translate("WndMain", u"1\u5c0f\u65f6", None))
        self.cmb_double_time.setItemText(1, QCoreApplication.translate("WndMain", u"2\u5c0f\u65f6", None))
        self.cmb_double_time.setItemText(2, QCoreApplication.translate("WndMain", u"4\u5c0f\u65f6", None))

        self.groupBox_21.setTitle(QCoreApplication.translate("WndMain", u"\u8fb9\u5883\u6551\u63f4", None))
        self.label_58.setText(QCoreApplication.translate("WndMain", u"\u6b21\u6570", None))
#if QT_CONFIG(tooltip)
        self.edt_bianjing_num.setToolTip(QCoreApplication.translate("WndMain", u"\u8bf7\u8f93\u51650-999\u4e4b\u95f4\u7684\u6570\u5b57", None))
#endif // QT_CONFIG(tooltip)
        self.edt_bianjing_num.setText(QCoreApplication.translate("WndMain", u"3", None))
        self.groupBox.setTitle(QCoreApplication.translate("WndMain", u"\u5e26\u961f\u6253\u91ce", None))
        self.label_4.setText(QCoreApplication.translate("WndMain", u"\u5730\u56fe", None))
        self.cmb_daye_map.setItemText(0, QCoreApplication.translate("WndMain", u"\u5f53\u524d\u5730\u56fe", None))
        self.cmb_daye_map.setItemText(1, QCoreApplication.translate("WndMain", u"\u9752\u6cb3\u9547\u5916", None))
        self.cmb_daye_map.setItemText(2, QCoreApplication.translate("WndMain", u"\u957f\u5b89\u57ce\u5916", None))
        self.cmb_daye_map.setItemText(3, QCoreApplication.translate("WndMain", u"\u5927\u5510\u56fd\u5883", None))
        self.cmb_daye_map.setItemText(4, QCoreApplication.translate("WndMain", u"\u5927\u5510\u5883\u5916", None))
        self.cmb_daye_map.setItemText(5, QCoreApplication.translate("WndMain", u"\u5927\u96c1\u5854\u4e00\u5c42", None))
        self.cmb_daye_map.setItemText(6, QCoreApplication.translate("WndMain", u"\u5927\u96c1\u5854\u4e8c\u5c42", None))
        self.cmb_daye_map.setItemText(7, QCoreApplication.translate("WndMain", u"\u5927\u96c1\u5854\u4e09\u5c42", None))
        self.cmb_daye_map.setItemText(8, QCoreApplication.translate("WndMain", u"\u5927\u96c1\u5854\u56db\u5c42", None))
        self.cmb_daye_map.setItemText(9, QCoreApplication.translate("WndMain", u"\u5927\u96c1\u5854\u4e94\u5c42", None))
        self.cmb_daye_map.setItemText(10, QCoreApplication.translate("WndMain", u"\u5927\u96c1\u5854\u516d\u5c42", None))
        self.cmb_daye_map.setItemText(11, QCoreApplication.translate("WndMain", u"\u4e4c\u65af\u85cf", None))
        self.cmb_daye_map.setItemText(12, QCoreApplication.translate("WndMain", u"\u82b1\u679c\u5c71", None))
        self.cmb_daye_map.setItemText(13, QCoreApplication.translate("WndMain", u"\u6606\u4ed1\u5c71", None))
        self.cmb_daye_map.setItemText(14, QCoreApplication.translate("WndMain", u"\u4e1c\u6d77\u8ff7\u5bab\u4e00\u5c42", None))
        self.cmb_daye_map.setItemText(15, QCoreApplication.translate("WndMain", u"\u4e1c\u6d77\u8ff7\u5bab\u4e8c\u5c42", None))
        self.cmb_daye_map.setItemText(16, QCoreApplication.translate("WndMain", u"\u4e1c\u6d77\u8ff7\u5bab\u4e09\u5c42", None))
        self.cmb_daye_map.setItemText(17, QCoreApplication.translate("WndMain", u"\u5730\u72f1\u8ff7\u5bab\u4e00\u5c42", None))
        self.cmb_daye_map.setItemText(18, QCoreApplication.translate("WndMain", u"\u5730\u72f1\u8ff7\u5bab\u4e8c\u5c42", None))
        self.cmb_daye_map.setItemText(19, QCoreApplication.translate("WndMain", u"\u5730\u72f1\u8ff7\u5bab\u4e09\u5c42", None))
        self.cmb_daye_map.setItemText(20, QCoreApplication.translate("WndMain", u"\u5317\u51a5", None))
        self.cmb_daye_map.setItemText(21, QCoreApplication.translate("WndMain", u"\u7409\u7483\u591a\u5b9d\u5854\u4e00\u5c42", None))
        self.cmb_daye_map.setItemText(22, QCoreApplication.translate("WndMain", u"\u7409\u7483\u591a\u5b9d\u5854\u4e8c\u5c42", None))
        self.cmb_daye_map.setItemText(23, QCoreApplication.translate("WndMain", u"\u7409\u7483\u591a\u5b9d\u5854\u4e09\u5c42", None))
        self.cmb_daye_map.setItemText(24, QCoreApplication.translate("WndMain", u"\u5bd2\u51b0\u5bab\u4e00\u5c42", None))
        self.cmb_daye_map.setItemText(25, QCoreApplication.translate("WndMain", u"\u5bd2\u51b0\u5bab\u4e8c\u5c42", None))
        self.cmb_daye_map.setItemText(26, QCoreApplication.translate("WndMain", u"\u5bd2\u51b0\u5bab\u4e09\u5c42", None))
        self.cmb_daye_map.setItemText(27, QCoreApplication.translate("WndMain", u"\u6c34\u5e18\u6d1e", None))
        self.cmb_daye_map.setItemText(28, QCoreApplication.translate("WndMain", u"\u795e\u5f03\u5e73\u539f", None))
        self.cmb_daye_map.setItemText(29, QCoreApplication.translate("WndMain", u"\u4e1c\u6d77\u5e7b\u5883", None))
        self.cmb_daye_map.setItemText(30, QCoreApplication.translate("WndMain", u"\u5e7f\u5bd2\u5bab", None))
        self.cmb_daye_map.setItemText(31, QCoreApplication.translate("WndMain", u"\u5b50\u6bcd\u6cb3\u7554", None))
        self.cmb_daye_map.setItemText(32, QCoreApplication.translate("WndMain", u"\u6843\u82b1\u5c9b", None))
        self.cmb_daye_map.setItemText(33, QCoreApplication.translate("WndMain", u"\u7075\u5251\u5cf0", None))
        self.cmb_daye_map.setItemText(34, QCoreApplication.translate("WndMain", u"\u4e0a\u53e4\u6218\u573a", None))
        self.cmb_daye_map.setItemText(35, QCoreApplication.translate("WndMain", u"\u5e73\u9876\u5c71", None))

        self.label_5.setText(QCoreApplication.translate("WndMain", u"\u65f6\u95f4", None))
#if QT_CONFIG(tooltip)
        self.edt_daye_time.setToolTip(QCoreApplication.translate("WndMain", u"\u8bf7\u8f93\u51650-999\u4e4b\u95f4\u7684\u6570\u5b57", None))
#endif // QT_CONFIG(tooltip)
        self.edt_daye_time.setText(QCoreApplication.translate("WndMain", u"600", None))
        self.label_6.setText(QCoreApplication.translate("WndMain", u"\u5206\u949f", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("WndMain", u"\u5e26\u961f\u6349\u9b3c", None))
        self.label_16.setText(QCoreApplication.translate("WndMain", u"\u6b21\u6570", None))
#if QT_CONFIG(tooltip)
        self.edt_zhuogui_num.setToolTip(QCoreApplication.translate("WndMain", u"\u8bf7\u8f93\u51650-999\u4e4b\u95f4\u7684\u6570\u5b57", None))
#endif // QT_CONFIG(tooltip)
        self.edt_zhuogui_num.setText(QCoreApplication.translate("WndMain", u"40", None))
        self.chk_zhuogui_qn.setText(QCoreApplication.translate("WndMain", u"\u6253\u5343\u5e74\u8001\u5996", None))
        self.groupBox_23.setTitle(QCoreApplication.translate("WndMain", u"\u5e26\u961f\u5c01\u5996", None))
        self.label_61.setText(QCoreApplication.translate("WndMain", u"\u5730\u56fe", None))
        self.cmb_fengyao_map.setItemText(0, QCoreApplication.translate("WndMain", u"\u9752\u6cb3\u9547\u5916", None))
        self.cmb_fengyao_map.setItemText(1, QCoreApplication.translate("WndMain", u"\u957f\u5b89\u57ce\u5916", None))
        self.cmb_fengyao_map.setItemText(2, QCoreApplication.translate("WndMain", u"\u5927\u5510\u56fd\u5883", None))
        self.cmb_fengyao_map.setItemText(3, QCoreApplication.translate("WndMain", u"\u4e4c\u65af\u85cf", None))
        self.cmb_fengyao_map.setItemText(4, QCoreApplication.translate("WndMain", u"\u6606\u4ed1\u5c71", None))
        self.cmb_fengyao_map.setItemText(5, QCoreApplication.translate("WndMain", u"\u5730\u72f1\u8ff7\u5bab\u4e00\u5c42", None))
        self.cmb_fengyao_map.setItemText(6, QCoreApplication.translate("WndMain", u"\u5730\u72f1\u8ff7\u5bab\u4e09\u5c42", None))
        self.cmb_fengyao_map.setItemText(7, QCoreApplication.translate("WndMain", u"\u5317\u51a5", None))
        self.cmb_fengyao_map.setItemText(8, QCoreApplication.translate("WndMain", u"\u7409\u7483\u591a\u5b9d\u5854\u4e8c\u5c42", None))
        self.cmb_fengyao_map.setItemText(9, QCoreApplication.translate("WndMain", u"\u5bd2\u51b0\u5bab\u4e00\u5c42", None))
        self.cmb_fengyao_map.setItemText(10, QCoreApplication.translate("WndMain", u"\u795e\u5f03\u5e73\u539f", None))
        self.cmb_fengyao_map.setItemText(11, QCoreApplication.translate("WndMain", u"\u4e1c\u6d77\u5e7b\u5883", None))
        self.cmb_fengyao_map.setItemText(12, QCoreApplication.translate("WndMain", u"\u5b50\u6bcd\u6cb3\u7554", None))

        self.label_62.setText(QCoreApplication.translate("WndMain", u"\u6b21\u6570", None))
#if QT_CONFIG(tooltip)
        self.edt_fengyao_num.setToolTip(QCoreApplication.translate("WndMain", u"\u8bf7\u8f93\u51650-999\u4e4b\u95f4\u7684\u6570\u5b57", None))
#endif // QT_CONFIG(tooltip)
        self.edt_fengyao_num.setText(QCoreApplication.translate("WndMain", u"30", None))
        self.groupBox_11.setTitle(QCoreApplication.translate("WndMain", u"\u5e26\u961f\u526f\u672c \u6df7\u961f\u526f\u672c", None))
        self.label_50.setText(QCoreApplication.translate("WndMain", u"\u526f\u672c1", None))
        self.cmb_fb1.setItemText(0, QCoreApplication.translate("WndMain", u"\u5929\u84ec\u5a36\u4eb2", None))
        self.cmb_fb1.setItemText(1, QCoreApplication.translate("WndMain", u"\u767d\u9f99\u95f9\u6d77", None))
        self.cmb_fb1.setItemText(2, QCoreApplication.translate("WndMain", u"\u5730\u5e9c\u6551\u7334\u738b", None))
        self.cmb_fb1.setItemText(3, QCoreApplication.translate("WndMain", u"\u4e09\u6253\u767d\u9aa8\u7cbe", None))
        self.cmb_fb1.setItemText(4, QCoreApplication.translate("WndMain", u"\u7384\u6b66\u95e8\u4e4b\u53d8", None))
        self.cmb_fb1.setItemText(5, QCoreApplication.translate("WndMain", u"\u795e\u9b54\u524d\u7ebf", None))
        self.cmb_fb1.setItemText(6, QCoreApplication.translate("WndMain", u"\u5929\u4eba\u56db\u52ab\u9635", None))
        self.cmb_fb1.setItemText(7, QCoreApplication.translate("WndMain", u"\u6d2a\u8352\u6218\u573a", None))
        self.cmb_fb1.setItemText(8, QCoreApplication.translate("WndMain", u"\u5251\u8d77\u65e0\u540d", None))

        self.cmb_fb1_num.setItemText(0, QCoreApplication.translate("WndMain", u"0", None))
        self.cmb_fb1_num.setItemText(1, QCoreApplication.translate("WndMain", u"1", None))
        self.cmb_fb1_num.setItemText(2, QCoreApplication.translate("WndMain", u"2", None))
        self.cmb_fb1_num.setItemText(3, QCoreApplication.translate("WndMain", u"3", None))
        self.cmb_fb1_num.setItemText(4, QCoreApplication.translate("WndMain", u"4", None))

        self.label_51.setText(QCoreApplication.translate("WndMain", u"\u526f\u672c2", None))
        self.cmb_fb2.setItemText(0, QCoreApplication.translate("WndMain", u"\u5929\u84ec\u5a36\u4eb2", None))
        self.cmb_fb2.setItemText(1, QCoreApplication.translate("WndMain", u"\u767d\u9f99\u95f9\u6d77", None))
        self.cmb_fb2.setItemText(2, QCoreApplication.translate("WndMain", u"\u5730\u5e9c\u6551\u7334\u738b", None))
        self.cmb_fb2.setItemText(3, QCoreApplication.translate("WndMain", u"\u4e09\u6253\u767d\u9aa8\u7cbe", None))
        self.cmb_fb2.setItemText(4, QCoreApplication.translate("WndMain", u"\u7384\u6b66\u95e8\u4e4b\u53d8", None))
        self.cmb_fb2.setItemText(5, QCoreApplication.translate("WndMain", u"\u795e\u9b54\u524d\u7ebf", None))
        self.cmb_fb2.setItemText(6, QCoreApplication.translate("WndMain", u"\u5929\u4eba\u56db\u52ab\u9635", None))
        self.cmb_fb2.setItemText(7, QCoreApplication.translate("WndMain", u"\u6d2a\u8352\u6218\u573a", None))
        self.cmb_fb2.setItemText(8, QCoreApplication.translate("WndMain", u"\u5251\u8d77\u65e0\u540d", None))

        self.cmb_fb2_num.setItemText(0, QCoreApplication.translate("WndMain", u"0", None))
        self.cmb_fb2_num.setItemText(1, QCoreApplication.translate("WndMain", u"1", None))
        self.cmb_fb2_num.setItemText(2, QCoreApplication.translate("WndMain", u"2", None))
        self.cmb_fb2_num.setItemText(3, QCoreApplication.translate("WndMain", u"3", None))
        self.cmb_fb2_num.setItemText(4, QCoreApplication.translate("WndMain", u"4", None))

        self.groupBox_27.setTitle(QCoreApplication.translate("WndMain", u"\u86ee\u6d1e\u5bc6\u4ee4", None))
        self.label_65.setText(QCoreApplication.translate("WndMain", u"\u6b21\u6570", None))
#if QT_CONFIG(tooltip)
        self.edt_mandong_num.setToolTip(QCoreApplication.translate("WndMain", u"\u8bf7\u8f93\u51650-999\u4e4b\u95f4\u7684\u6570\u5b57", None))
#endif // QT_CONFIG(tooltip)
        self.edt_mandong_num.setText(QCoreApplication.translate("WndMain", u"5", None))
        self.tab_set.setTabText(self.tab_set.indexOf(self.tab_6), QCoreApplication.translate("WndMain", u"\u7ec4\u961f\u76f8\u5173", None))
        self.btn_main_read.setText(QCoreApplication.translate("WndMain", u"\u8bfb \u53d6", None))
        self.btn_main_save.setText(QCoreApplication.translate("WndMain", u"\u4fdd \u5b58", None))
        self.tool_bar.setWindowTitle(QCoreApplication.translate("WndMain", u"toolBar", None))
    # retranslateUi

