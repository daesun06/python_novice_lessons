# Lesson 3 

## Plan - write a BS algorithm in python.

Imagine an array of numbers from 0 to 10. ANd you want to 
quickly find the number i guessed (for example 6). The 
idea is to recursively do the following: 
Step 1. Find the middle element . N is size of the array, the middle is at floor(N/2) (floor(2.6) == 2, ceiling(2.6) == 3).
Step 2. Compare array[N/2] > target or array[N/2] < target. Based on that we go left or right, generate a new range and run Step 1 until we find target. 

 