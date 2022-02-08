import sys
sys.path.append('build/lib.linux-x86_64-3.8')
import mod
import random 

def sort(val):
  for _ in range(len(val)):
    for i in range(len(val)-1):
      if val[i] > val[i+1]:
        tmp = val[i]
        val[i] = val[i+1]
        val[i+1] = tmp


print(mod.met(1,2))
print(mod.met(1,2,5))
print(mod.met(1,2,5,[2,3,4]))


t1 = [random.randint(0,6) for _ in range(10)]
t2 = t1[:]
mod.sort(t1)
sort(t2)
print(t1)
print(t2)