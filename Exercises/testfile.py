
from distutils.command.build_scripts import first_line_re
import re
import datetime
import os
import time


'''convert=float(25.4)
while True:
    print("*******MM*******")
    user_input = input()
    if user_input.lower() == "end":
        break
#     else:
#         MM = float(user_input)
#         Results=float(MM/convert)
#         print("*****Inches*****")
#         print("%.3f" % Results)
#         print("%.4f" % Results)
#         print("%.5f" % Results)

# num = int(input("Enter a number: "))
# flag = False

# # prime numbers are greater than 1
# if num > 1:
#     # check for factors
#     for i in range(2, num):
#         if (num % i) == 0:
#             # if factor is found, set flag to True
#             flag = True
#             # break out of loop
#             break

# # check if flag is True
# if flag:
#     print(num, "is not a prime number")
# else:
#     print(num, "is a prime number")

# '''
# from textwrap import dedent
# import textwrap

# x = "this is a sentence. i am very happy. my name is Reza"
# print(f"hello{'. '.join(map(lambda s: s.strip().capitalize(), x.split('.')))}")                           
#x = input(dedent(y)).lower()

#print(x)

# questions = ["What is 1 + 1",
#              "Who is the 45th president of the United States?",
#              "True or False... The Toronto Maple Leafs have won 13 Stanley   Cups?",
#              "What was the last year the Toronto Maple Leafs won the Stanley   Cup?",
#              "True or False... The current Prime Minister of Canada is Pierre Elliot Tredeau?"]
# answer_choices = ["a)1\nb)2\nc)3\nd)4\n:",
#                   "a)Barack Obama\nb)Hillary Clinton\nc)Donald Trump\nd)Tom Brady\n:",
#                   ":",
#                   "a)1967\nb)1955\nc)1987\nd)1994\n:",
#                   ":"]
# correct_choices = ["b",
#                    "c",
#                    "t",
#                    "a",
#                    "f"]
# answers = ["1 + 1 is 2",
#            "The 45th president is Donald Trump",
#            "",
#            "The last time the Toronto Maple Leafs won the Stanley Cup was 1967",
#            "The current Prime Minster of Canada is Justin Tredeau"]


# def quiz():
#     score = 0
#     for question, choices, correct_choice, answer in zip(questions, answer_choices, correct_choices, answers):
#         print(question)
#         user_answer = input(choices).lower()
#         if user_answer in correct_choice:
#             print("Correct")
#             score += 1
#         else:
#             print("Incorrect", answer)
#     print(score, "out of", len(questions), "that is", float(score / len(questions)) * 100, "%")
# quit
# - Create a repository just on your computer
# - Create a git notes file in that repository
# - Every time you make an entry into the file, make a commit
# - Research the topics listed below and add a short definition of them **in your words** to the README 
#   - Surface level research for now, we are not making a PHD here...
#   - Commit after each one!
# - Topics:
#   - "What makes a good commit message"
#   - "What is staging in git"
#   - "How to check which version of git you have installed"
#   - "What is Semantic Versioning (SemVer)"
#   - "How to see previous commands I have done in Linux"
# - Then add a new text file with the relevant commands that you have used doing this exercise





# text = """ Hello, This is a simple sentence. 
# The quick brown fox jumps over the lazy dog. 
# THE QUICK BROWN FOX jumps OVer ThE lAzy dog."""

# pattern = r"([A-Z][a-z].)"

# match = re.match(pattern, text)
# print(match)
# print("----------------------------")
# search = re.search(pattern, text)
# print(search)
# none = re.match("dci", text)
# null = re.search("dci", text)
# print(type(none))
# print(type(null))

