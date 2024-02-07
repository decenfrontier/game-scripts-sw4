import lib
import common

def 带队打野(wk: common.Worker):
    wk.cur_task = "[打野]"
    common.team.set_leader_task(wk, wk.cur_task)
    wk.record("开始执行")

    daye_map = lib.cfg_main["打野地图"]
    # 若不在设定地图,则先飞到打野地图
    if daye_map != "当前地图" and common.cur_map(wk) != daye_map:
        common.use_qu_mo_xiang(wk)
        wk.record(f"正在前往打野地图:{daye_map}")
        common.fly_to_map(wk, daye_map)
    common.cancel_qu_mo_xiang(wk)  # 取消驱魔香

    daye_time = common.get_cur_task_specify_count(wk)
    wk.record(f"打野开始,设定持续时间为:{daye_time}分钟")
    # 打野开始时间, 经历战斗次数
    start_time, fight_count = lib.cur_time_stamp, 0
    while wk.done_count < daye_time:
        common.walk_around_until_fight(wk)  # 四处寻路遇怪
        if common.is_fight(wk):  # 战斗中
            common.fight_operation(wk)
            fight_count += 1
            wk.done_count = lib.delta_minute(start_time, lib.cur_time_stamp)
            daye_time = common.get_cur_task_specify_count(wk)  # 重新读取, 允许中途改变
            wk.record(f"已遇暗雷怪{fight_count}次,已完成{wk.done_count}/{daye_time}")
        if common.cur_map(wk) == "幽冥地府":  # 若战斗失败, 人物死亡, 会自动飞到地图幽冥地府
            wk.record("人物已死亡,自动跳过此任务")
            break

    common.team.set_leader_task(wk)
