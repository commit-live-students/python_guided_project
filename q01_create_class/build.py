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
    
    def __init__(self,real=0,imag=0):
        self.real = real
        self.imag = imag     
    
    #Override addiction of complex numbers
    def __add__(self,other):
        real = self.real + other.real
        imag = self.imag + other.imag
        return complex_number(real,imag)
    
    #Override substraction of complex numbers
    def __sub__(self,other):
        real = self.real - other.real
        imag = self.imag - other.imag
        return complex_number(real,imag)

    #Override multiplication of complex numbers
    def __mul__(self,other):
        real = ((self.real * other.real) - (self.imag * other.imag))
        imag = ((self.imag * other.real) + (self.real * other.imag))
        return complex_number(real,imag)

    #Override division of complex numbers
    def __truediv__(self,other):
        real = ((self.real * other.real) + (self.imag * other.imag))/(other.real**2 + other.imag**2)
        imag = ((self.imag * other.real) - (self.real * other.imag))/(other.real**2 + other.imag**2)
        return real,imag

    #Conjugate complex numbers
    def conjugate(self):
        real = self.real
        imag = (-1)*self.imag
        return complex_number(real,imag)
    
    #Argument complex numbers
    def argument(self):
        real = math.degrees(np.arctan(self.imag/self.real))  
        return real
    
    #Absolute complex numbers
    def abs(self):
        z = (self.real**2 + self.imag**2)**(1/2)
        return z   
    
    #Magic function
    def __str__(self):
        if self.imag < 0:
            return ('{} - {}i'.format(self.real,self.imag*(-1)))
        else:
            return ('{} + {}i'.format(self.real,self.imag)) 
a = complex_number(4,4)
b = complex_number(4,-3)
print('1st Complex Number {}'.format(a))
print('2nd Complex Number {}'.format(b))
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a.conjugate())
print(a.argument())
print(a.abs())


