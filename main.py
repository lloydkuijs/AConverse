from src.detection.hotword import Detector
from src.intent.parser import IntentParser
import src.skills as skills

intentParser = None

def callback():
    print(intentParser.parse("Hello"))

if __name__ == "__main__":
    #intentParser = IntentParser.initialize()
    # Detector().listen(callback)
    pass
