import datetime
from colorama import Fore

def addToJournal(journal_entry):

    x = datetime.datetime.now()
    hour = x.strftime("%I")
    hour = hour.replace("0", "")
    minute = x.strftime("%M")

    try:
        with open("Journal.txt", "a") as f:
            f.write(f"{x.strftime("%A")}, {x.strftime("%B")} {x.strftime("%d")} {hour}:{minute} {x.strftime("%p")} >> {journal_entry}\n")
        print("Wrote to Journal.txt")
    except:
        print("An error may have occured.")

def addToDo(todo_entry):

    date = input("Date(M/D/Y): ")
    time = input("Time(XX:XX XM): ")

    try:
        with open("Todo.txt", "a") as f:
            f.write(f"{date} at {time}:  {todo_entry}\n")
        print("Wrote to Todo.txt")
    except:
        print("An error may have occured.")

def getToDo():
    count = 0
    x = datetime.datetime.now()
    date = x.strftime("%x")
    with open("Todo.txt", "r") as f:
        for line in f:
            if date in (f" {line} "):
               print(Fore.GREEN + line + Fore.WHITE)
               count += 1
            else:
                print(line)
        print(f"{Fore.CYAN}You have {Fore.RED}{count}{Fore.CYAN} things to do today.{Fore.WHITE}")
