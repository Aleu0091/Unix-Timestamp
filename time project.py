import time as t
from time import sleep 
while True:
    tt=t.time()
    stamp = tt-2
    time_stamp=format(stamp, ".0f")
    print(time_stamp)
    sleep(1)