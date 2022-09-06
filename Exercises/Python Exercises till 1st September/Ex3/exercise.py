# do exercise here
# upload to github for portfolio
# thank me later when your git graph is as green as the python money u gonna earn

'''
print("""
--------------------------------------------------------------------
Task 1
--------------------------------------------------------------------""")
for input1 in range(0,3):
    input1 = input("Enter a number: ")
    if float(input1) % 2 == 0:
        print("Even Number")
    else:
        print("Odd Number")
'''


'''
print("""
--------------------------------------------------------------------
Task 2
--------------------------------------------------------------------""")




while True:

    i = int(input("Please enter a number between 1 to 3 or '0' to end program: "))
    if i == 0:
        print("Bye bye!")
        break
    elif i == 1:
        j = int(input("Please enter the range number: "))
        for x in range(j+1):
            print(x)
    elif i == 2:
        k = int(input("Please enter starting number: "))
        l = int(input("Please enter stopping number: "))
        for y in range(k, l+1):
            print(y)
    elif i == 3:
        m = int(input("Please enter starting number: "))
        n = int(input("Please enter stopping number: "))
        o = int(input("Please enter step: "))
        for z in range(m, n, o+1):
            print(z)
    else:
        print("sorry, but you have to choose numbers between 1, 2 or 3! or '0' to end this.")
'''

'''
print("""
--------------------------------------------------------------------
Task 3
--------------------------------------------------------------------""")


number = int(input("enter your number: "))
for i in range(1, number+1):
    
    if number % i == 0:
        print(i)
'''




'''
print("""
--------------------------------------------------------------------
Task 4
--------------------------------------------------------------------""")

u = int(input("enter the number: "))

if u > 1:
    for t in range(2, u):
        if u % t == 0:
            print(u, "is not a prime number.")
            break
    else:
            print(u, "is a prime number.")
            
else:
    print("That is not a prime number!")
'''


'''
print("""
--------------------------------------------------------------------
Task 5
--------------------------------------------------------------------""")


for x in range(1, 101):
    if x % 15 == 0:
        print("BuzzFizz")
    elif x % 3 == 0:
        print("Buzz")
    elif x % 5 == 0:
        print("Fizz")
    else:
        print(x)
'''

print("""
--------------------------------------------------------------------
Task 6
--------------------------------------------------------------------""")

for p in range(999, 2001):
    if p % 7 == 0 and p % 5 != 0:
        print(p)

