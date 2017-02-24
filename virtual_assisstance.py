import pygame
import pyaudio
import wave
from gtts import gTTS
import os
import speech_recognition as sr
def record_audio():
	FORMAT = pyaudio.paInt16
	CHANNELS = 2
	RATE = 44100
	CHUNK = 1024
	RECORD_SECONDS = 5
	WAVE_OUTPUT_FILENAME = "\\tmp\\file.wav"
 
	audio = pyaudio.PyAudio()
 
	# start Recording
	stream = audio.open(format=FORMAT, channels=CHANNELS,rate=RATE, input=True,frames_per_buffer=CHUNK)
	print "recording..."
	frames = []
 
	for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
		data = stream.read(CHUNK)
		frames.append(data)
	print "finished recording"
	# stop Recording
	stream.stop_stream()
	stream.close()
	audio.terminate()
 
	waveFile = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
	waveFile.setnchannels(CHANNELS)
	waveFile.setsampwidth(audio.get_sample_size(FORMAT))
	waveFile.setframerate(RATE)
	waveFile.writeframes(b''.join(frames))
	waveFile.close()
def play_audio(audio_loc):
	pygame.mixer.init()
	pygame.mixer.music.load(audio_loc)
	pygame.mixer.music.play()
	while pygame.mixer.music.get_busy() == True:
		continue
def speech_recognize():
	AUDIO_FILE="\\tmp\\file.wav"
	r = sr.Recognizer()
	with sr.AudioFile(AUDIO_FILE) as source:
		audio = r.record(source)
	try:
		r=r.recognize_sphinx(audio)
		print(r)
	except sr.UnknownValueError:
		print("Sphinx could not understand audio")
	except sr.RequestError as e:
		print("Sphinx error; {0}".format(e))
welcome = gTTS(text='Hello, Master Akshay.What can i do for you', lang='en')
welcome.save("//tmp//temp.mp3")
play_audio("//tmp//temp.mp3")
print("Press 1 to ask any thing ")
x=input(">")
if x == 1:
	record_audio()
	speech_recognize()
