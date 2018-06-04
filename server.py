#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2015 breakwall
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

import time
import sys

# 线程模块
import threading
import os

if __name__ == '__main__':

	# inspect模块作用，1.进行类型检查，2.获取源码，3.获取类或函数的参数信息，4.解析堆栈
	import inspect

	# os.chdir用于改变当前工作目录到指定路径
	# os.path.dirname(参数) 用于返回参数的路径
	# os.path.realpath(参数) 用于返回参数的绝对路径
	# inspect.getfile(inspect.currentframe()) 用于返回当前文件路径
	os.chdir(os.path.dirname(os.path.realpath(inspect.getfile(inspect.currentframe()))))

import server_pool
import db_transfer
from shadowsocks import shell
from configloader import load_config, get_config

# MainThread 继承自 threading.Thread，threading.Thread 用于创建线程，所以当前类用于创建线程
class MainThread(threading.Thread):
	def __init__(self, obj):

		# 调用 threading.Thread 创建线程，无传递任何参数
		super(MainThread, self).__init__()
		self.daemon = True
		self.obj = obj

	# 线程在被执行时会自动调用 run 方法
	# 也就是说调用线程 start 方法就会自动调用 run 方法
	def run(self):
		self.obj.thread_db(self.obj)

	# 结束线程
	def stop(self):
		self.obj.thread_db_stop()

def main():

	# 检查 python 版本
	shell.check_python()

	# question:这一行永远都不会执行
	if False:
		db_transfer.DbTransfer.thread_db()
	else:

		# mudbjson 应该是将文件存储于本地，适用情况应该是单机多用户情况
		if get_config().API_INTERFACE == 'mudbjson':
			thread = MainThread(db_transfer.MuJsonTransfer)
		
		# sspanel 是个管理工具，使用 mysql 存储用户数据
		elif get_config().API_INTERFACE == 'sspanelv2':
			thread = MainThread(db_transfer.DbTransfer)

		else:
			thread = MainThread(db_transfer.Dbv3Transfer)
		
		# start 方法用于启动线程
		thread.start()

		try:
			# 判断当前线程是否为激活的
			while thread.is_alive():

				# 阻塞线程，等待子线程结束，如果超过所设置的时间参数未结束，则强制结束子线程
				thread.join(10.0)
		except (KeyboardInterrupt, IOError, OSError) as e:
			import traceback
			traceback.print_exc()
			thread.stop()

if __name__ == '__main__':
	main()

