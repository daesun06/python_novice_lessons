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

1. What is an if statement in python ? Can u wrtie an example that determines a print statement based on age ? 

If is a programming construct that allows to program decisions. 

```python
age=35
if age > 50: 
    print('You are to old.')
else:
    print('Hello kid')
```

# HW addition, read the 54-65, and write at least 1 sentence per section. 


### Cycles 

HW: 
68 - 79 - read and document in this file if needed.

A turtle in python is sort of like a turtle in real life.  A turtle is a way to import a module.  You can set a track to the turtle to move. 
And because of this you can draw shapes like a: square, triangle and other basic shapes.

     t.foward(50)

With this command the turtle should move foward.

1. What is a cycle ? 

Cycle is a programming construct that allows to loop through instructions. Write an example ?

range -> range(0, 2) -> [0, 1, 2)

```python
for digit in range(0, 5):
    print('Hello world')
```

# HW addition, read the 68-79, and write at least 1 sentence per section. 
