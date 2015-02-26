import math, os, sys
x=int(raw_input("Select number: "))

r= math.factorial(x-1)+1

v = r % x
if (v == 0):
    print "Prime"

else:
    print "Not Prime"
