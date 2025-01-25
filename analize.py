import pyttsx3
import speech_recognition as sr
import os
import colorconsole.terminal
import random
import datetime
import simpleaudio as sa


from wikipage import getpage
from forum import news
from wiki import analizevoice
from sshtoself import sshto
from dictionary import getdef
from papers import getpapers
from stocks import getstocks
from phrases import *

# init function to get an engine instance for the speech synthesis 
engine = pyttsx3.init()
r = sr.Recognizer()


random_facts = [
    "Bananas are berries, but strawberries are not.",
    "Honey never spoils. Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3,000 years old.",
    "The Eiffel Tower can be 15 cm taller during the summer due to the expansion of metal in the heat.",
    "Octopuses have three hearts, two pump blood to the gills, and one pumps it to the rest of the body.",
    "A day on Venus is longer than a year on Venus. It takes 243 Earth days to rotate once but only 225 Earth days to orbit the Sun.",
    "A crocodile can't stick its tongue out.",
    "Wombat poop is cube-shaped to prevent it from rolling away.",
    "The human nose can detect over 1 trillion different scents.",
    "Cleopatra lived closer in time to the first moon landing than to the construction of the Great Pyramid of Giza.",
    "Sharks have been around longer than trees. They have existed for over 400 million years.",
    "A single cloud can weigh more than a million pounds.",
    "There are more possible iterations of a game of chess than there are atoms in the known universe.",
    "Sloths can hold their breath longer than dolphins by slowing their heart rate to stay underwater for up to 40 minutes.",
    "The shortest war in history lasted only 38 to 45 minutes between Britain and Zanzibar in 1896.",
    "The inventor of the frisbee was turned into a frisbee after he died.",
    "Hot water freezes faster than cold water, a phenomenon known as the Mpemba effect.",
    "There’s enough DNA in the human body to stretch from the Earth to the Sun and back about 600 times.",
    "An octopus has blue blood because it uses copper instead of iron to transport oxygen.",
    "Butterflies can taste with their feet to identify the right plants to lay their eggs on.",
    "Venus is the only planet in our solar system that spins clockwise.",
    "A group of flamingos is called a 'flamboyance.'",
    "There’s a species of jellyfish that can revert its cells to an earlier stage, making it potentially immortal.",
    "Humans share about 60% of their DNA with bananas.",
    "The word 'alphabet' comes from the first two letters of the Greek alphabet: alpha and beta.",
    "A bolt of lightning is five times hotter than the surface of the sun.",
    "Penguins propose to their mates by presenting them with a perfect pebble.",
    "If you could fold a piece of paper 42 times, it would reach the Moon.",
    "You can’t hum while holding your nose closed.",
    "The heart of a blue whale is so large that a human could swim through its arteries.",
    "There are more fake flamingos in the world than real ones."
]





