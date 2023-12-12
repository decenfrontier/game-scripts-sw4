# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'wnd_login.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_WndLogin(object):
    def setupUi(self, WndLogin):
        if not WndLogin.objectName():
            WndLogin.setObjectName(u"WndLogin")
        WndLogin.resize(456, 307)
        WndLogin.setStyleSheet(u"    * {\n"
"        font-size: 12px;\n"
"        font-family: \"Microsoft YaHei\";\n"
"    }\n"
"    QTableView {\n"
"        selection-color: #000000;\n"
"	    selection-background-color: #c4e1d2; \n"
"    }\n"
"    QTableView::item:hover	{	\n"
"	    background-color: #a1b1c9;		\n"
"    }")
        WndLogin.setSizeGripEnabled(False)
        WndLogin.setModal(False)
        self.stack_widget = QStackedWidget(WndLogin)
        self.stack_widget.setObjectName(u"stack_widget")
        self.stack_widget.setGeometry(QRect(0, 0, 456, 311))
        self.page_login = QWidget()
        self.page_login.setObjectName(u"page_login")
        self.gridLayout_13 = QGridLayout(self.page_login)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.gridLayout_13.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(self.page_login)
        self.widget.setObjectName(u"widget")
        self.gridLayout_6 = QGridLayout(self.widget)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.verticalSpacer = QSpacerItem(20, 81, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_6.addItem(self.verticalSpacer, 0, 1, 1, 1)

        self.horizontalSpacer_9 = QSpacerItem(75, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacer_9, 1, 0, 1, 1)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.edt_login_account = QLineEdit(self.widget)
        self.edt_login_account.setObjectName(u"edt_login_account")

        self.gridLayout_2.addWidget(self.edt_login_account, 0, 1, 1, 1)

        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1)

        self.edt_login_pwd = QLineEdit(self.widget)
        self.edt_login_pwd.setObjectName(u"edt_login_pwd")
        self.edt_login_pwd.setEchoMode(QLineEdit.Password)

        self.gridLayout_2.addWidget(self.edt_login_pwd, 1, 1, 1, 1)

        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")

        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)


        self.verticalLayout_3.addLayout(self.gridLayout_2)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalSpacer_3 = QSpacerItem(30, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_3, 0, 0, 2, 1)

        self.chk_login_update = QCheckBox(self.widget)
        self.chk_login_update.setObjectName(u"chk_login_update")
        self.chk_login_update.setChecked(True)

        self.gridLayout.addWidget(self.chk_login_update, 0, 1, 1, 2)

        self.chk_login_remember = QCheckBox(self.widget)
        self.chk_login_remember.setObjectName(u"chk_login_remember")
        self.chk_login_remember.setChecked(True)

        self.gridLayout.addWidget(self.chk_login_remember, 0, 3, 1, 2)

        self.btn_login = QPushButton(self.widget)
        self.btn_login.setObjectName(u"btn_login")
        self.btn_login.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.btn_login, 1, 1, 1, 1)

        self.btn_unbind = QPushButton(self.widget)
        self.btn_unbind.setObjectName(u"btn_unbind")
        self.btn_unbind.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.btn_unbind, 1, 2, 1, 2)

        self.btn_exit = QPushButton(self.widget)
        self.btn_exit.setObjectName(u"btn_exit")
        self.btn_exit.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.btn_exit, 1, 4, 1, 1)


        self.verticalLayout_3.addLayout(self.gridLayout)


        self.gridLayout_6.addLayout(self.verticalLayout_3, 1, 1, 1, 1)

        self.horizontalSpacer_10 = QSpacerItem(74, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacer_10, 1, 2, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 80, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_6.addItem(self.verticalSpacer_2, 2, 1, 1, 1)


        self.gridLayout_13.addWidget(self.widget, 0, 0, 1, 1)

        self.stack_widget.addWidget(self.page_login)
        self.page_reg = QWidget()
        self.page_reg.setObjectName(u"page_reg")
        self.gridLayout_10 = QGridLayout(self.page_reg)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.gridLayout_10.setContentsMargins(0, 0, 0, 0)
        self.widget_2 = QWidget(self.page_reg)
        self.widget_2.setObjectName(u"widget_2")
        self.gridLayout_7 = QGridLayout(self.widget_2)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.horizontalSpacer_11 = QSpacerItem(63, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_7.addItem(self.horizontalSpacer_11, 1, 0, 1, 1)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.edt_reg_account = QLineEdit(self.widget_2)
        self.edt_reg_account.setObjectName(u"edt_reg_account")

        self.gridLayout_3.addWidget(self.edt_reg_account, 0, 1, 1, 1)

        self.edt_reg_pwd = QLineEdit(self.widget_2)
        self.edt_reg_pwd.setObjectName(u"edt_reg_pwd")

        self.gridLayout_3.addWidget(self.edt_reg_pwd, 1, 1, 1, 1)

        self.edt_reg_key = QLineEdit(self.widget_2)
        self.edt_reg_key.setObjectName(u"edt_reg_key")

        self.gridLayout_3.addWidget(self.edt_reg_key, 3, 1, 1, 1)

        self.label_6 = QLabel(self.widget_2)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_3.addWidget(self.label_6, 1, 0, 1, 1)

        self.label_5 = QLabel(self.widget_2)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_3.addWidget(self.label_5, 0, 0, 1, 1)

        self.edt_reg_qq = QLineEdit(self.widget_2)
        self.edt_reg_qq.setObjectName(u"edt_reg_qq")

        self.gridLayout_3.addWidget(self.edt_reg_qq, 2, 1, 1, 1)

        self.label_3 = QLabel(self.widget_2)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_3.addWidget(self.label_3, 2, 0, 1, 1)

        self.label_4 = QLabel(self.widget_2)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_3.addWidget(self.label_4, 3, 0, 1, 1)

        self.edt_reg_recmd = QLineEdit(self.widget_2)
        self.edt_reg_recmd.setObjectName(u"edt_reg_recmd")

        self.gridLayout_3.addWidget(self.edt_reg_recmd, 4, 1, 1, 1)

        self.label_7 = QLabel(self.widget_2)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_3.addWidget(self.label_7, 4, 0, 1, 1)


        self.gridLayout_7.addLayout(self.gridLayout_3, 1, 1, 1, 3)

        self.horizontalSpacer_12 = QSpacerItem(62, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_7.addItem(self.horizontalSpacer_12, 1, 4, 1, 1)

        self.horizontalSpacer_5 = QSpacerItem(53, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_7.addItem(self.horizontalSpacer_5, 2, 1, 1, 1)

        self.btn_reg = QPushButton(self.widget_2)
        self.btn_reg.setObjectName(u"btn_reg")
        self.btn_reg.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_7.addWidget(self.btn_reg, 2, 2, 1, 1)

        self.horizontalSpacer_6 = QSpacerItem(53, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_7.addItem(self.horizontalSpacer_6, 2, 3, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 55, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_7.addItem(self.verticalSpacer_3, 0, 2, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 54, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_7.addItem(self.verticalSpacer_4, 3, 2, 1, 1)


        self.gridLayout_10.addWidget(self.widget_2, 0, 0, 1, 1)

        self.stack_widget.addWidget(self.page_reg)
        self.page_pay = QWidget()
        self.page_pay.setObjectName(u"page_pay")
        self.gridLayout_11 = QGridLayout(self.page_pay)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.gridLayout_11.setContentsMargins(0, 0, 0, 0)
        self.widget_3 = QWidget(self.page_pay)
        self.widget_3.setObjectName(u"widget_3")
        self.gridLayout_8 = QGridLayout(self.widget_3)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.verticalSpacer_5 = QSpacerItem(20, 62, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_8.addItem(self.verticalSpacer_5, 0, 2, 1, 1)

        self.horizontalSpacer_13 = QSpacerItem(74, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_8.addItem(self.horizontalSpacer_13, 1, 0, 1, 1)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.label_13 = QLabel(self.widget_3)
        self.label_13.setObjectName(u"label_13")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_13)

        self.edt_pay_account = QLineEdit(self.widget_3)
        self.edt_pay_account.setObjectName(u"edt_pay_account")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.edt_pay_account)

        self.lbe_pay_key = QLabel(self.widget_3)
        self.lbe_pay_key.setObjectName(u"lbe_pay_key")
        self.lbe_pay_key.setOpenExternalLinks(True)
        self.lbe_pay_key.setTextInteractionFlags(Qt.LinksAccessibleByMouse)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.lbe_pay_key)

        self.edt_pay_key = QLineEdit(self.widget_3)
        self.edt_pay_key.setObjectName(u"edt_pay_key")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.edt_pay_key)


        self.gridLayout_8.addLayout(self.formLayout, 1, 1, 1, 3)

        self.horizontalSpacer_14 = QSpacerItem(73, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_8.addItem(self.horizontalSpacer_14, 1, 4, 1, 1)

        self.horizontalSpacer_7 = QSpacerItem(82, 17, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_8.addItem(self.horizontalSpacer_7, 2, 1, 1, 1)

        self.btn_pay = QPushButton(self.widget_3)
        self.btn_pay.setObjectName(u"btn_pay")
        self.btn_pay.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_8.addWidget(self.btn_pay, 2, 2, 1, 1)

        self.horizontalSpacer_8 = QSpacerItem(81, 17, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_8.addItem(self.horizontalSpacer_8, 2, 3, 1, 1)

        self.verticalSpacer_6 = QSpacerItem(20, 61, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_8.addItem(self.verticalSpacer_6, 3, 2, 1, 1)


        self.gridLayout_11.addWidget(self.widget_3, 0, 0, 1, 1)

        self.stack_widget.addWidget(self.page_pay)
        self.page_modify = QWidget()
        self.page_modify.setObjectName(u"page_modify")
        self.gridLayout_16 = QGridLayout(self.page_modify)
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.gridLayout_16.setContentsMargins(0, 0, 0, 0)
        self.widget_4 = QWidget(self.page_modify)
        self.widget_4.setObjectName(u"widget_4")
        self.gridLayout_4 = QGridLayout(self.widget_4)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.verticalSpacer_7 = QSpacerItem(20, 68, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_4.addItem(self.verticalSpacer_7, 0, 2, 1, 1)

        self.horizontalSpacer_15 = QSpacerItem(69, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_15, 1, 0, 1, 1)

        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.label_10 = QLabel(self.widget_4)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout_5.addWidget(self.label_10, 0, 0, 1, 1)

        self.edt_modify_account = QLineEdit(self.widget_4)
        self.edt_modify_account.setObjectName(u"edt_modify_account")

        self.gridLayout_5.addWidget(self.edt_modify_account, 0, 1, 1, 1)

        self.label_12 = QLabel(self.widget_4)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout_5.addWidget(self.label_12, 1, 0, 1, 1)

        self.edt_modify_qq = QLineEdit(self.widget_4)
        self.edt_modify_qq.setObjectName(u"edt_modify_qq")

        self.gridLayout_5.addWidget(self.edt_modify_qq, 1, 1, 1, 1)

        self.label_11 = QLabel(self.widget_4)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout_5.addWidget(self.label_11, 2, 0, 1, 1)

        self.edt_modify_new_pwd = QLineEdit(self.widget_4)
        self.edt_modify_new_pwd.setObjectName(u"edt_modify_new_pwd")

        self.gridLayout_5.addWidget(self.edt_modify_new_pwd, 2, 1, 1, 1)


        self.gridLayout_4.addLayout(self.gridLayout_5, 1, 1, 1, 3)

        self.horizontalSpacer_16 = QSpacerItem(68, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_16, 1, 4, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(47, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_2, 2, 1, 1, 1)

        self.btn_modify = QPushButton(self.widget_4)
        self.btn_modify.setObjectName(u"btn_modify")
        self.btn_modify.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_4.addWidget(self.btn_modify, 2, 2, 1, 1)

        self.horizontalSpacer = QSpacerItem(47, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer, 2, 3, 1, 1)

        self.verticalSpacer_8 = QSpacerItem(20, 67, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_4.addItem(self.verticalSpacer_8, 3, 2, 1, 1)


        self.gridLayout_16.addWidget(self.widget_4, 0, 0, 1, 1)

        self.stack_widget.addWidget(self.page_modify)
        self.page_notice = QWidget()
        self.page_notice.setObjectName(u"page_notice")
        self.gridLayout_9 = QGridLayout(self.page_notice)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_9.setVerticalSpacing(0)
        self.lbe_notice = QLabel(self.page_notice)
        self.lbe_notice.setObjectName(u"lbe_notice")
        self.lbe_notice.setContextMenuPolicy(Qt.CustomContextMenu)
        self.lbe_notice.setAlignment(Qt.AlignCenter)
        self.lbe_notice.setOpenExternalLinks(True)
        self.lbe_notice.setTextInteractionFlags(Qt.LinksAccessibleByMouse)

        self.gridLayout_9.addWidget(self.lbe_notice, 0, 1, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_9.addItem(self.horizontalSpacer_4, 1, 0, 1, 1)

        self.horizontalSpacer_17 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_9.addItem(self.horizontalSpacer_17, 1, 2, 1, 1)

        self.tbr_notice = QTextBrowser(self.page_notice)
        self.tbr_notice.setObjectName(u"tbr_notice")
        self.tbr_notice.setMinimumSize(QSize(300, 0))

        self.gridLayout_9.addWidget(self.tbr_notice, 1, 1, 1, 1)

        self.gridLayout_9.setRowStretch(0, 1)
        self.gridLayout_9.setRowStretch(1, 8)
        self.stack_widget.addWidget(self.page_notice)
#if QT_CONFIG(shortcut)
        self.label_2.setBuddy(self.edt_login_pwd)
        self.label.setBuddy(self.edt_login_account)
#endif // QT_CONFIG(shortcut)
        QWidget.setTabOrder(self.edt_login_account, self.edt_login_pwd)
        QWidget.setTabOrder(self.edt_login_pwd, self.btn_login)
        QWidget.setTabOrder(self.btn_login, self.btn_unbind)
        QWidget.setTabOrder(self.btn_unbind, self.btn_exit)
        QWidget.setTabOrder(self.btn_exit, self.edt_reg_account)
        QWidget.setTabOrder(self.edt_reg_account, self.edt_reg_pwd)
        QWidget.setTabOrder(self.edt_reg_pwd, self.edt_reg_qq)
        QWidget.setTabOrder(self.edt_reg_qq, self.btn_reg)
        QWidget.setTabOrder(self.btn_reg, self.edt_pay_account)
        QWidget.setTabOrder(self.edt_pay_account, self.edt_pay_key)
        QWidget.setTabOrder(self.edt_pay_key, self.btn_pay)
        QWidget.setTabOrder(self.btn_pay, self.edt_modify_account)
        QWidget.setTabOrder(self.edt_modify_account, self.edt_modify_qq)
        QWidget.setTabOrder(self.edt_modify_qq, self.edt_modify_new_pwd)
        QWidget.setTabOrder(self.edt_modify_new_pwd, self.btn_modify)

        self.retranslateUi(WndLogin)

        self.stack_widget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(WndLogin)
    # setupUi

    def retranslateUi(self, WndLogin):
        WndLogin.setWindowTitle(QCoreApplication.translate("WndLogin", u"Login", None))
#if QT_CONFIG(tooltip)
        self.stack_widget.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.edt_login_account.setText("")
        self.label_2.setText(QCoreApplication.translate("WndLogin", u"\u5bc6\u7801:", None))
        self.edt_login_pwd.setText("")
        self.label.setText(QCoreApplication.translate("WndLogin", u"\u8d26\u53f7:", None))
        self.chk_login_update.setText(QCoreApplication.translate("WndLogin", u"\u63d0\u793a\u66f4\u65b0\u7248\u672c", None))
        self.chk_login_remember.setText(QCoreApplication.translate("WndLogin", u"\u8bb0\u4f4f\u8d26\u53f7\u5bc6\u7801", None))
#if QT_CONFIG(tooltip)
        self.btn_login.setToolTip(QCoreApplication.translate("WndLogin", u"\u9996\u6b21\u767b\u5f55\u6210\u529f\u540e\u5f00\u59cb\u8ba1\u65f6", None))
#endif // QT_CONFIG(tooltip)
        self.btn_login.setText(QCoreApplication.translate("WndLogin", u"\u767b \u5f55", None))
#if QT_CONFIG(tooltip)
        self.btn_unbind.setToolTip(QCoreApplication.translate("WndLogin", u"\u8f6f\u4ef6\u662f\u7ed1\u5b9a\u673a\u5668\u7684, \u53ef\u4ee5\u5f02\u673a\u89e3\u7ed1, \u6bcf\u5929\u6700\u591a4\u6b21", None))
#endif // QT_CONFIG(tooltip)
        self.btn_unbind.setText(QCoreApplication.translate("WndLogin", u"\u89e3 \u7ed1", None))
        self.btn_exit.setText(QCoreApplication.translate("WndLogin", u"\u9000 \u51fa", None))
#if QT_CONFIG(tooltip)
        self.edt_reg_account.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.edt_reg_account.setText("")
        self.edt_reg_account.setPlaceholderText(QCoreApplication.translate("WndLogin", u"\u5b57\u6bcd\u6570\u5b57\u7ec4\u5408, 6-12\u4f4d", None))
#if QT_CONFIG(tooltip)
        self.edt_reg_pwd.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.edt_reg_pwd.setText("")
        self.edt_reg_pwd.setPlaceholderText(QCoreApplication.translate("WndLogin", u"\u5b57\u6bcd\u6570\u5b57\u7ec4\u5408, 6-12\u4f4d", None))
#if QT_CONFIG(tooltip)
        self.edt_reg_key.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.edt_reg_key.setText("")
        self.edt_reg_key.setPlaceholderText(QCoreApplication.translate("WndLogin", u"\u65b0\u7528\u6237\u4ee5\u6708\u5361\u6ce8\u518c\u90012\u5929", None))
        self.label_6.setText(QCoreApplication.translate("WndLogin", u"\u5bc6\u7801:", None))
        self.label_5.setText(QCoreApplication.translate("WndLogin", u"\u8d26\u53f7:", None))
#if QT_CONFIG(tooltip)
        self.edt_reg_qq.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.edt_reg_qq.setInputMask("")
        self.edt_reg_qq.setText("")
        self.edt_reg_qq.setPlaceholderText(QCoreApplication.translate("WndLogin", u"\u7528\u4e8e\u4fee\u6539\u5bc6\u7801, \u8bf7\u7262\u8bb0", None))
        self.label_3.setText(QCoreApplication.translate("WndLogin", u"QQ:", None))
        self.label_4.setText(QCoreApplication.translate("WndLogin", u"\u5145\u503c\u5361:", None))
#if QT_CONFIG(tooltip)
        self.edt_reg_recmd.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.edt_reg_recmd.setText("")
        self.edt_reg_recmd.setPlaceholderText(QCoreApplication.translate("WndLogin", u"\u6ca1\u6709\u53ef\u4e0d\u586b, \u63a8\u8350\u4eba\u90012\u5929", None))
        self.label_7.setText(QCoreApplication.translate("WndLogin", u"\u63a8\u8350\u4eba\u8d26\u53f7:", None))
        self.btn_reg.setText(QCoreApplication.translate("WndLogin", u"\u6ce8 \u518c", None))
        self.label_13.setText(QCoreApplication.translate("WndLogin", u"\u8d26\u53f7:", None))
#if QT_CONFIG(tooltip)
        self.edt_pay_account.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.edt_pay_account.setText("")
        self.edt_pay_account.setPlaceholderText(QCoreApplication.translate("WndLogin", u"\u586b\u5199\u60a8\u6ce8\u518c\u7684\u8d26\u53f7", None))
#if QT_CONFIG(tooltip)
        self.lbe_pay_key.setToolTip(QCoreApplication.translate("WndLogin", u">> \u70b9\u6211\u8d2d\u5361 <<", None))
#endif // QT_CONFIG(tooltip)
        self.lbe_pay_key.setText(QCoreApplication.translate("WndLogin", u"\u5145\u503c\u5361:", None))
        self.edt_pay_key.setText("")
        self.edt_pay_key.setPlaceholderText(QCoreApplication.translate("WndLogin", u"\u7eed\u8d39\u6708\u5361\u9001 2+\u7d2f\u8ba1\u5145\u503c\u6708\u6570 \u5929", None))
        self.btn_pay.setText(QCoreApplication.translate("WndLogin", u"\u5145 \u503c", None))
        self.label_10.setText(QCoreApplication.translate("WndLogin", u"\u8d26\u53f7:", None))
#if QT_CONFIG(tooltip)
        self.edt_modify_account.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.edt_modify_account.setPlaceholderText(QCoreApplication.translate("WndLogin", u"\u5b57\u6bcd\u6570\u5b57\u7ec4\u5408, 6-12\u4f4d", None))
        self.label_12.setText(QCoreApplication.translate("WndLogin", u"QQ:", None))
#if QT_CONFIG(tooltip)
        self.edt_modify_qq.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.edt_modify_qq.setPlaceholderText(QCoreApplication.translate("WndLogin", u"\u8bf7\u8f93\u5165\u6ce8\u518c\u8d26\u53f7\u65f6\u9884\u7559\u7684QQ\u53f7", None))
        self.label_11.setText(QCoreApplication.translate("WndLogin", u"\u65b0\u5bc6\u7801:", None))
#if QT_CONFIG(tooltip)
        self.edt_modify_new_pwd.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.edt_modify_new_pwd.setPlaceholderText(QCoreApplication.translate("WndLogin", u"\u5b57\u6bcd\u6570\u5b57\u7ec4\u5408, 6-12\u4f4d", None))
        self.btn_modify.setText(QCoreApplication.translate("WndLogin", u"\u6539 \u5bc6", None))
#if QT_CONFIG(tooltip)
        self.lbe_notice.setToolTip(QCoreApplication.translate("WndLogin", u">> \u70b9\u6211\u66f4\u65b0 <<\n"
"\u63d0\u53d6\u7801: 5x5p", None))
#endif // QT_CONFIG(tooltip)
        self.lbe_notice.setText(QCoreApplication.translate("WndLogin", u"\u516c \u544a", None))
    # retranslateUi

