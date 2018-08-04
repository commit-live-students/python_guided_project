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
    def __init__(self, real, imag=0.0):
        self.real = real
        self.imag = imag
        
        
    def __add__(self, other):
        return complex_number(self.real + other.real,
                       self.imag + other.imag)
    def __sub__(self, other):
        return complex_number(self.real - other.real,
                       self.imag - other.imag)

    def __mul__(self, other):
        return complex_number(self.real*other.real - self.imag*other.imag,
                       self.imag*other.real + self.real*other.imag)
    
    def __truediv__(first, second):
        if second.real*second.real + second.imag*second.imag != 0:
            return ((first.real*second.real + first.imag*second.imag) / (second.real*
                        second.real + second.imag*second.imag),
                    (first.imag*second.real - first.real*second.imag) / (second.real*
                        second.real + second.imag*second.imag))

    
    def abs(self):
        return math.sqrt(self.real**2 + self.imag**2)
    
    def conjugate(self):
        return complex_number(self.real, -self.imag)
    
    def argument(self):
        return math.degrees(math.atan(self.real/self.imag))

