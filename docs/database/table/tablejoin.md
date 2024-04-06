# 多表连接查询

## 查找鸠江区测站三线水位数据
采用多表联查，包含最新水位数据

SQL语句：
```sql
SELECT 
	tl.NAME AS localStationNAme,
    sc.NAME AS StationName,
    tl.SFSW AS SFSW,
    tl.JJSW AS JJSW,
    tl.BZSW AS BZSW,
    wl.Z AS LatestWaterLevel,
    wl.TM AS LatestTime
FROM 
    station_code sc
JOIN 
    three_line tl ON sc.STCD = tl.STCD
JOIN 
    (
        SELECT STCD, MAX(TM) AS MaxTime
        FROM water_level
        GROUP BY STCD
    ) max_wl ON sc.STCD = max_wl.STCD
JOIN 
    water_level wl ON sc.STCD = wl.STCD AND max_wl.MaxTime = wl.TM;
```