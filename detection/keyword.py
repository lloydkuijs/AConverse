from detection.snowboy import snowboydecoder
import os

class KeywordListener():

    def __init__(self, detected_callback, sensitivity=0.5, audio_gain=1):
        self._detected_callback = detected_callback
        # TODO: remove hardcoded path and make adjustable
        self._keyword_path = os.path.join(
            os.path.dirname(__file__), "snowboy/Mio.pmdl")
        self._audio_gain = audio_gain
        self._sensitivity = sensitivity

    def listen(self):
        detector = snowboydecoder.HotwordDetector(
            decoder_model=self._keyword_path, sensitivity=self._sensitivity, audio_gain=self._audio_gain)

        self.detector = detector

        detector.start(self._callback)
    
    def play_ding(self):
        snowboydecoder.play_audio_file()

    def _callback(self):
        self.play_ding()
        self._detected_callback()

    