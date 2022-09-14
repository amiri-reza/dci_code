import time


starting_point = input("press Enter to start")
start = time.time()
print(time.ctime())


ending_time = input("press Enter to end")
end = time.time()
print(time.ctime())

result = end-start


print(time.strftime("%H Hours %M Minutes %S Seconds", time.gmtime(result)))