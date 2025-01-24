import speech_recognition as sr
import pyttsx3
from analize import analize, analizetext
import os
from colorama import Fore

# Initialize recognizer class (for recognizing the speech)
r = sr.Recognizer()
engine = pyttsx3.init()

os.system("clear")

def speechmode():
    while True:
        wait = input("")
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
                if stt == "text mode":
                    textmode()
                analize(stt)
            except sr.UnknownValueError:
                stt = ""
                print("Sorry, I didn't understand that.")
            except sr.RequestError as e:
                stt = ""
                print("Error; {0}".format(e))
def textmode():
    while True:
        print("")
        comm = input(Fore.RED + "Jarvis >> " + Fore.BLUE)
        print(Fore.WHITE + "")
        if comm == "speech":
            speechmode()
        analizetext(comm)


speechOrText = input("Speech or Text(s/t): ")

if speechOrText == "s":
    speechmode()
elif speechOrText == "t":
    textmode()
else:
    print("not an option")
    exit(13)
