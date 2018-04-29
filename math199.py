import random # needed
import turtle
import math
from operator import add


import pip


def makegraph(n,p):
    
    graph = [] # initalizes an emptly graph
    
#creates n unconnected vertexes
    for i in range(0,(n)):
        graph.append([])

#connect each vertex with probability p following uniform distrobution:
    for i in range(0,(n-1)): #for every vertex except the last one
        for j in range(i+1,(n)): # test relationship with every remaining combination of vertx not including the starting vertex
            if random.random() < p:
                graph[i].append(j)
            
    return graph








#expected exactly a degree 2 list, so quite prone to crashing if you feed it anything else
# also, max graph size is about 250 ish, as I dont extend the canvas far beyond what the screen shows

# seT quick = True to immediately display the finished graph

def displaygraph(graph,quick = False):
    wn = turtle.Screen()
    wn.reset()
     # sets 256 based color for our random color maker
    if quick ==True:
        turtle.tracer(0, 0)
    subscale = 5
    dotsize = (7) # radius of the dots representing each graph node
    width = math.ceil(math.sqrt(len(graph)))
    scale = 25  # scales the graph by this many pixels
    turtle.setworldcoordinates(-scale, scale*width, scale*width, -scale)  #creates a canvas of the proper dimensions, with a little bit of offset 
# note (0,0) is upper left, and (down,right) is positive
    t = turtle.Turtle()
    t.hideturtle()  # so we dont see the cursor

    #make an approximately square graph and fill the graph with dots 
    t.penup()
    t.dot(dotsize)

    for i in range(0,len(graph)):

        list1 = [scale*y for y in divmod(i,width)] # makes an even square of nodes by abusing properties of the modulus
        list2 = [0.5*scale *((i%width)%2),0.5*scale *((i//width)%2)] # ofsets each node a little bit so we can see the connections  easier
        t.goto(list(map(add, list1, list2)))  # adds the offset
        t.dot(dotsize)                                       

    # fill in the relationship between each graph

    wn.colormode(255)  # so we can use rbg246 color mode for the paths

    for i in range (0,len(graph)):
        list1 = [scale*y for y in divmod(i,width)]
        list2 = [0.5*scale *((i%width)%2),0.5*scale *((i//width)%2)] # same thing
        for j in graph[i]: # draws the connection from the i-th point to every element in graph[i]
            list3 = [scale*z for z in divmod(j,width)]
            list4 = [0.5*scale *((j%width)%2),0.5*scale *((j//width)%2)] 
            t.penup()
            t.goto(list(map(add, list1, list2))) # go back to our starting node
            t.pendown()
            t.goto(list(map(add, list3, list4))) # draw tthe relationship
        t.pencolor(random.randint(10,254),random.randint(10,254),random.randint(10,254))  # changes color for each node
    if quick == True: #actually renders the window if we decided not to draw it till the end to save time
        turtle.update()        
    return  





#run this after you draw a graph to get a png of the turtle window for documentation purposes
# you must run AFTER you create the window
# modified  from https://stackoverflow.com/questions/25050156/save-turtle-output-as-jpeg

#need to install the following files:
    #canvasvg
    #



def saveimage():

    import os
    import shutil
    import tempfile
    import canvasvg
    from tkinter import filedialog

    ts = turtle.getscreen().getcanvas()
    filename = filedialog.asksaveasfilename()+ ".svg"
    canvasvg.saveall(filename, ts)

    return
        

# main file starts here


