from time import time_ns 
from sys import version
from random import uniform
import math
import functools

print("***********zadanie 1*********")

powt=1000
N=10000

def forStatement():
  z=[]
  sum =0
  for i in range(N):
    z.append(i**2)
  return z

def listComprehension():
  z = [i**2 for i in range(N)]
  return z

def mapFunction():
  z = map(lambda i: i**2, range(N))
  return z

def generatorExpression():
  z = (i**2 for i in range(N))
  return z

# zamiana funkcji tester

def tester(funkcja):
  czas = time_ns()
  for _ in range(powt):
    sum=0
    for i in funkcja():
      sum = sum + i
  return abs(time_ns() - czas)

'''
def tester(funcja):
  czas = time_ns()
  for i in range(powt):
    funcja()
  return abs(time_ns() - czas)
'''

print(version)
test=(forStatement, listComprehension, mapFunction, generatorExpression)
for testFunction in test:
    print(testFunction.__name__.ljust(20), '=>', tester(testFunction))

'''
#dodawanie elementu
3.8.8 (default, Feb 20 2021, 21:09:14) 
[GCC 7.5.0]
forStatement         => 2546485326
listComprehension    => 1169330949
mapFunction          => 1060689
generatorExpression  => 1156415

#dodawanie elementu podniesionego do kwadratu #zamiast i to i**2
3.8.8 (default, Feb 20 2021, 21:09:14) 
[GCC 7.5.0]
forStatement         => 9043256484
listComprehension    => 7617821790
mapFunction          => 1600369
generatorExpression  => 1421562

#sumowanie elementów z wykorzystaniem pętli for
3.8.8 (default, Feb 20 2021, 21:09:14) 
[GCC 7.5.0]
forStatement         => 12724339231
listComprehension    => 9293993540
mapFunction          => 12419878552
generatorExpression  => 10531425678

'''


print("***********zadanie 2*********")

def calka(funkcja, range1, range2, n):
  d = (range1 - range2)/n
  k=[]
  for i in range(n):
    if i==0:
      k.append(0)
    else:
      k.append(round(k[i-1] + d, 2))
  
  p = map(lambda x: eval(funkcja), k)
  sum = 0 
  for el in p:
    sum += round(el*d,2)
  
  print(sum)

calka('x**2', 0, 5, 50)

print("***********zadanie 3*********")

pkt = [uniform(-1,1)**2 + uniform(-1,1)**2 for _ in range(100000)]
print(len(list(filter(lambda x: x<=1, pkt)))*4/100000)

print("***********zadanie 4*********")

Ma = [[1,2,3,4], [5,6,7,8], [9,10,11,12]]
Mb = [[1,2,3,4], [5,6,7,8], [9,10,11,12]]

print(set(map(lambda x: max(x), Ma)))
print(set(map(lambda x: max(x), zip(*Ma))))
print([list(map(sum, zip(*x))) for x in zip(Ma, Mb)])

print("***********zadanie 5*********")

def fun5(listax, listay):
  lista = zip(listax, listay)
  srx = functools.reduce(lambda x,y: x+y, listax)/len(listax)
  sry = functools.reduce(lambda x,y: x+y, listay)/len(listay)
  D = functools.reduce(lambda x,y: x+y, map(lambda x: (x-srx)**2, listax))
  a = functools.reduce(lambda x,y: x+y, map(lambda x,y: y*(x-srx), listax, listay))/D
  b= sry - a*srx
  deltay = math.sqrt(functools.reduce(lambda x,y: x+y, map(lambda x, y: y-(a*x)+b, listax, listay))/len(listax))
  deltaa = deltay/math.sqrt(D)
  deltab = deltay*math.sqrt(1/len(listay) + srx**2/D)

  return a, b,  deltaa, deltab 

print(fun5([1,3,4,5],[2,5,7,8]))
  



