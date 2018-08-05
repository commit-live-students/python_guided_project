# %load q01_create_class/build.py
import pandas as pd
import numpy as np
import math as mt

'write your solution here'


class complex_number:
    '''The complex number class.

    Attributes:
    attr1 (x): Real part of complex number.
    attr2 (y): Imaginary part of complex number.

    '''


class complex_number:
    def __init__(self, a, b):
        self.real=a
        self.imag=b
    
    def __str__(self):
        return '%s + i%s' % (self.real, self.imag) 
        
    def __add__(self,rhs):
        new_a = self.real + rhs.real
        new_b = self.imag + rhs.imag
        return complex_number(new_a,new_b)
    
    def __sub__(self,rhs):
        new_a = self.real - rhs.real
        new_b = self.imag - rhs.imag
        return complex_number(new_a,new_b)
    
    def __mul__(self,rhs):
        new_a = (self.real * rhs.real) - (self.imag * rhs.imag)
        new_b = (self.imag * rhs.real) + (self.real * rhs.imag)
        return complex_number(new_a,new_b)

    def __truediv__(self,rhs):
        new_a = (self.real * rhs.real) + (self.imag * rhs.imag)
        new_b = (self.imag * rhs.real) - (self.real * rhs.imag)
        den  = rhs.real**2 + rhs.imag**2
        real = new_a/den
        imag = new_b/den
        return (real,imag)
    
    def abs(self):
        return mt.sqrt(self.real**2+self.imag**2)
    
    def conjugate(self):
        return complex_number(self.imag,self.real)

    def argument(self):
        return mt.degrees(mt.atan(self.real/self.imag))


