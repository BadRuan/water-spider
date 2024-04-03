# 配置环境及源码编译
基于Dataease源码构建运行环境

## 源码安装方式
- 安装JDK
- 安装Git
- 安装Node JS
- 安装Maven

创建``Dockerfile``文件实现配置环境及源码编译：
```dockerfile
FROM ubuntu:latest
WORKDIR /root
RUN apt-get update \
    && apt-get upgrade -y \
    && apt-get install -y wget \
    && apt-get install -y git \
    && apt install -y openjdk-17-jdk \
    && wget https://dlcdn.apache.org/maven/maven-3/3.9.6/binaries/apache-maven-3.9.6-bin.tar.gz \
    && tar zxvf apache-maven-3.9.6-bin.tar.gz \
    && mv apache-maven-3.9.6 /opt \
    && echo "export M2_HOME=/opt/apache-maven-3.9.6" >> ~/.bashrc \
    && echo "export PATH=\$PATH:\$M2_HOME/bin" >> ~/.bashrc \
    && source ~/.bashrc \
    && apt-get install -y xz-utils \
    && wget https://nodejs.org/dist/v16.15.0/node-v16.15.0-linux-x64.tar.xz \
    && tar xvf node-v16.15.0-linux-x64.tar.xz \
    && mv node-v16.15.0-linux-x64 /opt \
    && echo "export PATH=\$PATH:/opt/node-v16.15.0-linux-x64/bin" >> ~/.bashrc \
    && source ~/.bashrc \
    && git clone -b v2.3 https://gitee.com/fit2cloud-feizhiyun/DataEase.git \
    && cd DataEase \
    && mvn clean install \
    && cd core \
    && mvn clean package -Pstandalone -U -Dmaven.test.skip=true
```
Dockerfile经测试能成功生成CoreApplication.jar包。