import random 
import math

print("***********zadanie 1********")

def fibonaci():
  a,b =0,1
  yield a
  yield b
  while True:
    a,b=b,a+b
    yield b

def parz(ciag,b="nie"):
  for i in ciag:
    if b=="nie" and not i%2:
      yield i
    if b=="parz" and i%2:
      yield i

def mniejszy(ciag, n):
  for x in ciag:
    if x>n:
      break
    yield x 

print("nie parzyste: ", sum(mniejszy(parz(fibonaci()), 100)))
print("parzyste: ", sum(mniejszy(parz(fibonaci(), "parz"), 100)))

print("***********zadanie 2********")

def range2(a, b=None, krok=1.):
  a=float(a)
  if b==None:
    a,b=0.,a
  while True:
    if krok>0 and a>=b:
      break
    if krok<0 and a<=b:
      break
    if krok==0:
      break
    yield a
    a += krok

r = (range(10), range(-10), range(1,10), range(10,1), range(1,10,2), range(1,10,-2), range(10,1,2), range(10,1,-2))
r2 =(range2(10), range2(-10), range2(1,10), range2(10,1), range2(1,10,2), range2(1,10,-2), range2(10,1,2), range2(10,1,-2))

print("range: ")
for i in r[7]:
  print(i)
print("range2: ")
for i in r2[7]:
  print(i)

print("***********zadanie 3********")

def pascal():
  a=[1]
  yield sum(a),a
  while True:
    lista=[]
    k=0
    for i in a:
      lista.append(k+i)
      k=i
    lista.append(1)
    a=lista
    yield sum(a), a

zm=pascal()
for _ in range(10):
  print(next(zm))

print("***********zadanie 4********")

def Sin(a):
  n,wartosc = 0,0
  while True:
    wartosc+=(((-1)**n)/(math.factorial(1+2*n)))*(a**(1+2*n))
    n+=1
    yield wartosc,n

zm=Sin(3)
while math.fabs(math.sin(3)-next(zm)[0])>1e-8:
  next(zm)
print(next(zm))

print("***********zadanie 5********")

N=100
rand01=[random.choice([0,1]) for i in range(N)]

def zeros(ciag):
  k=0
  for i in ciag:
    if i==0:
      k += 1
    else:
      yield k
      k=0

sum=0
k=0
for i in zeros(rand01):
  sum += i
  k += 1
print("Srednia odleglosc: ", sum/k)