import random                           
from tkinter import PhotoImage
class Bee:
    def __init__(self,canvas,obj):
        self.canvas = canvas
        self.obj = obj
    def move(self):
        num = random.randint(1,9)
        if num == 1:
            self.canvas.move(self.obj,0,15)
        if num == 2:
            self.canvas.move(self.obj,15,0)
        if num == 3:
            self.canvas.move(self.obj,15,15)
        if num == 4:
            self.canvas.move(self.obj,0,-15)
        if num == 5:
            self.canvas.move(self.obj,-15,0)
        if num == 6:
            self.canvas.move(self.obj,-15,-15)
        if num == 7:
            self.canvas.move(self.obj,-15,15)
        if num == 8:
            self.canvas.move(self.obj,15,-15)
