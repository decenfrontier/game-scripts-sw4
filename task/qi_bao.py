import lib
import cm

def 旗包任务(wk: cm.Worker):
    wk.cur_task = "[旗包]"
    cm.team.set_leader_task(wk, wk.cur_task)
    wk.record("开始执行")

    while wk.done_count < 3:
        task_type = cm.sub_task(wk)
        if task_type == "接任务":
            goto_accept_task(wk)
        elif task_type == "打听消息":
            da_ting_xiao_xi(wk)
        elif task_type == "消灭盗贼":
            xiao_mie_dao_zei(wk)
        lib.msleep(800)

    cm.team.set_leader_task(wk)


def goto_accept_task(wk):
    if cm.schedule_query_cur_task_done_count(wk, 3):
        return

    wk.record("正在接任务...")
    cm.use_fei_xing_qi(wk, "长安城", cm.FLAG_RECT["捉鬼"])

    for i in range(10):
        if cm.is_talk_open(wk):
            break
        if not wk.is_find_way:
            x, y = cm.NPC_POS_WND["玄义"]
            cm.click_map_wnd_pos(wk, x, y)
        lib.msleep(500)
    if cm.is_talk_open(wk):  # 若对话打开
        cm.click_talk_specify_item(wk, "接旗包")
        cm.is_task_over(wk, 300)
        cm.close_talk(wk)
        cm.set_task_to_cur_task_bar(wk)

def da_ting_xiao_xi(wk: cm.Worker):
    wk.record("任务类型: 打听消息")
    cm.fly_task_map_fight(wk)

def xiao_mie_dao_zei(wk: cm.Worker):
    wk.record("任务类型: 消灭盗贼")
    cm.fly_task_map_fight(wk)
