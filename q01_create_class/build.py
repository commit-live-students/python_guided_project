# %load q01_create_class/build.py
import pandas as pd
import numpy as np
import math

'write your solution here'


class complex_number:
    '''The complex number class.

    Attributes:
    attr1 (x): Real part of complex number.
    attr2 (y): Imaginary part of complex number.'''
    def __init__(self,real,imag):
        self.real= real
        self.imag=imag
    def __add__(self,another_complex):
        a=self.real + another_complex.real
        b=self.imag + another_complex.imag
        c=complex_number(a,b)
        return c
#     def __repr__(self):
#         return str(self.real)+ ' + ' + str(self.imag)+'i'
#         return (self.real,self.imag)
    def __sub__(self,another_complex):
        a=self.real - another_complex.real
        b=self.imag - another_complex.imag
        c=complex_number(a,b)
        return c
    def __mul__(self,another_complex):
        a=self.real * another_complex.real - self.imag*another_complex.imag
        b=self.real * another_complex.imag + self.imag*another_complex.real
        c=complex_number(a,b)
        return c
    def __truediv__(self,another_complex):
        a=((self.real*another_complex.real)+(self.imag*another_complex.imag))/(another_complex.real**2 + another_complex.imag**2)
        b=((self.imag*another_complex.real)-(self.real*another_complex.imag))/(another_complex.real**2 + another_complex.imag**2)
        c=complex_number(a,b)
        return a,b
    def abs(self):
        return (self.real**2 + self.imag**2)**0.5
    def argument(self):
        return math.degrees(math.atan(self.imag/self.real))

a=complex_number(2,3)

b=complex_number(4,5)
b
a/b
c=a+b
c.imag
a.argument()


