from src.detection.voice import Recorder as _Recorder, DEFAULT_MAX_TIMEOUT as _DEFAULT_MAX_TIMEOUT, DEFAULT_SILENCE_TIMEOUT as _DEFAULT_SILENCE_TIMEOUT, SAMPLE_WIDTH, RATE, CHANNELS, FORMAT

from sys import getsizeof
import requests
import json
import io
import base64

# TODO: Make the request url easily adjustable? Maybe add versioning to the SDK
request_url = "https://localhost:5001/api/v0.4/"

# TODO: Remove verify false if release
_VERIFY = False


def transcribe(silence_timeout=_DEFAULT_SILENCE_TIMEOUT, max_timeout=_DEFAULT_MAX_TIMEOUT):

    audio = None
    with _Recorder() as recorder:
        audio = recorder.record(silence_timeout, max_timeout)
    
    print(audio)
    audio_encoded = base64.b64encode(audio)

    message = {
        "audio": audio_encoded.decode('utf-8'),
        "AudioType": "audio/l16",
        "SamplingRate": RATE,
        "Channels": CHANNELS
    }

    response = requests.post(request_url + "converse/transcribe", json=message, verify=_VERIFY)

    response = response.json()['results']
    response = response[0]
    response = response['alternatives'][0]
    response = response['transcript']
    
    return response

    
def synthesize(text: str):
    result = requests.post(request_url + "converse/synthesize", text)

    print(result)
