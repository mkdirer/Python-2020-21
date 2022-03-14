
from datetime import date


print("***********zadanie 1**********")

class Blad(Exception):
  print(Exception)
  pass

def cw1(psl, data, mk):
  pesel=[]
  l=[1,3,7,9,1,3,7,9,1,3]
  zm =0
  try:
    for i in psl:
      pesel.append(int(i))
  except ValueError:
    print("powinien składać sie z samych liczb")
  else:
    for i in range(10):
      zm= zm+pesel[i]*l[i]
    zm=zm%10
    zm=10-zm
    zm=zm%10

    k=0
    while pesel[2]>1:
      pesel[2]=pesel[2]-2
      k=k+1
    r=1900
    if k!=4:
      for i in range(k):
        r+=100
    else:
      r-=100
    
    r+=pesel[1]
    r+=pesel[0]*10
    m=pesel[2]*10+pesel[3]
    d=pesel[4]*10+pesel[5]

    if r!=data.year or m!=data.month or d != data.day:
      raise Blad("Zla data")
    if pesel[9]%2==0:
      if mk=='mezczyzna':
        raise Blad("Nie ta pelc")
    else:
      if mk=='kobieta':
        raise Blad("Nie ta pelc")

    if zm!=pesel[10]:
      raise Blad("Zla suma kontrolna")
    print("pesel ok")


data=date(1997, 2, 21)
pesel= '97022124323'
plec='kobieta'

cw1(pesel, data, plec)

'''
print("***********zadanie 2**********")
def cw2(file):
  ave= []
  with open(file, "r") as y:
    for line in y:
      col = line.split
      if len(col) < 3:
        raise Exception
      if col[0].isdigit() is False or col[1].isdigit() is False or col[2].isdigit() is False:
        raise Exception
      date(col[2], col[1], col[0])
      
'''

print("***********zadanie 3**********")


def zad3(lista, n):
  if not len(lista) %n:
    raise Exception("złe elementy listy")
  for i in range(0, len(lista) - n, n):
    try:
      if max(lista[i:i+n]) != lista[i +n-1]:
        raise Exception(" zły ostatni element w "+ str(lista[i: i+n]))
    except Exception as Bl:
        print(Bl)
    else:
        odd =0
        for j in lista[i: i+n]:
          if j% 2==0:
            odd=odd+1
        print(str(lista[i: i+num]), sum(el * el for el in lista[i:i+n-1]), lista[i+n-1]* lista[i+n-1] )
        if sum(el * el for el in lista[i:i+n-1])== lista[i+n-1]* lista[i+n-1]:
          print(lista[i+n-1] + " to trójka pitagorejska parzyste" + str( odd)+ " nieparzyste" + str(n - odd))


l=(3,4,5,5,12,13,7,24,25,9,40,41,6,8,10,60,80,100,18,24,30,15,8,17)
try:
  cw3(l, 3)
except Exception as Bl:
    print(Bl)
