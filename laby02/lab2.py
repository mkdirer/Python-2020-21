
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

c[-1][1] = '7,8,9'
print(c,k)

c=copy.deepcopy(k)
c[1]='7,8,9'
print(c,k)
print(id(c), id(k))

c[-1][1] = '7,8,9'
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
k = list(range(3,10,2))
k = list(range(10,0,-1))
print(k)
k = list(range(0,10,-1))
print(k)
k=[i for i in range(10)]

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

k = [8,0,17,1,10,13,19,13,10,3,]

#for i,v in enumerate(k):
  #del k[i] if v>0
d = len(k)

for i in range(1,d-1):
  if k[i]==10:
    del k[i]
    #k.remove(i)
print(k)

print("*********zadanie 2*********")
k = [8,0,17,1,10,13,19,13,10,3,]

i =1
while(i<len(k)):
  if k[i]==10:
    del k[i]
  ++i
print(k)

print("*********zadanie 3*********")

k = [8,0,17,1,10,13,19,13,10,3,]

d = len(k)

for i in range(1,d,2):
  print(k[i], end=', ')

print('\n')

print("*********zadanie 4*********")

