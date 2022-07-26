import time
import os


starting_time = time.time()
filled_sign = " "

progress_bar = 100*"-"


n = 0
while n < 101:
    os.system("clear")
    
    decreasing_bar = progress_bar[0:-int(n)]
    filled_sign += "#"
    if n == 0:
        print(f"#{progress_bar}- progress is {n} %.")
    else:
        print(f"{filled_sign}{decreasing_bar} progress is {n} %.")
    time.sleep(0.05)
    n += 1

print("Download is finished!")
finishing_time = time.time()
print("Download Duration:", round(finishing_time-starting_time, 2), "Seconds")