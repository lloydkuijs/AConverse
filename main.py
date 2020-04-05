from src.detection.hotword import Detector
import src.intent.parser as parser

intentParser = None

def callback():
    print(intentParser.parse("Hello"))
    

if __name__ == "__main__":
    intentParser = parser.IntentParser().initialize()
    Detector().listen(callback)
