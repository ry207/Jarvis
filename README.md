# Jarvis - AI Chatbot

A fully functional chatbot with voice recognition and text input, inspired by J.A.R.V.I.S. from *Iron Man*.
Jarvis can search wikipedia and download the wiki page, give you the news, download and play media and so much more!
I intend on adding more features, please feel free to contribute and suggest new features to add.

---

## Contents
   [Requirements](#Requirements)
   
   [Installation](#Installation)
   
   [Alternative Installation](#Alternatively)

   [Warning!](#Warning)

   [Features](#Features)
   
   [Screenshots](#Screenshots)

   [Why?](#Why)
   
---

## Requirements
To get started, ensure you have the following Python packages installed:

- `beautifulsoup4`
- `SpeechRecognition`
- `PyAudio`
- `pyttsx3`
- `colorconsole`
- `colorama`
- `requests`
- `lxml`
- `wikipedia`

You may need to set up a virtual environment before installing the dependencies.

---

## Installation
Follow these steps to install and run Jarvis:

1. **Install dependencies:**
   ```bash
   pip install beautifulsoup4 SpeechRecognition PyAudio pyttsx3 colorconsole yt-dlp colorama requests lxml wikipedia pyqt5 PyQt5 pyqt5-tools
   ```
2. **(Optional) Create and activate a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
3. **Run the chatbot:**
   ```bash
   python3 speech.py
   ```

*To run the gui*

1. **Install dependencies**
   ```bash
    pip install PyQt5 pyqt5-tools
   ```
3. **Run**
   ```bash
   python3 JarvisGUI.py
   ``` 

## Other required installs
Requirments that can't be installed using pip:
1. **mpv**
2. **btop**
3. **[yt-dlp](https://github.com/yt-dlp/yt-dlp/releases/latest/download/yt-dlp.exe)**

### Alternatively
You can install all dependences using the requirements.txt file

1. **Type this command to install all dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
Assuming no errors, all dependencies should be installed.

2. **Create an executable for windows:**
   ```bash
   pyinstaller .\JarvisGUI.py --onefile --icon=favicon.ico --hidden-import yt_dlp.compat._legacy -n JarvisGUI
   ```
   Then locate the dist directory that was created in the main folder, move the executable in the dist directory the the main directory and it should work!

---

# Warning

   ## Jarvis is not perfect!
   
   **Jarvis has a hard time listening so be patient and try and say things as slow and as clear as possible.** \
   **Text mode is faster and more precise but speech mode is easier for hands free work**

   ## Don't forget!

   **Don't forget to create these folders in the Jarvis directory: `WikiPages`, `Executables`**
   

---

## Features
Interact with Jarvis by saying or typing the following commands:

- **`text mode/speech`** - While in text mode, type 'speech' to enter speech mode. In speech mode, type 'text mode', to enter text mode.
- **`help`** - Shows a list of commands you can either say or type.
- **`find youtube video`** - Will ask for a search then output youtubes search results.
- **`shut down`** - Shuts downs the machine.
- **`open camera`** - Opens the camera application.
- **`add to do`** - Add to a text file with date time and task. (read [phrases.py](https://github.com/ry207/Jarvis/blob/main/phrases.py))
- - ***`get to do`*** - Read from to do list and show if you have anything scheduled today in highlighted text.(read [phrases.py](https://github.com/ry207/Jarvis/blob/main/phrases.py))
- **`weather`*** - Get weather from current location
- **`movie`** - Play any media file using this command.
- **`get video`**  - Download any youtube video via URL.
- **`add to journal`** - Prompt for a journal entry then Jarvis will write to a text file with a time stamp.
- **`tell me a fact`** - Tells a random fact.
- **`stocks`** - List trending stocks.
- **`what time is it`** - Tells date and time.
- **`research`** - Outputs interesting research papers with link.
- **`execute`** - Execute an executable you put in the `Executables` folder
- **`hack`** - Connect to [Over the wire: Bandit](https://overthewire.org/wargames/bandit/) via ssh for fun hacker challenges.
- **`terminal`** - ssh into your own computer to access full command prompt capabilities.
- **`new project`** - Create a new folder in your home directory titled whatever you like.
- **`memory`** - Use [btop](https://github.com/aristocratos/btop) command (Resource monitor that shows usage and stats for processor, memory, disks, network and processes.)\
     See [btop installation](https://github.com/aristocratos/btop?tab=readme-ov-file#installation), to be able to use this command.
- **`clear`** - Clear screen.
- **`advice`** - Jarvis gives you advice.
- **`definition`** - Get the definition of any word.
- **`system`** - Prompt for a command that will enter in the terminal.
     *For example:* `ls, echo, rm hello.txt`
- **`search`** – Prompts for a topic, searches Wikipedia, and provides a brief description (works better in text mode).

   *Example search terms:* `String theory`, `Abraham Lincoln`, `Blockchain`, `Bitcoin`.
  
- **`news`** - Displays hacker news titles.
- **`download`** - Download a wikipedia page to view and save the file to your computer.
  
  *Example search terms:* `Artificial intelligence`, `Mark Zuckerberg`, `Quantum mechanics`, `Google`, `Airplane`.

- **`tell me a joke`** – Displays a funny animation.
- **`who am I`** – Displays network information (may not work on all devices).
- **`tree`** – Displays active running tasks.
- **`function`** – Prompts for a word and outputs its length.



---

## Additional Keywords
### (see [phrases.py](https://github.com/ry207/Jarvis/blob/main/phrases.py) for the full list of phrases) 
Jarvis responds to the following (and more) keywords:

**Greetings:**
```
"Hello", "hello", "hello Jarvis", "jarvis", "hey Jarvis", "Jarvis", "come in Jarvis", "how are you", "how are you Jarvis", "what's up"
```

**Positive Responses:**
```
"Good", "good", "great", "okay", "okay jarvis", "thanks", "thanks jarvis", "Great", "I'm good", "i'm good", "im good", "i'm okay"
```

**Negative Responses:**
```
"bad", "not good", "no", "No"
```

---

## Screenshots

![Jarvis Basic Functions](screenshot1.png "Jarvis functions")
*Some of the basic functions Jarvis can perform.*

![Live server created by jarvis](screenshot2.png "Wikipedia page Jarvis downloaded")
*The page on aerodynamics I had Jarvis download, he then created a live server in which I could view it in!*

![Hacker games](screenshot3.png "Succesfull connection to bandit hacker games") \
*Jarvis successfully connected to OverTheWire: Bandit via ssh*

![Research Capabilities](screenshot4.png "Jarvis's research capabilities") \
*Jarvis's research capabilities*


---

## Why 
I created Jarvis because I thought it would be fun to have a chatbot that talks back—plus, I had nothing better to do... Jarvis has come a long way since I started but he still has a long way to go before he's finished. What features do you guys have in mind???

---

### Contributions
Feel free to contribute or suggest new features!

