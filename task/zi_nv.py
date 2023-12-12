import lib
import cm

MAX_COUNT_ZI_NV = 80


def 子女温饱(wk: cm.Worker):
    wk.cur_task = "[子女]"
    wk.record("开始执行")

    start_t = lib.cur_time_stamp
    for i in range(60):
        task_type = cm.sub_task(wk)
        if task_type == "接任务" and not goto_accept_task(wk):
            break
        elif task_type == "关注温饱":
            guan_zhu_wen_bao(wk)
        elif task_type == "完成":
            wan_cheng_wen_bao(wk)
        lib.msleep(800)
        if wk.done_count > 3:
            break


# 去接任务
def goto_accept_task(wk: cm.Worker):
    if not cm.bag_use_goods(wk, "物_乾坤镜.bmp"):
        cm.close_bag(wk)
        wk.record("背包里未发现乾坤镜!")
        return False
    lib.msleep(1200)
    if is_cur_wen_bao_reach_80(wk):
        wk.done_count += 1
        if wk.find_pic_click(*cm.RECT_FULL, "子女温饱度1.bmp"):
            wk.record("已切换到下一个子女")
    else:
        wk.find_pic_click(*cm.RECT_FULL, "关注温饱.bmp")
    cm.close_all_sub_wnd(wk)
    return True


# 是否当前子女温饱达到80
def is_cur_wen_bao_reach_80(wk: cm.Worker):
    x, y = wk.get_pic_pos(*cm.RECT_FULL, "子女温饱度2.bmp", timeout=300)
    if x < 0:
        wk.record("未找到子女温饱度")
        return False
    wen_bao = wk.ocr(x + 50, y-5, x + 80, y + 15, cm.COLOR_WHITE_BLUR, zk=cm.ZK_DIGIT_BLUR, sim=0.85)
    try:
        wen_bao = int(wen_bao)
        wk.record(f"当前子女温饱度: {wen_bao}/100")
    except:
        wen_bao = 0
        wk.record("未正确识别子女温饱度")
    if wen_bao >= 80:
        return True
    return False


# 关注温饱
def guan_zhu_wen_bao(wk: cm.Worker):
    wk.record("任务类型: 关注温饱")
    cm.buy_task_need_goods(wk)


# 关注温饱完成
def wan_cheng_wen_bao(wk: cm.Worker):
    wk.record("任务类型: 关注温饱完成")
    if not cm.bag_use_goods(wk, "物_乾坤镜.bmp"):
        cm.close_bag(wk)
        return
    lib.msleep(600)
    wk.find_pic_click(*cm.RECT_FULL, "完成温饱.bmp", timeout=300)
    lib.msleep(600)
    if not is_cur_wen_bao_reach_80(wk):  # 若温饱已达到80
        cm.click_talk_specify_item(wk, "继续领取", 300)
    cm.close_all_sub_wnd(wk)
