# 水位爬虫 (water-spider)

[![GitHub stars](https://img.shields.io/github/stars/BadRuan/water-spider?style=social)](https://github.com/BadRuan/water-spider)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](https://makeapullrequest.com)
[![Python 3.12+](https://img.shields.io/badge/python-3.12+-blue.svg)](https://www.python.org/downloads/)

[安徽省水信息系统](http://ahswj.cn/ahsxx/LOL/?refer=upl&to=public_public) **水情信息**专题网站水位数据爬虫。

自动爬取指定水文站点的水位数据，经过解密处理后存储至 [PostgreSQL](https://www.postgresql.org/) 数据库。

## 项目架构

```
water-spider/
├── main.py                # 入口文件
├── src/
│   ├── settings.py        # 配置管理（环境变量、站点列表）
│   ├── model.py           # 数据模型定义
│   ├── engine.py          # 爬虫调度引擎
│   ├── handle.py          # 责任链处理器（请求 → 解密 → 存储）
│   └── utils/
│       ├── logger.py      # 日志模块（控制台 + 文件轮转）
│       ├── datetool.py    # 日期范围切割工具
│       ├── security.py    # 数据加解密
│       └── storage.py     # 数据库操作（asyncpg 连接池）
├── .env                   # 环境变量（不纳入版本控制）
├── Dockerfile             # Docker 容器化部署
├── pyproject.toml         # 项目元数据与依赖
└── requirements.txt       # 依赖锁定
```

## 数据流程

```
目标时间范围
    │
    ▼
构建加密请求参数 ──▶ 发送 API 请求（支持自动重试）
    │
    ▼
解析加密响应数据 ──▶ 解密还原为 JSON
    │
    ▼
提取水位记录 ──▶ 批量写入 PostgreSQL（参数化查询，ON CONFLICT 去重）
```

## 设计模式

### 责任链模式 (Chain of Responsibility)

数据处理采用责任链模式，各环节单向流动、互不耦合：

```
SendApiHandler  ──▶  DecodeHandler  ──▶  StorageHandle
   (发送请求)          (解密数据)           (存储入库)
```

每个 Handler 只关心自己的职责，通过 `set_next()` 串联，易于扩展新的处理环节。

### 单例模式

加密工具 (`WaterSecurity`) 和解析器 (`Parser`) 采用线程安全的元类单例，避免重复初始化开销。

## 运行模式

### 1. 24 小时轮询模式（默认）

```python
await spider.run_in_24_hour()
```

持续运行，每轮获取最近 2 天数据，轮间随机休眠 100~600 秒。

### 2. 获取今年全年数据

```python
await spider.get_this_year_full_data()
```

自动按 20 天切割时间范围，逐步获取从今年 1 月 1 日至今的全部数据。

### 3. 获取指定年份数据

```python
await spider.get_target_year_full_data(2024)
```

获取指定年份 1 月 1 日至 12 月 31 日的全部数据。

### 4. 获取指定时间范围数据

```python
await spider.get_target_daterange_range_data("202401010000", "202406010000")
```

时间格式：`YYYYMMDDHHmm`，大范围自动切割。

## 快速开始

### 环境要求

- Python 3.12+
- PostgreSQL 数据库

### 安装

本项目使用 [uv](https://docs.astral.sh/uv/) 管理依赖：

```bash
# 克隆项目
git clone https://github.com/BadRuan/water-spider.git
cd water-spider

# 安装依赖
uv sync
```

### 配置

创建 `.env` 文件：

```env
# PostgreSQL 连接地址
DATABASE_URL=postgresql://user:password@host:port/database

# 时区（影响日志和数据库会话）
TIMEZONE=Asia/Shanghai
```

### 数据库表结构

为每个站点创建对应的表，以芜湖站为例：

```sql
CREATE TABLE station_60115400 (
    ts       TIMESTAMP PRIMARY KEY,  -- 观测时间
    height   NUMERIC                 -- 水位高度（米）
);
```

表名格式：`station_{站点编码}`，站点编码见 `src/settings.py` 中的配置。

### 运行

```bash
# 24 小时轮询模式
uv run python main.py

# 或在代码中调用其他模式
# uv run python -c "from asyncio import run; from src.engine import spider; run(spider.get_this_year_full_data())"
```

### Docker 部署

```bash
# 构建镜像
docker build -t water-spider .

# 运行容器
docker run -d \
  --name water-spider \
  -e DATABASE_URL=postgresql://user:password@host:port/database \
  -e TIMEZONE=Asia/Shanghai \
  water-spider
```

## 监控的站点

| 站点编码 | 站点名称 |
|----------|----------|
| 60115400 | 芜湖 |
| 62904400 | 凤凰颈新站闸上 |
| 62904500 | 凤凰颈新站闸下 |
| 62900700 | 裕溪闸下 |
| 62900600 | 裕溪闸上 |
| 62906500 | 清水 |
| 62905100 | 新桥闸上 |

新增站点只需在 `src/settings.py` 的 `_station_tuples` 列表中添加 `(编码, 名称)` 元组，并在数据库中创建对应的表。

## 技术栈

| 组件 | 技术 |
|------|------|
| 异步运行时 | Python asyncio |
| HTTP 客户端 | [httpx](https://www.python-httpx.org/)（异步） |
| 数据库驱动 | [asyncpg](https://magicstack.github.io/asyncpg/)（异步 PostgreSQL） |
| 配置管理 | [pydantic-settings](https://docs.pydantic.dev/latest/concepts/pydantic_settings/) |
| 日志 | logging + [Rich](https://rich.readthedocs.io/) |
| 容器化 | Docker (python:3.12-slim) |

## License

[MIT](LICENSE)