def analize(voice):
    if voice in exit_shutdown:
        engine.say("Goodbye, Sir")
        engine.runAndWait()
        exit(69)
    elif voice in stock_phrases:
        getstocks()
    elif voice == "news":
        news()
        engine.say("Heres the news, sir.")
        engine.runAndWait()
    elif voice == "download":
        engine.say("What page would you like to download: ")
        engine.runAndWait()
        with sr.Microphone() as source:
            print("Talk")
            audio_text = r.listen(source)
            print("Time over, thanks")
            try:
                stt = r.recognize_google(audio_text)
                sttsearch = stt.replace(" ", "_")
                engine.say(f"Getting the wiki page for {stt} then creating a live web server where you can access your file")
                engine.runAndWait()
                getpage(sttsearch)
            except:
                engine.say("An error occured")
                engine.runAndWait()
    elif voice in facts:
        randnum = random.randrange(0,30)
        random_fact = random_facts[randnum]
        engine.say(random_fact)
        engine.runAndWait()
        print(random_fact)
    elif voice in time_date:
        x = datetime.datetime.now()
        print(x.strftime("%A"))
        print(x.strftime("%B"), x.strftime("%d"))
        print(x.strftime("%I"), x.strftime("%M"), x.strftime("%p"))
        hour = x.strftime("%I")
        hour = hour.replace("0", "")
        minute = x.strftime("%M")
        minute = minute.replace("0", "")
        engine.say(f"Today is {x.strftime("%A")}, {x.strftime("%B")} {x.strftime("%d")}, and it {hour} {minute}, {x.strftime("%p")}")
        engine.runAndWait()
    elif voice in fun:
        os.system("curl ascii.live/can-you-hear-me")
        os.system("clear")
    elif voice == "color":
        engine.say("changine colors")
        engine.runAndWait()
        os.system("clear")
        screen = colorconsole.terminal.get_terminal()
        screen.cprint(6, 0, "\n")
    elif voice == "pause":
        pause = input("")
    elif voice == "who am I":
        os.system("curl ifconfig.me/all")
        engine.say("Here is your network data, sir")
        engine.runAndWait()
    elif voice == "tree":
        os.system("pstree")
        engine.say("Here is your active and running tasks tree, sir")
        engine.runAndWait()
    elif voice in todo != -1:
        engine.say('Nothing to do sir, lets have a nice day.')
        engine.runAndWait()
    elif voice in greetings != -1:
        engine.say('Hello sir.')
        engine.runAndWait()
    elif voice in good != -1:
        engine.say('Of course, sir.')
        engine.runAndWait()
    elif voice in howis != -1:
        engine.say('I am well, sir.')
        engine.runAndWait()
    elif voice in bad != -1:
        engine.say('Sorry, Sir.')
        engine.runAndWait()
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
                engine.runAndWait()
            except:
                engine.say("Sorry sir, I didn't get that.")
                engine.runAndWait()
    elif voice == "computer":
        engine.say("""Computers and computing devices from different eras—left to right, top to bottom:
Early vacuum tube computer (ENIAC)Mainframe computer (IBM System 360)Smartphone (LYF Water 2)Desktop computer (IBM ThinkCentre S50 with monitor)Video game console (Nintendo GameCube)Supercomputer (IBM Summit)
A computer is a machine that can be programmed to automatically carry out sequences of arithmetic or logical operations (computation). Modern digital electronic computers can perform generic sets of operations known as programs. These programs enable computers to perform a wide range of tasks. The term computer system may refer to a nominally complete computer that includes the hardware, operating system, software, and peripheral equipment needed and used for full operation; or to a group of computers that are linked and function together, such as a computer network or computer cluster.
A broad range of industrial and consumer products use computers as control systems, including simple special-purpose devices like microwave ovens and remote controls, and factory devices like industrial robots. Computers are at the core of general-purpose devices such as personal computers and mobile devices such as smartphones. Computers power the Internet, which links billions of computers and users.""")
        engine.runAndWait()
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
    elif voice in new_project != -1:
        engine.say("What shall this folder be named")
        engine.runAndWait()
        foldername = input("What should this folder be named: ")
        os.system(f"mkdir ~/{foldername}")
    elif voice == "terminal":
        name = input("what's the device name: ")
        engine.say("Goodbye for now sir.")
        engine.runAndWait()
        sshto(name)
        engine.say("Welcome back sir.")
        engine.runAndWait()
    elif voice == "movie":
        os.system("ls")
        os.system("dir")
        vf =  input("Name of video file: ")
        engine.say("Enjoy the movie, sir.")
        engine.runAndWait()
        os.system(f"mpv {vf}")
    elif voice == "get video":
        mov = input("Video or Audio(v/a): ")
        url = input("URL: ")
        if mov == "a":
            os.system(f"yt-dlp -o \"%(title)s\".mp3 {url}")
        if mov == "v":
            os.system(f"yt-dlp -o \"%(title)s\".mp4 {url}")
    elif voice == "help":
        print("Commands: help, shut down, system, tree, random, search, download, joke, color, news, computer, who am I, hack, terminal, new project, movie, get video, memory, clear, definition, research, execute, time, stocks")
        engine.say("How can i help sir.")
        engine.runAndWait()
    elif voice == "memory":
        try:
            os.system("btop")
        except:
            print("Cannot run this command.")
    elif voice == "system":
        command = input("What command would you like to run: ")
        engine.say("What command would you like to run?")
        engine.runAndWait()
        os.system(command)
    elif voice == "clear":
        os.system("clear")
    elif voice == "definition":
        getdef()
    elif voice == "research":
        getpapers()
    elif voice == "execute":
        os.system("dir .\Executables\\")
        os.system("ls Executables/")
        executablename = input("Name of executable: ")
        os.system(f".\Executables\{executablename}")
    else:
        engine.say("Not quite sure what you mean sir.")
        engine.runAndWait()



