import src.porcupine as porcupine
import pyaudio
import struct


class Detector(object):

    def __init__(self):
        pass
    
    def listen(self, callback, keyword_file_paths= None, sensitivities=None):
        audio_stream = None

        if(keyword_file_paths is None):
            handle = porcupine.create(keywords=porcupine.KEYWORDS) # Use default keywords
        else:
            handle = porcupine.create(keyword_file_paths=keyword_file_paths, sensitivities=sensitivities)

        pa = pyaudio.PyAudio()

        audio_stream = pa.open(
            rate=handle.sample_rate,
            channels=1,
            format=pyaudio.paInt16,
            input=True,
            frames_per_buffer=handle.frame_length)

        while True:
            try:
                pcm = audio_stream.read(handle.frame_length)
                pcm = struct.unpack_from("h" * handle.frame_length, pcm)

                result = handle.process(pcm)
            except:
                continue;

            if result > -1:
                print("Hotword detected")
                 # We close the stream in case the callback needs to access any sound calls
                audio_stream.close()
                callback()
                audio_stream = pa.open(
                    rate=handle.sample_rate,
                    channels=1,
                    format=pyaudio.paInt16,
                    input=True,
                    frames_per_buffer=handle.frame_length)

        handle.delete()