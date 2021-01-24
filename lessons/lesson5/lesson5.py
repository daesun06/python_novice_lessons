#class Human:
    #def sleep():
        #pass
    #def eat():
        #pass
    #def breathe():
        #pass
#class Nari(Human):
    #def annoy():
        #pass


#human = Human()
#nari = Nari()


## HW 4

###1

class Animals:
    sound = "roar"

    def breath(self):
        print('breathing')
    def walk(self):
        print('walking')
    def eat(self):
        print('eating')

class Mammals(Animals):
    def feed_kids_with_milk(self):
        print('feeding')

class Giraffes(Mammals):
    def left_Foot_Forward(self):
        print('left foot forward')
    def left_Foot_Back(self):
        print('left foot back')
    def right_Foot_Forward(self):
        print('right foot forward')
    def right_Foot_Back(self):
        print('right foot back')
    def dance(self):
        self.left_Foot_Forward()
        self.left_Foot_Back()
        self.right_Foot_Forward()
        self.right_Foot_Back()
        self.left_Foot_Back()
        self.right_Foot_Back()
        self.right_Foot_Forward()
        self.left_Foot_Forward()


reginald = Giraffes()
reginald.dance()

###2
import time 
import turtle 
nari = turtle.Pen()
deson = turtle.Pen()
fred = turtle.Pen()
frank = turtle.Pen()

nari.forward(100)
nari.left(90)
nari.forward(50)
nari.right(90)
nari.forward(50)

deson.forward(110)
deson.left(90)
deson.forward(25)
deson.right(90)
deson.forward(25)


fred.forward(100)
fred.right(90)
fred.forward(50)
fred.left(90)
fred.forward(50)

frank.forward(110)
frank.right(90)
frank.forward(25)
frank.left(90)
frank.forward(25)

time.sleep(60)





