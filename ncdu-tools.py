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
            print("Test [%s] system no found  install ncdu command，Please install ncdu tools."%systemversion)
            print("CentOS install Command：yum -y install ncdu")
            print("Ubuntu nstall Command：apt-get install ncdu")
            print("Other Linux Version，Plase fyi：https://dev.yorhel.nl/ncdu")
        elif  systemversion == 'Darwin':
            print("Test [%s] system no found  install ncdu command，Please install ncdu tools." % systemversion)
            print("MacOS install Command：brew install ncdu")
            print("about  brew，Plase fyi：https://formulae.brew.sh/formula/ncdu")
        elif systemversion == 'Windows':
            print("Ncdu-tools nonsupport Windows.")
        else:
            print("Test system fail，Please contact the administrator ，Email：qinglin@qinglin.net")
        sys.exit(ret_status[0] )


def readFile():
    try:
        with open('ncdu.out','r',encoding='utf8') as file:
            fileRead = file.read()
            file.close()
        return fileRead
    except Exception as e:
        print("Get Path fail，Please Try：",e)


def display(data, parentpath,size=None):
    for i in data:
        if isinstance(i,list):
            display(i, os.path.join(parentpath, i[0]["name"]),size)
            continue
        if "dsize" in i and size:
            if i["dsize"] > size * 1024 * 1024:
                print(os.path.join(parentpath,i["name"]))


def execute(path):
    res = subprocess.Popen("ncdu -x %s -o ncdu.out"%path, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    res.stdout.read()


def main(argv):
    help = '''python ncdu-tools.py  <-d>  <directory>  <options>  <value>
    
 -h         This help message
 -v         Print version
 -d         Specify the directory
 -m         Print input > MB
 -g         Prin input >GB
'''
    path = ""
    msize = ""
    gsize = ""
    if len(argv)  == 0:
        print(help)
    try:
        opts, args = getopt.getopt(argv, "vht:d:m:g:")
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
        elif opt in ("-g", "--g"):
            gsize = arg

    if path and msize:
        execute(path)
        data = json.loads(readFile())
        print("File > %s MB："%msize)
        display(data[-1], data[-1][0]["name"], int(msize))
    elif path and gsize:
        execute(path)
        data = json.loads(readFile())
        gcount = int(gsize)*1024
        print("File > %s GB：" % gsize)
        display(data[-1], data[-1][0]["name"], gcount)


if __name__ == '__main__':
    testncdu()
    main(sys.argv[1:])
