import math
import sys

#*************zadanie1************
print("***********zadanie1**************")
if len(sys.argv) < 2:
  print("Proszę podac argumenty")
else:
  pobrane = ''.join(sys.argv[1:])
  print(pobrane)
  
#*************zadanie2*************
print("***********zadanie2**************")
male = [z for z in pobrane if z.islower()]
print("Male: ", male)
duze = [z for z in pobrane if z.isupper()]
print("Duze: ",duze)
cyfry = [int(z) for z in pobrane if z.isnumeric()]
print("Cyfry: ",cyfry)
reszta = [z for z in pobrane if not z.isalnum()]
print("Inne: ", reszta)

#*************zadanie3*************
print("***********zadanie3**************")
powt = []
for z in male:
  if z not in powt:
    powt.append(z)
print("Powtorzenia malych: ", powt)

lis = [(z, male.count(z)) for z in powt]
print("Lista krotek (mala litera, krotność jej wystąpienia w liście oryginalnej): ",lis)

#*************zadanie4*************
print("***********zadanie4**************")
lis.sort(key = lambda x: x[1])
print("Posortowana lista krotek: ", lis)

#************zadanie5**************
print("***********zadanie5**************")

sam = ('a', 'e', 'i','o','u','y','A','E','I','O','U','Y')

a = sum(pobrane.count(z) for z in sam)

b= len(pobrane) - a

print("Parametry prostej a i b: ",a,b)
lista = [(z, a*z+b) for z in cyfry]
print("Lista: ",lista)

#***********zadanie6**************
print("***********zadanie6**************")

xsr= sum(cyfry) / len(cyfry)
ysr= sum([y for x,y in lista]) / len(lista)
print("Srednie: ", xsr, ysr)
D = sum([((x-xsr) **2) for x in cyfry])
print("Parametr D: ", D)
a= (1/D)*sum([(y*(x-xsr)) for x,y in lista])
print("Parametr a: ",a)
b = ysr - a*xsr
print("Parametr b: ",b)




