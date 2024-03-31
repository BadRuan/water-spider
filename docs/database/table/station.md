# 水文站点数据表

## 新建水文站代码映射表

字段说明:
1. ``ID``：序号，索引使用
2. ``STCD``: 水文站点代码
3. ``NAME``: 水文站名

```sql
CREATE TABLE IF NOT EXISTS `station_code` (
    `ID` int(11) NOT NULL AUTO_INCREMENT,
    `STCD` int(11) NOT NULL UNIQUE,
    `NAME` varchar(255) COLLATE utf8_bin NOT NULL,
    PRIMARY KEY (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin
AUTO_INCREMENT=1 ;
```


```
+-------+--------------+------+-----+---------+----------------+
| Field | Type         | Null | Key | Default | Extra          |
+-------+--------------+------+-----+---------+----------------+
| ID    | int          | NO   | PRI | NULL    | auto_increment |
| STCD  | int          | NO   | UNI | NULL    |                |
| NAME  | varchar(255) | NO   |     | NULL    |                |
+-------+--------------+------+-----+---------+----------------+
```

## 插入水文站代码数据

```sql
INSERT INTO `station_code` (`STCD`, `NAME`) VALUES (%s, '%s')
```

示例数据:
```sql
INSERT INTO `station_code` (`STCD`, `NAME`) VALUES (60115400, '芜湖')
INSERT INTO `station_code` (`STCD`, `NAME`) VALUES (51004350, '天长')
```

## 查找数据

### 查找所有水文站代码数据

```sql
SELECT * FROM `station_code`
```

