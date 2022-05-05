import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import time
import random as rand
from itertools import product
#%%
Itterations = 80#Itterations keep even
domain_size = 50#2*Itterations + 5#Odd
delay = 0.5
sscale = 8/Itterations

fig, ax = plt.subplots(figsize = (((domain_size-1)*sscale),((domain_size-1)*sscale)))
fig.set_facecolor("linen")
AliveList, AleadList, DeadList = [], [], []
plt.axis('off')
Alive, = plt.plot([], [], 's',ms = sscale*60, color = "black")
Alead, = plt.plot([], [], 's',ms = sscale*60, color = "grey")
Dead, = plt.plot([], [], 's',ms = sscale*60, color = "white")
#%%
Rulenum = rand.randint(0,3**11)# 11269 141674 101327 32853 21034 133111 36268

States = [i for i in product(range(2), repeat=3)]
Rules = [i for i in product(range(3), repeat=11)]
Rule = Rules[(Rulenum)]
print(f'{Rulenum} : {Rule}')
#%%
Dlist = []

addlist= [1,0],[-1,0],[0,1],[0,-1],[0,0]

def init(): 
    ax.set_xlim(0, (domain_size)*sscale)
    ax.set_ylim(0, (domain_size)*sscale)
    return Alive, Alead, Dead,

def GOL(Dom,frame):
    NDom = np.full((domain_size+1,domain_size+1),0, dtype = int)
    DomNew = np.full((domain_size+1,domain_size+1),0, dtype = int)
    Alive = [[],[]]
    Alead = [[],[]] 
    Dead = [[],[]]
    #for i in range (1,domain_size-1):       #(i,j) -> Cell Position
    for i in range (1,domain_size-1): 
     for j in range (1,domain_size-1):
         pos = (i,j)
         n = 0                           #n = number of Neighbours
         for a in range (0,len(addlist)):          #    (a,b) used to check neighbours
             v = tuple(np.add(pos,addlist[a]))
             if (Dom[v]==1) :
                n+=1 
             if (Dom[v]==2) :
                n+=2
         NDom[i,j]=n
         val = Rule[(10-n)]
         if (val == 0): 
             DomNew[pos] = 0
             Dead[0].append((i)*sscale)
             Dead[1].append(j*sscale)
         if (val == 1):
             DomNew[pos] = 1
             Alead[0].append((i)*sscale)
             Alead[1].append(j*sscale)
         else:
             DomNew[pos] = 2
             Alive[0].append((i)*sscale)
             Alive[1].append(j*sscale)
    return DomNew,Alive,Alead,Dead

Dlist = [np.full((domain_size,domain_size),0, dtype = int)]
#%%
cen = int((domain_size-1)/2)
Dlist[0][cen][cen]=1
#%%
def update(frame):
    nDom,Alivelist,Aleadlist,Deadlist = GOL(Dlist[int(frame)],frame)
    Dlist.append(nDom)
    Alive.set_data(Alivelist)
    Alead.set_data(Aleadlist)
    Dead.set_data(Deadlist)
    time.sleep(delay)
    return Alead,Dead,Alive,

ani = FuncAnimation(fig, update, frames=np.linspace(0, Itterations-1, Itterations),
                    init_func=init, blit= False , repeat = False)
plt.show()

#%%