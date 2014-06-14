# Anurag Mukkara
# 13 June 2014
# analog_clock.py

from graphics import * 
from math import *

class AnalogClock():
    def __init__(self, hour, minute, second, center, radius):
        self.hour = hour
        self.minute = minute
        self.second = second
        self.center = center
        self.radius = radius
        self.hour_hand = Line(self.center, Point(self.center.getX() + 0.6*self.radius*sin(2*pi*(self.hour/12.0 + \
                 1/12.0*self.minute/60.0 )), self.center.getY() - 0.6*self.radius*cos(2*pi*(self.hour/12.0 + 1/12.0*self.minute/60.0)) ) )
        self.minute_hand = Line(self.center, Point(self.center.getX() + 0.8*self.radius*sin(2*pi*(self.minute/60.0 + \
                 1/60.0*self.second/60 )),self.center.getY() - 0.8*self.radius*cos(2*pi*(self.minute/60.0 + 1/60.0*self.second/60)) ) )
        self.second_hand = Line(self.center, Point(self.center.getX() + 0.8*self.radius*sin(2*pi*(self.second/60.0)),\
                                           self.center.getY() - 0.8*self.radius*cos(2*pi*(self.second/60.0)) ) )
        self.hour_hand.setWidth(3)
        self.minute_hand.setWidth(3)
        self.second_hand.setWidth(1)

    def draw_circle(self, win):
        circle = Circle(self.center, self.radius)
        circle.setFill("pink")
        circle.setOutline("black")
        circle.setWidth(3)
        circle.draw(win)

    def draw_hands(self, win):
        self.hour_hand.draw(win)
        self.minute_hand.draw(win)
        self.second_hand.draw(win)

    def undraw_hands(self, win):
        self.hour_hand.undraw()
        self.minute_hand.undraw()
        self.second_hand.undraw()

    def draw(self, win):
        self.draw_circle(win)
        self.draw_hands(win)
        win.after(1000, self.tick, win)

    def update_time(self,win):
        time_in_seconds = 3600*self.hour + 60*self.minute + self.second
        new_time_in_seconds = (time_in_seconds + 1) % (3600*24)
        self.hour = new_time_in_seconds / 3600
        self.minute = ((new_time_in_seconds)%3600)/60
        self.second = ((new_time_in_seconds)%3600)%60
        self.undraw_hands(win)
        self.hour_hand = Line(self.center, Point(self.center.getX() + 0.6*self.radius*sin(2*pi*(self.hour/12.0 + \
                 1/12.0*self.minute/60.0 )), self.center.getY() - 0.6*self.radius*cos(2*pi*(self.hour/12.0 + 1/12.0*self.minute/60.0)) ) )
        self.minute_hand = Line(self.center, Point(self.center.getX() + 0.8*self.radius*sin(2*pi*(self.minute/60.0 + \
                 1/60.0*self.second/60 )),self.center.getY() - 0.8*self.radius*cos(2*pi*(self.minute/60.0 + 1/60.0*self.second/60)) ) )
        self.second_hand = Line(self.center, Point(self.center.getX() + 0.8*self.radius*sin(2*pi*(self.second/60.0)),\
                                           self.center.getY() - 0.8*self.radius*cos(2*pi*(self.second/60.0)) ) )
        self.hour_hand.setWidth(3)
        self.minute_hand.setWidth(3)
        self.second_hand.setWidth(1)
        self.draw_hands(win)
        
    def tick(self, win):
         self.update_time(win)
         win.after(1000, self.tick, win)
    
new_win = GraphWin("Analog Clock", 300,300)

clock = AnalogClock(15, 50, 40, Point(150,150), 130)
clock.draw(new_win)

new_win.mainloop() 
