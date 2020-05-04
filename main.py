from src.detection.hotword import Detector
from src.intent.parser import IntentParser
import src.skills as skills
import src.skills.sdk.skill_base as skill_base
import requests

intentParser = None
skill_invoker = None

def callback():
    skill_invoker.execute('sample_skill')
    #print(intentParser.parse("Hello"))

if __name__ == "__main__":
    # Create skill invoker
    skill_invoker = skill_base.skill_invoker()

    # register skills in invoker
    skill_invoker.register(skills.SampleSkill())

    intentParser = IntentParser.initialize()
    Detector().listen(callback)
    pass
