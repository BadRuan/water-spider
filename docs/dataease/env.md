# 配置环境及源码编译
基于Dataease源码构建运行环境

## 源码安装方式
- 安装JDK
- 安装Git
- 安装Node JS
- 安装Maven

1. 创建``Dockerfile``文件实现配置环境及源码编译：
```dockerfile
FROM ubuntu:latest
WORKDIR /root
RUN apt-get update \
    && apt-get upgrade -y \
    && apt-get install -y wget git openjdk-17-jdk xz-utils \
    && wget https://dlcdn.apache.org/maven/maven-3/3.9.6/binaries/apache-maven-3.9.6-bin.tar.gz \
    && wget https://nodejs.org/dist/v16.15.0/node-v16.15.0-linux-x64.tar.xz \
    && tar zxvf apache-maven-3.9.6-bin.tar.gz \
    && tar xvf node-v16.15.0-linux-x64.tar.xz \
    && mv apache-maven-3.9.6 /opt \
    && mv node-v16.15.0-linux-x64 /opt \
    && echo "export M2_HOME=/opt/apache-maven-3.9.6" >> ~/.bashrc \
    && echo "export PATH=\$PATH:\$M2_HOME/bin" >> ~/.bashrc \
    && echo "export PATH=\$PATH:/opt/node-v16.15.0-linux-x64/bin" >> ~/.bashrc \
    && source ~/.bashrc \
    && git clone -b v2.3 https://gitee.com/fit2cloud-feizhiyun/DataEase.git \
    && cd DataEase \
    && mvn clean install \
    && cd core \
    && mvn clean package -Pstandalone -U -Dmaven.test.skip=true
EXPOSE 8100
```
Dockerfile经测试能成功生成CoreApplication.jar包。

2. 构建Dataease运行环境:
```shell
docker build -t dataease_env:v1 .
```

3. 运行Docker容器
```shell
docker run -it --name my-dataease -v ./dataease:/root/DataEase/ -P dataease_env:v1
```