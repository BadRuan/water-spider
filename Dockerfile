FROM docker.1ms.run/library/python:latest
ENV TZ=Asia/Shanghai
WORKDIR /app
COPY . /app
RUN pip install --trusted-host https://mirrors.huaweicloud.com -i https://mirrors.huaweicloud.com/repository/pypi/simple -r requirements.txt 
CMD ["python", "main.py"]