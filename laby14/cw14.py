import math

print("*************zadnie 1*************")

class Coords:
  @property 
  def x(self):
    return self.__x
  
  @x.setter
  def x(self, k):
    self.__x = k

  @property 
  def y(self):
    return self.__y
  
  @y.setter
  def y(self, k):
    self.__y = k
  
  def __init__(self):
    self.x=0
    self.y=0
  
pkt = Coords()
pkt.x = 12
print(pkt.x)


print("*************zadnie 2*************")

def zakres(pkt1, pkt2):
  def zakres2(funkcja):
    def compar(p1, p2):
      if pkt1 <= p1.x <= pkt2 and pkt1 <= p1.y <= pkt2 and pkt1 <= p2.x <= pkt2 and pkt1 <= p2.y <= pkt2:
        return funkcja(p1, p2)
      else:
        raise ArithmeticError
    return compar
  return zakres2

@zakres(-30, 30)
def dodawanie(p1, p2):
  c = Coords()
  c.x = p1.x + p2.x
  c.y = p1.y + p2.y
  return c

p1 = Coords()
p2 = Coords()
p1.x = 7
p1.y = -17

p2.x = -7
p2.y = -3

print(dodawanie(p1, p2))

@zakres(-30, 30)
def odejmowanie(p1, p2):
  c = Coords()
  c.x = p1.x - p2.x
  c.y = p1.y - p2.y
  return c


print(odejmowanie(p2, p1))

print("*************zadnie 3*************")

class Oblicz():

  @staticmethod
  def count_area(p1, p2, p3, p4=None):
    if p4 is None:
      a= math.sqrt(math.pow(p1.x - p2.x, 2) + math.pow(p1.y - p2.y, 2))
      b= math.sqrt(math.pow(p2.x - p3.x, 2) + math.pow(p2.y - p3.y, 2))
      c= math.sqrt(math.pow(p3.x - p1.x, 2) + math.pow(p3.y - p1.y, 2))
      p = a+b+c
      return math.sqrt(p*(p-a)*(p-b)*(p-c))
    else:
      a= math.sqrt(math.pow(p1.x - p2.x, 2) + math.pow(p1.y - p2.y, 2))
      b= math.sqrt(math.pow(p2.x - p3.x, 2) + math.pow(p2.y - p3.y, 2))
      c= math.sqrt(math.pow(p3.x - p4.x, 2) + math.pow(p3.y - p4.y, 2))
      d= math.sqrt(math.pow(p4.x - p1.x, 2) + math.pow(p4.y - p1.y, 2))
      p = a+b+c+d
      return math.sqrt((p-a)*(p-b)*(p-c)*(p-d))
    
  @staticmethod
  def count_obw(p1, p2, p3, p4=None):
    if p4 is None:
      a= math.sqrt(math.pow(p1.x - p2.x, 2) + math.pow(p1.y - p2.y, 2))
      b= math.sqrt(math.pow(p2.x - p3.x, 2) + math.pow(p2.y - p3.y, 2))
      c= math.sqrt(math.pow(p3.x - p1.x, 2) + math.pow(p3.y - p1.y, 2))
      return a+b+c
    else:
      a= math.sqrt(math.pow(p1.x - p2.x, 2) + math.pow(p1.y - p2.y, 2))
      b= math.sqrt(math.pow(p2.x - p3.x, 2) + math.pow(p2.y - p3.y, 2))
      c= math.sqrt(math.pow(p3.x - p4.x, 2) + math.pow(p3.y - p4.y, 2))
      d= math.sqrt(math.pow(p4.x - p1.x, 2) + math.pow(p4.y - p1.y, 2))
      return a+b+c+d

p3 = Coords()
p4 = Coords()
p3.x=-4
p4.x=45
p3.y=-3
p4.y=3

print("Obwod trojkata: ", Oblicz.count_obw(p1, p2, p3))
print("Pole trojkata: ", Oblicz.count_area(p1, p2, p3))
print("Obwod czworokata: ", Oblicz.count_obw(p1, p2, p3, p4))
print("Pole czworokata: ", Oblicz.count_area(p1, p2, p3, p4))

print("*************zadnie 4*************")


class Cw4:
  count = {}
  def __init__(self, funkcja):
    self.funkcja = funkcja
    Cw4.count[funkcja] = 0 
  
  def __call__(self, *args, **zm):
    Cw4.count[self.funkcja] += 1
    self.funkcja(*args, **zm)
  
  @staticmethod
  def print_count():
    for i, j in Cw4.count.items():
      print(i, j)

@Cw4
def f1():
  pass

@Cw4
def f2():
  pass

@Cw4
def f3():
  pass

for x in range(38):
  f1()
  for y in range(15):
    f2()
    for z in range(2):
      f3()

print(Cw4.print_count())

