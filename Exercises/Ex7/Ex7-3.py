secret = input("Please tell me the secret: ")

name = input("Tell me your love name: ")

birthdate = input("What is your love's year of birth? ")

# will take the length of secret and subtracts 1
name_and_secret = secret+name

print("The cipher text is : " + name_and_secret[::-1] + birthdate)