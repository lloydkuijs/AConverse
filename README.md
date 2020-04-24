

# AConverse
A library of tools to communicate with the AConverse REST server


## Installation
### You should be used Python version <= 3.6.9, This library uses PyAudio which is not supported on higher versions as of 24/04/2020. Check up on the current state of PyAudio and Rasa for using newer versions or use a unofficial wheel

- Install the the requirements with `pip install -r requirements.txt`
- Run the installation file with python `Python install.py`

> If there are any problems with Rasa you might need to run `python -m spacy download en_core_web_md` and `python -m spacy link en_core_web_md`. If the problem is a index out of range exception you could try re-training the NLU model like so: `rasa train nlu`. Not all packages and dependencies are known to me currently and I am still working on the installation process.
