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
        
    def __add__(self,other):
        return complex_number(self.real + other.real, self.imag + other.imag)

    def __sub__(self,other):
        return complex_number(self.real - other.real, self.imag - other.imag)

    def __mul__(self,other):
        return complex_number(self.real * other.real-self.imag * other.imag, self.real*other.imag+self.imag*other.real)

    def abs(self):
        return math.sqrt((self.real**2+self.imag**2))

    def __conjugate__(self):
        return complex_number(self.real , -1*self.imag )
    
    def argument(self):
        if(self.real>0):
            return math.degrees(math.atan2(self.imag, self.real))
        elif(self.real<0 and self.imag>=0):
            return math.degrees(math.atan2(self.imag, self.real)+math.radians(180))
        elif(self.real<0 and self.imag<0):
            return math.degrees(math.atan2(self.imag, self.real)-math.radians(180))
        elif(self.real==0 and self.imag>0):
            return math.degrees(math.atan2(self.imag, self.real)+math.radians(90))
        elif(self.real==0 and self.imag<0):
            return math.degrees(math.atan2(self.imag, self.real)-math.radians(90))
        else:
            return 'NA'
    
        
    def __truediv__(self,other):
        x=other.__conjugate__()
        n=self*x
        d=other*x
        return (n.real / d.real, n.imag / d.real)

