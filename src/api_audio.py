"""
PyAudio example: Record a few seconds of audio and save to a WAVE
file.
"""

import pyaudio
import wave
import sys
import threading, time, 
DEBUG = True

def init_audio():
    global CHUNK, FORMAT, CHANNELS, RATE, RECORD_SECONDS, WAVE_OUTPUT_FILENAME, stream, p
    CHUNK = 2048
    FORMAT = pyaudio.paInt16
    CHANNELS = 2
    RATE = 44100
    RECORD_SECONDS = 10
    WAVE_OUTPUT_FILENAME = "output.wav"
    rec = False
#    if sys.platform == 'darwin':
#        CHANNELS = 1

    p = pyaudio.PyAudio()
    stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)
    if DEBUG:
        print " initialisation complete"

def start_recording():
    global CHUNK, FORMAT, CHANNELS, RATE, RECORD_SECONDS, WAVE_OUTPUT_FILENAME, rec, stream, frames
    print("* recording")

    frames = []

#    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    while rec:
        data = stream.read(CHUNK)
        frames.append(data)

def stop_recording():
    global CHUNK, FORMAT, CHANNELS, RATE, RECORD_SECONDS, WAVE_OUTPUT_FILENAME, rec, stream, p
    rec = False
    print("* done recording")
    stream.stop_stream()
    stream.close()
    p.terminate()
    save_file()

def save_file():
    global CHUNK, FORMAT, CHANNELS, RATE, RECORD_SECONDS, WAVE_OUTPUT_FILENAME, rec, stream, p, frames
    wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()


init_parameters()
rec = True
t=threading.Thread(target=start_recording)
t.start()
print " thread started"
time.sleep(10)
stop_recording()
print " thread over"
t.join()
