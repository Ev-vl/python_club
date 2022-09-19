#типизация
from math import pi
from re import A
import sys

print(4 * '7')
#input(4 + '7') # нельзя
print(4 + True) # True == 1
print(pi)

a = 3
b = 3
print(a == b)
print(a is b) #проврека на ссылку объекта, в данном случае 1, тоже самое: id(a) == id(b)

a = 1
b = 1

print(a is b)#True

a = 500
b = 500
print('1:',a is b)#false

#Всё из-за того, что спецсимволы, числа после 256 не кешируются

#a = sys.intern(500)
#b = sys.intern(500)

#print(a is b)

a = 'jello'
a = "über"
