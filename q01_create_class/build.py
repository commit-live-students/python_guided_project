import pandas as pd
import numpy as np
import math

"write your solution here"
class complex_numbers:
    def __init__(self,x,y):
        self.real = x
        self.imag = y

    def real(self):
        return self.real

    def imag(self):
        return self.imag

    def conjugate(self):
        return complex_numbers(self.real,self.imag*-1)

    def argument(self):
        return math.degrees(math.atan(self.imag/float(self.real)))

    def __str__(self):
        a = self.real
        b = self.imag
        if b > 0:
            return "{} + {}i".format(a,b)

        else:
            return "{} - {}i".format(a,-1*b)

    def __add__(self,ob):
        a = self.real
        b = self.imag

        c = ob.real
        d = ob.imag

        return complex_numbers((a+c),(b+d))

    def __sub__(self,ob):
        a = self.real
        b = self.imag

        c = ob.real
        d = ob.imag

        return complex_numbers((a-c),(b-d))

    def __mul__(self,ob):
        a = self.real
        b = self.imag

        c = ob.real
        d = ob.imag

        rt = a*c - b*d
        ct = a*d + b*c

        return complex_numbers(rt,ct)

    def __truediv__(self,ob):
        a = self.real
        b = self.imag

        c = ob.real
        d = ob.imag

        den = c*c + d*d
        numr = a*c + b*d
        numi = b*c - a*d
        rt = numr/den
        ct = numi/den

        return(rt,ct)

    def abs(self):
        a = float(self.real)
        b = float(self.imag)
        sq = a*a + b*b
        return math.sqrt(sq)
