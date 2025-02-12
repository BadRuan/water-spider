# 水位信息爬虫

![Static Badge](https://img.shields.io/badge/Python-3.12-blue)

## 目标站点

[安徽省水信息系统](http://yc.wswj.net/ahsxx/LOL/?refer=upl&to=public_public)**水情信息**专题网站水位数据

## 功能

爬取指定水文站点指定时间的水文数据并保存至[TDEngine](https://docs.taosdata.com/)数据库

## 安装

### pipenv

```shell
pipenv install
pipenv shell
```

## 重构进展

1. 完成日志功能
2. unittest单元测试功能
