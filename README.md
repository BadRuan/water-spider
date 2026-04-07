# 水位爬虫

[![GitHub stars](https://img.shields.io/github/stars/BadRuan/water-spider?style=social)](https://github.com/BadRuan/water-spider)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](https://makeapullrequest.com)

## What Is This?

[安徽省水信息系统](http://ahswj.cn/ahsxx/LOL/?refer=upl&to=public_public)**水情信息**专题网站水位数据爬虫

爬取指定水文站点指定时间水文数据并保存至[PostgreSQL](https://www.postgresql.org/)数据库

## How to use?

使用uv安装

## 数据走向

1. 目标时间范围;
2. API参数构建（构建加密请求）;
3. 执行API访问;
4. API访问失败，休息固定时间，再次执行步骤3；API访问成功;
5. 解析获取的加密数据;
6. 保存数据.

## 模式

1. 24小时运行模式，间隔时间一次轮训;
2. 获取今年整年所有水位数据;
3. 获取指定年份整年所有水位数据;
4. 获取指定时间范围的水位数据.

## 已实现

1. 应用**责任链设计模式**，数据单向流动，易阅读理解;
2. 大范围的日期，支持自动分割时间.

## 计划实现

1. 保证爬虫采集频次不过高，间隔时间设置随机数，变成随机间隔，防止机器识别;
2.完善的日志系统，方便查看爬虫运行的数据（单次、每次数据），错误信息等.
