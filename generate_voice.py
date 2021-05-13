from gtts import gTTS
import os,time

def save_sound(message):
    speech = gTTS(message)
    speech.save("audio.mp3")
