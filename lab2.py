import math
from math import *
x = 0.1 # начало отрезка а
z = 1.2 # начало отрезка b
while x < z:
    x += 0.05
    y = sin(4**x-log(3**x,math.e))
    print(y)
