from src.detection.hotword import Detector
from src.intent.parser import IntentParser
import src.skills as skills

intentParser = None
skill_invoker = None

def callback():
    print(intentParser.parse("Hello"))

if __name__ == "__main__":
    skill_invoker = skills.skill_invoker()
    skill_invoker.register(skills.SampleSkill())

    skill_invoker.execute("sample_skill")
    #intentParser = IntentParser.initialize()
    # Detector().listen(callback)
    pass
