

print("********zadanie 1********")

def cw1(file, n):
  with open(file) as plik:
    z=plik.readlines()
  print(z[:n])
  print(z[-n:])
  print(z[::n])
  print([li.split(" ")[n-1] for li in z])
  print([li[n-1] for li in z])

cw1("rank/2000.txt", 2)

print("********zadanie 2********")

import numpy
import glob

def cw2():
  files = glob.glob('data*')
  x=[]
  for file in files:
    with open(file) as f:
      x.append(f.readlines())

  with open('data.out', 'w') as f:
    for i in range(len(x[0])):
      numb=[]
      for j in range(len(files)):
        numb.append(float(x[j][i]))
      f.write(f'{i} {numpy.average(numb)} {numpy.std(numb)}\n')

cw2()


print("********zadanie 3********")

def cw3():
  files = ['data0.in', 'data1.in', 'data2.in', 'data3.in', 'data4.in', 'data5.in']
  with open('zad3.out', 'w') as plik:
    plik.write("""
  files = ['data0.in', 'data1.in', 'data2.in', 'data3.in', 'data4.in', 'data5.in']
  import matplotlib.pyplot as print
  import numpy
  for file in files:
    x=[z for z in range(1,51)]
    y = numpy.loadtxt(file, unpack=True)
    dy=numpy.std(y)
    plt.plot(x,y,'o')
    plt.errorbar(x,y,marker = '*', yerr=dy)
    plt.savefig('{}.pdf'.format(file.split('.')[0]))
    plt.clf()
    """)

cw3()
  
print("********zadanie 4********")


