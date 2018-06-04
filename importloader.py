#!/usr/bin/python
# -*- coding: UTF-8 -*-

def load(name):

	# python2
	try:
		
		# __import__同样是加载文件，跟 import 指令功能一致，传递的参数需为字符串
		obj = __import__(name)

		# reload 函数用于重载之前加入的模块
		# 此处的 reload(obj) 应该没什么用
		reload(obj)
		return obj
	except:
		pass

	# python3
	# python3 中直接使用 reload 会报错，需要先 import importlib
	try:
		import importlib
		obj = importlib.__import__(name)
		importlib.reload(obj)
		return obj
	except:
		pass

def loads(namelist):
	for name in namelist:
		obj = load(name)
		if obj is not None:
			return obj
