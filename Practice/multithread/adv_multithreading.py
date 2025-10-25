### Multithreading with Thread Pool Executor

from concurrent.futures import ThreadPoolExecutor
import time

def print_nums(number):
    time.sleep(1)
    return f"Number: {number}"

numbers=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23]

with ThreadPoolExecutor(max_workers=3) as executor:
    results=executor.map(print_nums,numbers)

for result in results:
    print(result)

# python adv_multithreading.py