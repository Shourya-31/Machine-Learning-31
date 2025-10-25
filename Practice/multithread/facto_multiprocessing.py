'''
Real-World Example: Multiprocessing for CPU-bound Tasks
Scenario: Factorial Calculation
Factorial calculations, especially for large numbers, 
involve significant computational work. Multiprocessing 
can be used to distribute the workload across multiple 
CPU cores, improving performance.

'''

import multiprocessing
import math
import sys
import time

## Maximum number of digits allowed for integer conversion
sys.set_int_max_str_digits(100000)

## function to compute factorial

def print_fact(num):
    print(f"Computing Factorial of {num}")
    result=math.factorial(num)
    print(f"Factorial of {num} is equal to: {result}")
    return result


if __name__=="__main__":
    nums=[300,4000,7000]

    start_time=time.time()

    # Create Pool of Worker Processes
    with multiprocessing.Pool() as pool:
        results=pool.map(print_fact,nums)

    end_time=time.time()

    print(f"Factorial Results: {results}")
    print(f"Time Taken: {end_time-start_time} seconds")