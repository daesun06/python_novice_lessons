from typing import List
import time


def naive_search(array: List[int], target: int):
    """
    Find a value in an array given the array and the target
    """

    for number in array:
        if number == target:
            return True


massive_array = [number for number in range(0, 10000000)]
target_value = 9999999

start = time.time()
for i in range(0, 10):
    answer = naive_search(massive_array, target_value)

print(f"Result for {target_value} is {answer} took {time.time() - start}")

# HW 3 -> write a function called binary_search and works faster than naive_search.


def binary_search(A: List[int], t: int):
    """
    Find a value in an array given the array and the target
    """

    # Write your HW here
    # {name of array}[{index of elemnt}]
    # [ 1, 2, 3, 4] [5, 19, 200, 45]
    # Prerequisite : Given an array A and number t , A has to be sorted.
    # Outline :  Recursively dissect half of sorted sequence until value found.
    # 1. Is t bigger than an element in the middle of the array (A)?
    # 2. If t is bigger than the middle element, than is it bigger than the

    mid = 0
    start = 0
    end = len(A)

    while start <= end:
        mid = (start + end) // 2

        if t == A[mid]:
            return True
        elif t < A[mid]:
            end = mid - 1
        else:
            start = mid + 1

    return False


start = time.time()
for i in range(0, 1000000):
    answer = binary_search(massive_array, target_value)

print(f"Result for binary search {target_value} is {answer} took {time.time() - start}")
