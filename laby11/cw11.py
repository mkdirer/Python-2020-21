import random
import math

print("********zadanie 1********")

class Automat:
  def __init__(self, N, regula, init):
    self.zm = ''
    if init:
      for i in range(N):
        self.zm += str(random.randint(0, 1))
    
    else:
      for i in range(N):
        if i == N//2:
          self.zm += '1'
        else:
          self.zm += '0'
    
    self.r = {}
    x = '{0:b}'.format(regula).zfill(8)
    self.r['111'] = x[0]
    self.r['110'] = x[1]
    self.r['101'] = x[2]
    self.r['100'] = x[3]
    self.r['011'] = x[4]
    self.r['010'] = x[5]
    self.r['001'] = x[6]
    self.r['000'] = x[7]

  def ewolucja(self, n):
    self.show(self.zm)
    for j in range(n):
      tmp = ''
      for i in range(len(self.zm)):
        if i+1 == len(self.zm):
          val = self.zm[i-1] + self.zm[i] + self.zm[0]
        else:
          val = self.zm[i-1] + self.zm[i] + self.zm[i+1]
        add = self.r[val]
        tmp += add
      self.zm = tmp
      self.show(self.zm)
  
  def show(self, fig):
    for i in fig:
      if i == '0':
        print(' ', end='')
      if i == '1':
        print('*', end='')
    print()



class Wektor:
  def __init__(self, *args):
    self.coordins = list(args)
  
  def __add__(self, inne):
    nowy = []
    for i in range(len(inne.coordins)):
      nowy.appned(self.coordins[i] + inne.coordins[i])
    return Wektor(*nowy)

  def __iadd__(self, inne):
    for i in range(len(inne.coordins)):
      self.coordins[i] += inne.coordins[i]
    return self
  
  def __sub__(self, inne):
    nowy = []
    for i in range(len(inne.coordins)):
      nowy.appned(self.coordins[i] - inne.coordins[i])
    return Wektor(*nowy)

  def __isub__(self, inne):
    for i in range(len(inne.coordins)):
      self.coordins[i] -= inne.coordins[i]
    return self

  def __mul__(self, inne):
    nowy = []
    for i in range(len(self.coordins)):
      nowy.appned(self.coordins[i] * inne)
    return Wektor(*nowy)

  __rmul__ = __mul__

  def __imul__(self, inne):
    for i in range(len(self.coordins)):
      self.coordins[i] *= inne
    return self

  def __len__(self):
    return len(self.coordins)
  
  def __getitem__(self, zm):
    return self.coordins[zm]

  def __str__(self):
    tmp = ''
    for i in self.coordins:
      tmp += str(i) + ''
    return tmp

  def __eq__(self, inne):
    for i in range(len(self.coordins)):
      if self.coordins[i] != inne.coordins[i]:
        return False
    return True
  
  def len(self):
    s = 0
    for i in range(0, len(self.coordins),2):
      s += self.coordins[i]*self.coordins[i]
    return math.sqrt(s)



if __name__ == "__main__":
  t = Automat(31, 90, False)
  t.ewolucja(16)
  t = Automat(31, 94, False)
  t.ewolucja(16)
  t = Automat(31, 182, False)
  t.ewolucja(16)

  print("********zadanie 2********")
  
  v = Wektor(1,2,3,4)
  print(v.len())
  n = Wektor(1,2,3,4)
  if v == n:
    print("takie same")
  else:
    print(v[1])
  print(n.coordins)



