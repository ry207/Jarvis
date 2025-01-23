import speech_recognition as sr
import pyttsx3
from analize import analize, analizetext
import os

# Initialize recognizer class (for recognizing the speech)
r = sr.Recognizer()
engine = pyttsx3.init()

os.system("clear")

def speech():
    while True:
        with sr.Microphone() as source:
            audio_text = r.listen(source)
            print("Talk")
            print("Time over, thanks")
            # recoginze_() method will throw a request
            # error if the API is unreachable,
            # hence using exception handling
            try:
                # using google speech recognition
                print("Text: "+r.recognize_google(audio_text))
                stt = r.recognize_google(audio_text)
                analize(stt)
            except sr.UnknownValueError:
                stt = ""
                print("Sorry, I didn't understand that.")
            except sr.RequestError as e:
                stt = ""
                print("Error; {0}".format(e))
def text():
    while True:
        comm = input("Jarvis >>")
        if comm == "shut down":
            exit(69)
        analizetext(comm)


speechOrText = input("Speech or Text(s/t): ")

if speechOrText == "s":
    speech()
elif speechOrText == "t":
    text()
