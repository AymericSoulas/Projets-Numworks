from math import *
from kandinsky import *
from ion import *
from random import *
from time import *
from coords import *
from perso import *
from maps import map1_f as carte

class pacman:
  def __init__(self):
    self.cf=color(0,0,0)
    self.cm=color(0,0,200)
    self.terr=carte
    self.nb_rand=1
    self.perdu=True
    self.gagne=False
    self.score=0
    self.score_max=0
    self.dt=0.001
    self.constr_map()
    self.mobs=[pero(),pero(10,5,1),pero(9,5,1)]
    for i in range(1, len(self.mobs)):
      self.mobs[i].coul=color(randint(100,255),randint(100,255),randint(100,255))
    self.affiche_perso()
    print(self.terr)
    self.boucle()
    self.perdu_a()

  def constr_map(self):
    for i in range(16):
      for j in range(11):
        if self.terr[i][j]==0:
          self.score_max+=1
        self.terr[i][j]=coordonnees(i,j,self.terr[i][j])
        self.affiche_case(self.terr[i][j])
    fill_rect(0,220,320,3,self.cm)

  def affiche_case(self,case):
    if case.state==1:
      fill_rect(case.x*20,case.y*20,20,20,self.cm)
    else:
      fill_rect(case.x*20,case.y*20,20,20,self.cf)
      if case.state==0:
        fill_rect(case.x*20+8,case.y*20+8,4,4,color(255,255,0))
  
  def affiche_perso(self):
    if self.mobs[0].f_anim==20:
      self.dir_s()
      for i in range(len(self.mobs)):
        self.mobs[i].f_anim=0
    if self.mobs[0].f_anim==0:
      for i in range(len(self.mobs)):
        self.collision(i)
        if i>0 and i<self.nb_rand+1:
          self.choix_mr(i)
        elif i>self.nb_rand:
          self.choix_m(i)
        self.affiche_case(self.terr[self.mobs[i].x2][self.mobs[i].y2])
        self.mobs[i].inherit()
        if i==0:
          if self.terr[self.mobs[0].x][self.mobs[0].y].state==0:
            self.terr[self.mobs[0].x][self.mobs[0].y].state=2
            self.score+=1
            if self.score==self.score_max:
              self.perdu=False
              self.gagne=True
        if self.mobs[i].dir==1 and self.terr[self.mobs[i].x][self.mobs[i].y-1].state!=1:
          self.mobs[i].y-=1
        elif self.mobs[i].dir==2 and self.terr[self.mobs[i].x+1][self.mobs[i].y].state!=1:
          self.mobs[i].x+=1
        elif self.mobs[i].dir==3 and self.terr[self.mobs[i].x][self.mobs[i].y+1].state!=1:
          self.mobs[i].y+=1
        elif self.mobs[i].dir==4 and self.terr[self.mobs[i].x-1][self.mobs[i].y].state!=1:
          self.mobs[i].x-=1
        self.collision(i)
    for i in self.mobs:
      i.affiche()
  
  def choix(self):
    if keydown(KEY_UP) and self.mobs[0].dir!=3:
      self.mobs[0].dirs=1
    elif keydown(KEY_RIGHT) and self.mobs[0].dir != 4:
      self.mobs[0].dirs=2
    elif keydown(KEY_DOWN) and self.mobs[0].dir!=1:
      self.mobs[0].dirs=3
    elif keydown(KEY_LEFT) and self.mobs[0].dir!=2:
      self.mobs[0].dirs=4
    if keydown(KEY_IMAGINARY):
      print("score:",self.score," score_max:", self.score_max)
  
  def dir_s(self):
    if self.mobs[0].dirs==1 and self.terr[self.mobs[0].x][self.mobs[0].y-1].state!=1:
      self.mobs[0].dir=1
    elif self.mobs[0].dirs==2 and self.terr[self.mobs[0].x+1][self.mobs[0].y].state!=1:
      self.mobs[0].dir=2
    elif self.mobs[0].dirs==3 and self.terr[self.mobs[0].x][self.mobs[0].y+1].state!=1:
      self.mobs[0].dir=3
    elif self.mobs[0].dirs==4 and self.terr[self.mobs[0].x-1][self.mobs[0].y].state!=1:
      self.mobs[0].dir=4
  
  def choix_mr(self,i):
    a=[]
    if self.terr[self.mobs[i].x-1][self.mobs[i].y].state!=1 and self.mobs[i].dir!=2:
      a.append(4)
    if self.terr[self.mobs[i].x+1][self.mobs[i].y].state!=1 and self.mobs[i].dir!=4:
      a.append(2)
    if self.terr[self.mobs[i].x][self.mobs[i].y+1].state!=1 and self.mobs[i].dir!=1:
      a.append(3)
    if self.terr[self.mobs[i].x][self.mobs[i].y-1].state!=1 and self.mobs[i].dir!=3:
      a.append(1)
    self.mobs[i].dir=choice(a)
    
  def choix_m(self,i):
    self.choix_mr(i)

  def collision(self,i):
    if self.mobs[i].x==self.mobs[0].x and self.mobs[i].y==self.mobs[0].y and i>0:
      self.perdu=False

  def perdu_a(self):
    fill_rect(0,0,320,222,color(255,255,255))
    if self.gagne:
      draw_string("Gagne",100,100)
    else:
      draw_string("Perdu",100,100)

  def boucle(self):
    t=monotonic()
    while self.perdu:
      self.choix()
      self.affiche_perso()

a=pacman()

