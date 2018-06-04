#!/bin/bash

# CyMySQL 是 cpython 的 mysql 数据库驱动
rm -rf CyMySQL
rm -rf cymysql
git clone https://github.com/nakagami/CyMySQL.git
mv CyMySQL/cymysql ./
rm -rf CyMySQL
