input_text = input("Type a word or sentence: " )

print("Let's check if the length of above sentence is even or odd")


import time
time.sleep(5)



length = len(input_text)%2

if length == 0:
    print(input_text, "--> even")
else:
    print(input_text, "--> odd")
