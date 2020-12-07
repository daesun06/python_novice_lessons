from typing import List
import time 

def naive_search(array: List[int], target: int):
    '''
        Find a value in an array given the array and the target
    '''

    for number in array:
        if number == target:
            return True

massive_array = [number for number in range(0, 10000000)]
target_value = 9999999

start = time.time()
answer = naive_search(massive_array, target_value)

print(f'Result for {target_value} is {answer} took {time.time() - start}')

# HW 3 -> write a function called binary_search and works faster than naive_search.

def binary_search(array: List[int], target: int):
    '''
        Find a value in an array given the array and the target
    '''

    # Write your HW here 
    