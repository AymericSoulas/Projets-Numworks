from math import *

def pgcd(a,b):
  if b==1:
    return 1
  else:
    if a%b==0:
      return b
    else:
      return pgcd(b,a%b)

def pgcd_det(a,b):
  if b==1:
    print("PGCD("+str(a)+" , "+str(b)+") = "+str(a//b)+"*"+str(b)+" + "+str(a%b))
    return 1
  else:
    if a%b==0:
      print("PGCD("+str(a)+" , "+str(b)+") = "+str(a//b)+"*"+str(b)+" + "+str(a%b))
      return b
    else:
      print("PGCD("+str(a)+" , "+str(b)+") = "+str(a//b)+"*"+str(b)+" + "+str(a%b))
      return pgcd_det(b,a%b)

def premier(a):
  for i in range(2,floor(sqrt(a)+1)):
    if a%i==0:
      return False
  return True

def premier_2(a,b):
  if a%b==0 or b%a==0:
    return True
  return False

def premier_n(a):
  for i in range(2,a//2+1):
    if a%i==0:
      return False,i
  return True


def fac_p(a):
  res=[]
  while not premier(a):
    b=premier_n(a)
    res.append(b[1])
    a=a//b[1]
    print(a,b[1])
  res.append(a)
  return res

def diviseurs(a):
  res=[1]
  if premier(a):
    pass
  else:
    for i in range(2,a//2+1):
      if a%i==0:
        res.append(i)
  res.append(a)
  return res

def somme_diviseurs(a):
  l=diviseurs(a)
  l.pop()
  res=0
  for i in l:
    res+=i
  return res

def euclide_2(a,b):
  det=[]
  while b!=1 or a%b!=0:
    print()
    det.append(a,b,a%b)
    a=b
    b=a%b

