from src.detection.hotword import Detector
from rasa_nlu import train

def callback():
    print("hello hotword")

Detector().listen(callback)