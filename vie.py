from math import *
from kandinsky import *
from ion import *
from random import *
from time import *

class vie():
  def __init__(self):
    print("Nombre de boucles\n par secondes!")
    #self.wait=1/int(input())
    self.wait=1
    self.taille=10
    self.x=0
    self.y=0
    self.cf=color(255,255,255)
    self.cc=color(255,0,0)
    self.ccel=color(0,0,255)
    #self.lx=int(input("Cellules en largeur:"))
    #self.lx=5
    self.lx=int(320/self.taille)
    #self.ly=int(input("Cellules en hauteur:"))
    self.ly=int(222/self.taille)
    #self.ly=5
    #self.nbloop=int(input("Nombre de boucles:"))
    self.nbloop=50
    self.alea=int(input("Generation aleatoire:"))==1
    if self.alea:
      self.gr=[[randint(0,1) for i in range(self.ly)]for j in range(self.lx)]
    else:
      self.gr=[[0 for i in range(self.ly)]for j in range(self.lx)]
    self.construction()
    self.loop_choix()
    self.boucle()
  
  def construction(self):
    fill_rect(0,0,320,222,self.cf)
    self.dx=(320-self.lx*self.taille)//2
    self.dy=(222-self.ly*self.taille)//2
    fill_rect(self.dx,self.dy,self.lx*self.taille,self.ly*self.taille,self.cc)
    for i in range(self.lx):
      for j in range(self.ly):
        if self.gr[i][j]==0:
          fill_rect(self.dx+i*self.taille+1,self.dy+self.taille*j+1,self.taille-2,self.taille-2,self.cf)
        else:
          fill_rect(self.dx+i*self.taille+1,self.dy+self.taille*j+1,self.taille-2,self.taille-2,self.ccel)
  
  def croix(self,x,y):
    fill_rect(self.dx+x*self.taille+self.taille//3+1,self.dy+self.taille*y+1,self.taille//3-1,self.taille-2,self.cc)
    fill_rect(self.dx+x*self.taille+1,self.dy+y*self.taille+self.taille//3+1,self.taille-2,self.taille//3-1,self.cc)
  
  def case(self,x,y):
    if self.gr[x][y]==1:
      fill_rect(self.dx+x*self.taille+1,self.dy+self.taille*y+1,self.taille-2,self.taille-2,self.ccel)
    else:
      fill_rect(self.dx+x*self.taille+1,self.dy+self.taille*y+1,self.taille-2,self.taille-2,self.cf)
  
  def loop_choix(self):
    x=0
    y=0
    self.croix(x,y)
    while not keydown(KEY_EXE):
      if keydown(KEY_UP):
        self.case(x,y)
        if y==0: y=self.ly-1
        else:y-=1
        self.croix(x,y)
      elif keydown(KEY_RIGHT):
        self.case(x,y)
        if x==self.lx-1: x=0
        else:x+=1
        self.croix(x,y)
      elif keydown(KEY_DOWN):
        self.case(x,y)
        if y==self.ly-1: y=0
        else:y+=1
        self.croix(x,y)
      elif keydown(KEY_LEFT):
        self.case(x,y)
        if x==0: x=self.lx-1
        else:x-=1
        self.croix(x,y)
      elif keydown(KEY_OK):
        self.gr[x][y]=abs(self.gr[x][y]-1)
        self.case(x,y)
        self.croix(x,y)
      sleep(0.1)

  def affichage(self):
    for x in range(self.lx):
      for y in range(self.ly):
        self.case(x,y)

  def valeur_suivante(self,x,y):
    if x==self.lx-1: x=-1
    if y==self.ly-1: y=-1
    nb=0
    for i in range(x-1,x+2):
      for j in range(y-1,y+2):
        if self.gr[i][j]==1:
          nb+=1
    if self.gr[x][y]==1:
      nb-=1
    if nb<=1 or nb>3:
      self.gr2[x][y]=0
    elif nb==3:
      self.gr2[x][y]=1
    else:
      self.gr2[x][y]=self.gr[x][y]
    print("x: "+str(x)+", y: "+str(y)+", nb: "+str(nb)+", case: "+str(self.gr[x][y])+", next"+str(self.gr2[x][y]))

  def boucle(self):
    while self.nbloop<0 or self.nbloop+1>1:
      self.nbloop-=1
      self.gr2=[[0 for i in range(self.ly)]for j in range(self.lx)]
      for x in range(self.lx):
        for y in range(self.ly):
          self.valeur_suivante(x,y)
      print(self.gr[1][0])
      for i in range(self.lx):
        for j in range(self.ly):
          self.gr[i][j]=self.gr2[i][j]
      self.affichage()
      #sleep(self.wait)

a=vie()
print(a.gr)