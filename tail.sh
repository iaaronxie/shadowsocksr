#!/bin/bash
cd `dirname $0`

# 将文件写到标准输出
tail -f ssserver.log
