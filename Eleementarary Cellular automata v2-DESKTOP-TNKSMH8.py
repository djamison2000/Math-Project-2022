import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import time
from itertools import product
#%%
def GOL(Dom,Itt):
    DomNew = Dom
    Alivex,Alivey = [],[]
    for i in range (1,len(DomNew[0])-1):
         if tuple(DomNew[Itt][i-1:i+2]) in lrule:
             DomNew[Itt+1][i]= 0
             Alivex.append(((i)*sscale))
             Alivey.append(((size-(Itt))*sscale))
         else:
             DomNew[Itt+1][i] = 1 
    return DomNew,Alivex,Alivey
#%%#%%
Rulenum = 54# < 256 # 30 , 60 ,69 , 105 ,193, 73, 45, 58, 18

Itterations = 150#nice to keep odd
size = Itterations*2
sscale = 3/Itterations
delay = 0.01
colors = ["red","green","yellow"]

Dlist = [np.full((size+2,(2*size)+2),1, dtype = int)]
Alivesx = [(int((size+1)/2))*sscale]
Alivesy = [size*sscale]

fig, ax = plt.subplots(figsize = ((2*size*sscale),(size*sscale)))
AliveList = []
plt.axis('off')
Alive, = plt.plot([], [], 's',ms = sscale*80, color = "black")

States = [i for i in product(range(2), repeat=3)]    #States
Rules = [i for i in product(range(2), repeat=8)]
Ruleset = Rules[255-(Rulenum)]          #len(Rule) = 256)
lrule = []

for i in range(len(States)):
    if (Ruleset[(i)] ==0):
        lrule.append(States[i])
print(lrule)

live = ((1,int((size+1)/2)),())
for i in range(len(Dlist[0])):
    for j in range(len(Dlist[0])):
        if (i,j)in live:
            Dlist[0][i][j] = 0
            
#%%
def init():
    ax.set_xlim(-2*sscale, (size+2)*sscale)
    ax.set_ylim(-2*sscale +(size)*sscale/2, (size+1)*sscale)
    return Alive,

def update(frame): 
    i = int(frame)
    nDom,nAlivex,nAlivey = GOL(Dlist[i],i+1)
    Alive, = plt.plot([], [], 's',ms = sscale*(80), color = "black")
    Dlist.append(nDom) 
    Alivesx.extend(nAlivex)
    Alivesy.extend(nAlivey)
    Alivelist = (Alivesx,Alivesy)
    Alive.set_data(Alivelist)
    time.sleep(delay)
    return Alive,

ani = FuncAnimation(fig, update, frames=np.linspace(0, Itterations-1, Itterations),
                    init_func=init, blit=True)
plt.show()
