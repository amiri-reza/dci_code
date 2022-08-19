import os
import time
import datetime
from colorama import *
from art import *
import smtplib

#initializing colorama
init()

def gmail_send(subject, message, from_mail, to_mail, password):
    global link
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(from_mail, password)
    msg            = EmailMessage()
    message        = f'{message}'
    msg.set_content(message)
    msg['Subject'] = subject
    msg['From']    = from_mail
    msg['To']      = to_mail
    server.send_message(msg)



#art GUI
print(Fore.LIGHTCYAN_EX+"")
tprint("AWESOME JOURNAL", font="random")
print(""+Style.RESET_ALL)




t =open("journal.txt", "r")
print(t.read())



new_entry = input("ENTER DIARY ENTRY HERE: ")
now = datetime.datetime.now().isoformat(sep=" ", timespec="seconds")

here = os.getcwd().replace("\\","/") # defining path variable for later if statement


if here.upper() in new_entry.upper(): # if weird path bug, dont save
    print("")
elif new_entry != "": # if entry is not empty, save entry

    with open("journal.txt", "a") as file:
        file.write(f"{now} {new_entry} \n")
else:
    print("Empty string. NOT ADDING.") # if entry empty, dont save
