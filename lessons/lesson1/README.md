# python_novice_lessons
My journey to python 3

# Lesson 1 - Variables and Arithmetic Operations 

## What is computer ? 

Is an electronic device that consist of 2 parts: 
1. CPU  - Central Processing Unit 
2. RAM  - Random Access Memory

## What is a program ?

A program is a set of instructions. Instructions cause a computer to perform some kind of action. 

Most of the programs can be looked as:

```

Input -> Computation -> Output

```

## What is programming ? 

A process of creating instructions aka programs. 


## What is a programming language ? 

A particular way to talk to a computer - a way to use instructions that both human and computer understand. 

## Why Python ? 

Python is an easy to learn language - best suited for beginning programmers. 


## Variables 

Imagine RAM as a large table 

[id,  value ]
[1,   empty ]
[2, "Daesun"]

```python

name = "Nari"

def delete_symbol(name): # Exact copy of "Nari" string
    # Delete last characther
    name.pop()

print(name)  # Nari 

delete_symbol(name) 

print(name) # Nar

```

A variable is a container for storing a value. 

### Types of variables 

Types; 
- String 
- Int (2), Float (2.5)
- list [1, 2, 3], tuple (Float, Int)
- bool (True, False)


## Arithmetic operations 

1. Addition -> +
2. Substraction  -> -
3. Multiplication -> *
4. Division -> /
5. Modulus -> %
6. Exponentiation -> **  