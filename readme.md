[![Python](https://img.shields.io/badge/Python-3.x-brightgreen.svg)]()
[![Django](https://img.shields.io/badge/Ncdu-1.13-orange.svg)]()
[![Django](https://img.shields.io/badge/Dev-管清麟-ff69b4.svg)]()
## ncdu-tools 大文件检索工具

## 运行环境
* Mac os

* Linux os

## 依赖环境
*Python 3运行环境

*ncdu命令工具

## 运行说明
1. python3 ncdu-tools.py -d 指定目录(必须) -m (MB大小) 或 -g (GB大小)
2. python3 ncdu-tools.py -h 帮助文档

## 例子
检索大于100M的内容

`python3 ncdu-tools.py  -d /vol/ -m 100`

`File > 200 MB：`

`/vol/haha/mishi.ts`
`/vol/haha/heihei/hehe.ts`
`/vol/hehe/1_XMTg2MDk1Mzk2MA==.ts`
`/vol/hehe/haha/tod/jiushida.ts`
`/vol/hehe/a.mkv`

检索大于1G的内容
`python3 ncdu-tools.py  -d /vol/ -g 1`

`File > 1 GB：`

`/vol/hehe/a.mkv`
## 目录结构

	ncdu-tools
	    ├── ncdu-tools.py    # 主程序
	    ├── README.md        # 文档说明
	    └── .gitignore
	        