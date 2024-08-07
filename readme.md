# web-tts 一个基于edge-tts的文本转语音工具

## 1. 介绍

这是一个简单的文本转语音 (TTS) Web 应用程序，使用 Flask 框架和 Microsoft Azure 的 Edge TTS 服务。用户可以输入文本，选择不同的发音人声，并将文本转换成语音。

- **后端**: Flask
- **前端**: HTML, CSS, JavaScript
- **文本转语音**: Microsoft Azure Edge TTS

## 2. 功能

- 用户界面允许输入文本和选择不同的音色。
- 提交表单后，文本会被转换成 MP3 格式的语音文件。
- 用户可以播放、暂停和删除生成的语音文件。

![](./page_show.avif)

## 3. 快速开始

### 安装依赖

确保您已经安装了 Python 和 pip。然后安装所需的 Python 包：

```bash
pip install flask edge-tts
```

### 运行应用

从项目根目录运行以下命令启动 Flask 开发服务器：

```bash
python app.py
```

应用程序将在本地主机的默认端口 5000 上运行。打开浏览器并访问 [http://localhost:5000](http://localhost:5000) 来查看应用程序。

## 4. 文件结构
```sh
- webapp  #根目录  
  - templates     
    - index.html   # html页面
  - static
    - css
      - style.css  # 主样式表
    - audio
      - output.mp3 # 输出的语音文件     
  - app.py   # 主要的 Flask 应用程序脚本
```

## 5. docker



将`/docker/web-tts`替换为语音存放目录

将`5001`替换为你想要暴露的端口

**AMD64**

```sh
docker run -d -v /docker/web-tts:/usr/src/app/static/audio -p 5001:5000 --name web-tts sanqi37/web-tts
```

**ARM64**

```sh
docker run -d -v /docker/web-tts:/usr/src/app/static/audio -p 5001:5000 --name web-tts sanqi37/web-tts:1.0
```

