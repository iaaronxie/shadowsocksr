#!/bin/bash
cd `dirname $0`

# grep 是 linux 系统中的文本搜索工具
# 当前命令为输出 python 的标准版本
python_ver=$(ls /usr/bin|grep -e "^python[23]\.[1-9]\+$"|tail -1)

# ps 用于显示当前进程
# ps -ef 显示所有进程信息，连同命令行
# awk 把文件逐行读入，以空格为默认分割符将每行切片，切开的部分再进行分析处理
# 这里应该是将之前执行的 python 命令终止
eval $(ps -ef | grep "[0-9] ${python_ver} server\\.py m" | awk '{print "kill "$2}')

# ulimit命令用于控制shell程序的资源， -n 指的同一时间最多可开启的文件数
ulimit -n 512000

# nohup 命令能够将当前命令运行于后台并控制台断掉、账号退出调仍然能够继续运行
# 2>&1 指的是将错误输出到屏幕，0:输入，1:输出，2:错误输出
# https://unmi.cc/linux-input-output-redirection/
# /dev/null 表示空设备，用来忽略调输出
nohup ${python_ver} server.py m>> /dev/null 2>&1 &
