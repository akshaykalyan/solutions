from os import path
import speech_recognition as sr
AUDIO_FILE=path.join(path.dirname(path.realpath(__file__)), "male.wav")
r = sr.Recognizer()
with sr.AudioFile(AUDIO_FILE) as source:
	audio = r.record(source)
try:
	print(r.recognize_sphinx(audio))
except sr.UnknownValueError:
	print("Sphinx could not understand audio")
except sr.RequestError as e:
	print("Sphinx error; {0}".format(e))
