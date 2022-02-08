import abc
from math import sin, pi
import random

print("**********************zadanie 1*****************")

class Calka(abc.ABC):
  def __init__(self, a, b, n, fun):
    self.a=a
    self.b=b
    self.n=n
    self.fun= fun

  @abc.abstractmethod
  def licz(self):
    '''metoda abstrakcyjna'''
    pass

class Trapez(Calka):
  def licz(self):
    '''definicja abstrakcyjnej'''
    wynik = 0 
    deltax = (self.b - self.a) / self.n
    for i in range(self.n):
      xi = i*deltax + self.a
      xii = xi + deltax
      wynik += 0.5 * deltax * (self.fun(xi) + self.fun(xii))
    return wynik

class Simpson(Calka):
  def licz(self):
    '''definicja abstrakcyjnej'''
    deltax= (self.b - self.a)/(2*self.n)
    four, two = 0, 0
    for i in range(1, 2*self.n):
      if i%2 == 1:
        xi = i*deltax + self.a
        four += self.fun(xi)
      if i%2 == 0:
        xi = i*deltax + self.a
        two +=self.fun(xi)
    wynik = deltax/3 * (self.fun(self.a)+ 4 *four + 2 * two + self.fun(2*self.n))
    return wynik

def funkcja(x):
  return sin(x)

t1=Trapez(1, pi, 100, funkcja)
print(Trapez.mro())
print("Trapez: ", t1.licz())
t2=Simpson(1, pi, 100, funkcja)
print(Simpson.mro())
print("Simpson: ", t2.licz())


print("**********************zadanie 2*****************")

class Stos:
  def __init__(self, other_stos=None):
    if type(other_stos) is Stos:
      self.items = [elem for elem in other_stos.items]
    else:
      self.items = []

  def push(self, ite):
    self.items.append(ite)
  
  def pop(self):
    return self.items.pop(len(self.items)-1)

  def push_stos(self, other_stos):
    if type(other_stos) is Stos:
      for ite in other_stos.items:
        self.push(ite)
    else:
      print("argument nie jest typu stos!")
  
  def __len__(self):
    return len(self.items)

  def __str__(self):
    print(self.items, end =" ")
    return ""

#sortowanie rosnace 
class SortowanieStosu(Stos):
  def __init__(self, other_stos=None):
    if type(other_stos) is SortowanieStosu:
      self.items = [elem for elem in other_stos.items]
    else:
      self.items = []
  
  def push(self, elem):
    if len(self.items)==0 or elem>=self.items[-1]:
      self.items.append(elem)

  def push_stos(self, other_stos):
    if type(other_stos) is SortowanieStosu:
      for elem in other_stos.items:
        self.push(elem)
    else:
      print("argument nie jest typu sortowany_stos!")

    
  

s = Stos()
s.push(2)
s.push(6)
s.push(4)
print("Stos1: ", s)
s2 = s.pop()
print("Stos1 po pop(): ", s)
print("Pop wartosci: ", s2)

s3 = SortowanieStosu()
s3.push(2)
s3.push(5)
s3.push(4)
print("sortowany sotos3: ", s3)
s3.push_stos(s)
print("sorotwany stos3: ", s3)
s4= SortowanieStosu(s2)
s5= SortowanieStosu(s3)
print("sortowany stos s3: ", s3)
print("sortowany stos s4: ", s4)
print("sortowany stos s5: ", s5)

sum_len =0
for _ in range(100):
  aver = SortowanieStosu()
  for _ in range(100):
    aver.push(random.randint(0, 100))
  sum_len = sum_len + len(aver)
print("średnia długość stosu: ", sum_len/100)


print("**********************zadanie 3*****************")

class Licz:
  def __init__(self):
    self.chars = 0
    self.words = 0
    self.lines = 0

  def licz(self, file):
    f = open(file, "r")
    for line in f:
      words= line.split()
      self.lines += 1
      self.words += len(words)
      self.chars += len(line)
    f.close()
    print('lines: {}, words: {} chars: {} in file {}'.format(self.lines, self.words, self.chars, file))

  #@staticmethod
  #def razem():
    #print

i=Licz()
i.licz('plik1.txt')
