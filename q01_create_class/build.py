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
    def __init__(self, real=0, imag=0):
        self.real = real
        self.imag = imag
    def __add__(self, other):
        return complex_number(self.real+other.real, self.imag+other.imag)
    def __sub__(self, other):
        return complex_number(self.real-other.real, self.imag-other.imag)
    def __mul__(self, other):
        return complex_number(self.real*other.real-self.imag*other.imag, self.real*other.imag+self.imag*other.real)
    def __truediv__(self, other):
        #r = (other.real**2 + other.imag**2)
        return ((self.real*other.real+self.imag*other.imag)/(other.real**2 + other.imag**2), (self.imag*other.real-self.imag*other.imag)/(other.real**2 + other.imag**2))
    def abs(self):
        return math.sqrt(self.real**2 + self.imag**2)
    def argument(self):
        return math.degrees(math.atan(self.real/self.imag))
    def conjugate(self):
        return complex_number(self.real,-self.imag)
    def __str__(self):
        if '-' in str(self.imag):
            return ('{0}-i{1}'.format(self.real,self.imag))
        else:
            return ('{0}+i{1}'.format(self.real,self.imag))



