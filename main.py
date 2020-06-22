import json

from src.detection.hotword import Detector
from src.intent.parser import IntentParser
import src.skills as skills
import src.skills.sdk.converse as converse
import src.skills.sdk.skill_base as skill_base
import requests
from src.detection.voice import Recorder

intentParser = None
skill_invoker = None


def callback():
    Recorder.stabilize_threshold(0.5)  # Default value
    response = converse.transcribe()

    intent = intentParser.parse(response)

    test = intent['name']
    #skill_invoker.execute('sample_skill')
    pass
if __name__ == "__main__":

    intentParser = IntentParser.initialize()

    # Create skill invoker
    skill_invoker = skill_base.skill_invoker()

    # register skills in invoker
    skill_invoker.register(skills.SampleSkill())

    Detector().listen(callback)
    pass
