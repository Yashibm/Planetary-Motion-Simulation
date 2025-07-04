# -*- coding: utf-8 -*-

"""
Planetary Motion Simulation
"""
from  tkinter import*
root=Tk()
import pygame as pg
import math

#INITIALISING PYGAME
pg.init()

img1=pg.image.load("sunny3.png")
img2=pg.image.load("earth33.png")
img1=pg.transform.scale(img1,(80,80))           #scaling down the image size
img2=pg.transform.scale(img2,(50,50))
#COLOUR PALLET
white=(255,255,255) 
black=(0,0,0)
red=(255,0,0)
blue=(0,100,200)                                 
yellow=(255,150,0)                               

#SETTING UP DISPLAY
Display = pg.display.set_mode((1300,700))        #setting background dimension
pg.display.set_caption("PLANETARY MOTION")       #naming the simulation

sw=1300                                          #screen width
sl=800                                           #screen length

Exit = False                                     #constant variable 

x=300                                            #earth's initial x-position
y=349                                            #earth's initial y-position

r=100                                            #jupiter's initial x-position
s=350                                            #jupiter's initial y-position

u=380                                            #mercury's initial x-position
v=360                                            #mercury's initial y-position

m= 350                                           #venus's initial x-position     
n= 360                                          #venus's initial y-position
 
clock=pg.time.Clock()                           

def planets():
    root.destroy()
    global x,y,r,s,u,v,m,n,Exit
    
    #Simulation Begins
    while not Exit : 
        for event in pg.event.get():
            print(event)
    
            if event.type == pg.QUIT :      
                Exit =True
        
        #Earth's motion
        if x<=1099 and y>=349:    
             x +=1.5
             y = math.floor(math.sqrt((200**2)*(1-((x-700)**2)/(400**2)))+350)
    
        else:
             x -=1.5
             y = -math.floor(math.sqrt((200**2)*(1-((x-700)**2)/(400**2)))-350)
       
        #Jupiter's motion
        if r<=1199 and s>=349:    
             r +=1
             s = math.floor(math.sqrt((250**2)*(1-((r-650)**2)/(550**2)))+360)
             
        else:
             r -=1
             s = -math.floor(math.sqrt((250**2)*(1-((r-650)**2)/(550**2)))-360)
        
        #Mercury's motion
        if u<=779 and v>=349:    
             u +=2
             v = math.floor(math.sqrt((125**2)*(1-((u-580)**2)/(200**2)))+350)
           
        else:
             u -=2
             v = -math.floor(math.sqrt((125**2)*(1-((u-580)**2)/(200**2)))-350)
        '''
       #Venus's motion                                                              #changes to be made soon
        if m<=879 and n>=349:    
             m +=1.75
             n = math.floor(math.sqrt((150**2)*(1-((m-625)**2)/(225**2)))+360)
           
        else:
             m -=1.75
             n = -math.floor(math.sqrt((150**2)*(1-((m-625)**2)/(225**2)))-360)
    
        '''
    
        Display.fill(black)                                 #setting the background

        pg.draw.ellipse(Display,white,[380,227,400,250],1)  #mercury's orbit
        pg.draw.ellipse(Display,white,[350,210,550,300],1)  #Venus's orbit
        pg.draw.ellipse(Display,white,[318,175,800,400],1)  #earth's orbit
        pg.draw.ellipse(Display,white,[100,110,1100,500],1) #jupiter's orbit
        Display.blit(img1,[450,310])                        #Attaching the image of sun      
        Display.blit(img2,[x,y])                            #Attaching the image of earth 
        pg.draw.circle(Display,red,[r,s],25)                #jupiter
        pg.draw.circle(Display,yellow,[u,v],13)             #mercury
        pg.draw.circle(Display,red,[m,n],18)                #venus
        
        pg.display.update()                                 #To update the screen as changes are made
       
        clock.tick(100)                                     #Deciding the fps                        
    
    pg.quit()                                               #To come out of the simulation

button=Button(root,text="Click to enjoy the Planetary Motion Simulation",fg="red",bg="pink",width=100,command=planets)
button.grid(row=0,columnspan=2)

root.mainloop()
