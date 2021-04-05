"""This module is intended to make and move PNG images on a Tkinter canvas.
It is specialized for width 1400 and height 700 Tkinter canvas's .
This can be changed easily by changing the variables in the move function."""


from tkinter import PhotoImage,Canvas

class Object:
    def __init__(self,x,y, img, canvas):
        self.x = x
        self.y = y
        self.img = PhotoImage(file=img)
        self.canvas = canvas
        self.obj = self.canvas.create_image(self.x, self.y, image=self.img)

    def move(self,event):
        if event.char == "w":
            if self.y < 700 and self.y > 0:

                self.canvas.move(self.obj,0,-5)
                self.y -= 5
            else:
                self.canvas.move(self.obj,0,5)
                self.y += 5 

        if event.char == "a":
            if self.x < 1400 and self.x > 0:
                self.canvas.move(self.obj,-5,0)
                self.x -= 5
            else:
                self.canvas.move(self.obj,5,0)
                self.x += 5
        if event.char == "s":
            if self.y < 700 and self.y > 0:
                self.canvas.move(self.obj,0,5)
                self.y += 5
            else:
                self.canvas.move(self.obj,0,-5)
                self.y -= 5
        if event.char == "d":
            if self.x < 1400 and self.x > 0:
                self.canvas.move(self.obj,5,0)
                self.x += 5
            else:
                self.canvas.move(self.obj,-5,0)
                self.x -= 5
    
