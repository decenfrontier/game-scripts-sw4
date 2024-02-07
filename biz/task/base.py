import common

class TaskBase():
    def __init__(self, wk: common.Worker, task_name: str) -> None:
        self.task_name = task_name

    def before_run(self, wk: common.Worker):
        # 每执行一个任务前, 都重置任务类型和完成次数
        wk.cur_task, wk.sub_task = "", ""
        wk.done_count = 0
        # 在战斗就等战斗结束
        if common.is_fight(wk):
            common.fight_operation(wk)
        # 每执行一个任务前, 都关闭所有界面
        common.close_all_sub_wnd(wk)
        common.close_talk(wk)
        wk.cur_task = self.task_name
        wk.record(f"开始执行")

    def run(self, wk: common.Worker):
        raise Exception("子类必须实现该方法")

    def after_run(self, wk: common.Worker):
        wk.record("执行完成")

    def cfg_save(self, wk: common.Worker):
        pass

    def cfg_load(self, wk: common.Worker):
        pass