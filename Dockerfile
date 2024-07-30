# 使用官方的 Python 运行时作为父镜像
FROM python:3.10-slim

# 设置工作目录
WORKDIR /usr/src/app

# 将当前目录的内容复制到容器中的 /usr/src/app
COPY . .

# 安装依赖包
RUN pip install --no-cache-dir -r requirements.txt

# 声明运行时容器将监听的端口
EXPOSE 5000

# 定义环境变量
ENV NAME World

# 运行 Flask 应用
CMD ["python", "app.py"]