import setuptools

with open("README.md", "r") as fh:
   long_description = fh.read()

setuptools.setup(
    name="AConverse", # Replace with your own username
    version="0.0.1",
    author="Lloyd Kuijs",
    author_email="lloydkuijs@outlook.com",
    description="A simple interface that takes in a voice and is able to respond with a server over http to request a response from a AI or other device.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/lloydkuijs/AConverse",
    packages=setuptools.find_packages(),
    python_requires='>=3.5',
    install_requires=[
        'SpeechRecognition>=3.8.1',
        'pydub>=0.23.1',
        'requests>=2.22.0',
        'gTTS>=2.1.1'
    ]
)
