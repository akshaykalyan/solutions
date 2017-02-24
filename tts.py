from gtts import gTTS
import os
tts = gTTS(text='he is an ass hole', lang='en')
tts.save("good.mp3")
os.system("mpg321 good.mp3")

