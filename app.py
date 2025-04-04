

from flask import Flask, request, send_file, send_from_directory, jsonify
from flask_cors import CORS
import base64
import soundfile as sf
from pydub import AudioSegment
import simpleaudio as sa
from openai import OpenAI
import sys
from dashscope.audio.tts import SpeechSynthesizer
import dashscope
import io
import os
import traceback

# 创建Flask应用并启用CORS ---AI写的
app = Flask(__name__)
CORS(app)

# 创建OpenAI客户端实例  ---API文档里的
client = OpenAI(
    api_key="ALIYUN_API_KEY",
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
)
# 设置 DashScope API Key  ---API文档里的
dashscope.api_key = "ALIYUN_API_KEY"


# 定义音频编码函数 ---API文档里的
def encode_audio(audio_path):
    with open(audio_path, "rb") as audio_file:
        return base64.b64encode(audio_file.read()).decode("utf-8")


# 定义教材知识库-----AI写的
textbook = {
    "L0": {
        "level": "beginners",
        "words": ["hello", "goodbye", "please", "thank you", "yes"],
        "sentences": [
            "Hello, how are you?",
            "Goodbye, see you later.",
            "Please pass me the salt.",
            "Thank you very much.",
            "Yes, I can help you.",
        ],
    },
    "L1": {
        "level": "intermediate learners",
        "words": ["restaurant", "reservation", "menu", "order", "dessert"],
        "sentences": [
            "Can I make a reservation?",
            "What's on the menu?",
            "I'd like to order the steak.",
            "Do you have any dessert options?",
            "The service was excellent.",
        ],
    },
    "L2": {
        "level": "advanced learners",
        "words": ["discourse", "eloquence", "eloquent", "eloquently", "eloquence"],
        "sentences": [
            "His discourse was both eloquent and insightful.",
            "She demonstrated remarkable eloquence in her speech.",
            "He spoke eloquently about the topic.",
            "Her eloquence was evident in her writing.",
            "The eloquence of the oration was impressive.",
        ],
    },
}

# 选择教材级别（L0, L1, L2）---AI写的
textbook_level = "L1"


# 添加一个新的路由来设置课程级别
@app.route("/set_level", methods=["POST"])
def set_level():
    global textbook_level
    data = request.json
    new_level = data.get("level")

    # 验证级别是否有效
    if new_level in textbook:
        textbook_level = new_level
        print(f"课程级别已更新为: {textbook_level}")  # 添加日志
        return jsonify({"status": "success", "level": textbook_level})
    else:
        print(f"无效的课程级别: {new_level}")  # 添加日志
        return jsonify({"status": "error", "message": "Invalid level"}), 400


# 动态设置 system 角色的内容 ---AI写的
level_info = textbook[textbook_level]
system_message = (
    f"You're an English teacher and you like pink. You are having a conversation with your student. Your aim is to teach him English. "
    f"The class you're talking to is {level_info['level']}. "
    f"Here are some words and sentences for your class:\n"
    f"Words: {', '.join(level_info['words'])}\n"
    f"Sentences:\n- " + "\n- ".join(level_info["sentences"])
)


