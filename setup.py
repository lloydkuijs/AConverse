import setuptools

#with open("README.md", "r") as fh:
#   long_description = fh.read()

setuptools.setup(
    name="Mio-framework", # Replace with your own username
    version="0.0.1",
    author="Lloyd Kuijs",
    author_email="lloydkuijs@outlook.com",
    description="A framework of combined packages and modules to create a personal assistant with.",
    url="https://github.com/lloydkuijs/AI-visualized-backend",
    packages=setuptools.find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha"
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",

    ],
    python_requires='>=3.5',
    install_requires=[
        'rasa>=1.6.0',
        'SpeechRecognition>=3.8.1',
        'pydub>=0.23.1',
        'requests>=2.22.0',
        'gTTS>=2.1.1'
    ]
)
