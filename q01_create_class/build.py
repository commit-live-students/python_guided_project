# %load q01_create_class/build.py
import pandas as pd
import numpy as np
import math

#write your solution here'


class complex_number:
#   '''The complex number class.

#   Attributes:
#   attr1 (x): Real part of complex number.
#   attr2 (y): Imaginary part of complex number.

#   '''
    def __init__(self,real,imag):
        self.real = real
        self.imag = imag
    def __add__(self,other):
        return complex_number(self.real+other.real,self.imag+other.imag)
    def __sub__(self,other):
        return complex_number(self.real-other.real,self.imag-other.imag)
    def abs(self):
        return (self.real*self.real+self.imag*self.imag)**0.5
    def conjugate(self):
        return complex_number(self.real,-(self.imag))
    def argument(self):
        return np.arctan2(self.imag,self.real)*180/np.pi
    def __mul__(self,other):
        return complex_number(self.real*other.real-self.imag*other.imag,self.real*other.imag+self.imag*other.real)
    def __truediv__(self,other):
        return ((self.real*other.real)+(self.imag*other.imag))/(other.real**2+other.imag**2),((self.imag*other.real)-(self.real*other.imag))/(other.real**2+other.imag**2)
    def __str__(self):
        if self.imag>=0:
            return ('%.2f'%(self.real))+'+'+('%.2f'%(self.imag))+'i'
        else:
            return ('%.2f'%(self.real))+('%.2f'%(self.imag))+'i'


