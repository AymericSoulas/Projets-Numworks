from math import *

def ab10_bx(a,x):
  res=[]
  while a>x:
    res.append(a%x)
    a=a//x
  res.append(a)
  res.reverse()
  a=""
  for i in res:
    a+=str(i)
  return int(a)

def abx_b10(a,x):
  b=str(a)
  a=[]
  for i in b:
    a.insert(0,int(i))
  res=0
  for i in range(len(a)):
    res+=a[i]*x**i
  return res

def abx_by(a=None,x=None,y=None):
  if x==None:
    print("Inserez la base de depart:")
    x=int(input("Base de depart: "))
  if a==None:
    print("Inserez le nombre de depart:")
    a=int(input("Nombre de depart: "))
  if y==None:
    print("Inserez la base d arrivee:")
    y=int(input("Base arrivee: "))
  a=abx_b10(a,x)
  return ab10_bx(a,y)

print(abx_by())