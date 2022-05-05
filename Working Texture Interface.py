
import tkinter 
from tkinter import *
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.backend_bases import key_press_handler
from matplotlib import pyplot as plt, animation
import numpy as np
from itertools import product
import random as rand

class Main_win():
    def __init__(self,master,Itterations, Dom_size, Rule):
        master.config(width=650 , height=500)
        self.master = master
        master.title("Automata Application")
        self.animrun = True
        
        self.frame = 0
        self.itterations = Itterations
        self.dom_size = Dom_size
        self.rulenum = Rule#141674
        self.sscale = 4.5/self.dom_size
        self.rule = self.GetRule(self.rulenum)
        self.col_list = (("black","grey","white"),("linen","silver","grey"),("black","green","white"))
        self.DListSet()
        
        plt.rcParams["figure.figsize"] = [7.00, 3.50]
        plt.rcParams["figure.autolayout"] = True
        #self.fig = plt.Figure(dpi=100, facecolor="linen")
        #self.ax = self.fig.add_subplot(xlim=(0, self.dom_size), ylim=(0,self.dom_size))
        self.fig, self.ax = plt.subplots(figsize = (((self.dom_size-1)*self.sscale),((self.dom_size-1)*self.sscale)))
        self.fig.set_facecolor("white")
        self.ax.axis("off")
        self.canvas = FigureCanvasTkAgg(self.fig, master)
        self.canvas.draw()
        self.canvas.get_tk_widget().place(x = 200, y=0 ,height=500, width=500)
        
        self.Alive, = plt.plot([], [], 's',ms = self.sscale*65, color = "black")
        self.Alead, = plt.plot([], [], 's',ms = self.sscale*65, color = "grey")
        self.Dead, = plt.plot([], [], 's',ms = self.sscale*65, color = "white")
        
        self.RuleNumLabel = tkinter.Label(master ,text = "Rule Number :")
        self.RuleNumLabel.place(y =0,height = 20,width = 200)
        self.RuleNumEntry = tkinter.Entry(master , justify = "center")
        self.RuleNumEntry.place(y =20,height = 20,width = 200)
        self.RuleNumEntry.insert(0, self.rulenum)
        
        self.RRuleButton = tkinter.Button(master, justify = "center", text = "Random Rule", command = self.RRulePress)
        self.RRuleButton.place(y =40,height = 20,width = 200)
        
        self.DomSizeLabel = tkinter.Label(master ,text = "Domain Size :")
        self.DomSizeLabel.place(y =80,height = 20,width = 200)
        self.DomSizeEntry = tkinter.Entry(master=root, justify = "center")
        self.DomSizeEntry.place(y =100,height = 20,width = 200)
        self.DomSizeEntry.insert(0, self.dom_size)
                
        self.ItterLabel = tkinter.Label(master ,text = "Itterations :")
        self.ItterLabel.place(y =130,height = 20,width = 200)
        self.ItterEntry = tkinter.Entry(master=root, justify = "center")
        self.ItterEntry.place(y =150,height = 20,width = 200)
        self.ItterEntry.insert(0, self.itterations)
        
        self.PPauseButton = tkinter.Button(master, justify = "center", text = "Pause / Play", command = self.PPausePress)
        self.PPauseButton.place(y =170,height = 20,width = 200)
        self.PPause = False      
        
        self.ResetButton = tkinter.Button(master, justify = "center", text = "Reset", command = self.ResetPress)
        self.ResetButton.place(y =190,height = 20,width = 200)
        self.Reset = False
        
        self.radiovar = tkinter.IntVar()
        self.ColLabel = tkinter.Label(master ,text = "Color Way :")
        self.ColLabel.place(y =220,height = 20,width = 200)
        self.ColorRad1 = tkinter.Radiobutton(master, variable= self.radiovar, value=0, command= self.ColSel)
        self.ColorRad1.place( y= 240, x =45, height = 20, width = 20)
        self.ColorRad2 = tkinter.Radiobutton(master, variable= self.radiovar, value=1, command= self.ColSel)
        self.ColorRad2.place( y= 240, x =95, height = 20, width = 20)
        self.ColorRad3 = tkinter.Radiobutton(master, variable= self.radiovar, value=2, command= self.ColSel)
        self.ColorRad3.place( y= 240, x =145, height = 20, width = 20)
        
        self.ExportButton = tkinter.Button(master, text = "Export as JPG" ,justify = "center")
        self.ExportButton.place(y =260,height = 20,width = 200)
        
        self.ExecButton = tkinter.Button(master, text = "EXECUTE" ,justify = "center", bg ="grey", font = "Helvetica 14 bold", command =lambda:[self.ExecPress()])
        self.ExecButton.place(y =440,x=40,height = 40,width = 120)
        
        self.FrameLabel = tkinter.Label(master ,text = self.frame, font = "Helvetica 10 bold")
        self.FrameLabel.place(x= 520,y = 460,height = 20,width = 100)
        
        self.AnimStart()

    
    def DListSet(self):
        self.Dlist =[]
        self.Dlist.clear()
        self.Dlist = [np.full((self.dom_size,self.dom_size),0, dtype = int)]
        self.cen = int((self.dom_size-1)/2)
        self.Dlist[0][self.cen][self.cen]=1
        self.addlist= [1,0],[-1,0],[0,1],[0,-1],[0,0]
        
    def RRulePress(self):
        Rulenum = rand.randint(0,3**11)# 11269 141674 101327 32853 21034 133111 36268
        Rules = [i for i in product(range(3), repeat=11)]
        Rule = Rules[(Rulenum)]
        self.rule = Rule
        self.RuleNumEntry.delete(0, tkinter.END)
        self.RuleNumEntry.insert(0,Rulenum)
 
    def GetRule(self,rulenum):
        Rules = [i for i in product(range(3), repeat=11)]
        Rule = Rules[(rulenum)]
        return Rule
 
    def PPausePress(self):
        self.anim_toggle()
    
    def ResetPress(self):
        if self.Reset == False:
            self.Reset = True
        else :
            self.Reset = False
        self.DListSet()
        print(len(self.Dlist))
        self.anim = self.anim.new_frame_seq()


    def ColSel(self):
        self.Alive, = plt.plot([], [], 's',ms = self.sscale*65, color = self.col_list[self.radiovar.get()][0])
        self.Alead, = plt.plot([], [], 's',ms = self.sscale*65, color = self.col_list[self.radiovar.get()][1])
        self.Dead, = plt.plot([], [], 's',ms = self.sscale*65, color = self.col_list[self.radiovar.get()][2])
    
    
    def AnimStart(self):
        self.anim = animation.FuncAnimation(self.fig, self.animate, frames=np.linspace(0, self.itterations-1, self.itterations),
               init_func=self.init, blit= False , repeat = True)
        self.Anim_stop()
    
    def ExecPress(self):
        self.itterations = self.ItterEntry.get()
        self.rule = self.rule
        self.anim_toggle()
        self.AnimStart()
        print(f'Itt : {self.itterations}\nRule : {self.rule}')
                
    def Anim_stop(self):     
        self.anim_toggle()
        
    def anim_toggle(self):
        if self.animrun == True:
            self.animrun = False
            self.anim.event_source.stop()
        else :
            self.animrun = True
            self.anim.event_source.start()

   
    def itterget(self):
        self.itterations = self.ItterEntry.get()
        print(self.itterations)

    def init(self):
        self.ax.set_xlim(0, (self.dom_size)*self.sscale)
        self.ax.set_ylim(0, (self.dom_size)*self.sscale)
        return self.Alive, self.Alead, self.Dead,
    
    def animate(self,frame):
        nDom,Alivelist,Aleadlist,Deadlist = self.GOL(self.Dlist[int(frame)],frame) #Use Totalistic function
        self.frame = frame #Assigns Frame 
        self.FrameLabel.config(text =f'Frame : {int(self.frame)}') #Sets Frame label
        self.Dlist.append(nDom) #Appends neighbour matrix values to a Global Matrix
        self.Alive.set_data(Alivelist)  #Plots Alive cells
        self.Alead.set_data(Aleadlist)  #Plots Alead cells
        self.Dead.set_data(Deadlist)    #Plots Dead cells
        return self.Alead,self.Dead,self.Alive, #Returns Values
    
    def GOL(self,Dom,frame):
        pos_shift = (1.1,0.5) #Shifting Values so that it fits interface
        NDom = np.full((self.dom_size,self.dom_size),0, dtype = int) #Creates a Matrix of Neighbour values
        DomNew = np.full((self.dom_size,self.dom_size),0, dtype = int) #Creates a Matrix for Cell Values
        Alive = [[],[]] #Creates list of X,Y values of Alive Cells
        Alead = [[],[]] #Creates list of X,Y values of Alead Cells (2nd Cell type)
        Dead = [[],[]]  #Creates list of X,Y values of Dead Cells
        for i in range (0,self.dom_size-1): #Itterates through Matrix
         for j in range (0,self.dom_size-1): #Similar Above
             pos = (i,j) # Variable declaring the Position within Matrices
             n = 0                           #n = number of Neighbours
             for a in range (0,len(self.addlist)): # (a,b) used to check neighbours
                 v = tuple(np.add(pos,self.addlist[a])) #add list give vector addition for cells in neighbourhood
                 if (Dom[v]==1) :   #If cell Alead
                    n+=1    #Add 1 
                 if (Dom[v]==2) :   #If cell Dead
                    n+=2    #Add 2 to neighbours variable
             NDom[i,j]=n    #Assigns Neighbour value to neighbours matrix
             val = self.rule[(10-n)]    #determines rule through neighbour value
             if (val == 0): #If rule output is 0
                 DomNew[pos] = 0  #assign new value of 0 (Dead)
                 Dead[0].append((i + pos_shift[0])*self.sscale)#Adds to Dead list for plotting
                 Dead[1].append((j+ pos_shift[1])*self.sscale)
             if (val == 1): #If rule output is 1
                 DomNew[pos] = 1  #assign new value of 0 (Alead)
                 Alead[0].append((i+ pos_shift[0])*self.sscale) #Adds to Alead list for plotting
                 Alead[1].append((j+ pos_shift[1])*self.sscale) 
             else:
                 DomNew[pos] = 2 #assign new value of 2 (Alive)
                 Alive[0].append((i+ pos_shift[0])*self.sscale) #Adds to Alive list for plotting
                 Alive[1].append((j+ pos_shift[1])*self.sscale)
        return DomNew,Alive,Alead,Dead #Returns Values to Animation Function

        
root = tkinter.Tk()
app = Main_win(root,1000,75,141674)
root.mainloop()


    #%%