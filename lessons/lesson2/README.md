# Lesson2 

## Lesson 1 recap

1. What are the 2 main parts of a computer ? 

CPU - Central Processing Unit and RAM - Random Access Memory

1 byte - 8 bit 

1 mbyte - 1 000 000 byte 

1gbyte - 1000 mb

To read 1 byte from RAM : 100ns 
Sending 1 packet of data from Ca -> Netherlands -> Ca 150ms 


2. What is a program ? 

A programm is a set of instructions with a code that helps you to perform some kind of action.

3. What is programming ? 

Programming is a way of talking with a computer during which both you and computer understand what you are talking about.

4. What is a programming language ? 

A programming language is a code (language) that you and the computer can understand.

5. Why python  ? 

Python is the easiest language for begginer programmers.

6. Sample variable types ?

1. Strings 

2. Int -> 2 

3. Float -> 2.1

4. Bool  -> 0 - False, 1 - True 

7. Signs of all arithmetic operation ?

+ = addition
- = subtraction
* = multiplication
/ = division

## Basic programming constructs and BS


### Programming construct 

Simplest building block of a programming language

### Conditions - Decision making statement, IF 

```python

basket = Basket()

if basket.size() > 10:
    print("Ooooo big basket!") 
elif basket.size() > 5:
    print("Meh medium basket :-( ! ")
else:
    print("small basket")

```

sample syntax 'if {statement}:' , statement has to return boolean. 
if more than 2 statements are needed, use elif. 

```python

def nameCheck(name: str):
    num_char = len(name)

    if len < 4 :
        print("That's a small name!"):
    else :
        print("that's a big name")          

```

HW : 
54-65 page in python for kinds.

### Cycles 

HW: 
68 - 79 - read and document in this file if needed.

## Binary search and Complexity 