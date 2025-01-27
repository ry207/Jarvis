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
    print("""
        __                 _     
        / /___ _______   __(_)____
    __  / / __ `/ ___/ | / / / ___/
    / /_/ / /_/ / /   | |/ / (__  ) 
    \____/\__,_/_/    |___/_/____/  
                                                            
    """)
    while True:
        print(Fore.RED + "Speak: "  + Fore.WHITE)
        try:
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
                    elif "hey Jarvis" in stt:
                        stt = stt.replace("hey Jarvis ", "")
                        analize(stt)
                        continue
                    analize(stt)
                except sr.UnknownValueError:
                    stt = ""
                    print("Sorry, I didn't understand that.")
                except sr.RequestError as e:
                    stt = ""
                    print("Error; {0}".format(e))
        except KeyboardInterrupt:
            sure = input(Fore.RED + "\n\nAre you sure you want to leave(y/n): " + Fore.WHITE)
            if sure == "y":
                exit(69)
            elif sure == "n":
                print(Fore.GREEN + "okay you can stay..." + Fore.WHITE)
                continue
            else:
                print("bye")
                exit(69)
def textmode():
    print("""
           __                 _     
          / /___ _______   __(_)____
     __  / / __ `/ ___/ | / / / ___/
    / /_/ / /_/ / /   | |/ / (__  )
    \____/\__,_/_/    |___/_/____/
                                                        
""")
    while True:
        try:
            print("")
            comm = input(Fore.RED + "Jarvis >> " + Fore.BLUE)
            print(Fore.WHITE + "")
            if comm == "speech":
                speechmode()
            analizetext(comm)
        except KeyboardInterrupt:
            sure = input(Fore.RED + "\n\nAre you sure you want to leave(y/n): " + Fore.WHITE)
            if sure == "y":
                exit(69)
            elif sure == "n":
                print(Fore.GREEN + "okay you can stay..." + Fore.WHITE)
                continue
            else:
                print("bye")
                exit(69)

speechOrText = input("Speech or Text(s/t): ")

if speechOrText == "s":
    speechmode()
elif speechOrText == "t":
    textmode()
else:
    print("not an option")
    exit(13)
