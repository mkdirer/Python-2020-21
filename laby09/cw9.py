"""łancuch dokumentacyjny 

  Wiadomość widoczna przy pomocy help 

"""
import random 
import matplotlib.pyplot as plt
import scipy.integrate as inte

print("********zadanie 1********")

def paproc(a):
  """ 
  Rysowanie paproci
  """

  listax = [random.uniform(0,1)]
  listay = [random.uniform(0,1)]

  for i in range(a):
    lenx=len(listax)
    leny=len(listay)
    w = ((0,0,0,0,0.16,0), (0.2,-0.26,0,0.23,0.22,1.6), (-0.15,0.28,0,0.26,0.24,0.44), (0.85,0.04,0,-0.04,0.85,1.6))
    mw= random.choices(w, weights=[1, 7, 7, 85])
    x=mw[0][0]*listax[lenx-1]+mw[0][1]*listay[leny-1]+mw[0][2]
    y=mw[0][3]*listax[lenx-1]+mw[0][4]*listay[leny-1]+mw[0][5]
    listax.append(x)
    listay.append(y)
  
  plt.plot(listax, listay, 'rx')
  plt.show()
  
print("********zadanie 2********")

def monte(funkcja, a, b, ybot, ytop, zm):
  """
  funkcaj zwracajaca wartosć całki metodą monte carlo
  """
  n,t=0,0
  prawdziwa_war= inte.quad(funkcja, a, b)
  wartosc=0
  while wartosc + zm < prawdziwa_war[0] or wartosc - zm > prawdziwa_war[0]:
    n +=1
    x = random.uniform(a, b)
    y= random.uniform(ybot, ytop)

    if 0<y<= funkcja(x):
      t +=1
    if 0>y>= funkcja(x):
      t -= 1
    wartosc = (b-a) * (ytop - ybot)*t/n
  print(n, wartosc)

def cw3(funkcja, a, b, zm):
  """
  monte carlo zadanie 3
  """
  n=0
  prawdziwa_war= inte.quad(funkcja, a, b)
  wartosc=0
  listax =[]
  while wartosc + zm < prawdziwa_war[0] or wartosc - zm > prawdziwa_war[0]:
    n +=1
    x = random.uniform(a, b)
    listax.append(funkcja(x))
    wartosc = (sum(listax)/len(listax)) * (b-a)
    
  print(n, wartosc)

if __name__ == '__name__':
  pass


