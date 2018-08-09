# %load q01_create_class/build.py
import pandas as pd
import numpy as np
import math

'write your solution here'


class complex_number:
    '''The complex number class.

    Attributes:
    attr1 (x): Real part of complex number.
    attr2 (y): Imaginary part of complex number.
    
 

    '''
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag
    
    def __add__(self, other):
        return complex_number(self.real+other.real, self.imag+other.imag)

    def __sub__(self, other):
        return complex_number(self.real-other.real, self.imag-other.imag)
    
    def __mul__(self, other):
        return complex_number(self.real*other.real-self.imag*other.imag, self.real*other.imag+self.imag*other.real)
    
    def __truediv__(self, other):
        num1 = (self.real*other.real + other.imag*self.imag)
        deno = (other.real**2 + other.imag**2)
        num2= ((self.imag*other.real)-(self.real*other.imag))
        return ((num1/deno),(num2/deno))
        
    def abs(self):
        return math.sqrt(self.real**2 + self.imag**2)

    def argument(self):
        a=math.atan2(self.imag,self.real)
        return math.degrees(a)        
    
    def conjugate(self):
        a=self.real
        b=self.imag*(-1)
        return complex_number(a,b)
        
    def __str__(self, precision=2):
        return str(('%.'+'%df'%precision)%float(self.real))+('+' if self.imag>=0 else '-')+str(('%.'+'%df'%precision)%float(abs(self.imag)))+'i'
   
a =complex_number
print(a.__add__((5+7j),(5+7j)))



