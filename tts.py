from gtts import gTTS
import os
x=input(">")
tts = gTTS(text=x, lang='en')
tts.save("good.mp3")
os.system("mpg321 good.mp3")

