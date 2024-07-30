from flask import Flask, render_template, request
import asyncio
from edge_tts import Communicate
import os
from datetime import datetime

app = Flask(__name__)

DEFAULT_VOICE = {
    'Xiaoxiao-晓晓': 'zh-CN-XiaoxiaoNeural',
    'Yunyang-云扬': 'zh-CN-YunyangNeural',
    'Xiaoyi-晓伊': 'zh-CN-XiaoyiNeural',
    'Yunjian-云健': 'zh-CN-YunjianNeural',
    'Yunxi-云希': 'zh-CN-YunxiNeural',
    'Yunxia-云夏': 'zh-CN-YunxiaNeural',
    'liaoning-Xiaobei-晓北辽宁': 'zh-CN-liaoning-XiaobeiNeural',
    'shaanxi-Xiaoni-陕西晓妮': 'zh-CN-shaanxi-XiaoniNeural'
}

@app.route('/')
def home():
    print("Rendering index.html")
    return render_template('index.html', voices=DEFAULT_VOICE)

@app.route('/convert', methods=['POST'])
def convert():
    data = request.form
    text = data.get('text')
    voice = data.get('voice')

    if not text:
        return "Please enter some text."

    voice_id = DEFAULT_VOICE[voice]
    
    # 获取当前时间
    current_time = datetime.now().strftime('%H%M%S')

    # Get the first 10 characters of the text for the filename
    filename_base = text[:10].strip().replace(' ', '_')
    filename = f"{current_time}_{filename_base}.mp3"
    filepath = os.path.join('static/audio', filename)

    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(convert_to_speech(text, voice_id, filepath))
    loop.close()

    return filename

@app.route('/delete_audio/<filename>', methods=['DELETE'])
def delete_audio(filename):
    filepath = os.path.join('static/audio', filename)
    try:
        os.remove(filepath)
        return {'message': 'File deleted successfully.'}, 200
    except Exception as e:
        return {'error': str(e)}, 500
    
async def convert_to_speech(text, voice_id, filename):
    communicate = Communicate(text, voice_id)
    await communicate.save(filename)

if __name__ == '__main__':
    app.run(debug=True)