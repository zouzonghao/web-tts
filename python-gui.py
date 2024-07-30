import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QTextEdit, QPushButton, QComboBox
from PyQt5.QtCore import Qt
import asyncio
from edge_tts import Communicate

# Define the voices dictionary globally
DEFAULT_VOICE = {
    'Yunyang-云扬': 'zh-CN-YunyangNeural',
    'Xiaoxiao-晓晓': 'zh-CN-XiaoxiaoNeural',
    'Xiaoyi-晓伊': 'zh-CN-XiaoyiNeural',
    'Yunjian-云健': 'zh-CN-YunjianNeural',
    'Yunxi-云希': 'zh-CN-YunxiNeural',
    'Yunxia-云夏': 'zh-CN-YunxiaNeural',
    'liaoning-Xiaobei-晓北辽宁': 'zh-CN-liaoning-XiaobeiNeural',
    'shaanxi-Xiaoni-陕西晓妮': 'zh-CN-shaanxi-XiaoniNeural'
}

class TextToSpeechApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Text to Speech with edge_tts')
        layout = QVBoxLayout()

        # Text input
        text_layout = QVBoxLayout()
        self.text_label = QLabel('Text:')
        self.text_input = QTextEdit()
        self.text_input.setFixedHeight(200)  # Set fixed height for the text area
        self.text_input.setFixedWidth(300)  # Set fixed width for the text area
        text_layout.addWidget(self.text_label)
        text_layout.addWidget(self.text_input)
        layout.addLayout(text_layout)

        # Voice selection
        voice_layout = QHBoxLayout()
        self.voice_label = QLabel('Voice:')
        self.voice_combo = QComboBox()
        self.voice_combo.addItems(DEFAULT_VOICE.keys())
        voice_layout.addWidget(self.voice_label)
        voice_layout.addWidget(self.voice_combo)
        layout.addLayout(voice_layout)

        # Button
        self.convert_button = QPushButton('Convert to Speech')
        self.convert_button.clicked.connect(self.on_convert_clicked)
        layout.addWidget(self.convert_button)

        self.setLayout(layout)

    async def convert_to_speech(self, text, voice_id, filename):
        communicate = Communicate(text, voice_id)
        await communicate.save(filename)

    def on_convert_clicked(self):
        selected_voice = self.voice_combo.currentText()
        voice_id = DEFAULT_VOICE[selected_voice]
        text = self.text_input.toPlainText()  # Use toPlainText to get the text from QTextEdit

        if not text:
            print("Please enter some text.")
            return

        # Get the first 10 characters of the text for the filename
        filename = f"{text[:10].strip().replace(' ', '_')}.mp3"

        asyncio.run(self.convert_to_speech(text, voice_id, filename))
        print(f"Converted text to speech and saved as {filename}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = TextToSpeechApp()
    ex.show()
    sys.exit(app.exec_())