# do exercise here
# upload to github for portfolio
# thank me later when your git graph is as green as the python money u gonna earn

'''
print("""
--------------------------------------------------------------------
Task 1
--------------------------------------------------------------------""")


i = 1
while i < 3 :
    print("\n")
    inp1 = int(input("First Number: "))
    inp2 = int(input("Second Number: "))
    inp3 = int(input("Third Number: "))
    sum = inp1 + inp2 + inp3
    triple = inp1 * inp2 * inp3
    if inp1 == inp2 == inp3:
        print("The triple sum is: ", triple)
    else:
        print("The sum is: ", sum)
    i += 1
print("\n", "Thank you!")
'''
'''
print("""
--------------------------------------------------------------------
Task 2
--------------------------------------------------------------------""")

n = 1
while n < 4:
    print("\n")
    in1 = int(input("First number: "))
    in2 = int(input("Second number: "))
    diff = 2 * (in1 - in2)
    diff2 = abs(in1 - in2)
    if in1 > in2:
        print("The result of calculation is: ", diff)
    else:
        print("The result of calculation is: ", diff2)
    n += 1
print("\n", "Thank you!")
'''


'''
print("""
--------------------------------------------------------------------
Task 3
--------------------------------------------------------------------""")

s = 1
while s < 5:
    print("\n")
    input1 = int(input("Number to check: "))
    if input1 == 0:
        print("0 is not an even or odd number!")
    elif input1 % 2 == 0:
        print(input1, "is an even number!")
    elif input1 % 2 != 0:
        print(input1, "is an odd number!")
    s += 1
print("\n", "Thank you!")

'''




'''

print("""
--------------------------------------------------------------------
Task 4
--------------------------------------------------------------------""")
from math import pi
radius = float(input("Enter the radius of the circle: "))
area = round((pi * pow(radius, 2)), 2)

print("The area of the circle with radius ", radius, "is: ", area)


'''


print("""
--------------------------------------------------------------------
Task 5
--------------------------------------------------------------------""")
from datetime import datetime
now = str(datetime.now())
lastMiniSec = now[-1:]
z = 1
while z < 11:
    guess = input("Guess a number between 1 and 10 until you get it right: ")
    if guess == lastMiniSec:
        print("Well done!")
    else:
        print("try again!")
    z += 1


'''
print("""
--------------------------------------------------------------------
Task 6
--------------------------------------------------------------------""")

p = 1
while p < 3:
    print("............................................")
    print("Celsius in Fahrenheit: Press CF")
    print("Fahrenheit in Celsius: Press FC")
    cf = input("select one option by pressing 'CF' or 'FC': ")
    temp = float(input("Enter a temperature: "))
    cf1 = ["celsius", "fahrenheit"]
    formula_cf = (temp* 9/5) + 32
    formula_fc = (temp-32) * 5/9
    if cf.lower() == "cf":
        print("The temperature in Fahrenheit is:", round((formula_cf), 2), "°F!")
    elif cf.lower() == "fc":
        print("The temperature in Celsius is: ", round((formula_fc), 2), "°C!")
    
    p += 1

'''
'''
print("""
--------------------------------------------------------------------
Task 7
--------------------------------------------------------------------""")

print(" ","\n "," ","\n "," "," ","\n "," "," "," ","\n "," "," "," "," "," ", sep="*")

for i in reversed(range(5)):
    print(i * " *")
'''


'''
from termios import FF1


print("""
--------------------------------------------------------------------
Task 8
--------------------------------------------------------------------""")
f = 0
f1 = 0
f2 = 1
while f < 50:
    print(f1)
    plus = f1 + f2
    f1 = f2
    f2 = plus
    f += 1
    if f1 > 50:
        break

  '''  

