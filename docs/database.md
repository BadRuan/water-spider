# 数据库相关命令存档

## 新建数据库
```sql
CREATE DATABASE water;
```

## 新建数据表

### 新建水文站代码映射表

表格说明:
1. ID：序号，索引使用
2. STCD: 水文站点代码
3. NAME: 水文站名

```sql
CREATE TABLE IF NOT EXISTS `station_code` (
    `ID` int(11) NOT NULL AUTO_INCREMENT,
    `STCD` int(11) NOT NULL UNIQUE,
    `NAME` varchar(255) COLLATE utf8_bin NOT NULL,
    PRIMARY KEY (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin
AUTO_INCREMENT=1 ;
```

+-------+--------------+------+-----+---------+----------------+
| Field | Type         | Null | Key | Default | Extra          |
+-------+--------------+------+-----+---------+----------------+
| ID    | int          | NO   | PRI | NULL    | auto_increment |
| STCD  | int          | NO   | UNI | NULL    |                |
| NAME  | varchar(255) | NO   |     | NULL    |                |
+-------+--------------+------+-----+---------+----------------+

### 新建水位信息数据表

表格说明:
1. ID：序号，索引使用
2. STCD: 水文站点代码
3. Z: 水位高程
4. TM: 具体时间

```sql
CREATE TABLE IF NOT EXISTS `water_level` (
    `ID` int(11) NOT NULL AUTO_INCREMENT,
    `STCD` int(11) NOT NULL,
    `Z` float(4, 2) NOT NULL,
    `TM` datetime COLLATE utf8_bin UNIQUE NOT NULL ,
    PRIMARY KEY (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin
AUTO_INCREMENT=1 ;
```

+-------+------------+------+-----+---------+----------------+
| Field | Type       | Null | Key | Default | Extra          |
+-------+------------+------+-----+---------+----------------+
| ID    | int        | NO   | PRI | NULL    | auto_increment |
| STCD  | int        | NO   |     | NULL    |                |
| Z     | float(4,2) | NO   |     | NULL    |                |
| TM    | datetime   | NO   | UNI | NULL    |                |
+-------+------------+------+-----+---------+----------------+

## CURD：增删改查

### 插入数据

#### 插入水文站代码数据

```sql
INSERT INTO `station_code` (`STCD`, `NAME`) VALUES (%s, '%s')
```

示例数据:
```sql
INSERT INTO `station_code` (`STCD`, `NAME`) VALUES (60115400, '芜湖')
INSERT INTO `station_code` (`STCD`, `NAME`) VALUES (51004350, '天长')
```


#### 插入水位信息数据

```sql
INSERT INTO `water_level` (`STCD`, `Z`, `TM`) VALUES (%s, %s, `%s`)
```

示例数据:
```sql
INSERT INTO `water_level` (`STCD`, `Z`, `TM`) VALUES (60115400, 5.96, '2024-03-01 12:35')
```

### 更新数据

### 删除数据

### 查找数据

#### 查找所有水文站代码数据

```sql
SELECT * FROM `station_code`
```

#### 查找某水文站水文数据

```sql
SELECT * FROM `water_level` where `STCD` = %s
```