# 多表连接查询

## 查找鸠江区测站三线水位数据
SQL语句：
```sql
SELECT a.NAME, b.NAME, SFSW, JJSW, BZSW
FROM `three_line` a
LEFT JOIN `station_code` b
ON a.STCD=b.STCD
```
查询结果：
```
{'NAME': '无为大堤', 'b.NAME': '凤凰颈闸下', 'SFSW': 11.5, 'JJSW': 13.2, 'BZSW': 15.84}
{'NAME': '城北圩', 'b.NAME': '芜湖', 'SFSW': 9.4, 'JJSW': 11.2, 'BZSW': 13.4}
{'NAME': '江北（沈巷）长江堤', 'b.NAME': '裕溪闸下', 'SFSW': 8.7, 'JJSW': 10.7, 'BZSW': 12.7}
{'NAME': '万春圈堤', 'b.NAME': '清水', 'SFSW': 10.1, 'JJSW': 12.1, 'BZSW': 14.1}
{'NAME': '裕溪口江堤', 'b.NAME': '裕溪闸下', 'SFSW': 9.4, 'JJSW': 11.2, 'BZSW': 12.3}
{'NAME': '裕溪河堤', 'b.NAME': '裕溪闸上', 'SFSW': 9.5, 'JJSW': 10.5, 'BZSW': 12.0}
{'NAME': '牛屯河堤', 'b.NAME': '新桥闸上', 'SFSW': 8.5, 'JJSW': 9.5, 'BZSW': 11.5}
{'NAME': '惠生连圩堤', 'b.NAME': '凤凰颈闸下', 'SFSW': 11.5, 'JJSW': 13.2, 'BZSW': 14.5}
{'NAME': '永定大圩堤', 'b.NAME': '凤凰颈闸下', 'SFSW': 11.5, 'JJSW': 13.2, 'BZSW': 15.84}
{'NAME': '黑沙洲、天然洲圩', 'b.NAME': '凤凰颈闸下', 'SFSW': 11.0, 'JJSW': 13.0, 'BZSW': 13.5}
```