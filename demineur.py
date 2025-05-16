from math import *
from kandinsky import *
from random import *
from ion import *
from time import *

class Demineur():
  def __init__(self,nb,t=20):
    self.t=t
    self.h=222//self.t
    self.l=320//self.t
    self.nb=nb
    self.drapeau=color(0,255,0)
    self.cu=color(0,0,255)
    self.grille=[[0 for i in range(self.h+2)]for j in range(self.l+2)]
    self.grille2=[[0 for i in range(self.h+2)]for j in range(self.l+2)]
    nb2=nb
    print(len(self.grille[0]))
    self.x=0
    self.y=0
    self.bord=color(255,0,0)
    self.couv=color(0,0,0)
    self.ouv=color(255,255,255)
    while nb2!=0:
      x=randint(1,self.l-1)
      y=randint(1,self.h-1)
      if self.grille[x+1][y+1]!=-1:
        self.grille[x+1][y+1]=-1
        nb2-=1
    for i in range(1,self.l+1):
      for j in range(1,self.h+1):
        if self.grille[i][j]==0:
          for x in range(i-1,i+2):
            for y in range(j-1,j+2):
              if self.grille[x][y]==-1 and not(x==i and y==j):
                self.grille[i][j]+=1
    
    self.construction()
    print("------------------------------")
    self.boucle()
  
  def construction(self):
    fill_rect(0,0,320,222,self.bord)
    for i in range(self.l):
      for j in range(self.h):
        self.carre(i,j)
    self.curseur(self.x,self.y)
  
  def boucle(self):
    self.perdu=False
    while not keydown(KEY_BACK) and not self.perdu:
      self.test_touche()
    self.fin()
  
  def test_touche(self):
    if keydown(KEY_UP) and self.y>0:
      self.carre(self.x,self.y)
      self.y-=1
      self.curseur(self.x,self.y)
      sleep(0.1)
    
    elif keydown(KEY_RIGHT) and self.x<self.l-1:
      self.carre(self.x,self.y)
      self.x+=1
      self.curseur(self.x,self.y)
      sleep(0.1)
 
    elif keydown(KEY_DOWN) and self.y<self.h-1:
      self.carre(self.x,self.y)
      self.y+=1
      self.curseur(self.x,self.y)
      sleep(0.1)
  
    elif keydown(KEY_LEFT) and self.x>0:
      self.carre(self.x,self.y)
      self.x-=1
      self.curseur(self.x,self.y)
      sleep(0.1)
      print(self.x,self.y)
    
    elif keydown(KEY_OK) and self.grille2[self.x+1][self.y+1]!=1:
      if self.grille[self.x+1][self.y+1]==-1:
        self.perdu=True
        self.gagne=False
      elif self:
        self.autour(self.x,self.y)
        self.test_fin()
      sleep(0.1)
      print(self.perdu)
    
    elif keydown(KEY_EXE) and self.grille2[self.x+1][self.y+1]!=1:
      print(1)
      if self.grille2[self.x+1][self.y+1]==0:
        print(2)
        self.grille2[self.x+1][self.y+1]=-1
        self.carre(self.x,self.y)
        self.curseur(self.x,self.y)
      elif self.grille2[self.x+1][self.y+1]==-1:
        print(3)
        self.grille2[self.x+1][self.y+1]=0
        self.carre(self.x,self.y)
        self.curseur(self.x,self.y)
      sleep(0.1)
  
  def autour(self,x,y):
    if x<0 or x>=self.l or y<0 or y>=self.h:
      return
    elif self.grille2[x+1][y+1]==0:
      if self.grille[x+1][y+1]!=0:
        self.grille2[x+1][y+1]=1
        self.carre(x,y)
        return
      else:
        self.grille2[x+1][y+1]=1
        self.carre(x,y)
        for i in range(x-1,x+2):
          for j in range(y-1,y+2):
            self.autour(i,j)
    else: return
  
  def carre(self,x,y):
    print("Carre: x="+str(x)+", y="+str(y))
    if self.grille2[x+1][y+1]==0:
      fill_rect(x*self.t+1,y*self.t+1,self.t-2,self.t-2,self.couv)
    elif self.grille2[x+1][y+1]==-1:
      fill_rect(x*self.t+1,y*self.t+1,self.t-2,self.t-2,self.drapeau)
    elif self.grille[x+1][y+1]==-1:
      fill_rect(self.x*self.t+1,self.y*self.t+1,self.t-2,self.t-2,color(255,0,0))
    else:
      fill_rect(x*self.t+1,y*self.t+1,self.t-2,self.t-2,self.ouv)
      if self.grille[x+1][y+1]!=0:
        draw_string(str(self.grille[x+1][y+1]),x*self.t+6,(y)*self.t+1)
  
  def curseur(self,x,y):
    fill_rect(self.t*x+self.t//3+1,self.t*y+1,self.t//3-2,self.t-2,self.cu)
    fill_rect(self.t*x+1,self.t*y+self.t//3+1,self.t-2,self.t//3-2,self.cu)
  
  def fin(self):
    fill_rect(self.x*self.t+1,self.y*self.t+1,self.t-2,self.t-2,color(255,0,0))
    while not (keydown(KEY_EXE) or keydown(KEY_OK)):
      fill_rect(0,0,320,222,color(255,255,255))
    if self.gagne==True:
      draw_string("Gagne!",135,110)
    else:
      draw_string("Perdu!",135,110)
  

  def test_fin(self):
    nb=0
    for i in self.grille:
      for j in i:
        nb+=j
    if nb==self.h*self.l-self.nb:
      self.perdu=True
      self.gagne=True


a=Demineur(25)

