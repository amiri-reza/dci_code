#write a program to defer the even or odd number of characters.

input = input("enter a word >>> ")

if len(input)%2 == 0:
    print(f"'{input}' --> 'even'")
else:
    print(f"'{input}' --> 'odd'")
