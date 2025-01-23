import pyttsx3
import speech_recognition as sr
from wiki import analizevoice
import os
import colorconsole.terminal

# init function to get an engine instance for the speech synthesis 
engine = pyttsx3.init()
r = sr.Recognizer()

greetings = ["Hello", "hello", "hello Jarvis", "jarvis", "hey Jarvis", "Jarvis", "come in Jarvis", "how are you", "how are you Jarvis", "what's up"]
good = ["Good", "good", "great", "okay", "okay jarvis", "thanks", "thanks jarvis", "okay jarvis", "Great", "I'm good", "i'm good", "im good", "i'm okay"]
bad = ["bad", "not good", "no", "No"]
function1 = ["function"]
todo = ["what to do", "to do", "to-do", "Todo", "To-Do"]


def analize(voice):
    if voice == "power off":
        engine.say("Goodbye, Sir")
        exit(69)
    elif voice == "joke":
        os.system("curl ascii.live/can-you-hear-me")
        os.system("clear")
    elif voice == "color":
        engine.say("changine colors")
        os.system("clear")
        screen = colorconsole.terminal.get_terminal()
        screen.cprint(6, 0, "\n")
    elif voice == "pause":
        pause = input("")
    elif voice == "who am I":
        os.system("curl ifconfig.me/all")
        engine.say("Here is your network data, sir")
    elif voice == "tree":
        os.system("pstree")
        engine.say("Here is your active and running tasks tree, sir")
    elif voice in todo != -1:
        engine.say('Nothing to do sir')
    elif voice in greetings != -1:
        engine.say('Hello sir, how may I help you, sir.')
    elif voice in good != -1:
        engine.say('Of course, sir.')
    elif voice in bad != -1:
        engine.say('Sorry, Sir.')
    elif voice in function1 != -1:
        engine.say('What word would you like?')
        engine.runAndWait()
        with sr.Microphone() as source:
            print("Talk")
            audio_text = r.listen(source)
            print("Time over, thanks")
            try:
                stt = r.recognize_google(audio_text)
                sttlen = len(stt)
                print(f"The length of {stt} is {sttlen} characters.")
                engine.say(f"The length of {stt} is {sttlen} characters.")
            except:
                engine.say("Sorry sir, I didn't get that.")
    elif voice == "computer":
        engine.say("""Computers and computing devices from different eras—left to right, top to bottom:
Early vacuum tube computer (ENIAC)Mainframe computer (IBM System 360)Smartphone (LYF Water 2)Desktop computer (IBM ThinkCentre S50 with monitor)Video game console (Nintendo GameCube)Supercomputer (IBM Summit)
A computer is a machine that can be programmed to automatically carry out sequences of arithmetic or logical operations (computation). Modern digital electronic computers can perform generic sets of operations known as programs. These programs enable computers to perform a wide range of tasks. The term computer system may refer to a nominally complete computer that includes the hardware, operating system, software, and peripheral equipment needed and used for full operation; or to a group of computers that are linked and function together, such as a computer network or computer cluster.
A broad range of industrial and consumer products use computers as control systems, including simple special-purpose devices like microwave ovens and remote controls, and factory devices like industrial robots. Computers are at the core of general-purpose devices such as personal computers and mobile devices such as smartphones. Computers power the Internet, which links billions of computers and users.""")
    elif voice == "search":
        print("searching..")
        engine.say('What word would you like to search?')
        engine.runAndWait()
        with sr.Microphone() as source:
            print("Talk")
            audio_text = r.listen(source)
            print("Time over, thanks")
            print("Search: "+r.recognize_google(audio_text))
            try:
                stt = r.recognize_google(audio_text)
                analizevoice(stt)
            except:
                engine.say("Sorry sir, I didn't get that.")

    engine.runAndWait()


def analizetext(comm):
    if comm in todo != -1:
        engine.say('Nothing to do sir')
    elif comm in greetings != -1:
        engine.say('Hello sir, how may I help you, sir.')
    elif comm in good != -1:
        engine.say('Of course, sir.')
    elif comm in bad != -1:
        engine.say('Sorry, Sir.')
    elif comm in function1 != -1:
        engine.say('What word would you like?')
        engine.runAndWait()
        word = input("What word would you like: ")
        sttlen = len(word)
        print(f"The length of {word} is {sttlen} characters.")
        engine.say(f"The length of {word} is {sttlen} characters.")
    elif comm == "computer":
        engine.say("""Computers and computing devices from different eras—left to right, top to bottom:
Early vacuum tube computer (ENIAC)Mainframe computer (IBM System 360)Smartphone (LYF Water 2)Desktop computer (IBM ThinkCentre S50 with monitor)Video game console (Nintendo GameCube)Supercomputer (IBM Summit)
A computer is a machine that can be programmed to automatically carry out sequences of arithmetic or logical operations (computation). Modern digital electronic computers can perform generic sets of operations known as programs. These programs enable computers to perform a wide range of tasks. The term computer system may refer to a nominally complete computer that includes the hardware, operating system, software, and peripheral equipment needed and used for full operation; or to a group of computers that are linked and function together, such as a computer network or computer cluster.
A broad range of industrial and consumer products use computers as control systems, including simple special-purpose devices like microwave ovens and remote controls, and factory devices like industrial robots. Computers are at the core of general-purpose devices such as personal computers and mobile devices such as smartphones. Computers power the Internet, which links billions of computers and users.""")
    elif comm == "search":
        print("searching..")
        engine.say('What word would you like to search?')
        engine.runAndWait()
        search = input("Search(Xxx_Xxx): ")
        analizevoice(search)
    elif comm == "joke":
        os.system("curl ascii.live/can-you-hear-me")
        os.system("clear")
    elif comm == "color":
        engine.say("changine colors")
        os.system("clear")
        screen = colorconsole.terminal.get_terminal()
        screen.cprint(6, 0, "\n")
    elif comm == "pause":
        pause = input("")
    elif comm == "who am I":
        os.system("curl ifconfig.me/all")
        engine.say("Here is your network data, sir")
    elif comm == "tree":
        os.system("pstree")
        engine.say("Here is your active and running tasks tree, sir")

    engine.runAndWait()


