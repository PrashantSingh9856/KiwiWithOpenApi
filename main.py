import speech_recognition as sr
import openAi2
import textToSpeech

class Recognize:
    def __init__(self) -> None:
        self.r = sr.Recognizer()
        self.speakobj = textToSpeech.TextToSpeech()

    def getText(self):
        with sr.Microphone() as source:
            print("Speak anything:...")
            audio = self.r.listen(source)
            try:
                text = self.r.recognize_google(audio)
                print("You said: {}".format(text))
                self.speakobj.speak(text)
                if len(text)>0:
                    try:
                        responseText = openAi2.generate_gpt3_response(text,print_output=False)
                        print(responseText)
                    except Exception as e:
                        print("Got Exception from OpenAI!",e)
                        return
                    if text.__contains__('stop'):
                        self.speakobj.stopSpeaking()
                        return 
                    elif text.__contains__('exit'):
                        return True
                    elif text.__contains__('quit'):
                        return True
                    elif text.__contains__('cancel'):
                        return True
                    self.speakobj.speak(responseText)
                     
            except:
                print("Sorry, I could not recognize your voice.")
if __name__ =="__main__":
    while True:
        resp = Recognize().getText()
        if resp==True:
            break
