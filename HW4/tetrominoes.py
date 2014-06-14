# -*- coding: utf-8 -*-
# Anurag Mukkara
# 13 June 2014
# terominoes.py

from graphics import *

class Block(Rectangle):
    def __init__(self, corner, color):
        upper_left_corner = Point(corner.getX()*30,corner.getY()*30)
        lower_right_corner = Point(corner.getX()*30 + 30,corner.getY()*30 + 30)
        Rectangle.__init__(self, upper_left_corner, lower_right_corner)
        Rectangle.setFill(self,color)
        
class Shape():
    def __init__(self, coords, color):
        self.blocks = [Block(coord, color) for coord in coords]

    def draw(self, win):
        for block in self.blocks:
            block.draw(win)

class I_shape(Shape): 
    def __init__(self, center):
        coords = [Point(center.x - 2, center.y), 
        Point(center.x - 1, center.y), 
        Point(center.x , center.y), 
        Point(center.x + 1, center.y)] 
        Shape.__init__(self, coords, "blue") 

class J_shape(Shape): 
    def __init__(self, center):
        coords = [Point(center.x - 1, center.y), 
        Point(center.x , center.y), 
        Point(center.x + 1 , center.y), 
        Point(center.x + 1, center.y + 1)] 
        Shape.__init__(self, coords, "orange") 

class L_shape(Shape): 
    def __init__(self, center):
        coords = [Point(center.x - 1, center.y + 1), 
        Point(center.x - 1, center.y), 
        Point(center.x , center.y), 
        Point(center.x + 1, center.y)] 
        Shape.__init__(self, coords, "aquamarine") 

class O_shape(Shape): 
    def __init__(self, center):
        coords = [Point(center.x - 1, center.y), 
        Point(center.x , center.y), 
        Point(center.x - 1, center.y + 1), 
        Point(center.x , center.y + 1)] 
        Shape.__init__(self, coords, "red") 

class S_shape(Shape): 
    def __init__(self, center):
        coords = [Point(center.x - 1, center.y + 1), 
        Point(center.x , center.y + 1), 
        Point(center.x , center.y), 
        Point(center.x + 1, center.y)] 
        Shape.__init__(self, coords, "green") 

class T_shape(Shape): 
    def __init__(self, center):
        coords = [Point(center.x - 1, center.y), 
        Point(center.x + 1, center.y), 
        Point(center.x , center.y), 
        Point(center.x , center.y + 1)] 
        Shape.__init__(self, coords, "yellow") 

class Z_shape(Shape): 
    def __init__(self, center):
        coords = [Point(center.x - 1, center.y), 
        Point(center.x , center.y), 
        Point(center.x , center.y + 1), 
        Point(center.x + 1, center.y + 1)] 
        Shape.__init__(self, coords, "deep pink") 


win = GraphWin("Tetrominoes", 900, 150)

# a list of shape classes
tetrominoes = [I_shape, J_shape, L_shape, O_shape, S_shape, T_shape, Z_shape]

x = 3
for tetromino in tetrominoes:
    shape = tetromino(Point(x, 1))
    shape.draw(win)
    x += 4

win.mainloop() 

        
