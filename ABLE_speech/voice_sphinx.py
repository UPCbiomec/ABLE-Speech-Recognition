#!/usr/bin/env python3
import speech_recognition as sr
import sphinxbase
import pocketsphinx
from time import sleep

 # obtain audio from the microphone
r = sr.Recognizer()
with sr.Microphone() as source:
   print("Please wait. Calibrating microphone...")
   # listen for 5 seconds and create the ambient noise energy level
   r.adjust_for_ambient_noise(source, duration=5)
while True:
  with sr.Microphone() as source:
      print("ABLE Voice Recognition. Speak:")
      audio = r.listen(source)

  try:
      listened=r.recognize_sphinx(audio)
      print(listened)
      if(listened=="start"):
        print("ABLE: MOTORS ARE STARTING")
        sleep(2) #time in seconds
        print("ABLE: MOTORS ARE READY")
      elif(listened=="stop"):
        print("ABLE: MOTORS ARE STOPPING")
        sleep(2) #time in seconds
        print("ABLE: MOTORS ARE STOPPED")
      elif(listened=="sit down"):
        print("ABLE: YOU ARE SITTING DOWN")
        sleep(2) #time in seconds
        print("ABLE: YOU ARE SITTED DOWN")
      elif(listened=="stand up"):
        print("ABLE: YOU ARE STANDING UP")
        sleep(2) #time in seconds
        print("ABLE: YOU ARE STANDED UP")
      else:
        print("DOESNT EXIST ACTION REQUIERED")

  # recognize speech using Sphinx
  except sr.UnknownValueError:
   print("Sphinx could not understand audio")
  except sr.RequestError as e:
   print("Sphinx error; {0}".format(e))
