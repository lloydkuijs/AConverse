import pyaudio
import math
import struct
import wave
import time
import os

SHORT_NORMALIZE = (1.0/32768.0)
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 16000
CHUNK = 1024
SAMPLE_WIDTH = 2
DEFAULT_SILENCE_TIMEOUT = 2
DEFAULT_MAX_TIMEOUT = 15

# TODO: Should we replace this with a adjustable property for each Recorder object?
AMBIENT_THRESHOLD = 5 # Introducing some wiggle room for irregular ambient noise

class Recorder:
    # TODO: Check for a better way than having a static variable to keep track of last base_line, is there any?
    base_line = 0

    @staticmethod
    def rms(frame):
        count = len(frame) / SAMPLE_WIDTH  # Divide CHUNK in samples
        format = "%dh" % (count)  # replaces %d with count
        shorts = struct.unpack(format, frame)

        sum_squares = 0.0
        for sample in shorts:
            n = sample * SHORT_NORMALIZE
            sum_squares += n * n
        rms = math.pow(sum_squares / count, 0.5)

        return rms * 1000

    def __init__(self):
        self._p = pyaudio.PyAudio()
        self._stream = self._p.open(format=FORMAT,
                                    channels=CHANNELS,
                                    rate=RATE,
                                    input=True,
                                    output=True,
                                    frames_per_buffer=CHUNK)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self._stream.stop_stream()
        self._stream.close()
        self._p.terminate()
        
    # TODO: If this function causes memory issues on a specific device, use temporary files to write to and replace the rec = [] by that in a future version
    def record(self, silence_timeout=DEFAULT_SILENCE_TIMEOUT, max_timeout=DEFAULT_MAX_TIMEOUT):
        """Time is in seconds"""

        rec = []
        current = time.time()
        max_time = time.time() + max_timeout
        # Is only set if silence is detected, set to max_timeout so it doesn't falsely interrupt
        silence_start = max_time

        while current <= max_time:
            data = self._stream.read(CHUNK)

            rms_val = self.rms(data)

            current = time.time()
            print("Audio level: ", rms_val)
            if rms_val <= Recorder.base_line:
                if(silence_start is max_time):  # No previous silence
                    silence_start = time.time()
                else:  # start time was set
                    if((silence_start + silence_timeout) < current):
                        rec.append(data) # Append the last bit of data recorded
                        break
            else:
                silence_start = max_time  # Reset the silence start

            rec.append(data)

        return rec

    @staticmethod
    def stabilize_threshold(time_seconds: int = 2):
        """Records and gets the RMS of each sample, then calculates the average. 
        This function sets the Recorder.base_line property, this is "inherited" for any new Record object."""

        p = pyaudio.PyAudio()
        
        stream = p.open(format=FORMAT,
                        channels=CHANNELS,
                        rate=RATE,
                        input=True,
                        output=False,
                        frames_per_buffer=CHUNK)
        
        current = time.time()
        end = current + time_seconds

        rms_values = []

        while current <= end:
            input = stream.read(CHUNK)
            rms_val = Recorder.rms(input)

            rms_values.append(rms_val)
            current = time.time()

        Recorder.base_line = sum(rms_values) / len(rms_values) + AMBIENT_THRESHOLD

        stream.stop_stream()
        stream.close()

        p.terminate()
        
if __name__ == "__main__":

    with Recorder() as recorder:
        recorder.stabilize_threshold(2)
        print("Recording now!!")
        print(recorder.record(silence_timeout=1.5))
