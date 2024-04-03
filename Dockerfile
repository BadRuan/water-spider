FROM python:latest
WORKDIR /app
COPY water_info .
RUN pip install --trusted-host https://mirrors.huaweicloud.com -i https://mirrors.huaweicloud.com/repository/pypi/simple -r requirements.txt
CMD ["python", "main.py"]