# import speech_recognition as sr
from playsound import playsound
import pygame
import speech_recognition as sr

pygame.mixer.init()

pygame.mixer.music.load("vsauce.mp3")


r = sr.Recognizer()

DURATION_CHUNK = 2

pharse= "or is it?"

try:
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source,duration=1)
        print("Please talk")
        while True:
            audio_data = r.listen(source,timeout=None,phrase_time_limit=DURATION_CHUNK)
            try:
                text =  r.recognize_whisper(audio_data, model="base")
                print(text.strip())
                if pharse in text.lower():
                    pygame.mixer.music.play()

                    while pygame.mixer.music.get_busy():
                        pygame.time.Clock().tick(10)
            except Exception as e:
                pass
except KeyboardInterrupt:
    print("stopping")