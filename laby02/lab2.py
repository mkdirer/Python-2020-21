
k=[1 ,2.3, '3', (5,7), [2,3,4],]
print(len(k))

print(k[0], k[len(k)-1], k[-1])

print(bool([]) , bool('a'))

a, b = 1,None
print(bool(a), bool(b))

k = [8,0,17,1,10,13,19,13,10,3,]

print(k[:])

print(k[3:6])

print(k[2:-3])
print(k[2:-3:2])
print(k[2:])
print(k[:-3])
print(k[::-1])

print("******************")

k=[1,2.3, '3', (4,7), [2,3,4],]

c=k
c[1]=[7,8,9]
print(c,k)
print(id(c),id(k))

c=k[:]
c[1]= '7,8,9'
print(c,k)
print(id(c), id(k))

c[-1][1] = '7,8,9'
print(c,k)

c=k.copy()
c[1]= '34,56,122'
print(c,k)
print(id(c), id(k))

import copy

c=copy.copy(k)
c[1]='7,8,9'
print(c,k)
print(id(c), id(k))

c[-1][1] = '7,7,7'
print(c,k)

c=copy.deepcopy(k)
c[1]='7,8,9'
print(c,k)
print(id(c), id(k))

c[-1][1] = '8,8,8'
print(c,k)

print("******************")

z = [8,0,17,1,10,13,19,13,10,3,]
print(z.count(13))
print(z.count(-13))

print(z.index(13))
#print(z.index(-13))

print(13 in z)
print(13 not in z)

if 13 in z:
  pass

z.insert(4,-13)
print(z)

z.insert(-23, 4)
z.insert(23, 4)
print(z)

z[1:4]=[7,8,9,10,]
print(z)

z[1:4] = [[7,8,],]
print(z)

print("******************")

z.remove(4)
print(z)

del z[3]
print(z)

del z[-3:]
print(z)

print(z.pop())
print(z.pop(-3))

z.clear()
print(z)

z =[1]*10
z[3]+=1

print(z)

z=[[]]*10
z[3].append(1)

print(z)

print("******************")

z=[[] for i in range(10)]
z[3].append(1)

print(z)
z[3].append([1,2,3])
print(z)
z[3].extend([1,2,3])
print(z)

print("******************")

k=[]
for i in range(10):
  k.append(i)

print(k)

k = list(range(10))
print(k)

k = list(range(3,10))
print(k)
k = list(range(3,10,2))
print(k)
k = list(range(10,0,-1))
print(k)
k = list(range(0,10,-1))
print(k)
k=[i for i in range(10)]
print(k)

print("******************")
z = [8,0,17,1,10,13,19,13,10,3,]

for i in k:
  i*=2
  print(i, end=', ')

print('\n',k)

for i in range(len(k)):
  k[i]*=2

for i,v in enumerate(k):
  k[i]=1 if v>0 else -1 #nie ma ? i :. Gdy wartośc v jest większa od zera to wstawia 1 w przecienym wypadku -1, możemy też zapisać a<v<b


print(k)

for i in k:
  if i%2:  #if not i%2: 
    #print("nowy")
    break
else:
  print('kiedy?') #to wyświetli się wtedy kiedy nigdy nie dojdzie do przewania pętli ifem, break 

print("******************")

k = [8,0,17,1,10,13,19,13,10,3,]

np = [i for i in k if i%2]
np = [1 if i>0 else -1 for i in k]

k=[(k[i], k[-i-1]) for i in range(len(k)//2)]
print(k)

for i,j in k:
  print(i,j)

print("******************")

k=[(89,34),(92,31), (96,0), (48,30), (38,10),]

c=k[:]
c.sort() #inaczej c=c.sort()
print(c)

c=k[:]
c.sort(key = lambda x: x[1])
print(c)

c=k[:]
c.sort(reverse= True) #sortowanie w odwrotnej kolejności
print(c)

c=k[:]
for i,j in sorted(k):
  print(i,j)
print(c)

print("******************")

k = [8,0,17,1,10,13,19,13,10,3,]

c=k[:]
#c.recerse()
print(c)







print("*********zadanie 1*********")

import copy
k = [8,0,17,1,10,13,19,13,10,3,]

#for i,v in enumerate(k):
  #del k[i] if v>0
l = k[:]
z = 0
for i in range(len(k)):
  if k[i]==10:
    del l[i-z]
    z+=1
    #k.remove(i)
print(k)
print(l)

print("*********zadanie 2*********")
'''
k = [8,0,17,1,10,13,19,13,10,3,]
l = copy.deepcopy(k)
z = 0
i = 0

while(i<len(k)):
    if k[i]==10:
        del l[i-z]
        #l.remove(i-z)
        z+=1
    ++i
print(k)
print(l)
'''

print("*********zadanie 3*********")

k = [8,0,17,1,10,13,19,13,10,3,]

d = len(k)

for i in range(1,d,2):
  print(k[i], end=', ')

print('\n')

print("*********zadanie 4*********")
#print(help(enumerate))
for i,v in enumerate(k):
    print(k[i], end=', ') if i%2 else None 

print('\n')

print("*********zadanie 5*********")

k = [8,0,17,1,10,13,19,13,10,3,]

d = len(k)

for i in range(d-1,0,-2):
  print(k[i], end=', ')

print('\n')

print("*********zadanie 6*********")
#print(help(enumerate))
for i,v in enumerate(k):
    print(k[abs(i-len(k))], end=', ') if i%2 else None 

print("*********zadanie 7*********")
import random
#print(help(enumerate))
l = [(i, v) for i,v in enumerate(k)]

print(l)

print("*********zadanie 8*********")
l.sort(key = lambda x: x[1])
print(l)

print("*********zadanie 9*********")
import random
#print(help(enumerate))
x = [(i, v) for i,v in enumerate(k) if v%2 == 0]
print(x)

print("*********zadanie 10*********")
x = [(i, v) for i,v in enumerate(k) if i<v]+[(v, i) for i,v in enumerate(k) if v<i]
print(x)
