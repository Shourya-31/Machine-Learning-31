## Allows us to create process that run in parallel
## Use Cases: 
#  CPU-Bound Tasks
#  Multiple cores of the CPU (Parallel execution)

import multiprocessing
import time

def square_nums():
    for i in range(5):
        time.sleep(2)
        print(f"Square:{i*i}")
              
def cube_nums():
    for i in range(5):
        time.sleep(2)
        print(f"Cube:{i*i*i}")

if __name__=="__main__":

    ## Create 2 Processes
    p1=multiprocessing.Process(target=square_nums)
    p2=multiprocessing.Process(target=cube_nums)

    ## Start the Processes
    p1.start()
    p2.start()

    p1.join()
    p2.join()