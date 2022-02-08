#import list

print('Hello World!')

import keyword

print(keyword.kwlist)

import math
dir(math)
help(math.modf)

dir('')
help(''.strip)
#''.strip.__doc__

print('******************')

print(type(''))
print(type(""))

a = 7
print(type(a))

a = 1.5
print(type(a))

a = 1,1
print(type(a))
print(a)

a, b= 1,'2'
print(type(a), type(b))

a,*b=1,'2',3.,4,5
print(type(a), type(b))

print(1/2, 1//2) # // operacja całkowita
print(1./2, 1.//2)

print(2**3, pow(2,3), math.pow(2,3))
print(pow(2,3,4), pow(2,3,5)) # potęgowanie 2^3 a kolejno operacj modulo (2^3)%4

print(math.ceil(1/3), math.floor(1/3), round(1/3), round(1/3, 3))
print(math.ceil(2/3), math.floor(2/3), round(2/3), round(2/3, 3))

print(math.modf(1/3), math.modf(2.5))

print(min(2,11,3,4,2), max(2,11,3,4,2))

a=-1.7
print(abs(a), math.fabs(a))
a=-1
print(abs(a), math.fabs(a))

print('******************')

import math

print('Równanie kwadratow typu: ax^2+bx+c=0')

a = 1
b = 4
c = 4 
 
 
delta = (b*b)-(4*a*c)
 
print (delta)
 
if delta > 0:
    x1=-b-math.sqrt(delta)/(2*a)
    x2=-b+math.sqrt(delta)/(2*a)    
     
    print ("x1 = ", x1)    
    print ("x2 = ", x2)      
elif delta ==0:
        x=-b/(2*a)
        print ("x = ", x)
else:
    print ("brak miejsc zerowych")

print('******************')

k = ()
print(type(k))

k = (2)
print(type(k))

k = (2,)
print(type(k))