## AConverse
A library consisting of cross platform hotword detection, speech recognition, and text to speech.

## Installation Windows + linux {user} [Not working currently due to porcupine pypi package excluding their windows folder]
1. Install the project through pip [pip install] https://pip.pypa.io/en/stable/quickstart/
2. Run the install python script manually [Make sure you have git installed]
3. You need to install FFmpeg if you plan on using text to speech since this is needed for conversion from mp3, for a tutorial on installing FFmpeg see the pydub github page: https://github.com/jiaaro/pydub#getting-ffmpeg-set-up

## Installation Windows + linux {developer}
1. Install the project through pip [pip install] https://pip.pypa.io/en/stable/quickstart/
2. Run the install python script manually [Make sure you have git installed]
3. You need to install FFmpeg if you plan on using text to speech since this is needed for conversion from mp3, for a tutorial on installing FFmpeg see the pydub github page: https://github.com/jiaaro/pydub#getting-ffmpeg-set-up

## Extra
If you want google.cloud support, you need to install the google cloud package from pypi: https://pypi.org/project/google-cloud/


## Developer note
I am planning on extending this library far beyond its current scope but I am working on another project besides this one so it will take a while. Planned features are: XML based TTS caching and voice emotion selection, Server availability checking for TTS (google speech is not a officially supported API so if it's suddenly offline it'd be nice to be able to immediately switch to a paid service), more TTS and STT options (WATSON etc).
