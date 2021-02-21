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
save_file = open('favorites.dat', 'wb')
load_file = open('favorites.dat', 'rb')
loaded_my_fav_things = pickle.load(load_file)
load_file.close()

print(loaded_my_fav_things)

#11

##N1

import turtle
t = turtle.Pen()
t.forward(50)
t.right(45)
t.forward(35)
t.right(45)
t.forward(50)
t.right(45)
t.forward(35)
t.right(45)
t.forward(50)
t.right(45)
t.forward(35)
t.right(45)
t.forward(50)
t.right(45)
t.forward(35)
t.right(45)

##N2

###I don't understan what programm you need to make, to color the figure.

##N3

def draw_star(size, points):
    