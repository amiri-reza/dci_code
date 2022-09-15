import os
import time


user_input = int(input("Countdown number from: "))

for number in range(user_input, -1, -1):
    os.system("clear")
    print(number)
    time.sleep(1)
    
os.system("clear")
print("Finished!")
    
    
    
