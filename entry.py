import sys, os
import socket
import webbrowser

from PySide2.QtGui import QIcon, QCloseEvent, QRegExpValidator, QPixmap, \
    QMouseEvent, QPaintEvent, QPainter, QBitmap
from PySide2.QtWidgets import QDialog, QLabel, QMessageBox, QToolBar, QVBoxLayout, \
    QStatusBar, QApplication, QStyleFactory, QLineEdit, QPushButton
from PySide2.QtCore import Qt, QRegExp, QSize, QPoint, Signal, QObject, QEvent

import wnd_login_rc
from ui.wnd_login import Ui_WndLogin
from wnd_main_code import WndMain
import lib, crypto
from lib import rnd
import wnd_login_code

if not __name__ != '__main__':
    wnd_login_code()