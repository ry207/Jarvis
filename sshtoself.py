import os

def sshto(name):
    os.system("curl ifconfig.me/ip")
    ip = input("\nCopy the ip above then paste here: ")
    final = f"ssh {name}@{ip}"
    print("Now enter your password and continue.")
    os.system(final)

