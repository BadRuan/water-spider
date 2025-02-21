# TDengine-Database

为什么选择``TDengine``？

> TDengine 是一款专为物联网、工业互联网等场景设计并优化的大数据平台，其核心模块是高性能、集群开源、云原生、极简的时序数据库。它能安全高效地将大量设备、数据采集器每天产生的高达 TB 甚至 PB 级的数据进行汇聚、存储、分析和分发，对业务运行状态进行实时监测、预警，提供实时的商业洞察。

## 搭建TDengine数据库

### 拉取镜像

```shell
docker pull tdengine/tdengine:latest
```

### 创建容器

```shell
docker run -d -p 6030:6030 -p 6041:6041 -p 6043-6049:6043-6049 -p 6043-6049:6043-6049/udp tdengine/tdengine
```

如果需要将数据持久化到本机的某一个文件夹

```shell
docker run -d -v ~/data/taos/dnode/data:/var/lib/taos \
  -v ~/data/taos/dnode/log:/var/log/taos \
  -p 6030:6030 -p 6041:6041 -p 6043-6049:6043-6049 -p 6043-6049:6043-6049/udp tdengine/tdengine
```

### 进入容器

进入容器：

```shell
docker exec -it <container name> bash
```

进入数据库：

```shell
taos -u root -p
```

## 数据表设计

### 创建水位信息数据表

字段说明:

1. ``ts``: 时间戳
2. ``Z``: 水位高程
3. ``STCD``: 水文站点代码
4. ``NAME``: 站点名

```sql
CREATE TABLE IF NOT EXISTS `waterlevel` 
        (`ts` TIMESTAMP, `current` FLOAT) 
        TAGS (`STCD` INT, `NAME` BINARY(16))
```

### 插入水位数据

```sql
INSERT INTO t站点代码
 USING waterlevel TAGS('STCD', '站点名称')
 VALUES
 ('{item['TM']}:00.000', 水位)
```

### 查找数据

#### 查找某水文站指定数量的水位数据

```sql
taos> SELECT * FROM waterlevel;
```
