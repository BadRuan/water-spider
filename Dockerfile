FROM python:latest
WORKDIR /app
COPY src/ .
RUN pip install --trusted-host https://mirrors.huaweicloud.com -i https://mirrors.huaweicloud.com/repository/pypi/simple -r requirements.txt
CMD ["python", "app.py"]