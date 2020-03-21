import enum
import tempfile
import os
from pydub import AudioSegment
from pydub.playback import play


class Service(enum.Enum):
    custom = 0
    google_speech = 1
    google_cloud = 2
    #watson = 3


class TextToSpeech():

    def __init__(self, caching: bool, service: Service):
        self.service = service
        self.caching = caching
        self.cache_dir = "cache/{}/".format(self.service.name)  # relative cache path
        
        try:
            # Create target Directory
            os.makedirs(self.cache_dir)
            print("Directory ", self.cache_dir,  " Created ")
        except FileExistsError:
            print("Directory ", self.cache_dir,  " already exists")

    def convert(self, text: str, play_sound=False):
        audio_segment = None  # pydub audio segment
        file_name = "{}{}.mp3".format(self.cache_dir, text)
        file_exists = os.path.isfile(file_name)
        
        if(not file_exists or self.service == Service.custom):
            self._generate_audio(text, file_name, self.service)
        
        audio_segment = AudioSegment.from_mp3(file_name)
        play(audio_segment)  # play the audio

        # if caching is off we remove the specified audio file
        if(not self.caching):
            os.remove(file_name)

        pass

    def _generate_audio(self, text: str, file_name, service: Service):

        if(self.service == Service.custom):
            return

        else if(self.service == Service.google_speech):
            from gtts import gTTS 

            tts = gTTS(text)
            tts.save(file_name)

        else if(self.service == Service.google_cloud):
            from google.cloud import texttospeech

            # Instantiates a client
            client = texttospeech.TextToSpeechClient()

            # Set the text input to be synthesized
            synthesis_input = texttospeech.types.cloud_tts_pb2.SynthesisInput(text=text)

            # Build the voice request, select the language code ("en-US") and the ssml
            # voice gender ("neutral")
            voice = texttospeech.types.cloud_tts_pb2.VoiceSelectionParams(
                language_code='en-US',
                ssml_gender=texttospeech.enums.SsmlVoiceGender.FEMALE)

            # Select the type of audio file you want returned
            audio_config = texttospeech.types.cloud_tts_pb2.AudioConfig(
            audio_encoding=texttospeech.enums.AudioEncoding.MP3)

            # Perform the text-to-speech request on the text input with the selected
            # voice parameters and audio file type
            response = client.synthesize_speech(synthesis_input, voice, audio_config)
            
            with open(file_name, 'wb') as out:
                out.write(response.audio_content)
                print("'Audio content written to file {}".format(file_name))