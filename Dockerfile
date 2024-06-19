FROM python:latest
ENV TZ Asia/Shanghai
WORKDIR /app
COPY src .
RUN pip install --no-cache-dir -r requirements.txt
CMD ["python", "main.py"]
