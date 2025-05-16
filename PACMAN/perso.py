from kandinsky import *
from ont import cercle
from math import sqrt

class pero:
  def __init__(self,x=1,y=1,esp=0):
    self.esp=esp
    self.r=9
    self.x=x
    self.x1=x
    self.x2=x
    self.y=y
    self.y1=y
    self.y2=y
    self.dir=2
    self.dirs=3
    self.coul=color(255,255,0)
    self.random=1
    self.f_anim=0

  def affiche(self):
    if self.dir==1:
      self.dep_1()
    elif self.dir==2:
      self.dep_2c2()
    elif self.dir==3:
      self.dep_3()
    elif self.dir==4:
      self.dep_4()
    self.f_anim+=1
  
  def dep_1c(self):
    for i in range(0,self.r):
      set_pixel(self.x*20+10+i,self.y*20+30-self.f_anim+self.r-int(i*i/sqrt(i**2+self.r**2)),color(0,0,0))
      set_pixel(self.x*20+10+i,self.y*20+30-self.f_anim-self.r+int(i*i/sqrt(i**2+self.r**2)),self.coul)
      set_pixel(self.x*20+10-i,self.y*20+30-self.f_anim+self.r-int(i*i/sqrt(i**2+self.r**2)),color(0,0,0))
      set_pixel(self.x*20+10-i,self.y*20+30-self.f_anim-self.r+int(i*i/sqrt(i**2+self.r**2)),self.coul)
  
  def dep_2c(self):
    for i in range(0,self.r+1):
      dy=int(sqrt(self.r**2-i**2))
      set_pixel(self.x*20-10+i+self.f_anim,self.y*20+10+dy,self.coul)
      set_pixel(self.x*20-10+i+self.f_anim,self.y*20+10-dy,self.coul)
      set_pixel(self.x*20-10-i+self.f_anim,self.y*20+10+dy,color(0,0,0))
      set_pixel(self.x*20-10-i+self.f_anim,self.y*20+10-dy,color(0,0,0))
      set_pixel(self.x*20-10+dy+self.f_anim,self.y*20+10+i,self.coul)
      set_pixel(self.x*20-10+dy+self.f_anim,self.y*20+10+i,self.coul)
      set_pixel(self.x*20-10-dy+self.f_anim,self.y*20+10-i,color(0,0,0))
      set_pixel(self.x*20-10-dy+self.f_anim,self.y*20+10-i,color(0,0,0))
  
  def dep_2c2(self):
    for i in range(0,self.r+1):
      dy=int(sqrt(self.r**2-i**2))
      st=int(i**2/sqrt(i**2+self.r**2))
      fill_rect(self.x*20-10+i+self.f_anim,self.y*20+10-dy,-2,2*dy,self.coul)
      set_pixel(self.x*20-10-i+self.f_anim,self.y*20+10+self.r-st,color(0,0,0))
      set_pixel(self.x*20-10-i+self.f_anim,self.y*20+10-self.r+st,color(0,0,0))
    fill_rect(self.x*20-20+self.f_anim,self.y*20+8,1,5,color(0,0,0))
      
  def dep_3c(self):
    for i in range(0,self.r+1):
      dx=int(sqrt(self.r**2-i**2))
      fill_rect(self.x*20-10+dx,self.y*20+10+i+self.f_anim,2*dx,2,self.coul)
      
  def inherit(self):
    self.x2=self.x1
    self.x1=self.x
    self.y2=self.y1
    self.y1=self.y
  
  def dep_1(self):
    fill_rect(self.x*20,self.y*20+20-self.f_anim,20,1,self.coul)
    fill_rect(self.x*20,self.y*20+39-self.f_anim,20,2,color(0,0,0))
  def dep_2(self):
    fill_rect(self.x*20+self.f_anim,self.y*20,1,20,self.coul)
    fill_rect(self.x*20-20+self.f_anim,self.y*20,1,20,color(0,0,0))
  def dep_3(self):
    fill_rect(self.x*20,self.y*20+self.f_anim,20,1,self.coul)
    fill_rect(self.x*20,self.y*20-20+self.f_anim,20,1,color(0,0,0))
  def dep_4(self):
    fill_rect(self.x*20+20-self.f_anim,self.y*20,1,20,self.coul)
    fill_rect(self.x*20+39-self.f_anim,self.y*20,2,20,color(0,0,0))

