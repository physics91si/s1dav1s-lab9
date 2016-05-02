#!/usr/bin/python
import sys
import math

#Python script that returns the roots of a quadratic equation
#of the form a*x^2 + b*x + c = 0
#Enter values for a, b, and c in the command line
#e.g. run: >python quadratic.py 1 2 -15
def main():
    a = sys.argv[1]
    b = sys.argv[2]
    c = sys.argv[3]
    x1, x2 = find_roots(a, b, c)
    print ("This is x1: %f" %x1)
    print ("This is x2: %f" %x2)


def find_roots(a,b,c):
    try:
        a=float(a)
        b=float(b)
        c=float(c)
        mid = b**2 - 4*a*c 
    except: 
        print "Non-numerical input"
        exit()
    try:
        sqrt_mid = math.sqrt(mid)
    except:
        print "Imaginary roots"
        exit()
    try:
        x1 = (-b + sqrt_mid)/(2*a)
    except: 
        print "a=0"
        exit()
    x2 = (-b - sqrt_mid)/(2*a)
    return x1, x2


if __name__=="__main__":
        main()
