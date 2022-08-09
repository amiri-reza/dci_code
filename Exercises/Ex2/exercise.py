# do exercise here
# upload to github for portfolio
# thank me later when your git graph is as green as the python money u gonna earn


from math import ceil, floor


print("""
--------------------------------------------------------------------
Task 1
--------------------------------------------------------------------""")

num1 = 26
num2 = 32.856654
num3 = 56
num4 = 1024
num5 = 2
num6 = 6
value7 = True
value8 = False
Complex_value = complex(2,-3)

print(num1, "+", num2, "=", round(num1+num2, 3))
print(num1, "-", num6, "=", num1-num6)
print(num1, "*", num5, "=", num1*num5)
print(num3, "/", num1, "=", round(num3/num1, 3))
print(num1, "%", num6, "=", num1%num6) #it gives the remainder of divide operation between right num and left num.
print(num5, "**", num6, "=", num5**num6)
print(num1, "//", num2, "=", num1//num2)
print(value7, "*", value8, "=", value7*value8)
print(num5, "*", Complex_value, "=", num5*Complex_value)


print("""
--------------------------------------------------------------------
Task 2
--------------------------------------------------------------------""")

num1 = 26
num2 = 32.85
num3 = -56
num4 = 1024
num5 = 2
num6 = 6
value7 = True
value8 = False
Complex_value = complex(2,-3)

print("max(", num1, ", ", num5, ", ", num2, ") = ", max(num1, num5, num2), sep="")
print("min(", num1, ", ", num5, ", ", num2, ") = ", min(num1, num5, num2), sep="")
print("abs(", num3, ") = ", abs(num3), sep="")
print("pow(", num5, ", ", num6, ") = ", pow(num5, num6), sep="")
print("ceil(", num2, " / ", num6, ") = ", ceil(num2/num6), sep="")
print("floor(", num2, " / ", num6, ") = ", floor(num2/num6), sep="")
print("max(", value7, ", ", value8, ") = ", max(value7, value8), sep="")
print("abs", Complex_value, " = ", round(abs(Complex_value), 3), sep="")







