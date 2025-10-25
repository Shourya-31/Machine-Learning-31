### Multi-Processing with ProcessPoolExecutor

from concurrent.futures import ProcessPoolExecutor
import time

def square_nums(i):
        time.sleep(2)
        print(f"Square:{i*i}")

num=[1,2,3,4,5,6,7,8,9,10]
if __name__=="__main__":

    with ProcessPoolExecutor(max_workers=3) as executor:
        results=executor.map(square_nums,num)

    for result in results:
        print(results)

# python adv_multiprocessing.py