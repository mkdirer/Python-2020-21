import math
from scipy import misc
import random

print("*************zadanie 1***************")

class FirstPrime:
  def __init__(self, x, y):
    self.mi = x - 1
    self.ma = y

  def __iter__(self):
    return self
  
  def __next__(self):
    self.mi += 1
    while True:
      for i in range(2, self.mi//2+1):
        if self.mi % i ==0:
          break
      else:
        return self.mi
      self.mi += 1
      if self.mi > self.ma:
        raise StopIteration

class SecondPrime:
  def __init__(self, x, y):
    self.mi = x
    self.ma = y

  def __iter__(self):
    return NextSecondPrime(self.mi, self.ma)

class NextSecondPrime:
  def __init__(self, x, y):
    self.mi = x-1
    self.ma = y

  def __next__(self):
    self.mi += 1
    while True:
      for el in range(2, self.mi//2+1):
        if self.mi % el == 0:
          break
      else:
        return self.mi
      self.mi += 1
      if self.mi > self.ma:
        raise StopIteration


print("pierwsze dal 1 klasy")
t1 = FirstPrime(3, 32)
for i in t1:
  print(i, end=' ')

print()
print("drugie dla 1 klasy")
for e in t1:
  print(e, end=' ')

print("pierwsze dal 2 klasy")
t2 = SecondPrime(3, 32)
for i in t2:
  print(i, end=' ')

print()
print("\drugie dla 2 klasy")
for i in t2:
  print(i, end=' ')
print()

print("*************zadanie 2***************")

def fun(x):
  return math.sin(x)-(0.5*x)*(0.5*x)

class N_R:
  def __init__(self, funkcja, x, eps):
    self.f = funkcja
    self.x = x
    self.eps = eps

  def __iter__(self):
    return self
  
  def __next__(self):
    self.x = self.x - (self.f(self.x)/misc.derivative(self.f, self.x))
    if abs(self.f(self.x))<self.eps:
      raise StopIteration
    return self.x

np = N_R(fun, 1.5, 10**-5)
for el in np:
  print(el)

print("**********zadanie 3*****************")

#Xn+1 = (aXn + c) mod m, dla m = 231-1, a = 75, c = 0, x0 = 1

class Pseudo:
  def __init__(self):
    self.m = (2**31)-1
    self.a = 7**5
    self.c = 0
    self.x = 1 

  def __iter__(self):
    return self
  
  def __next__(self):
    self.x = (self.a * self.x + self.c) % self.m
    return self.x/self.m

#Korzystając z zaimplementowanego iteratora proszę wylosować 105 par liczb z przedziału [0,1). Proszę sprawdzić jaki procent wylosowanych par mieści się w kwadracie o boku 0.1*n, gdzie n∈[1,10].Otrzymany wynik proszę porównać z wynikiem uzyskiwanym z wykorzystaniem generatora liczb pseudolosowych z języka Python (5p).

ran = Pseudo()
lista = []
for j in range(10**5):
  lista.append((next(ran), next(ran)))

proc = []
for j in range(1,11):
  p = 0
  for x,y in lista:
    if x <= 0.1*j and y <= 0.1*j:
      p += 1
  p = p / len(lista)
  proc.append(p)

for x in enumerate(proc):
  print(x)

print("dla generatora liczb pseudolosowych z języka Python")

lista2 = []
for j in range(10**5):
  lista2.append((random.random(), random.random()))

proc2 = []
for j in range(1,11):
  p = 0
  for x,y in lista2:
    if x <= 0.1*j and y <= 0.1*j:
      p += 1
  p = p / len(lista2)
  proc2.append(p)

for x in enumerate(proc2):
  print(x)
