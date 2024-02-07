from PySide2.QtWidgets import QApplication
from PySide2.QtCore import Qt

from utils.com import create_com_obj, reg_com_to_system
from utils.log import Logger
from utils.plugin import Lw, Dm
import globals
from wnd_main_code import WndMain

if __name__ == '__main__':
    import sys
    from PySide2.QtWidgets import QStyleFactory
    # 创建log 对象
    log = Logger()
    # 注册com组件到系统
    if reg_com_to_system(globals.COM_NAME):
        log.info("注册com组件2到系统, 成功")
    else:
        log.info("注册com组件2到系统, 失败")

    # 创建com原生对象
    ori_obj = create_com_obj(globals.COM_NAME)
    # 把 原生对象 再封装一层, 以统一不同插件接口函数名
    com_obj = Lw(ori_obj) if globals.COM_NAME == Lw.COM_NAME else Dm(ori_obj)
    # 界面随DPI自动缩放
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    app = QApplication()
    app.setStyle(QStyleFactory.create("fusion"))
    globals.log.info("初始化界面样式完成")
    globals.wnd_main = WndMain()
    globals.wnd_main.show()
    sys.exit(app.exec_())
