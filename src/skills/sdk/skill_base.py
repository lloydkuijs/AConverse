from abc import ABC, abstractmethod


class ISkill(ABC):

    @abstractmethod
    def name(self) -> str:
        pass

    @abstractmethod
    def execute(self):
        pass


class skill_invoker:

    def __init__(self):
        self._skills = {}

    def register(self, skill: ISkill):
        self._skills[skill.name()] = skill

    def execute(self, skill_name):
        if(skill_name in self._skills.keys()):
            self._skills[skill_name].execute()
        else:
            print("Failed to execute {skill_name}, not found.")

