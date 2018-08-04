# %load q01_create_class/build.py
import pandas as pd
import numpy as np
import math

class complex_number(object):
    def __init__(self, real, imag=1.0):
        self.real = real
        self.imag = imag
        #self.abs = math.sqrt(self.real**2 + self.imag**2)
        #self.argument = math.tan(self.imag/self.real)


    def __add__(self, other):
        return complex_number(self.real + other.real,
                       self.imag + other.imag)
    
    def __sub__(self, other):
        return complex_number(self.real - other.real,self.imag - other.imag)
    
    def __mul__(self, other):
        return complex_number(self.real*other.real - self.imag*other.imag,
                       self.imag*other.real + self.real*other.imag)
    
    def __truediv__(self, other):
        return((self.real * other.real+ self.imag * other.imag)/(other.real*other.real +other.imag*other.imag),
               (self.imag * other.real- self.imag * other.imag)/(other.real*other.real +other.imag*other.imag))
    
    
    def argument(self):
        return math.degrees(math.atan(self.real/self.imag))

    
    def abs(self):
        return math.sqrt(self.real**2 + self.imag**2)
    
    def __neg__(self):   # defines -c (c is Complex)
        return complex_number(self.real, -self.imag)

    def __eq__(self, other):
        return self.real == other.real and self.imag == other.imag

    def __ne__(self, other):
        return not self.__eq__(other)
    
    def __str__(self):
        return '(%g, %gj)' % (self.real, self.imag)
    
    def __repr__(self):
        return 'Complex' + str(self)

    def __pow__(self, power):
        raise NotImplementedError
    
other1= complex_number(4,4)
other2= complex_number(4,-3)




