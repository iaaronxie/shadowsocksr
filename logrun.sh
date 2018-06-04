#!/bin/bash
cd `dirname $0`
python_ver=$(ls /usr/bin|grep -e "^python[23]\.[1-9]\+$"|tail -1)
eval $(ps -ef | grep "[0-9] ${python_ver} server\\.py m" | awk '{print "kill "$2}')
ulimit -n 512000

# >> 或 > 都是输出重定向，其中 > 表示覆盖内容，>> 表示追加内容
nohup ${python_ver} server.py m>> ssserver.log 2>&1 &

