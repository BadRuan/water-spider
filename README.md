# 水位站数据分析

## 目标站点
[安徽省水信息系统](http://yc.wswj.net/ahsxx/LOL/?refer=upl&to=public_public)水情信息专题网站水位数据

## 需求
爬取制定水文站点某段时间内的水文数据并保存至MySQL数据库中

## 开发进展
1. 已有加密解密函数
2. 已完成解析加密数据请求头
3. 已完成响应数据解析
4. 完成基本MySQL CURD代码编写
5. 已完成保存数据业务开发
6. 已完成项目结构优化
7. 已完成日志功能

## 该项目MySQL数据库
[MySQL数据库备忘](docs/database.md)

## 后续开发计划(不分先后)
1. 完善异常报错机制
2. 输出自动化运行构建
3. 构建自动化测试功能
4. docker compose
5. 多线程性能优化
6. 融合设计模式：如单例模式管理数据库连接
7. 文档页面开发


## Docker 部署
```shell
docker build -t water_info:v1 .
docker run -d --name water-info water_info:v1
```