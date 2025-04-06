# AI_spoken_language_teaching
AI外教一对一口语教学（可按课程智能教学）

## 核心功能——量身定制的专属口语课堂
本软件能精准评估孩子的口语水平，并据此匹配特定的课程级别和教程，实现个性化教学。AI外教凭借强大的语言交互能力，与孩子进行自然、流畅的一对一对话练习，从日常交流到主题讨论，全面锻炼孩子的听说能力。

## 多模态AI与智能交互的完美融合
1. 前沿AI大模型：软件依托今年3月最新推出的多模态AI大模型，这个多模态ai模型支持文本, 图像，语音，视频输入理解和混合输入理解，具备文本和语音同时流式生成能力。所以该模型具备出色的语言理解和生成能力，能实时理解孩子的表达意图，并给出准确、自然的回应。
2. 语音合成技术：集成先进的文字转语音模块，AI外教的语音输出清晰、自然，富有情感，营造沉浸式的语言学习环境。
3. 教程知识库：内置丰富的指定英语教程知识库，涵盖从基础到高阶的各类学习内容，且支持实时更新，确保教学内容与时俱进。

## 项目架构设计图
![AI外教一对一口语教学软件架构设计图](https://github.com/user-attachments/assets/6f149f8a-9080-45f9-8ec4-53bee1b00467)

## 安装步骤
### 1、确认python版本
**检查python版本,至少3.10**

python3 --version

### 2、下载源码/安装依赖/配置
**下载源码**

git clone https://github.com/Sunstarluna/AI_spoken_language_teaching

**切换到项目文件目录**

cd AI_spoken_language_teaching

**安装依赖**
sudo apt update
sudo apt install python3-pip

pip3 install Flask
pip3 install flask-cors
pip3 install openai
pip3 install dashscope
pip3 install pydub
pip3 install simpleaudio
pip3 install soundfile

### 注意
项目里的模型采用的是多模态的通义千问2.5-Omni-7B模型 和 Sambert语音合成模型。项目代码里的API-KEY 请替换为 aliyun的API-KEY。


