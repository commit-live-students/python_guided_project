# %load q01_create_class/build.py
import pandas as pd
import numpy as np
import math


class complex_number:
    def __init__(self, real, imag=0.0):
        self.real = real
        self.imag = imag
        
    def __str__(self):
        if '-' in str(self.imag):
            return '{0}-i{1}'.format(self.real, abs(self.imag))
        else:
            return '{0}+i{1}'.format(self.real, abs(self.imag))
        
    def __add__(self, other):
        return complex_number(self.real + other.real,
                              self.imag + other.imag)
    
    def __sub__(self, other):
        return complex_number(self.real - other.real,
                              self.imag - other.imag)
    
    def __mul__(self, other):
        return complex_number(self.real*other.real - self.imag*other.imag,
                              self.imag*other.real + self.real*other.imag)
    
    def __truediv__(self, other):
        return (self.real*other.real+self.imag*other.imag)/(other.real**2+other.imag**2),(self.imag*other.real-self.real*other.imag)/(other.real**2+other.imag**2)
    
    def abs(self):
        return (self.real**2 + self.imag**2)**0.5
    
    def conjugate(self):
        return (self.real-other.imag)
    
    def argument(self):
        return (math.degrees(math.atan(self.imag/self.real)))
    
    '''The complex number class.

    Attributes:
    attr1 (real): Real part of complex number.
    attr2 (imag): Imaginary part of complex number.

    '''





