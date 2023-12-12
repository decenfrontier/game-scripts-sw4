# pyqt-sw4游戏脚本
![](https://img.shields.io/badge/Python-3.8-blue.svg)
![](https://img.shields.io/badge/PySide2-5.15.2-blue.svg)
![](https://img.shields.io/badge/License-MIT-green.svg)
## 1 项目介绍
一款回合制端游的自动完成日常任务的游戏脚本,   
- 基于python和pyqt实现 ui和业务逻辑  
- 基于大漠插件 实现 后台键鼠操作，支持多窗口同时后台操作   
- 基于图灵插件 实现 图片处理, 自研算法自动过人机验证  
- 与服务端定时发送心跳包, 用户到期后 或被Admin冻结后, 触发下线操作
    - 网络验证服务端开源地址: https://github.com/decenfrontier/PyNetAuth

## 2 使用说明
本项目是2年前写的, 游戏已经更新了很多版本, 现已不再适用. 只建议大家参考一下设计思路.  
其实python是很适合写游戏脚本的, 但市面上大家都只教易语言, C++, C#, TC, 按键精灵等, 几乎没有python的成品商业级游戏脚本, 现开源出来, 希望大家参与建设, 让python的游戏脚本生态越来越好
免责声明: 仅供学习交流, 请勿用作商业用途

运行方式:
> python wnd_main_code.py