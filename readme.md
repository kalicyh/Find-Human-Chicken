# 人坤检测

## 启动项目

```
docker-compose up
```

启动后找到当前目录下的data目录，`docker-compose.yml`在哪里=`data`就在哪里

拷贝出`mitmproxy-ca-cert.cer`也就是手机端证书


## 配置手机

1. 安装手机端证书
- 电脑用户: 将`手机端证书.cer`文件拷贝到手机。
- 服务器/NAS用户: 使用Finalshell将`手机端证书.cer`文件下载到手机。
2. 打开手机设置，找到“安全和隐私”或“安全”选项
- 选择“证书”或“信任证书”
- 点击“从存储设备安装”
- 选择`手机端证书.cer`文件并安装

安卓手机安装模块 `MoveCertificate-v1.5.1.zip`


---
原文：https://www.coolapk.com/feed/60320350