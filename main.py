from threading import Thread
from PySide2.QtWidgets import QApplication
from PySide2.QtCore import Qt

from utils.com import create_com_obj, reg_com_to_system
from utils.log import log
from utils.plugin import Lw, Dm, COM_NAME, pass_dm_vip
import settings
from wnd_main_code import WndMain

if __name__ == '__main__':
    import sys
    from PySide2.QtWidgets import QStyleFactory
    # 注册com组件到系统
    reg_com_to_system(COM_NAME)
    # 创建com原生对象
    ori_obj = create_com_obj(COM_NAME)
    # 把 原生对象 再封装一层, 以统一不同插件接口函数名
    if COM_NAME == Dm.COM_NAME:
        com_obj = Dm(ori_obj)
        pass_dm_vip(com_obj)
        # Thread(target=pass_dm_vip, args=[com_obj], daemon=True).start()
    else:
        com_obj = Lw(ori_obj)
    # 界面随DPI自动缩放
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    app = QApplication()
    app.setStyle(QStyleFactory.create("fusion"))
    log.info("初始化界面样式完成")
    settings.wnd_main = WndMain()
    settings.wnd_main.show()
    sys.exit(app.exec_())
