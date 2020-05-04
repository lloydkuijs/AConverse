from src.detection.voice import Recorder, DEFAULT_MAX_TIMEOUT, DEFAULT_SILENCE_TIMEOUT

from sys import getsizeof
import requests

# TODO: Make the request url easily adjustable? Maybe add versioning to the SDK
request_url = "https://localhost:5001/api/v0.4/" 

def transcribe(silence_timeout=DEFAULT_SILENCE_TIMEOUT, max_timeout=DEFAULT_MAX_TIMEOUT):

    audio = None
    with Recorder() as recorder:
        recorder.stabilize_threshold(2)  # Default value
        audio = recorder.record(silence_timeout, max_timeout)
    
    print(getsizeof(audio))


def synthesize(text : str):
    result = requests.post(request_url + "tts/synthesize", text)

    print(result)



