
def moon_weigth(weight: int, increase):
    # Write your solution here

    for year in range(1, 16):
        weight = weight + increase
        moon_weigth = weight * 0.165
        print(moon_weigth, year)

#moon_weigth(50, 25)


def moon_weigth_2(weight: int, increase, year_period: int):
    # Write your solution here

    for year in range(1, year_period + 1):
        weight = weight + increase 
        moon_weigth = weight * 0.165
        print(moon_weigth, year)

# moon_weigth_2(50, 25, 7)

import sys

def name_printer():
    print("Whats your name?")
    name = sys.stdin.readline()
    print(f'{name} - hello!')


def moon_weigth_3():
    # Write your solution here
    print("Please enter your current Earth weight")
    weight = int(sys.stdin.readline())

    print("Please enter the amount your weight might increase each year")
    increase = float(sys.stdin.readline())

    print("Please enter the number of years")
    year_period = int(sys.stdin.readline())

    for year in range(1, year_period + 1):
        weight = weight + increase 
        moon_weigth = weight * 0.165
        print(moon_weigth, year)

moon_weigth_3()
# What is a function argument | parameter ?
# f(x) = x + 5 = 10
# Define python function syntax template:
# def {name of function}({args1: arg1_type, args2:arg2_type ...}):