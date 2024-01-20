import speech_recognition as sr
import pyaudio
import pocketsphinx

# obtain audio from the microphone
r = sr.Recognizer()
with sr.Microphone() as source:
    while True:
            print("Say something!")
            audio = r.listen(source)
            try:
                print(r.recognize_google(audio))
            except sr.UnknownValueError:
                print("Could not understand audio")
            except sr.RequestError as e:
                print("Error; {0}".format(e))