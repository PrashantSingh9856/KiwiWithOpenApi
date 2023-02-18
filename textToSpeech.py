import pyttsx3

class TextToSpeech:
    def __init__(self) -> None:
        self.engine = pyttsx3.init()
       # Set the voice to use
        voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice', voices[0].id)
        # Set the speaking rate
        self.engine.setProperty('rate', 150)
        # Set the volume
        self.engine.setProperty('volume', 0.5)
    def speak(self,text):
        self.engine.say(text)
        self.engine.runAndWait()
    def stopSpeaking(self):
        self.engine.stop()