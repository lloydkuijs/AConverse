# Clones the porcupine library
import warnings
import subprocess

def git(*args):
    return subprocess.check_call(['git'] + list(args))

# Performs installation and then returns the setup function
def install():
    try:
        print("Cloning!")
        git("clone", "https://github.com/Picovoice/porcupine.git", "src/porcupine")
        print("Done with cloning")
    except:
        print("[IGNORE THIS IF PORCUPINE IS ALREADY INSTALLED UNDER src/porcupine] Failed to clone the porcupine repository to the local folder src/porcupine, install git and run the setup again or install it yourself.")
    
if __name__ == "__main__":
    install()
