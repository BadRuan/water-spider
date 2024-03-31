# 三线水位信息数据表

## 新建三线水位信息数据表

字段说明:
1. ``ID``：序号，索引使用
2. ``STCD``: 水文站点代码
3. ``SFSW``: 设防水位
4. ``JJSW``: 警戒水位
5. ``BZSW``: 保证水位
6. ``NAME``: 测站名称

```sql
CREATE TABLE IF NOT EXISTS `three_line` (
    `ID` int(11) NOT NULL AUTO_INCREMENT,
    `STCD` int(11) NOT NULL,
    `SFSW` float(4, 2) NOT NULL,
    `JJSW` float(4, 2) NOT NULL,
    `BZSW` float(4, 2) NOT NULL,
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
| STCD  | int          | NO   |     | NULL    |                |
| SFSW  | float(4,2)   | NO   |     | NULL    |                |
| JJSW  | float(4,2)   | NO   |     | NULL    |                |
| BZSW  | float(4,2)   | NO   |     | NULL    |                |
| NAME  | varchar(255) | NO   |     | NULL    |                |
+-------+--------------+------+-----+---------+----------------+
```

## 清空数据表
TRUNCATE 关键字用于完全清空一个表。其语法格式如下：
```sql
TRUNCATE three_line;
```


## 插入水位信息数据

```sql
INSERT INTO `three_line` (`STCD`, `SFSW`, `JJSW`, `BZSW`, `NAME`) VALUES ('%s', `%s`, `%s`, `%s`, '%s')
```

示例数据:
```sql
INSERT INTO `three_line` (`STCD`, `SFSW`, `JJSW`, `BZSW`, `NAME`) VALUES (62904400, 11.5, 13.2, 15.84 ,'无为大堤');
INSERT INTO `three_line` (`STCD`, `SFSW`, `JJSW`, `BZSW`, `NAME`) VALUES (60115400, 9.4, 11.2, 13.4, '城北圩');
INSERT INTO `three_line` (`STCD`, `SFSW`, `JJSW`, `BZSW`, `NAME`) VALUES (62900700, 8.7, 10.7, 12.7 ,'江北（沈巷）长江堤');
INSERT INTO `three_line` (`STCD`, `SFSW`, `JJSW`, `BZSW`, `NAME`) VALUES (62906500, 10.1, 12.1, 14.1 ,'万春圈堤');
INSERT INTO `three_line` (`STCD`, `SFSW`, `JJSW`, `BZSW`, `NAME`) VALUES (62900700, 9.4, 11.2, 12.3 ,'裕溪口江堤');
INSERT INTO `three_line` (`STCD`, `SFSW`, `JJSW`, `BZSW`, `NAME`) VALUES (62900600, 9.5, 10.5, 12.0 ,'裕溪河堤');
INSERT INTO `three_line` (`STCD`, `SFSW`, `JJSW`, `BZSW`, `NAME`) VALUES (62905100, 8.5, 9.5, 11.5 ,'牛屯河堤');
INSERT INTO `three_line` (`STCD`, `SFSW`, `JJSW`, `BZSW`, `NAME`) VALUES (62904400, 11.5, 13.2, 14.5 ,'惠生连圩堤');
INSERT INTO `three_line` (`STCD`, `SFSW`, `JJSW`, `BZSW`, `NAME`) VALUES (62904400, 11.5, 13.2, 15.84 ,'永定大圩堤');
INSERT INTO `three_line` (`STCD`, `SFSW`, `JJSW`, `BZSW`, `NAME`) VALUES (62904400, 11.0, 13.0, 13.5 ,'黑沙洲、天然洲圩');
```

## 查找数据

### 查找三线水位数据

```sql
SELECT * FROM `three_line`
```

```
+----+----------+-------+-------+-------+------+
| ID | STCD     | SFSW  | JJSW  | BZSW  | NAME |
+----+----------+-------+-------+-------+------+
|  1 | 62904400 | 11.50 | 13.20 | 15.84 |      |
|  2 | 60115400 |  9.40 | 11.20 | 13.40 |      |
|  3 | 62900700 |  8.70 | 10.70 | 12.70 |      |
|  4 | 62906500 | 10.10 | 12.10 | 14.10 |      |
|  5 | 62900700 |  9.40 | 11.20 | 12.30 |      |
|  6 | 62900600 |  9.50 | 10.50 | 12.00 |      |
|  7 | 62905100 |  8.50 |  9.50 | 11.50 |      |
|  8 | 62904400 | 11.50 | 13.20 | 14.50 |      |
|  9 | 62904400 | 11.50 | 13.20 | 15.84 |      |
| 10 | 62904400 | 11.00 | 13.00 | 13.50 |      |
+----+----------+-------+-------+-------+------+
```