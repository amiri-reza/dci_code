secret = input("Please tell me the secret: ")
translated0 = '' #cipher text is stored in this variable

l_name = input("Tell me your love name: ")
translated1 = '' #cipher text is stored in this variable

l_bdate = input("What is your love's year of birth? ")
translated2 = '' #cipher text is stored in this variable

i0 = len(secret) - 1
while i0 >= 0:
   translated0 = translated0 + secret[i0]
   i0 = i0 - 1

i1 = len(l_name) - 1
while i1 >= 0:
  translated1 = translated1 + l_name[i1]
  i1 = i1 - 1

i2 = len(l_bdate) - 1
while i2 >= 0:
  translated2 = translated2 + l_bdate[i2]
  i2 = i2 - 1
print("The cipher text is : " + translated1 + translated0 + l_bdate)

