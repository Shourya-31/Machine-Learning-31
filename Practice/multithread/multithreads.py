## Multithreading:
## IO Bound tasks
## Concurrent execution to improve throughput of program

import threading
import time

def print_nums():
    for i in range(5):
        time.sleep(1)
        print(f"Number:{i}")

def print_letter():
    for letter in "abcde":
        time.sleep(2)
        print(f"Letter: {letter}")


## Create 2 threads
t1=threading.Thread(target=print_nums)
t2=threading.Thread(target=print_letter)

t=time.time()
# print_letter()
# print_nums()
# Start the thread
t1.start()
t2.start()

## Wait for the threads to complete
t1.join()
t2.join()
finished_time=time.time()-t
print(finished_time)