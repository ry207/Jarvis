import datetime

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
