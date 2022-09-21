import time
import os


starting_point = input("press Enter to start")
start = time.time()
print(time.ctime())


                                            # making python wait for the user input (not working yet)
# Flag = True
# while Flag:
#     try:
#         print(time.ctime())
#         print("Press Enter to end")
#         User_inp = input()
        
#         if User_inp == "":
#             pass
#         else:
#             end = time.time()
#             Flag = False
            
#     except:
#         print('except part') 







ending_time = input("press Enter to end")
end = time.time()
print(time.ctime())

result = end-start


print(time.strftime("%H Hours %M Minutes %S Seconds", time.gmtime(result)))
