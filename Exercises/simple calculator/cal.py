num1 =      float(input("First number: "))
num2 =      float(input("Second number: "))
result =    input("* for 'ADD' press 'A'\n* for 'SUBTRACT' press 'S'\n> ")

if result.lower() == "a":
    print(num1 + num2)
elif result.lower() == "s":
    print(num1 - num2)
else:
    print("enter a valid input!")
