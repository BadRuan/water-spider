# Docker搭建TDengine数据库

## 拉取 TDengine 镜像

```shell
docker pull tdengine/tdengine:latest
```

## 查看本地镜像

```shell
docker images
```

显示本地镜像如下：
```
REPOSITORY          TAG       IMAGE ID       CREATED       SIZE
tdengine/tdengine   latest    b1a8957bf226   6 weeks ago   686MB
```

## 运行容器

```shell
docker run -itd --name=tdengine -p 6030:6030 -p 6041:6041 -p 6043-6049:6043-6049 -p 6043-6049:6043-6049/udp tdengine/tdengine
```

TDengine 3.0 服务端仅使用 6030 TCP 端口。6041 为 taosAdapter 所使用提供 REST 服务端口。6043-6049 为 taosAdapter 提供第三方应用接入所使用端口，可根据需要选择是否打开。


如果需要将数据持久化到本机的某一个文件夹

```shell
docker run -d -v ~/data/taos/dnode/data:/var/lib/taos \
  -v ~/data/taos/dnode/log:/var/log/taos \
  -p 6030:6030 -p 6041:6041 -p 6043-6049:6043-6049 -p 6043-6049:6043-6049/udp tdengine/tdengine
```


```
➜  ~ docker ps
CONTAINER ID   IMAGE               COMMAND                  CREATED        STATUS       PORTS
                                                                                     NAMES
ed8d92b30959   tdengine/tdengine   "/tini -- /usr/bin/e…"   41 hours ago   Up 4 hours   0.0.0.0:6030->6030/tcp, 0.0.0.0:6041->6041/tcp, 0.0.0.0:6043-6049->6043-6049/tcp, 0.0.0.0:6043-6049->6043-6049/udp   tdgengine
```

## 进入容器
```shell
docker exec -it <container name> bash
```



登录TDengine：

```shell
taos
```

然后输入刚设置的密码即可，登录成功显示如下：
```
Enter password: Welcome to the TDengine Command Line Interface, Client Version:3.2.3.0
Copyright (c) 2023 by TDengine, all rights reserved.

  ********************************  Tab Completion  ************************************
  *   The TDengine CLI supports tab completion for a variety of items,                 *
  *   including database names, table names, function names and keywords.              *
  *   The full list of shortcut keys is as follows:                                    *
  *    [ TAB ]        ......  complete the current word                                *
  *                   ......  if used on a blank line, display all supported commands  *
  *    [ Ctrl + A ]   ......  move cursor to the st[A]rt of the line                   *
  *    [ Ctrl + E ]   ......  move cursor to the [E]nd of the line                     *
  *    [ Ctrl + W ]   ......  move cursor to the middle of the line                    *
  *    [ Ctrl + L ]   ......  clear the entire screen                                  *
  *    [ Ctrl + K ]   ......  clear the screen after the cursor                        *
  *    [ Ctrl + U ]   ......  clear the screen before the cursor                       *
  **************************************************************************************

Server is Community Edition.
```

## 修改root密码

```sql
ALTER USER root PASS "123456";
```

## 修改TDengine时区
在 Linux 下，客户端配置文件目录为 ``/etc/taos/taos.cfg``，修改 ``timezone`` 属性为 ``UTC-8``

在 Linux/macOS 中，客户端会自动读取系统设置的时区信息。用户也可以采用多种方式在配置文件设置时区。

```
timezone UTC-8
timezone GMT-8
timezone Asia/Shanghai
```
均是合法的设置东八区时区的格式。

## 新建数据库
```sql
CREATE DATABASE water;
```

## 使用数据库
```sql
USE water;
```