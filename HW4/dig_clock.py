# Anurag Mukkara
# 13 June 2014
# dig_clock.py

from graphics import * 

class DigitalClock():
    meridians = ["AM", "PM"]
    def __init__(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second
        self.pos = Point(0,0)
        self.display = Text(Point(60,30), str(self.hour%12)+":"+str(self.minute)+":"+str(self.second)+" "\
               + self.meridians[self.hour/12])

    def draw_face(self, win):
        box = Rectangle(Point(10,10), Point(110, 50))
        box.setFill("green")
        box.setOutline("black")
        box.setWidth(5)
        box.draw(win)

    def draw_text(self, win):
        self.display.draw(win)

    def draw(self, win):
        self.draw_face(win)
        self.draw_text(win)
        win.after(1000, self.tick, win)

    def update_time(self):
        time_in_seconds = 3600*self.hour + 60*self.minute + self.second
        new_time_in_seconds = (time_in_seconds + 1) % (3600*24)
        self.hour = new_time_in_seconds / 3600
        self.minute = ((new_time_in_seconds)%3600)/60
        self.second = ((new_time_in_seconds)%3600)%60
        self.display.setText("%02d" % (self.hour%12) + ":" + "%02d" % self.minute + ":"+ "%02d" % self.second + " "\
               + self.meridians[self.hour/12])
        
    def tick(self, win):
         self.update_time()
         win.after(1000, self.tick, win)
    
new_win = GraphWin("Digital Clock", 120,60)

clock = DigitalClock(23, 59, 40)
clock.draw(new_win)

new_win.mainloop() 
