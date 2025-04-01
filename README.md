**AI_spoken_language_teaching**

## 项目概述

AI_spoken_language_teaching 是一个基于 AI 的英语口语教学软件，旨在为孩子提供个性化的一对一口语教学服务。通过精准评估孩子的口语水平，软件能够匹配最适合的课程级别和教程，配合 AI 外教的自然对话练习，全面提高孩子的听说能力。

## 核心功能

* **个性化课程匹配** ：根据孩子的口语水平，精准匹配课程级别和教程，实现个性化教学。
* **AI 外教一对一对话练习** ：AI 外教凭借强大的语言交互能力，与孩子进行自然、流畅的对话练习，从日常交流到主题讨论，全面锻炼听说能力。

## 技术亮点

1. **前沿 AI 大模型** ：软件采用今年 3 月最新推出的多模态 AI 大模型，支持文本、图像、语音和视频等多模态输入，具备出色的自然语言理解和生成能力，能实时理解孩子的表达意图，并给出准确、自然的回应。
2. **语音合成技术** ：集成先进的文字转语音模块，AI 外教的语音输出清晰、自然，富有情感，营造沉浸式的语言学习环境。
3. **丰富的教程知识库** ：内置指定的英语教程知识库，涵盖从基础到高阶的各类学习内容，并支持实时更新，确保教学内容与时俱进。

## 项目架构

