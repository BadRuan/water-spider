# Docker搭建MySQL数据库

## Docker镜像
Docker:[MySQL 镜像库地址](https://hub.docker.com/_/mysql?tab=tags)

## 拉取 MySQL 镜像

```shell
docker pull mysql:latest
```

## 查看本地镜像

```shell
docker images
```

显示本地镜像如下：
```
REPOSITORY   TAG       IMAGE ID       CREATED       SIZE
mysql        latest    82563e0cbf18   5 days ago    632MB
```

## 运行容器

```shell
docker run -itd --name mysql-test -p 3306:3306 -e MYSQL_ROOT_PASSWORD=123456 mysql
```

参数说明：
- p 3306:3306 ：映射容器服务的 3306 端口到宿主机的 3306 端口，外部主机可以直接通过 宿主机 ip:3306 访问到 MySQL 的服务。
- MYSQL_ROOT_PASSWORD=123456：设置 MySQL 服务 root 用户的密码。

```
➜  ~ docker ps
CONTAINER ID   IMAGE     COMMAND                  CREATED      STATUS       PORTS                               NAMES
bcabdeb9344e   mysql     "docker-entrypoint.s…"   2 days ago   Up 3 hours   0.0.0.0:3306->3306/tcp, 33060/tcp   mysql-demo
```

## 进入容器
```shell
docker exec -it bcab bash
```
显示如下：
```
bash-4.4#
```
登录MySQL：
```shell
mysql -u root -p 
```
显示：``Enter password:``
然后输入刚设置的密码即可，登录成功显示如下：
```
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 54
Server version: 8.3.0 MySQL Community Server - GPL

Copyright (c) 2000, 2024, Oracle and/or its affiliates.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql>
```