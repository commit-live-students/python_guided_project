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
        return str(('%s+%si'))%(self.real,self.imag)
    
    #Addition of two complex numbers
    def __add__(self, other):
        return complex_number(self.real+other.real , self.imag+other.imag)
    
    
    #Subtraction of two complex numbers
    def __sub__(self, other):
        return complex_number(self.real-other.real , self.imag-other.imag)
    
    
    #Multiplication of two complex numbers
    def __mul__(self, other):
        return complex_number((self.real*other.real-self.imag*other.imag),(self.imag*other.real+self.real*other.imag))
    
    
    #Division of two complex numbers
    def __truediv__(self, other):
        return ((self.real*other.real + self.imag*other.imag)/(other.real*other.real + other.imag*other.imag),
                              (self.imag*other.real - self.imag*other.imag)/(other.real*other.real + other.imag*other.imag))

    
    #Absolute of two numbers
    def abs(self):
        return math.sqrt(self.real**2 + self.imag**2)
    
    #Conjugate of complex number
    def conjugate(self):
        return (-self.real,-self.imag)
    
    #Arg of Complex number
    def argument(self):
        return math.degrees(math.atan(self.real/self.imag))
a=complex_number(4,4)
b=complex_number(4,-3)
c=a/b
print(c)

