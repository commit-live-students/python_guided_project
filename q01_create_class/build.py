# %load q01_create_class/build.py
import pandas as pd
import numpy as np
import math

'write your solution here'


class complex_number(object):
    '''The complex number class.

    Attributes:
    attr1 (x): Real part of complex number.
    attr2 (y): Imaginary part of complex number.

    '''
    
    def __init__(self,real=0.0,imag=0.0):
        self.real = real
        self.imag = imag
        
    def __str__(self):
        if self.imag < 0.0:
            return '{}-{}i'.format(self.real,abs(self.imag))
        else:
            return '{}+{}i'.format(self.real,self.imag)
    
        
    def __add__(self,other):
        c = self.real + other.real
        d = self.imag + other.imag
        return complex_number(c,d)
    
    def __sub__(self, others):
        return complex_number(self.real - others.real, self.imag - others.imag)
    
    def __mul__(self, others):
        return complex_number(self.real*others.real-self.imag*others.imag, self.real*others.imag+self.imag*others.real)
    
    def __truediv__(self,others):
        a = (self.real*others.real+self.imag*others.imag)/(others.real**2 + others.imag**2) 
        b = (self.imag*others.real-self.real*others.imag)/(others.real**2 + others.imag**2)
        return a,b                    
    
        
    def abs(self):
        return np.sqrt(np.square(self.real)+np.square(self.imag))
           
    def argument(self):
        return math.degrees(math.atan(self.real/self.imag))
        
        
    def conjugate(self):
        return complex_number(self.real, -self.imag)

d1 = complex_number(5,5)
print(d1)

d1 = complex_number(5,1)
d2 = complex_number(6,0)
print(d1 + d2)
# print(d2 - d1)
print(d2 / d1)
# print(d2 * d1)
# print(d1.conjugate())
# print(d2.conjugate())
# print(d1.abs())
# print(d2.abs())
# print(d1.argument())


