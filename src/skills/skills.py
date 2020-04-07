from src.skills.sdk.skill_tools import ISkill

class SampleSkill(ISkill):

    def __init__(self) -> None:
        pass
    
    def name(self):
        return "sample_skill"

    def execute(self) -> None:
        print("Hello skill!")
