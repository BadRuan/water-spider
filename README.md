# 水位站数据分析

## 目标站点
[安徽省水信息系统](http://yc.wswj.net/ahsxx/LOL/?refer=upl&to=public_public)水情信息专题网站水位数据

## 需求
爬取制定水文站点某段时间内的水文数据并保存至MySQL数据库中

## 开发进展
1. 已有加密解密函数
2. 已完成解析加密数据请求头
3. 已完成响应数据解析
4. 已完成保存数据业务开发
5. 已完成项目结构优化
6. 已完成日志功能
7. 完成基本TDEngine数据库基础代码编写
8. 完成异步API请求，性能得到提升

## 该项目使用TDEngine数据库
[TDEngine](https://docs.taosdata.com/)

## 后续开发计划(不分先后)
1. 完善异常报错机制
2. 输出自动化运行构建
3. 构建自动化测试功能
4. docker compose


## Docker 部署
```shell
docker build -t water_info:v2 .
docker run -d --name water-spider2 water_info:v2
```