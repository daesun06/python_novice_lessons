#10

##N1

###1.
  #I think it will return 4.

###2.
  #I think it will return 4 too.


import copy
class Car:
    pass

car1 = Car()
car1.wheels = 4
car2 = Car()
car2.wheels = 3
print(car1.wheels)

car3 = copy.copy(car1)
car3.wheels = 6
print(car1.wheels)

##N2

import pickle
my_fav_things = ('guitar', 'steak', 'programming', 'lessons')
f = open('favorites.dat', 'wb')
pickle.dump(my_fav_things, f)
f.close()

load_file = open('favorites.dat', 'rb')
loaded_my_fav_things = pickle.load(load_file)
load_file.close()

print(loaded_my_fav_things)

#11

##N1

import turtle
t = turtle.Pen()

def octagon(size: int):
  for _ in range(1, 9):
    t.forward(size)
    t.right(45)

# octagon(100)

##N2

###I don't understan what programm you need to make, to color the figure.


import turtle
t = turtle.Pen()

def octagon_with_color(size: int, filled: bool):
  if filled == True:
    t.begin_fill()

  for _ in range(1, 9):
    t.forward(size)
    t.right(45)
  
  if filled == True:
    t.end_fill()

# t.color(1, 0.85, 0)
# octagon_with_color(100, True)
# t.color(0, 0, 0)
# octagon_with_color(100, False)

print("Help")

##N3

t = turtle.Pen()

def draw_star(size, points, filled):
    if filled == True:
      t.begin_fill()
    angle = 360 / points
    for _ in range(0, points):
      t.forward(size)
      t.left(180 - angle)
      t.forward(size)
      t.right(180 - (angle * 2))
    if filled == True:
      t.end_fill()

t.color(0, 0, 0)
draw_star(80, 70, True)

print("Help")