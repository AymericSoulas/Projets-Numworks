from math import sqrt
class coordonnees:
  def __init__(self,x=None,y=None,st=None):
    self.x=x
    self.y=y
    self.state=st
  
  def distance(self,p2):
    res=coordonnees()
    res.x=abs(p2.x-self.x)
    res.y=abs(p2.y-self.y)
    return res
  
  def distance_abs(self,p2):
    res=self.distance(p2)
    return sqrt(res.x**2+res.y**2)