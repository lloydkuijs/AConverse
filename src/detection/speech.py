import speech_recognition as sr
import requests
import json
from tts.tts_cached import Service, TextToSpeech


url = "http://localhost:5005/webhooks/rest/webhook" # Url to send requests to

# TODO: replace speech recognition with speech in detection package
def recognize():
    try:
        recognizer = sr.Recognizer()

        with sr.Microphone() as source:
            recognizer.adjust_for_ambient_noise(source, duration=0.1)
            print("Say anything : ")
            audio = recognizer.listen(source, timeout=2)
            print("Audio recorded")

            text = recognizer.recognize_google(audio)
            print("text retrieved")

            payload = {'sender': "Anna", 'message': text}
            response = requests.post(url, json=payload)
            
            response = response.json()[0]
            response = response['text']
        
    except Exception as e:
        print(e)
        response = "Sorry I could not understand what you meant with that"
    
    print("Response: " + response)
    tts = TextToSpeech(True, Service.google_speech)
    tts.convert(response, play_sound=True)