# 定义接收前端录音文件的函数 ---AI写的
# 修改 process_audio 函数定义
def process_audio(audio_data, system_message):
    try:
        # 保存原始音频文件
        input_file = "temp.webm"  # 改为 .webm 扩展名
        with open(input_file, "wb") as f:
            f.write(audio_data)
        print(f"音频文件已保存：{input_file}")

        # 打印文件大小
        print(f"音频文件大小：{os.path.getsize(input_file)} bytes")

        # 使用 pydub 转换音频
        audio = AudioSegment.from_file(input_file)  # 不指定格式，让 pydub 自动检测

        # 直接导出为 wav
        output_wav = "temp.wav"
        audio.export(output_wav, format="wav")
        print(f"WAV文件已生成：{output_wav}")

        # 对本地音频文件进行Base64编码
        base64_audio = encode_audio(output_wav)
        print("音频文件已编码为Base64格式")

        # 调用API进行多模态对话
        print("正在调用 API...")
        completion = client.chat.completions.create(
            model="qwen-omni-turbo",
            messages=[
                {
                    "role": "system",
                    "content": [{"type": "text", "text": system_message}],
                },
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "input_audio",
                            "input_audio": {
                                "data": f"data:audio/mp3;base64,{base64_audio}",
                                "format": "mp3",
                            },
                        },
                        {"type": "text", "text": "教我学英语"},
                    ],
                },
            ],
            modalities=["text"],
            stream=True,
            stream_options={"include_usage": True},
        )
        print("API 调用完成")

        # 处理响应
        text = []
        for chunk in completion:
            if chunk.choices:
                if hasattr(chunk.choices[0].delta, "content"):
                    content = chunk.choices[0].delta.content
                    if isinstance(content, str):
                        text.append(content)

        final_text = "".join(text)
        print(f"生成的文本：{final_text}")

        # 语音合成
        result = SpeechSynthesizer.call(
            model="sambert-zhimiao-emo-v1",
            text=final_text,
            sample_rate=16000,
            format="wav",
        )

        if result.get_audio_data() is not None:
            output_wav = "output.wav"
            with open(output_wav, "wb") as f:
                f.write(result.get_audio_data())
            print(f"生成的音频已保存：{output_wav}")
            return output_wav
        else:
            print(f"语音合成失败：{result.get_response()}")
            return None

    except Exception as e:
        print(f"处理音频时出错：{str(e)}")
        traceback.print_exc()  # 打印详细的错误堆栈
        return None


# 定义根路径路由来提供 index.html ---AI写的
@app.route("/")
def index():
    # 使用当前目录下的index.html
    return send_from_directory(".", "index.html")


# 定义上传音频文件的反馈函数 ---AI写的
# 在 app.py 文件中修改 upload_audio 函数

@app.route("/upload", methods=["POST"])
def upload_audio():
    global textbook_level
    
    try:
        # 打印当前使用的课程级别（调试用）
        print(f"处理音频上传，当前课程级别: {textbook_level}")
        
        if "audio" not in request.files:
            print("没有收到音频文件")
            return "No audio file part", 400

        file = request.files["audio"]
        if file.filename == "":
            print("文件名为空")
            return "No selected file", 400

        if file:
            print("开始处理音频文件...")
            audio_data = file.read()
            
            # 确保使用最新的课程级别
            current_level = textbook_level
            print(f"使用课程级别: {current_level}")
            
            # 使用当前选择的课程级别
            level_info = textbook[current_level]
            
            # 动态设置 system 角色的内容
            system_message = (
                f"You're an English teacher and you like pink. You are having a conversation with your student. Your aim is to teach him English. "
                f"The class you're talking to is {level_info['level']}. "
                f"Here are some words and sentences for your class:\n"
                f"Words: {', '.join(level_info['words'])}\n"
                f"Sentences:\n- " + "\n- ".join(level_info["sentences"])
            )
            
            # 将 system_message 传递给 process_audio 函数
            wav_file_path = process_audio(audio_data, system_message)

            if wav_file_path:
                print(f"音频处理成功，返回文件：{wav_file_path}")
                try:
                    return send_file(
                        wav_file_path,
                        mimetype="audio/wav",
                        as_attachment=True,
                        download_name="response.wav",
                    )
                except Exception as e:
                    print(f"发送文件时出错：{str(e)}")
                    return f"Error sending file: {str(e)}", 500
            else:
                print("音频处理失败")
                return "Error processing audio", 500

    except Exception as e:
        print(f"处理请求时出错：{str(e)}")
        traceback.print_exc()  # 打印详细的错误堆栈
        return f"Error processing request: {str(e)}", 500


# 当 app.py 被直接运行时，启动一个 Flask 开发服务器。
# 服务器会在 0.0.0.0:5010 地址上监听请求，并启用调试模式以便于开发和调试。
# ---AI写的
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5010)
