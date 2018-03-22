#!/usr/bin/env python3

import speech_recognition as sr
from time import sleep
#get audio form microphone
r = sr.Recognizer()

while True:
  with sr.Microphone() as source:
      print("ABLE Voice Recognition. Speak:")
      audio = r.listen(source)

  try:
      listened=r.recognize_google(audio)
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

  except sr.UnknownValueError:
      print("Could not understand audio")
  except sr.RequestError as e:
      print("Could not request results; {0}".format(e))