# d1 = datetime.datetime.today()   # this shows current date and time
# d2 = datetime.datetime(2022, 1, 1, 1 , 1 , 30)   # this convert the numbers to the datetime object (with time)
# d3 = datetime.datetime.strptime('January 15, 2005', '%B %d, %Y') # presents our date and time in datetime object
# d4 = d3.strftime('%Y-%d-%B %H:%M:%S')   # format the datetime object according to our formatting
# d5 = datetime.date(2022,1,1)     # this convert the numbers to the datetime object (without time)
# d6 = datetime.date.today()     # this just shows the current date
# d7 = datetime.date.fromisoformat('2005-01-01')     # creates date time object
# d8 = datetime.date(year=2000, month=1, day=1)     # datetime instance, (year, month and day are 'keys')
# d9 = d3.year              # takes out the year from a datetime object as 'int' value
# d10= d3.month             # takes out the month from a datetime object as 'int' value
# d11= d3.hour             # takes out the hour from a datetime object as 'int' value
# d12= d2 + datdef full_name (*name):
# collect_name = ""
# for i in name:
# if i != name[-1]:
# collect_name += f"{i} "
# else:
# collect_name += f"{i}"
# return collect_name

# enter_name = full_name("ABC", "abc", "lmn", "LMN")
# print(enter_name) 



# print("d1", d1,"\nd2", d2,"\nd3",d3,"\nd4",d4,"\nd5",d5,"\nd6",d6,"\nd7",d7,"\nd8",d8,"\nd9",d9,"\nd10",d10,"\nd11",d11,"\nd12",d12,"\nd13",d13,"\nd14",d14)



# def sub(first_number, second_number):
#     return first_number-second_number

# def multiply(first_number, second_number):
#     return first_number*second_number

# def divide(first_number, second_number):
#     return first_number/second_number

# def add(first_number, second_number):
#     return first_number+second_number

# first_input = int(input("Enter the first number: "))
# second_input = int(input("Enter the second number: "))


# print(f"Subtraction result of first number to the second number is {sub(first_input, second_input)}.")
# print(f"Multiplication result of first number to the second number is {multiply(first_input, second_input)}.")
# print(f"Division result of first number to the second number is {divide(first_input, second_input)}.")
# print(f"Addition result of first number to the second number is {add(first_input, second_input)}.")



# names = ["Victor", "Peter", "Mary", "John", "Badara", "Peer"]

# names[-1] = "Malcom X"

# additional_names = ["Ahmad", "Jack"]

# names = names+additional_names
# names.extend(additional_names)
# names.insert(3, "Shantanu")
# names.append("Appended")
# names.index("Malcom X")
# names.pop()
# names.remove("Victor")
# names.reverse()
# names.clear()


# print(names)


# names = []
# user_input=""
# while user_input != "q":
#     user_input = input("name: ")

#     if user_input == "q":
#         print(names)
#         quit()
#     names.append(user_input)
#     print(names)

# def full_name (*name):
# collect_name = ""
# for i in name:
# if i != name[-1]:
# collect_name += f"{i} "
# else:
# collect_name += f"{i}"
# return collect_name

# enter_name = full_name("ABC", "abc", "lmn", "LMN")
# print(enter_name) 

# def full_name(**kwargs):
#     print(kwargs)
#     first_name = kwargs["first_name"]
#     last_name = kwargs["last_name"]
#     def add_sir(name):
#         return f"Sir {name}"
#     return f"{first_name} {last_name}"


# print(full_name(first_name="Jane", last_name="Doe", location="Berlin"))

# last_name = {"Doe": "John",
#              "Jack": "Brown",
#              "Jeo": "White",
#              "Brianne": "Stark",
#              "Molly": "Andrews"         
# }
#                                                 # "Pass by reference" variables can change
# def full_name(last_name):
#                                                 # variations 
#     last_name["Doe"] = "Hoffmann"
#     last_name["Brianne"] = "Tarth"
    
#     return last_name["Doe"], last_name["Brianne"]

# print(full_name(last_name))
# print(last_name)
    
    
    
    
    
                                                #print(last_name)



last_name = "Emily"        
                                                # "Pass by reference" variables can change
def full_name(last_name):
                                                # variations 
    last_name = "Tom"
    
    return last_name

full_name(last_name)
print(last_name)















