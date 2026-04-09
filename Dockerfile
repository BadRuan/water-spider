FROM python:latest
WORKDIR /var/lib/app
COPY src .
RUN pip install --trusted-host https://mirrors.huaweicloud.com -i https://mirrors.huaweicloud.com/repository/pypi/simple -r requirements.txt 
ENV POST_HOST=100.95.218.64 PSOT_USER=root POST_PASS=E,*f*YdGgYSgqfze1tLqc0Pm8CK2 POST_PORT=44455
CMD ["python", "main.py"]