
import math
import sys 
import random

print("*******zadanie 1*******")
e=[]
for arg in sys.argv:
  e.append(arg)  

z=['a*x+b', 'a*x**2+b*x+c']

def ad1(k):
  li=[]
  zm = str.maketrans('abc',f'{random.randrange(10)}{random.randrange(10)}{random.randrange(10)}')
  k=k.translate(zm)
  for s in range(10):
    x=random.random()
    li.append((x,eval(k)))
  return li;

print(ad1(z[0]))
print("druga funkcja")
print(ad1(z[1]))
print("**********")
print(ad1(e[1]))
print("druga funkcja")
print(ad1(e[2]))



print("*******zadanie 2*******")
 
def ad2(*par):
  lista = []
  for i in par[0]:
    for j in par[1:]:
      if i not in j:
        break
    else:
      lista.append(i)
  return lista

print(ad2([1,2,3], (1,3,5), [3,2]))
print(ad2([1,2,3], (1,3,5), [3,2,1]))

print("*******zadanie 3*******")

def ad3(s1, s2, Flag=True):
  if Flag:
    lis = [(s1[i],s2[i]) for i in range(min(len(s2), len(s1) ))]
  else:
    lis = [(s1[i],s2[i]) if i< min(len(s2), len(s1)) else None for i in range(max(len(s2), len(s1) ))]
  return lis

print(ad3([1,2,3], (1,3,5,4), False))

print("*******zadanie 4*******")

def ad4(kwota, bank= (10,5,2)):
  k=kwota
  stop = 0
  krok = 0
  while k>0 and stop < 70 and krok<3:
    if k >= bank[krok]:
      M = int(k/bank[krok])
      k= k-bank[krok]*M
    krok= krok +1
    stop=stop +1
  print(k,krok,stop,M)

ad4(72, (10,2,1))
ad4(72)

print("*******zadanie 5*******")

def ad5(searched, range1, range2, typ='r'):
  step =1
  test = random.randrange(range1, range2) if typ=='r' else int((range1+range2)/2)
  while test != searched:
    step =step +1
    n_range1=test if test < searched else range1
    n_range2= test if test > searched else range2
    test = random.randrange(n_range1, n_range2) if typ== 'r' else(n_range1+ n_range2 // 2)
  print(f"Ilosc krokow: {step}, wartosc: {test}")

ad5(45, 19, 85, "")
ad5(45, 19, 85)
