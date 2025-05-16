from math import *
from kandinsky import *
from time import *

def cercle(x,y,r,couleur=color(255,0,255)):
  for i in range(0,r+1):
    dy=int(sqrt(r**2-i**2))
    fill_rect(x-i,y-dy,2*i,2*dy,couleur)
    #set_pixel(x-i,y-dy,couleur)

def efface(x,y,r,couleur=color(255,255,255)):
  fill_rect(x-r,y-r,2*r,2*r,couleur)

def efface_moitie(x,y,r,sens=0,coul=color(255,255,255)):
  if sens==0:
    fill_rect(x-r,y-r,2*r,r,coul)
  elif sens==1:
    fill_rect(x,y-r,r,2*r,coul)
  elif sens==2:
    fill_rect(x-r,y,2*r,r,coul)
  else:
    fill_rect(x-r,y-r,r,2*r,coul)

def bcp():
  for i in range(320):
    cercle(i,111,10)
    efface_moitie(i-1,111,10,3)
    cercle(i,111,10)
    sleep(0.005)

def test_cercle(r=10):
  x=100
  y=100
  for f_anim in range(0,r):
    for i in range(0,r+1):
      dy=round(sqrt(r**2-i**2))
      set_pixel(x*20-10+i+f_anim,y*20+10+dy,color(255,0,0))
      set_pixel(x*20-10+i+f_anim,y*20+10-dy,color(255,0,0))
      set_pixel(x*20-10+i+dy,y*20+10+f_anim,color(255,0,0))
      set_pixel(x*20-10+i-dy,y*20+10+f_anim,color(255,0,0))