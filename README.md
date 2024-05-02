# 水位站数据分析

## 项目技术栈
- 基础语言: [Python](https://www.python.org/)
- 数据库: [TDEngine](https://docs.taosdata.com/)
- 环境部署: [Docker](https://www.docker.com/)

## 目标站点
[安徽省水信息系统](http://yc.wswj.net/ahsxx/LOL/?refer=upl&to=public_public)水情信息专题网站水位数据

## 需求
爬取指定水文站点指定时间的水文数据并保存至[TDEngine](https://docs.taosdata.com/)数据库中

## 开发进展
1. 完成加密解密函数
2. 完成请求及响应数据加密解密
3. 完成[TDEngine数据库](https://docs.taosdata.com/)基础代码编写
4. 完成项目结构优化, 业务分层, 数据提取及入库业务开发
5. 完成[日志](https://docs.python.org/zh-cn/3/library/logging.html)功能
6. 完善异常报错机制
7. 完成异步API请求，性能得到提升
8. 完成[Pydantic](https://docs.pydantic.dev/latest/)数据结构优化
9. 完成Dockerfile文件编写

## 后续开发计划
1. 需要完善测试功能
2. docker compose
3. 增加单元测试


## Docker 部署
```shell
docker build -t water_spdier:v2 .
docker run -itd --name=water-spider --restart=always water_spdier:v2
```