import math 
import sys  
import random

#1
print("zadanie 1")
k=20
z=[random.randrange(5*k) for i in range(k)]

print(z)

tmp = z[:]
for i in range(100):
  random.shuffle(tmp)

print(tmp)

s=0

for i in range(len(z)):
  if z[i]==tmp[i]:
    s+=1
print("Zostalo ", s, " elementów na swoich miejscach")
slo = {'ilosc': s}
print(slo)

#2
print("zadanie 2")

losowy = (''.join(chr(random.randint(97,122)) for i in range(k)))
print(losowy)
#k=len(losowy)

print(k)
x=''
for i in range(k):
  x += random.choice(losowy)
  x += '.'

print(x)

#3
print("zadanie 3")
lis = []
for i in range(100):
  lis.append(random.randint(0,20))

s1 = {}
s2 = {}

print("b)")
for i in range(10):
  s1.setdefault(lis[i], []).append(lis.index(lis[i],i))

print(s1)

print("a)")
for i in range(20):
    s2.setdefault(lis[i], []).append(z for z,v in enumerate(lis) if lis[i]==v)

print(s2)

#4
print("zadanie 4")

def ifPalindrome(a):
  a_string = str(a)
  if a_string == a_string[::1]:
    return True
  else:
    return False

n =[3,6]
lis = []
for i in range(1000):
  lis.append(random.randint(10**n[0],10**n[1]-1))

dic1={}

for i in range(1000):
    dic1={lis[i]: ifPalindrome(lis[i])}

print(dic1)

