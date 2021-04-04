#! /home/kavi/miniconda3/python3.7

import objectpng
import bee
import random
import time
from tkinter import Tk,Canvas
import tkinter.messagebox



#Variables for the game
health = 50
seedscore = 0
starttime = time.time()
seedlist = []
seed1list = []
beelist = []
width = 1400
height = 700
timer = 50

#Create canvas
root = Tk()
root.title("Collect the seeds indev v0.1")
c = Canvas(root, width=width, height=height, bg = "green")
c.pack()

# Creating a new chick object
chickobj =  objectpng.Object(width/2, height/2, "chick3.png", c)

# Create score text
scoretxt = c.create_text(70,30, text=("Score:", seedscore), font=("Comic Sans", 20))
# Add time text to that
timetxt = c.create_text(1200,30, text = "Time left:"+str(timer - (round(time.time()-starttime))), font = ("Comic Sans", 20))
# Finally add health text
healthtxt = c.create_text(500,30, text=("Health:", health), font=("Comic Sans", 20))
#New seed creater

def new_seed():
    #Pick random to place seed on the canvas randomly.
    seedx = random.randint(0,width-20)
    seedy = random.randint(0,height-20)

    # Then,make the seed...
    newseed = c.create_oval(seedx,seedy,seedx+20,seedy+10, fill = "brown", width =0)
    
    # ...and append it to the seed tracker list.
    seedlist.append(newseed)


    root.after(400,new_seed)

def new_seed1():
    #Pick random to place seed on the canvas randomly.
    seed1x = random.randint(0,width-20)
    seed1y = random.randint(0,height-20)

    # Then,make the seed...
    newseed1 = c.create_oval(seed1x,seed1y,seed1x+20,seed1y+10, fill = "blue", width =0)
    
    # ...and append it to the seed tracker list.
    seed1list.append(newseed1)


    root.after(1000,new_seed1)
def new_bee():
    #Pick random to place bee on the canvas randomly.
    beex = random.randint(0,width-20)
    beey = random.randint(0,height-20)

    # Then,make the bee...
    beeobj = c.create_oval(beex,beey,beex+10,beey+10, fill = "yellow", width =0)
    beeobj = [bee.Bee(c,beeobj),beeobj]
    # ...and append it to the bee tracker list.
    beelist.append(beeobj)


    root.after(1000,new_bee)

def check_collision():
    
    global seedscore
    global health
    #For each seed..
    for seed in seedlist:

        #... get x & y...
        box = c.bbox(seed)

        #If seed isn't eaten...
        if box:

            #...check if it is overlapping anything...
            coord = c.find_overlapping(box[0], box[1], box[2], box[3])
            coord = list(coord)

            #and do a collision if it is.
            if 1 in coord:
            #Todo:Add health bar and make health random from -1 to 3
                c.itemconfig(seed, state = 'hidden')
                seedscore += random.randint(-1,3)
                health += random.randint(-5,1)

                
                
    #Same for the poison seeds.    
    for seed1 in seed1list:

        #Get x & y.
        box1 = c.bbox(seed1)

        #If seed isn't eaten...
        if box1:

            #...check if it is overlapping anything...
            coord1 = c.find_overlapping(box1[0], box1[1], box1[2], box1[3])
            coord1 = list(coord1)

            #and do a collision if it is.
            if 1 in coord1:
                c.itemconfig(seed1, state = 'hidden')
                health += random.randint(-1,3)
                seedscore += 1
                
    
    root.after(400, check_collision)
def update_all():
    global scoretxt
    global timetxt
    global healthtxt
    global timer
    c.itemconfigure(scoretxt, text="Score: " + str(seedscore))
    c.itemconfigure(timetxt, text = "Time left:"+str(timer - (round(time.time()-starttime))))
    c.itemconfigure(healthtxt, text = ("Health:", health))
    if timer - (round(time.time()-starttime)) < 0 or health < 0:
        root.withdraw()
        tkinter.messagebox.showinfo("You lost!", "You collected  {0} seeds!".format(str(seedscore)))
        root.destroy()
    root.after(100, update_all)
    
def bee_update():
    global seedscore
    global health
    for bee in beelist:
        bee[0].move()
        
        box2 = c.bbox(bee[1])

        #If bee isn't killed...
        if box2:

            #...check if it is overlapping anything...
            coord2 = c.find_overlapping(box2[0], box2[1], box2[2], box2[3])
            coord2 = list(coord2)

            #and do a collision if it is.
            if 1 in coord2 :
                if random.randint(1,3) == 1:
                    health -= random.randint(1,10)
                else:
                    c.itemconfig(bee[1], state = 'hidden')
                    seedscore += random.randint(3,6)
                    c.delete(bee[1])
                    beelist.remove(bee)
                    del bee[0]
        

    root.after(41,bee_update)


root.bind("<Key>",chickobj.move)
root.after(400, new_seed)
root.after(400, check_collision)
root.after(7500,new_seed1)
root.after(1000,new_bee)
root.after(41,bee_update)
root.after(100,update_all)
root.mainloop()
    
