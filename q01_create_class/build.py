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
#     attr1 = 0
#     attr2 = 0 
    def __init__(self, real = 0, imag = 0):
        self.real = real
        self.imag = imag
    
    def __add__(self,other):
        real = self.real + other.real
        imag = self.imag + other.imag
        return complex(real,imag)
    
    def __sub__(self,other):
        real = self.real - other.real
        imag = self.imag - other.imag
        return complex(real,imag)
    
    def __mul__(self,other):
        real_part = ((self.real*other.real)-(self.imag*other.imag))
        complex_part = ((self.imag*other.real)+(self.real*other.imag))   
        return complex(real_part,complex_part)
    
    def __truediv__(self,other):
        real_part = ((self.real*other.real)+(self.imag*other.imag))
        complex_part = ((self.imag*other.real)-(self.real*other.imag))   
        divisor = ((other.real*other.real)+(other.imag*other.imag))
        return (real_part/divisor),(complex_part/divisor)
    
    def abs(self):
        sum_of_squares = (self.real*self.real)+(self.imag*self.imag)
        return math.sqrt(sum_of_squares)
    
#     def abs(self):
#         return math.sqrt((self.x*self.x)+(self.y*self.y))
    
    def conjugate(self):
        return complex(self,other.real,-self.imag)
    
    def argument(self):
        return math.degrees(math.atan(self.real/self.imag))
    



