# %load q01_create_class/build.py
import pandas as pd
import numpy as np
import math

'write your solution here'


class complex_number:
        
    def __init__(self, real = 0, imag = 0):
        self.real = real
        self.imag = imag
    
    def __str__(self):
        if '-' in str(self.imag):
            return '{0}-{1}i'.format(self.real,-self.imag)
        else:
            return '{0}+{1}i'.format(self.real,self.imag)
    
    def __add__(self, other):
        x = (self.real + other.real) 
        y = self.imag +  other.imag
        
        return complex_number(x,y)
    
    
    def __sub__(self, other):
        x = self.real - other.real
        y = self.imag -  other.imag
        return complex_number(x,y)
    
    def __mul__(self, other):
        x = (self.real * other.real) - (self.imag * other.imag)
        y = (self.imag * other.real) + (self.real * other.imag)
        return complex_number(x,y)
    
    def __truediv__(self, other):
        
        x = ((self.real * other.real) + (self.imag * other.imag))/((other.real * other.real) + (other.imag * other.imag))
        y = ((self.imag * other.real) - (self.real * other.imag))/((other.real * other.real) + (other.imag * other.imag))
        
       
        return x,y
    
    def abs(self):
        
        return (self.real * self.imag + self.imag * self.imag)**0.5
    
    def conjugate(self):
        
        return self.__class__(self.real, -self.imag)
    
    def argument(self):
        return math.degrees(math.atan(self.real / self.imag))





