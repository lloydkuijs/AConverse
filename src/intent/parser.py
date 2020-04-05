from rasa.nlu.model import Interpreter
from rasa.constants import DEFAULT_MODELS_PATH
from rasa.model import get_model, get_model_subdirectories, ModelNotFound
import rasa

class IntentParser(object):
    def initialize(self, model_path = None):
        try:
            model_path = get_model(DEFAULT_MODELS_PATH)
        except ModelNotFound:
            print(
                "No model found. Train a model before running the "
                "server using `rasa train nlu`."
            )
            return

        _, nlu_model = get_model_subdirectories(model_path)

        if not nlu_model:
            print(
                "No NLU model found. Train a model before running the "
                "server using `rasa train nlu`."
            )
            return

        return Interpreter.load(nlu_model)

        

    pass