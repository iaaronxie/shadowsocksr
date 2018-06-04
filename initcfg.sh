#!/bin/bash

# -x 参数赋予 *.sh 执行权限
chmod +x *.sh
chmod +x shadowsocks/*.sh

# -n 参数表明不要覆盖已存在的文件，也就是说如果已经存在了要复制出来的文件，就不执行复制
cp -n apiconfig.py userapiconfig.py
cp -n config.json user-config.json
cp -n mysql.json usermysql.json

