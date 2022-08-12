# do exercise here
# upload to github for portfolio
# thank me later when your git graph is as green as the python money u gonna earn

'''
print("""
--------------------------------------------------------------------
Task 1
--------------------------------------------------------------------""")
n = 1
while n < 4:
    print("--------------------------------------------------")
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    print("--------------------------------------------------")
    if num1 == num2:
        print("Numbers are equal!")
    if num1 != num2:
        print("Numbers are not equal!")
    if num1 > num2:
        print("First number is greater than second number!")
    if num1 < num2:
        print("Second number is greater than first number!")
    if num1 >= 1000 and num2 >= 1000:
        print("Both numbers are big numbers!")
    if num1 >= 1000 and num2 <= 1000:
        print("First number is big and second one is small!")
    if num1 <= 1000 and num2 >= 1000:
        print("Second number is big and first one is small!")
    if not(num1 >= 1000 and num2 >= 1000):
        print("Both numbers are small numbers!")
    if num1 == 0 or num2 == 0:
        print("One of numbers are equal to zero!")
    if num1 and num2 :
        print("Both numbers have boolean value!")

    n += 1
else:
    print(" \n Thank you!") 
'''


print("""
--------------------------------------------------------------------
Task 2
--------------------------------------------------------------------""")
print("January, February, March, April, May, June, July, August, September, October, November, December")
print(".............................................................")
month_31 = ["january", "1", "march", "3", "may", "5", "july", "6", "august", "8", "october", "9", "december", "12"]
month_28 = ["February", "2"]
month_30 = ["april", "4", "june", "6", "september" ,"9", "november", "11"]

days_31 = "31 days"
days_28 = "28 days"
days_30 = "30 days"

m_input = input("Input the name of Month or number of Month: ")
if (m_input.lower() in month_31) or (m_input in month_31):
    print(" Number of days: ", days_31)
elif m_input.lower() in month_28 or m_input.lower().startswith("f"):
    print(" Number of days: ", days_28)
elif m_input.lower() in month_30:
    print(" Number of days: ", days_30)
else:
    print("please check the spelling!")

