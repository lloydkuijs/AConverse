import porcupine
import pyaudio
import struct


class Detector(object):

    def __init__(self):
        pass
    
    def listen(self, callback):
        audio_stream = None
        handle = porcupine.create(keywords=['picovoice', 'bumblebee'])

        pa = pyaudio.PyAudio()

        audio_stream = pa.open(
            rate=handle.sample_rate,
            channels=1,
            format=pyaudio.paInt16,
            input=True,
            frames_per_buffer=handle.frame_length)

        while True:
            pcm = audio_stream.read(handle.frame_length)
            pcm = struct.unpack_from("h" * handle.frame_length, pcm)

            result = handle.process(pcm)

            if result > -1:
                print("Hotword detected")
                callback()

        audio_stream.close()
        handle.delete()