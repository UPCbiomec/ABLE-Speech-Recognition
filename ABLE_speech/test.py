import os
from os import path
from pocketsphinx import pocketsphinx
from pocketsphinx import Decoder
import speech_recognition as sr
from time import sleep


MODELDIR = "BIOMEC_DICTIONARY"

config = Decoder.default_config()
config.set_string('-hmm', path.join(MODELDIR, 'acoustic-model'))
config.set_string('-lm', path.join(MODELDIR, '4177.lm'))
config.set_string('-dict', path.join(MODELDIR, '4177.dict'))
config.set_string("-logfn", os.devnull)
decoder = Decoder(config)

commands = [
		 'DOWN',
		 'GO',
		 'LEFT',
		 'RIGHT',
		 'STOP',
		 'UP'
]

def getCommand(phrase, commands=commands):
	for i in range(len(commands)):
		if phrase.find(commands[i]) != -1:
			return (commands[i])
	

r = sr.Recognizer()
r.energy_threshold = 1000 # minimum audio energy to consider for recording
r.pause_threshold = 0.25 # seconds of non-speaking audio before a phrase is cons$
r.phrase_threshold = 0.15 # minimum seconds of speaking audio before we conside$
r.non_speaking_duration = 0.25 # seconds of non-speaking audio to keep on both $
with sr.Microphone() as source:
   print("Please wait. Calibrating microphone...")
   # listen for 5 seconds and create the ambient noise energy level
   r.adjust_for_ambient_noise(source, duration=5)
   print "ABLE is listening..."
   audio = r.listen(source)
try:
	
	print "ABLE is recognizing..."
	raw_data = audio.get_raw_data(convert_rate=16000, convert_width=2)
	decoder.start_utt()
	decoder.process_raw(raw_data, False, True)
	decoder.end_utt()
	hypothesis = decoder.hyp()
	HYPOTESIS = hypothesis.hypstr.split()
	RESULT = getCommand(hypothesis.hypstr)
	print HYPOTESIS, RESULT
        if(RESULT=="GO"):
           print("ABLE: MOTORS ARE STARTING")
           sleep(2) #time in seconds
           print("ABLE: MOTORS ARE READY")
        else:
           print("DOESNT EXIST ACTION REQUIERED")

except:
	print "ABLE SAYS BYE..."
    



