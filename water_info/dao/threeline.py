from dao.mysqltool import MySQLTool

class ThreelineDao:

    def __init__(self) -> None:
        self.m = MySQLTool()

    def create_threeline_table(self) -> int:
        SQL = """CREATE TABLE IF NOT EXISTS `three_line` (
                    `ID` int(11) NOT NULL AUTO_INCREMENT,
                    `STCD` int(11) NOT NULL,
                    `SFSW` float(4, 2) NOT NULL,
                    `JJSW` float(4, 2) NOT NULL,
                    `BZSW` float(4, 2) NOT NULL,
                    `NAME` varchar(255) COLLATE utf8_bin NOT NULL,
                    PRIMARY KEY (`ID`)
                ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin
                AUTO_INCREMENT=1 ;"""
        return self.m.execute(SQL)

    # 插入三线数据
    def insert_three_line(self, STCD: int, SFSW: float, JJSW: float, BZSW: float,NAME: str) -> int:
        SQL = f"INSERT INTO `three_line` (`STCD`, `SFSW`, `JJSW`, `BZSW`, `NAME`) VALUES ('{STCD}', {SFSW}, {JJSW}, {BZSW}, '{NAME}')"
        return self.m.execute_insert(SQL)
    
    # 获取所有三线数据
    def get_all_three_line_list(self) -> list:
        SQL = "SELECT * FROM `three_line`"
        res_data = self.m.execute_fetchall(SQL)
        return res_data
    
    # 关闭数据库连接
    def close(self):
        self.dao.close()