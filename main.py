from src.detection.hotword import Detector
from src.tts.tts_cached import TextToSpeech, Service

tts = TextToSpeech(False, Service.google_speech)

def callback():
    tts.convert("hello world", True)


Detector().listen(callback)