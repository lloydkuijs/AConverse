from datetime import datetime

from detection.keyword import KeywordListener
from detection.speech import recognize

def main():
    keyword_recognizer = KeywordListener(detected_callback=recognize)
    keyword_recognizer.listen()


if __name__ == '__main__':
    main()