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
        self._commands = {}

    def register(self, skill: ISkill):
        self._commands[skill.name] = skill

    def execute(self, skill_name):
        if(skill_name in self._commands.keys()):
            self._commands[skill_name].execute()
        else:
            print(f"Failed to execute {skill_name}, not found.")

