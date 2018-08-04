# %load q01_create_class/build.py
import pandas as pd
import numpy as np
import math
from math import pow

'write your solution here'


class complex_number:
    '''The complex number class.

    Attributes:
    attr1 (x): Real part of complex number.
    attr2 (y): Imaginary part of complex number.

    '''
    def __init__(self,real,imag =0.0):
        self.real = real
        self.imag = imag
    def __str__(self):
        if self.imag<0:
            return '{0}-{1}i'.format(self.real,self.imag)
        else:
            return '{0}+{1}i'.format(self.real,self.imag)
            
        
    
    def __add__(self, num):
        return complex_number(self.real + num.real, self.imag + num.imag)
    def __sub__(self, num):
        return complex_number(self.real - num.real, self.imag - num.imag)
    
    def __mul__(self, num):
        return complex_number(self.real * num.real - self.imag * num.imag , self.imag * num.imag + self.real * num.real)
    
    def __truediv__(self, num):
        return ((self.real * num.real + self.imag * num.imag)/(num.real * num.real + num.imag*num.imag),
               (self.imag * num.real - self.imag * num.imag)/(num.real * num.real + num.imag * num.imag))
    def abs(self):
        return math.sqrt(self.real**2 + self.imag**2)
    def conjugate(self):
        return complex_number(self.real , -self.imag)
    def argument(self):
        return math.degrees(math.atan(self.real/self.imag))
 

a = complex_number(4,4)
b = complex_number(4,-3)

c = complex_number(4,4)
d = complex_number(4,-3)






