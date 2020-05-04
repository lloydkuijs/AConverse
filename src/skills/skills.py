from src.skills.sdk.skill_base import ISkill
from src.skills.sdk.speech import transcribe

class SampleSkill(ISkill):

    def __init__(self) -> None:
        pass
    
    def name(self):
        return "sample_skill"

    def execute(self) -> None:
        transcribe()
        
