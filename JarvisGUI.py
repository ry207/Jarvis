from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QTextEdit, QLineEdit, QVBoxLayout, QHBoxLayout, QWidget, QLabel, QInputDialog
from PyQt5.QtGui import QIcon
import sys
import os
import random
import datetime
import pyttsx3
import speech_recognition as sr
import subprocess as sp
import requests

from wikipage import getpage
from forum import news
from stocks import getstocks
from phrases import *
from yahooyt import yaho
from journal import addToJournal
from papers import getpapers
from wiki import analizevoice




engine = pyttsx3.init('sapi5')

# Set Rate
engine.setProperty('rate', 190)

# Set Volume
engine.setProperty('volume', 0.75)

# Set Voice (Female)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


r = sr.Recognizer()

class JarvisGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Jarvis AI Assistant")
        self.setGeometry(100, 100, 800, 500)
        
        self.setStyleSheet("""
            QWidget {
                background: #222222;
                color: white;
                font: Futura;
            }
            QPushButton {
                background-color: #222222;
                color: #FFFFFF;
                border-style: outset;
                padding: 2px;
                font: bold 16px;
                border-width: 6px;
                border-radius: 10px;
                border-color: #222222;
            }
            QPushButton:hover {
                background-color: #191919;
            }
            QPushButton#okButton {                             /*    <--- #okButton      */
                background-color: #444444;
            }
            QTextEdit {
                background-color: #222222;
            }
        """)

        # Main layout
        main_layout = QVBoxLayout()

        self.setWindowIcon(QIcon('favicon.ico'))

        # Command Section
        command_layout = QHBoxLayout()
        self.command_label = QLabel("Enter Command:")
        self.input = QLineEdit(self)
        self.input.setPlaceholderText("Type a command...")
        self.button = QPushButton("Execute", self)
        self.input.returnPressed.connect(self.run_command)  # Connect Enter key press
        self.button.clicked.connect(self.run_command)
        command_layout.addWidget(self.command_label)
        command_layout.addWidget(self.input)
        command_layout.addWidget(self.button)

        # Output Section
        self.output_label = QLabel("Output:")
        self.output = QTextEdit(self)
        self.output.setReadOnly(True)

        # Assemble layouts
        main_layout.addLayout(command_layout)
        main_layout.addWidget(self.output_label)
        main_layout.addWidget(self.output)

        # Set layout to central widget
        container = QWidget()
        container.setLayout(main_layout)
        self.setCentralWidget(container)

        # Redirect console output to GUI
        sys.stdout = self
        sys.stderr = self

    def write(self, text):
        """ Redirect console output to the GUI output window. """
        self.output.append(text.strip())

    def flush(self):
        """ Required for sys.stdout compatibility. """
        pass

    def get_user_input(self, prompt):
        """ Show a dialog to get user input instead of using console input(). """
        text, ok = QInputDialog.getText(self, "Input Required", prompt)
        if ok and text.strip():
            return text.strip()
        return None
    

    def run_command(self):
        voice = self.input.text().strip()
        if not voice:
            self.output.append("Please enter a command.")
            return
        
        self.output.append(f"> {voice}")  # Show entered command
        self.input.clear()

        if voice in exit_shutdown:
            self.output.append("Shutting down...")
            engine.say("Goodbye, Sir")
            engine.runAndWait()
            sys.exit(69)

        elif voice in greetings:
            engine.say("Hello sir")
            engine.runAndWait()

        elif voice in youtube_phrases:
            engine.say("What YouTube video, sir?")
            engine.runAndWait()
            ytsearch = self.get_user_input("What YouTube video would you like to search for?")
            if ytsearch:
                yaho(ytsearch)
                self.output.append(f"Searching YouTube for: {ytsearch}")

        elif voice in stock_phrases:
            self.output.append("Fetching trending stocks...")
            getstocks()

        elif voice in thanks:
            engine.say("you're welcome sir")
            engine.runAndWait()
            self.output.append("You're welcome sir.")

        elif voice in todo != -1:
            engine.say('Nothing to do sir, lets have a nice day.')
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

        elif voice in facts:
            randnum = random.randrange(0,30)
            random_fact = random_facts[randnum]
            engine.say(random_fact)
            engine.runAndWait()
            self.output.append(f"Fact: {random_fact}")

        elif voice in time_date:
            now = datetime.datetime.now()
            formatted_time = now.strftime("%A, %B %d, %I:%M %p")
            engine.say(f"Today is {formatted_time}")
            engine.runAndWait()
            self.output.append(f"Current date and time: {formatted_time}")

        elif voice == "research":
            getpapers()

        elif voice == "advice":
            res = requests.get("https://api.adviceslip.com/advice").json()
            print(res['slip']['advice'])

        elif voice == "download":
            engine.say("What page would you like to download: ")
            engine.runAndWait()
            stt = self.get_user_input("Wiki search: ")
            sttsearch = stt.replace(" ", "_")
            engine.say(f"Getting the wiki page for {stt} then creating a live web server where you can access your file")
            engine.runAndWait()
            getpage(sttsearch)

        elif voice == "help":
            print("Commands: help, shut down, tell me a fact, search, download, news, who am I, hack, terminal, movie, get video, research, time, stocks, find youtube video, add to journal, advice, open camera")
            engine.say("How can i help sir.")
            engine.runAndWait()

        elif voice == "who am I":
            os.system("curl ifconfig.me/all")
            engine.say("Here is your network data, sir")
            engine.runAndWait()

        elif voice == "search":
            self.output.append("searching..")
            engine.say('What word would you like to search?')
            engine.runAndWait()
            stt = self.get_user_input("Wiki search: ")
            analizevoice(stt)

        elif voice == "open camera":
            sp.run('start microsoft.windows.camera:', shell=True)

        elif voice == "add to journal":
            engine.say("What would you like to write, sir?")
            engine.runAndWait()
            entry = self.get_user_input("Enter journal entry:")
            if entry:
                addToJournal(entry)
                self.output.append("Journal entry added.")

        elif voice == "news":
            news()
            engine.say("Here's the news, sir.")
            engine.runAndWait()
            self.output.append("Displaying latest news.")

        elif voice == "download":
            engine.say("What page would you like to download?")
            engine.runAndWait()
            page = self.get_user_input("Enter Wikipedia page to download:")
            if page:
                getpage(page.replace(" ", "_"))
                self.output.append(f"Downloaded Wikipedia page: {page}")

        elif voice == "movie":
            os.system("ls")
            os.system("dir")
            vf = self.get_user_input("Name of video file: ")
            engine.say("Enjoy the movie, sir.")
            engine.runAndWait()
            if vf:
                os.system(f"mpv \"{vf}\"")

        elif voice == "get video":
            engine.say("What video sir.")
            engine.runAndWait()
            url = self.get_user_input("URL: ")
            os.system(f"yt-dlp -o \"%(title)s\".mp4 {url}")

        else:
            engine.say("Not quite sure what you mean, sir.")
            engine.runAndWait()
            self.output.append("Command not recognized.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = JarvisGUI()
    window.show()
    sys.exit(app.exec_())


        
