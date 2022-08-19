'''convert=float(25.4)
while True:
    print("*******MM*******")
    user_input = input()
    if user_input.lower() == "end":
        break
    else:
        MM = float(user_input)
        Results=float(MM/convert)
        print("*****Inches*****")
        print("%.3f" % Results)
        print("%.4f" % Results)
        print("%.5f" % Results)

num = int(input("Enter a number: "))
flag = False

# prime numbers are greater than 1
if num > 1:
    # check for factors
    for i in range(2, num):
        if (num % i) == 0:
            # if factor is found, set flag to True
            flag = True
            # break out of loop
            break

# check if flag is True
if flag:
    print(num, "is not a prime number")
else:
    print(num, "is a prime number")

'''
g1 = "What is the biggest continent in the world?"
g1o = "A: Africa  B: Europe  C: Asia   D: North America to quit, press Q"

print(g1.center(100), g1o.center(100), sep="\n")
