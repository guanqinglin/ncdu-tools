#!/usr/bin/env python
#_*_coding:utf-8_*_
#QQ 7796755
#Blog:www.qinglin.net
#author = "Guanqinglin"
from __future__ import unicode_literals,print_function,division
import os
import sys
import json
import getopt
import platform
import subprocess


def testncdu():
    ret_status = subprocess.getstatusoutput("ncdu -v")
    if ret_status[0] != 0:
        systemversion = platform.system()
        if systemversion == 'Linux':
            print("检测到本机[%s]系统没有安装ncdu工具，请安装ncdu工具"%systemversion)
            print("CentOS安装命令：yum -y install ncdu")
            print("Ubuntu安装命令：apt-get install ncdu")
            print("其他Linux版本，请参考网站：https://dev.yorhel.nl/ncdu")
        elif  systemversion == 'Darwin':
            print("检测到本机[%s]系统没有安装ncdu工具，请安装ncdu工具" % systemversion)
            print("MacOS安装命令：brew install ncdu")
            print("关于brew的安装，请参考网站：https://formulae.brew.sh/formula/ncdu")
        elif systemversion == 'Windows':
            print("本工具暂不支持windows系列操作系统")
        else:
            print("未检测到您系统版本，请联系管理员，邮箱：qinglin@qinglin.net")
        sys.exit(ret_status[0] )


def readFile():
    try:
        with open('ncdu.out','r',encoding='utf8') as file:
            fileRead = file.read()
            file.close()
        return fileRead
    except Exception as e:
        print("获取路径信息失败，请重试：",e)


def display(data, parentPath,size):
    for i in data:
        if isinstance(i,list):
            display(i, os.path.join(parentPath, i[0]["name"]),size)
            continue
        if "dsize" in i:
            if i["dsize"] > size * 1024 * 1024:
                print(os.path.join(parentPath,i["name"]))


def execute(path):
    res = subprocess.Popen("ncdu -x %s -o ncdu.out"%path, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    res.stdout.read()


def main(argv):
    help = '''python ncdu-tools.py  <options>  <directory>
    
 -h                       This help message
 -v                       Print version
 -d                       Specify the path,Print >1MB file.
 -m                      Print input > MB
'''
    if len(argv)  == 0:
        print(help)
    try:
        opts, args = getopt.getopt(argv, "vhd:m:")
    except getopt.GetoptError:
        print(help)
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print(help)
            sys.exit()
        elif opt == '-v':
            print("ncdu-tools 1.0.0")
        elif opt in ("-d", "--d"):
            path = arg
        elif opt in ("-m", "--m"):
            msize = arg
    if path and msize:
        execute(path)
        data = json.loads(readFile())
        print("大于%sM文件："%msize)
        display(data[-1], data[-1][0]["name"],int(msize))
    else:
        print("参数不完整")

if __name__ == '__main__':
    testncdu()
    main(sys.argv[1:])

