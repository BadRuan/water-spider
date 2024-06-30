# 水文站数据爬虫

![Static Badge](https://img.shields.io/badge/Python-3.12-blue)

## 目标站点

[安徽省水信息系统](http://yc.wswj.net/ahsxx/LOL/?refer=upl&to=public_public)水情信息专题网站水位数据

## 需求

爬取指定水文站点指定时间的水文数据并保存至[TDEngine](https://docs.taosdata.com/)数据库

## 安装

### pip

```shell
pip install -r requirements.txt
```

### pipenv

```shell
pipenv install
pipenv shell
```

## 生产环境部署：Docker

```shell
docker build -t water_spdier:latest .
docker run -itd --name=water-spider --restart=always water_spdier:latest
```
