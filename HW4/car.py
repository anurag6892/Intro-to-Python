# -*- coding: utf-8 -*-
# Anurag Mukkara
# 13 June 2014
# car.py

from graphics import *
from wheel import *

class Car(Wheel):
        def __init__(self, center1, radius1, center2, radius2, width):
            self.wheel1 = Wheel(center1, 0.6*radius1, radius1)
            self.wheel2 = Wheel(center2, 0.6*radius2, radius2)
            self.body = Rectangle(Point(center1.getX(),center1.getY()-width),\
                                  center2)
            
        def draw(self, win):
            self.body.draw(win)
            self.wheel1.draw(win)
            self.wheel2.draw(win)

        def move(self, dx, dy):
            self.body.move(dx,dy)
            self.wheel1.move(dx,dy)
            self.wheel2.move(dx,dy)
            
        def set_color(self, tire_color, wheel_color, body_color):
            self.body.setFill(body_color)
            self.wheel1.set_color(wheel_color, tire_color)
            self.wheel2.set_color(wheel_color, tire_color)

        def undraw(self):
            self.body.undraw()
            self.wheel1.undraw()
            self.wheel2.undraw()
            
        def animate(self, win, dx, dy, n):
            if n > 0 :
                self.move(dx,dy)
                win.after(100, self.animate, win, dx, dy, n-1)
        
new_win = GraphWin('A Car', 700, 300) 
# create a car object

# 1st wheel centered at 50,50 with radius 15

# 2nd wheel centered at 100,50 with radius 15

# rectangle with a height of 40

car1 = Car(Point(50, 50), 15, Point(100,50), 15, 40)

car1.draw( new_win )

# color the wheels grey with black tires, and the body pink

car1.set_color('black', 'grey', 'pink' )

# make the car move on the screen

car1.animate(new_win, 1, 0, 400)

new_win.mainloop() 
