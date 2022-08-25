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




