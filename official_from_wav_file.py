# test simple      https://github.com/alphacep/vosk-api/blob/master/python/example/test_simple.py
import json
# pip install voskp
# pip install vosk
# pip install pyaudio


#!/usr/bin/env python3

import wave
import sys

from vosk import Model, KaldiRecognizer, SetLogLevel

# You can set log level to -1 to disable debug messages
SetLogLevel(0)

wf = wave.open('test.wav', "rb") # было     wf = wave.open(sys.argv[1], "rb")
if wf.getnchannels() != 1 or wf.getsampwidth() != 2 or wf.getcomptype() != "NONE":
    print("Audio file must be WAV format mono PCM.")
    sys.exit(1)

model = Model('vosk-model-ru-0.42_trained_04')

# You can also init model by name or with a folder path
# model = Model(model_name="vosk-model-en-us-0.21")
# model = Model("models/en")

rec = KaldiRecognizer(model, wf.getframerate())
rec.SetWords(True)
rec.SetPartialWords(False)

while True:
    data = wf.readframes(4000)
    if len(data) == 0:
        break
    if rec.AcceptWaveform(data):
        pass
        # print(rec.Result())
    else:
        # print(rec.PartialResult())
        pass

#print(rec.FinalResult())

dictionary2 = rec.FinalResult()
dictionary2 = json.loads(dictionary2)
# print(dictionary2['text'])

with open("test.txt", 'w', encoding="utf-8") as f:  ##аут
        f.write(dictionary2['text'])

