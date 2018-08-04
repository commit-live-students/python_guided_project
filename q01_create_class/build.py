# %load q01_create_class/build.py

import pandas as pd
import numpy as np
import math
class complex_number:
    '''The complex number class.

    Attributes:
    attr1 (x): Real part of complex number.
    attr2 (y): Imaginary part of complex number.

    '''
    def __init__(self,real,imag=0.0):
        self.real = real
        self.imag = imag
    def __str__(self):
        if self.imag<0:
            return '{0} - {1}',format(self.real,self.imag)
        else:
            return '{0} + {1}',format(self.real,self.imag)
        
    def __add__(self,other):
          return complex_number(self.real + other.real,self.imag + other.imag)
    
    def __sub__(self,other):
        return complex_number(self.real - other.real , self.imag - other.imag)
    
    def __mul__(self,other):
        return complex_number(self.real * other.real - other.imag * self.imag,self.imag * other.real + other.imag * self.real)
    
    def __truediv__(self, other):
        sr, si, ore, oi = self.real, self.imag,other.real, other.imag # short forms
        r = float(ore**2 + oi**2)
        return ((sr*ore+si*oi)/r, (si*ore-sr*oi)/r)
    
    def abs(self):
        return math.sqrt(self.real**2 + self.imag**2)
    
    def conjugate(self):
        return complex_number(real,-imag)
    
    def argument(self):
        return math.degrees(math.atan(self.real/self.imag))
    


        


