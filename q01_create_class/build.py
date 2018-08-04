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
    def __init__(self,real,imag):
        self.real=real
        self.imag=imag
    def __str__(self):
        if self.imag<0:
            return '{0}+{1}i'.format(self.real,self.imag)
        else:
            return '{0}+{1}i'.format(self.real,self.imag)
    
    
    def __add__(self,other):
        a=self.real+other.real
        b=self.imag+other.imag
        return complex_number(a,b)
    
    def __sub__(self,other):
        a=self.real-other.real
        b=self.imag-other.imag
        return complex_number(a,b)
        
        
    def __mul__(self,other):
        a=(self.real*other.real)-(self.imag*other.imag)
        b=(self.imag*other.real)+(other.imag*self.real)
        return complex_number(a,b)
    
    def __truediv__(self,other):
        a=(self.real*other.real+self.imag*other.imag)/((other.imag**2)+(other.real**2))
        b=(self.imag*other.real-self.real*other.imag)/((other.imag**2)+(other.real**2))
        return (a,b)
    
    def abs(self):
        return (math.sqrt((self.real**2)+(self.imag**2)))
    
    def conjugate(self):
        a=self.real
        b=self.imag*(-1)
        return complex_number(a,b)
    
    def argument(self):
        a=math.atan2(self.imag,self.real)
        return math.degrees(a)
 
        
        

x=complex_number(4,4)
y=complex_number(4,-3)
print(x/y)


