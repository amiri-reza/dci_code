# do exercise here
# upload to github for portfolio
# thank me later when your git graph is as green as the python money u gonna earn

'''
print("""------------------------------------------------------------
Task 1
---------------------------------------------------------------------""")

three_mul = 'fizz'  # the string was unterminated.
five_mul = 'buzz'
num1 = 3
num2 = 5  # number should be 5
max_num = 100
   
for i in range(1,max_num):   # max_num, not max_number
    if i%num1 == 0 and i%num2 == 0:  #the multiplied one, should come first
        print(i, three_mul+five_mul)   #print should be indented
    elif i%num1 == 0:   # equal sign is ==, not =
        print(i, three_mul)
    elif i%num2 == 0:
        print(i, five_mul)      

'''
'''

print("""------------------------------------------------------------
Task 2
---------------------------------------------------------------------""")



n = 5        
number = 1     
sum = 0      
while number < n + 1:
    sum = sum + number    # instead of 1, enter "number"  # 1 3 6 10 15  
    number = number + 1                                   # 2 3 4 5   

print("Sum =", sum)

'''



'''
print("""------------------------------------------------------------
Task 3
---------------------------------------------------------------------""")

n = 5
sum = 0
for num in range(n+1):      #just add a +1 in the range function
    sum += num
print("Sum =", sum)
'''



'''
print("""------------------------------------------------------------
Task 4
---------------------------------------------------------------------""")

print(" \n Program 1 \n")
for x in range(3):   #use : after for loop
    print(x)


print(" \n Program 2 \n")
for j in range(5):
    print("This is loop number", j)  #write "j" out of string

print(" \n Program 3 \n")
x = 10     #define x before using it.
while x > 0:
    print(x)
    x -= 1

print(" \n Program 4 \n")
countdown = 5   #countdown should have value 5
while countdown:
    print(f"{countdown}")
    countdown -= 1
else:
    print("Start!")


'''




'''
print("""------------------------------------------------------------
Task 5
---------------------------------------------------------------------""")
i = 0
while i < 3:
    x = int(input("First number: "))  #should use integer format
    y = int(input("Second number: "))  #should use integer format
    z = int(input("Third number: "))      #should use integer format  

    if x == y or y == z or x==z:      #equal sign is == , not =  **** x==z should be written
        print("result = 0 \n")   #should use print
    else:
        sum = x + y + z
        print("Calculated sum is ", sum, "\n")    #sum is the calculated result, not result
                                             # print should be indented.
    i += 1

'''

'''

print("""------------------------------------------------------------
Task 6
---------------------------------------------------------------------""")


a = 0
while a < 2:
    print("\n")
    x = int(input("First number: "))
    y = int(input("Second number: "))

    result = x + y
    if result > 15 and result < 20:
        print("Calculated sum is \n", 20)
    else:
        print("Calculated sum is ", result)
    a += 1


'''





'''

print("""------------------------------------------------------------
Task 7
---------------------------------------------------------------------""")
a = input("First value: ")
b = input("Second value: ")

print("Before swapping: a =", a, " ,b =", b)

temp = a
a = b
b = temp


print("After swapping: a =", a, " ,b =", b)
'''


'''
print("""------------------------------------------------------------
Task 8
---------------------------------------------------------------------""")
x = float(input("First number: "))
y = float(input("Second number: "))
z = float(input("Third number: "))
print("**************first method*********************")
print("The maximum value is ", max(x, y ,z))
print("The minimum value is ", min(x, y ,z))
print("***********************************")

print("..............second method....................")
if x > y and x > z:
    print("the maximum value is ", x)
elif y > x and y > z:
    print("The maximum value is ", y)
elif z > x and z > y:
    print("The maximum value is ", z)
print("..................................")
if not(x > y and x > z):
    print("the minimum value is ", x)
elif not(y > x and y > z):
    print("The minimum value is ", y)
elif not(z > x and z > y):
    print("The minimum value is ", z)   
print("..................................")
'''

'''
print("""------------------------------------------------------------
Task 9
---------------------------------------------------------------------""")
o = 0
while o < 3:
    try:
        x = input(" \n Type your value: ")
        y = int(x)
        
        if y == 0:
            print("Your entered value is now ", bool(y))
        elif y == 1:
            print("Your entered value is now ", bool(y))
        else:
            print("Your entered value is ", x)
    except ValueError:
        print("Your entered value is now ", x)
     
    o += 1
'''



print("""------------------------------------------------------------
Task 10
---------------------------------------------------------------------""")

x = int(input("First number: "))
y = int(input("Second number: "))

if x % y == 0:
    print("First number is divisible by second number, result =", x / y)
elif y % x == 0:
    print("Second number is divisible by first number, result =", y / x)
else:
    print("Numbers are non-divisible!")
