def analizetext(comm):
    if comm in todo != -1:
        engine.say('Nothing to do sir, lets have a nice day')
        engine.runAndWait()
    elif comm == "hack":
        level = input("Select level 0-34: ")
        if level == "0":
            print("Password is bandit0, good luck.")
        os.system(f"ssh bandit{level}@bandit.labs.overthewire.org -p 2220")
    elif comm == "system":
        engine.say("What command would you like to run?")
        engine.runAndWait()
        command = input("What command would you like to run: ")
        os.system(command)
    elif comm == "news":
        news()
        engine.say("Heres the news, sir.")
        engine.runAndWait()
    elif comm == "download":
        search = input("Wikipage to get: ")
        sttsearch = search.replace(" ", "_")
        engine.say(f"Here is your wikipedia page for {search}, sir.")
        engine.runAndWait()
        getpage(sttsearch)
    elif comm in greetings != -1:
        engine.say('Hello sir.')
        engine.runAndWait()
        print("How may I help you sir?")
    elif comm in good != -1:
        engine.say('Of course, sir.')
        engine.runAndWait()
        print("Of course sir.")
    elif comm in bad != -1:
        engine.say('Sorry, Sir.')
        engine.runAndWait()
        print("Sorry sir.")
    elif comm in howis != -1:
        engine.say('I am well, sir.')
        engine.runAndWait()
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
        engine.runAndWait()
    elif comm == "search":
        print("searching..")
        engine.say('What word would you like to search?')
        engine.runAndWait()
        search = input("Search: ")
        sttsearch = search.replace(" ", "_")
        analizevoice(sttsearch)
    elif comm in fun:
        os.system("curl ascii.live/can-you-hear-me")
        os.system("clear")
    elif comm == "color":
        engine.say("changine colors")
        engine.runAndWait()
        os.system("clear")
        screen = colorconsole.terminal.get_terminal()
        screen.cprint(6, 0, "\n")
    elif comm == "pause":
        pause = input("")
    elif comm == "who am I":
        os.system("curl ifconfig.me/all")
        engine.say("Here is your network data, sir")
        engine.runAndWait()
    elif comm == "tree":
        os.system("pstree")
        engine.say("Here is your active and running tasks tree, sir")
        engine.runAndWait()
    elif comm in facts:
        randnum = random.randrange(0,10)
        random_fact = random_facts[randnum]
        engine.say(random_fact)
        engine.runAndWait()
        print(random_fact)
    elif comm in new_project != -1:
        engine.say("What shall this folder be named")
        engine.runAndWait()
        foldername = input("What should this folder be named: ")
        os.system(f"mkdir ~/{foldername}")
    elif comm == "terminal":
        name = input("what's the device name: ")
        engine.say("Goodbye for now sir.")
        engine.runAndWait()
        sshto(name)
        engine.say("Welcome back, sir.")
        engine.runAndWait()
    elif comm == "help":
        print("Commands: help, shut down, system, tree, random, search, download, joke, color, news, computer, who am I, hack, terminal, new project, movie, get video, memory, clear, definition, research, execute, time, stocks")
        engine.say("How can i help sir.")
        engine.runAndWait()
    elif comm in exit_shutdown:
        engine.say("Goodbye sir")
        engine.runAndWait()
        exit(69)
    elif comm == "movie":
        os.system("ls")
        os.system("dir")
        vf =  input("Name of video file: ")
        engine.say("Enjoy the movie, sir.")
        engine.runAndWait()
        os.system(f"mpv {vf}")
    elif comm == "get video":
        mov = input("Video or Audio(v/a): ")
        url = input("URL: ")
        if mov == "a":
            os.system(f"yt-dlp -o \"%(title)s\".mp3 {url}")
        if mov == "v":
            os.system(f"yt-dlp -o \"%(title)s\".mp4 {url}")
    elif comm == "memory":
        try:
            os.system("btop")
        except:
            print("Cannot run this command.")
    elif comm == "clear":
        os.system("clear")
    elif comm == "definition":
        getdef()
    elif comm == "research":
        getpapers()
    elif comm == "execute":
        os.system("dir .\Executables\\")
        os.system("ls Executables/")
        executablename = input("Name of executable: ")
        os.system(f".\Executables\{executablename}")
    elif comm in getstocks:
        getstocks()
    else:
        engine.say("Not quite sure what you mean, sir.") 
        engine.runAndWait()
