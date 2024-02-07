import base64
import crypt
import pythoncom
import wmi
import platform
import socket

from utils.file import dict_to_json_str, json_str_to_dict

# 获取机器码(主板序列号+硬盘序列号)
def get_machine_code():
    pythoncom.CoInitialize()
    c = wmi.WMI()
    try:
        board_serial = c.Win32_BaseBoard()[0].SerialNumber
        disk_serial = c.Win32_DiskDrive()[0].SerialNumber
        disk_serial = disk_serial.strip(".").replace("_", "")
        machine_code = board_serial + disk_serial
        machine_code = machine_code[12:] + machine_code[:12]
        machine_code = machine_code[::-1]
    except:
        machine_code = ""
    return machine_code


# 获取操作系统
def get_operation_system() -> str:
    return platform.platform()


# 连接服务端tcp
def connect_server_tcp(server_ip, server_port):
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    err_no = tcp_socket.connect_ex((server_ip, server_port))
    if err_no != 0:
        return None
    return tcp_socket


# 发送数据给服务端
def send_to_server(tcp_socket: socket.socket, client_info_dict: dict):
    aes_key = ''
    aes = crypt.AesEncryption(aes_key)
    # 内容 转 json字符串
    client_info_dict["内容"] = dict_to_json_str(client_info_dict["内容"])
    # 根据消息类型决定是否对内容aes加密
    if client_info_dict["消息类型"] != "初始":
        # 对json内容进行aes加密
        client_info_dict["内容"] = aes.encrypt(client_info_dict["内容"])
    # 把整个客户端信息字典 转 json字符串
    json_str = dict_to_json_str(client_info_dict)
    # json字符串 base85编码
    send_bytes = base64.b85encode(json_str.encode())
    try:
        tcp_socket.send(send_bytes)
        print(f"客户端数据, 发送成功: {json_str}")
    except Exception as e:
        print(f"客户端数据, 发送失败: {e}")


# 从服务端接收数据
def recv_from_server(tcp_socket: socket.socket):
    aes_key = ''
    aes = crypt.AesEncryption(aes_key)
    tcp_socket.settimeout(5)  # 设置为非阻塞接收, 只等5秒
    recv_bytes = ""
    try:  # 若等待服务端发出消息时, 客户端套接字关闭会异常
        recv_bytes = tcp_socket.recv(4096)
    except:
        ...
    tcp_socket.settimeout(None)  # 重新设置为阻塞模式
    if not recv_bytes:  # 若客户端退出,会收到一个空str
        return "", {}
    # base85解码
    json_str = base64.b85decode(recv_bytes).decode()
    print(f"收到服务端的消息: {json_str}")
    # json字符串 转 py字典
    server_info_dict = json_str_to_dict(json_str)
    msg_type = server_info_dict["消息类型"]
    server_content_str = server_info_dict["内容"]
    # 把内容json字符串 转 py字典
    if msg_type != "初始":  # 若不为初始类型的消息, 要先aes解密
        # 先aes解密, 获取json字符串
        server_content_str = aes.decrypt(server_content_str)
    # json字符串 转 py字典
    server_content_dict = json_str_to_dict(server_content_str)
    return msg_type, server_content_dict