![AI 外教一对一口语教学软件架构设计图](https://github.com/Sunstarluna/AI_spoken_language_teaching/blob/main/assets/architecture_diagram.png)

## 安装指南

遵循以下步骤，您可以在本地环境中安装并配置 AI_spoken_language_teaching 软件。

1. **确认 Python 版本**
   确保您的系统中已安装 Python 3.10 或更高版本。您可以使用以下命令检查 Python 版本：

   <pre><div class="CodeBlockWrapper-gJHgOG bFWpew code-block"><div class="CodeHeader-kZBWoT dBDUBA"><div><div class="CodeLanguage-cvUWFC emAjim"><TEXT></div></div><div class="Box-hNxnGY Stack-cqVNEr HStack-dDxHab bBHTRB jTolXW gcygOE"><i class="iconfont icon-copy copy"></i></div></div><div class="CodeContent-fSMUHF bmLmts"><pre class="shiki one-light" tabindex="0"><code><span class="line"><span>python3 --version</span></span></code></pre></div></div></pre>
2. **下载源码**
   使用 Git 下载项目源码：

   <pre><div class="CodeBlockWrapper-gJHgOG bFWpew code-block"><div class="CodeHeader-kZBWoT dBDUBA"><div><div class="CodeLanguage-cvUWFC emAjim"><TEXT></div></div><div class="Box-hNxnGY Stack-cqVNEr HStack-dDxHab bBHTRB jTolXW gcygOE"><i class="iconfont icon-copy copy"></i></div></div><div class="CodeContent-fSMUHF bmLmts"><pre class="shiki one-light" tabindex="0"><code><span class="line"><span>git clone https://github.com/Sunstarluna/AI_spoken_language_teaching</span></span></code></pre></div></div></pre>

   然后，切换到项目目录：

   <pre><div class="CodeBlockWrapper-gJHgOG bFWpew code-block"><div class="CodeHeader-kZBWoT dBDUBA"><div><div class="CodeLanguage-cvUWFC emAjim"><TEXT></div></div><div class="Box-hNxnGY Stack-cqVNEr HStack-dDxHab bBHTRB jTolXW gcygOE"><i class="iconfont icon-copy copy"></i></div></div><div class="CodeContent-fSMUHF bmLmts"><pre class="shiki one-light" tabindex="0"><code><span class="line"><span>cd AI_spoken_language_teaching</span></span></code></pre></div></div></pre>
3. **安装依赖**
   使用 pip 安装项目所需的依赖包：

   <pre><div class="CodeBlockWrapper-gJHgOG bFWpew code-block"><div class="CodeHeader-kZBWoT dBDUBA"><div><div class="CodeLanguage-cvUWFC emAjim"><TEXT></div></div><div class="Box-hNxnGY Stack-cqVNEr HStack-dDxHab bBHTRB jTolXW gcygOE"><i class="iconfont icon-copy copy"></i></div></div><div class="CodeContent-fSMUHF bmLmts"><pre class="shiki one-light" tabindex="0"><code><span class="line"><span>pip3 install -r requirements.txt</span></span></code></pre></div></div></pre>

   此外，还需要安装以下软件包：

   <pre><div class="CodeBlockWrapper-gJHgOG bFWpew code-block"><div class="CodeHeader-kZBWoT dBDUBA"><div><div class="CodeLanguage-cvUWFC emAjim"><TEXT></div></div><div class="Box-hNxnGY Stack-cqVNEr HStack-dDxHab bBHTRB jTolXW gcygOE"><i class="iconfont icon-copy copy"></i></div></div><div class="CodeContent-fSMUHF bmLmts"><pre class="shiki one-light" tabindex="0"><code><span class="line"><span>pip3 install flask</span></span><span class="line"><span>pip3 install flask-cors</span></span><span class="line"><span>pip3 install pydub</span></span></code></pre></div></div></pre>
4. **系统配置**

   * 更新系统软件包列表：
     <pre><div class="CodeBlockWrapper-gJHgOG bFWpew code-block"><div class="CodeHeader-kZBWoT dBDUBA"><div><div class="CodeLanguage-cvUWFC emAjim"><TEXT></div></div><div class="Box-hNxnGY Stack-cqVNEr HStack-dDxHab bBHTRB jTolXW gcygOE"><i class="iconfont icon-copy copy"></i></div></div><div class="CodeContent-fSMUHF bmLmts"><pre class="shiki one-light" tabindex="0"><code><span class="line"><span>sudo apt update</span></span></code></pre></div></div></pre>
   * 安装声音和多媒体相关软件包：
     <pre><div class="CodeBlockWrapper-gJHgOG bFWpew code-block"><div class="CodeHeader-kZBWoT dBDUBA"><div><div class="CodeLanguage-cvUWFC emAjim"><TEXT></div></div><div class="Box-hNxnGY Stack-cqVNEr HStack-dDxHab bBHTRB jTolXW gcygOE"><i class="iconfont icon-copy copy"></i></div></div><div class="CodeContent-fSMUHF bmLmts"><pre class="shiki one-light" tabindex="0"><code><span class="line"><span>sudo apt install python3-dev libasound2-dev</span></span></code></pre></div></div></pre>
   * 安装 FFmpeg 和 libsndfile1：
     <pre><div class="CodeBlockWrapper-gJHgOG bFWpew code-block"><div class="CodeHeader-kZBWoT dBDUBA"><div><div class="CodeLanguage-cvUWFC emAjim"><TEXT></div></div><div class="Box-hNxnGY Stack-cqVNEr HStack-dDxHab bBHTRB jTolXW gcygOE"><i class="iconfont icon-copy copy"></i></div></div><div class="CodeContent-fSMUHF bmLmts"><pre class="shiki one-light" tabindex="0"><code><span class="line"><span>sudo apt install ffmpeg libsndfile1</span></span></code></pre></div></div></pre>
   * 安装 Python 3 开发工具：
     <pre><div class="CodeBlockWrapper-gJHgOG bFWpew code-block"><div class="CodeHeader-kZBWoT dBDUBA"><div><div class="CodeLanguage-cvUWFC emAjim"><TEXT></div></div><div class="Box-hNxnGY Stack-cqVNEr HStack-dDxHab bBHTRB jTolXW gcygOE"><i class="iconfont icon-copy copy"></i></div></div><div class="CodeContent-fSMUHF bmLmts"><pre class="shiki one-light" tabindex="0"><code><span class="line"><span>sudo apt install python3-dev</span></span></code></pre></div></div></pre>
   * 安装 simpleaudio：
     <pre><div class="CodeBlockWrapper-gJHgOG bFWpew code-block"><div class="CodeHeader-kZBWoT dBDUBA"><div><div class="CodeLanguage-cvUWFC emAjim"><TEXT></div></div><div class="Box-hNxnGY Stack-cqVNEr HStack-dDxHab bBHTRB jTolXW gcygOE"><i class="iconfont icon-copy copy"></i></div></div><div class="CodeContent-fSMUHF bmLmts"><pre class="shiki one-light" tabindex="0"><code><span class="line"><span>pip3 install simpleaudio</span></span></code></pre></div></div></pre>
5. **注意**
   项目使用的模型是多模态的通义千问 2.5-Omni-7B 模型和 Sambert 语音合成模型。在项目代码中，API-KEY 需要替换为阿里云的 API-KEY。
