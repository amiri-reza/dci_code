from art import *
from colorama import *
from textwrap import dedent
import os
os.system('cls' if os.name == 'nt' else 'clear')


questions =[
    " saw a lady who needs help. what is better to be done?",
    """\
    was helping that person, suddenly a thief robbed the baggages
    and drove. What should be done?""",
    """\
    asked for help and the lady accept to drive and follow after
    thief. So they drove but couldn't find the thief. What now? """, 
    "went to a Police Station and asked for help. What should Police do?", 
    """\
    waited until police finds the thief. They found the thief and 
    sent a car to capture him. Now what should be done?""", 
    "thanked policemen and left the police station. Now what should they do?"
    ],[
        """\
        is very tired but took the bus in front of airport for 
        Elizabeth's address. Sleep in the bus?""", 
        " wakes up but it is the last stop. what should be done?", 
        " is very tired and needs some water and food.", 
        """\
        ate some food and is ready to continue walking. pay the 
        restaurant or run?""", 
        ]
ways =[
    "\nTo Help him PRESS H \nor \nTo Leave it PRESS L\n", 
    "\nTo Follow thief PRESS F \nor \nTo Ask for help PRESS A\n", 
    "\nTo Go to Police Station PRESS P\nor\nTo Continue searching PRESS S\n", 
    "\nTo Check the CCTVs PRESS C\nor\nTo Leave & wait for police, PRESS W\n",
    "\nTo Go to beat up the thief PRESS B\nor\nTo Call Elizabeth PRESS C\n", 
    "\nTo Thank that lady too PRESS T \nor \nTo Leave the country PRESS L\n"
    ],[
        "\nFor Yes PRESS Y \nor \nFor No PRESS N\n", 
        "\nTo Take a taxi PRESS T \nor \nTo Walk back PRESS W\n", 
        "\nTo Go to a restaurant PRESS R \nor\nTo Continue walking PRESS C\n",
        "\nTo Ran away PRESS R \nor To Payed the restaurant PRESS P\n"]
right_ways =[
    ["h", "Helped\n"], 
    ["a", "Asked for help\n"], 
    ["p", "Went to police station\n"], 
    ["c", "Checked the CCTV\n"], 
    ["c", "Called Elizabeth\n"], 
    ["t", "Thanked that lady\n"]
    ],[
        ["y", "Yes\n"], 
        ["w", "Started to walk the way back\n"], 
        ["r", "Went to a restaurant\n"], 
        ["p", "Pay the restaurant\n"],]
wrong_ways =[
    ["l", "Left\n"], 
    ["f", "Followed thief\n"],
    ["s", "Continued searching\n"],
    ["w", "Waited until they find something\n"],
    ["b", "Went to beat up the thief\n"],
    ["l", "Left the country immediately\n"]
    ],[
        ["n", "No\n"],
        ["t", "Took a taxi\n"], 
        ["c", "Continue walking\n"],
        ["r", "Ran away\n"]]
bad_results =[
    "A thief came and robbed all the belongings with little beat up.",
    "Thief had a sport car and left the scene very fast. No Chance.",
    "Searching needle in haystack???",
    "\n...\n...\n..\n...\n... Still no news... waiting...",
    "Police reacted quickly. Spending some time in jail is good!.",
    "So what? comparing a country with one event?"
    ],[
        "Got off the bus and found the house. Thank you! ",
        "Taxi reached the destination and met Elizabeth. Thank You!",
        "Walking with empty stomach, thirsty and lack of sleep? RIP!",
        "Ran away. But not far. Police was fast!"]


separator = "*"*79
print(separator, Fore.LIGHTCYAN_EX+"")
tprint("NICOS WEG", font="random")
print(""+Style.RESET_ALL+separator )


gender = input(dedent("""\
    For Male Character Press 1
    or
    For Female Character Press 2\n"""))
if gender ==    "1":
    name =      "Nicolas"
    he_she =    "he"
    him_her =   "him"
    his_her =   "his"
elif gender == "2":
    name = "Lisa"
    he_she = "she"
    him_her = "her"
    his_her = "her"
else:
    print("Please select the ight_wcorrect answer and try again!")
    quit()
x = (
    f"""\
    {separator}
    {name} is at the Airport. {he_she.capitalize()} is from Spain and doesn't
    know any German. {he_she.capitalize()} came to Germany to see {his_her}
    aunt "Elizabeth". On the way out of airport, {he_she} has two options.
    Which one you choose:\n""")
print(dedent(x))


choice = input("To Turn Left PRESS L \nor \nTo Turn Right PRESS R?\n")
progress = 0
if choice == "r":
    for question, way, right_way, wrong_way, bad_result in zip(
        questions[0], ways[0], right_ways[0], wrong_ways[0], bad_results[0]):
        print(separator+"\n"+name, dedent(question))
        choice = input(way)
        if choice.lower() in right_way:
            progress += 1
            print(right_way[1])
        elif choice.lower() in wrong_way:
            print(wrong_way[1],"\n"+(bad_result))
            break
        else:
            print("Wrong Keyboard Input. Try Again!")
            break
    print("\nYour progress was",round(float(progress/len(questions[0]))*100),"%")
elif choice == "l":
    for question, way, right_way, wrong_way, bad_result in zip(
        questions[1], ways[1], right_ways[1], wrong_ways[1], bad_results[1]):
        print(name, dedent(question))
        choice = input(way)
        if choice.lower() in right_way:
            progress += 1
            print(right_way[1])
        elif choice.lower() in wrong_way:
            print(wrong_way[1],"\n"+(bad_result))
            break
        else:
            print("Wrong Keyboard Input. Try Again!")
            break
    print(name, "is at Elizabeth's door. The story is finished. Thank you!")
    print("\nYour progress was",round(float(progress/len(questions[1]))*100),"%")
else:
    print("Wrong Input. Try Again! Thank You.")

print(f"THE END!".center(71))



