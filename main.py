# pip install voskp
# pip install vosk
# pip install pyaudio

import json, pyaudio
from vosk import Model, KaldiRecognizer

model = Model('vosk-model-ru-0.42_trained_06')
rec = KaldiRecognizer(model, 16000)

p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8000)
stream.start_stream()

def listen():
    while True:
        data = stream.read(4000, exception_on_overflow=False)
        if (rec.AcceptWaveform(data)) and (len(data) > 0):
            answer = json.loads(rec.Result())
            if answer['text']:
                yield answer['text']
print("start")
for text in listen():
    print(text)
    
    
    # print("start")
    
     
    # if text == 'пока':
    #     quit()

    # elif text == 'привет':
    #     print("hello world")
    #     print(text)
# input('good')