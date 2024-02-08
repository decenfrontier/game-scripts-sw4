import json
import os

def path_exist(path: str):
    # 路径是否存在
    if os.path.exists(path):
        return True
    return False


def dir_create(dir: str):
    # 创建目录, 不存在才创建
    if not path_exist(dir):
        os.makedirs(dir)


def dir_get_files(dir: str):
    # 获取目录中的文件
    ret = ""
    for root, dirs, files in os.walk(dir):
        ret = files
        break
    return ret


def file_create(path: str, content=""):
    # 创建文件
    with open(path, "a") as f:
        f.write(content)


def file_remove(path: str):
    # 删除文件, 存在才删除
    if path_exist(path):
        os.remove(path)


def file_rename(dir: str, old_file: str, new_file: str):
    # 文件重命名
    try:
        os.rename(f"{dir}\\{old_file}", f"{dir}\\{new_file}")
    except:
        print("file_rename error")
        raise OSError


def file_clear_content(path: str):
    # 清空文件内容, 若没有文件会自动创建文件
    with open(path, "w+") as f:  # 打开文件并将光标置于开头
        f.truncate()  # 截断文件光标后的内容


def file_read_content(path: str) -> str:
    # 读取文件内容
    if not path_exist(path):
        file_create(path)
    content = ""
    with open(path, "r") as f:
        content = f.read()
    return content


def file_append_content(path: str, content: str):
    # 添加文件内容, 若没有文件会自动创建文件
    with open(path, "a") as f:
        f.write(content)


# json文件 -> py字典
def json_file_to_dict(path_cfg: str, default_cfg={}):
    try:
        # 若文件不存在, 则用默认的配置字典先创建json文件
        if not path_exist(path_cfg):
            with open(path_cfg, "w", encoding="utf-8") as f:
                json.dump(default_cfg, f, ensure_ascii=False,
                          sort_keys=True, indent=4)
            return default_cfg
        with open(path_cfg, "r", encoding="utf-8") as f:
            cfg_load = json.load(f) or {}
    except:
        print(f"json decode error! {path_cfg} {default_cfg}")
        cfg_load = {}
    return cfg_load


# json字符串 -> py字典
def json_str_to_dict(json_str: str):
    try:
        cfg_load = json.loads(json_str)
    except:
        print(f"json decode error! {json_str}")
        cfg_load = {}
    return cfg_load


# py对象 -> json文件
def dict_to_json_file(py_dict: dict, path_cfg: str):
    try:
        with open(path_cfg, "w", encoding="utf-8") as f:
            json.dump(py_dict, f, ensure_ascii=False, sort_keys=True, indent=4)
    except:
        print(f"json encode error! {py_dict} {path_cfg}")


# py对象 -> json字符串
def dict_to_json_str(py_dict: dict):
    try:
        json_str = json.dumps(py_dict, ensure_ascii=False, sort_keys=True)
    except:
        print(f"json encode error! {py_dict}")
        json_str = "{}"
    return json_str
