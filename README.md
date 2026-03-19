# 水位爬虫

[![GitHub stars](https://img.shields.io/github/stars/BadRuan/water-spider?style=social)](https://github.com/BadRuan/water-spider)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](https://makeapullrequest.com)
[![License](https://img.shields.io/badge/license-MIT-blue?style=for-the-badge)](LICENSE)
![Static Badge](https://img.shields.io/badge/Python-3.12-blue)
![https://img.shields.io/badge/UV-20B2AA?style=for-the-badge](https://hellowac.github.io/uv-zh-cn/#script-support)

## What Is This?

[安徽省水信息系统](http://yc.wswj.net/ahsxx/LOL/?refer=upl&to=public_public)**水情信息**专题网站水位数据爬虫

爬取指定水文站点指定时间水文数据并保存至[PostgreSQL](https://www.postgresql.org/)数据库

## How to use?

使用uv安装

## 构思备忘

使用队列，数据单向流动，使用责任链设计模式：

1. 目标期望
2. API参数构建（构建加密请求）
3. 执行API访问
4. API访问失败，休息固定时间，再次执行步骤3；API访问成功
5. 解析获取的加密数据
6. 保存数据

根据访问目标（一次获取全年，或者24hour常态执行），将目标范围日期数据保存至队列中，按需求取出，逐个数据采集目标，若队列中访问目标消耗完毕，固定间隔时间后再查看队列是否为空，队列有数据就执行，保证爬虫采集频次不过高，间隔时间可设置随机数，变成随机间隔，防止机器识别。

一端存，一端取，固定时间取，每次取出的数据用来发送请求访问，请求发送获取数据并保存数据才为成功，否则再重试固定间隔次数后再次发送请求，需要有完善的日志系统，方便查看爬虫运行的数据（单次、每次数据），错误信息等。

Python**队列**思路雏形:

```python
from rich.console import Console
import queue
from time import sleep


console = Console()
q = queue.Queue()

q.put(1)
q.put(2)
q.put(3)
q.put(4)

def main():
    while True:
        console.print("准备拿数据")
        if q.empty() != True:
            console.print("队列有数据，可以拿")
            console.print(f"成功拿到数据: {q.get()}")
        else:
            console.print("队列无数据，不用拿")
        console.print("休息 2 秒,再执行下次动作")
        sleep(2)


if __name__ == "__main__":
    main()
```
