from math import *
def binaire(n):
  l = []
  while n>0:
    r=n%2
    l.append(r)
    n=n//2
  l.reverse()
  return l