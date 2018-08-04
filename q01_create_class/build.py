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

    def __str__(self):
        return '%s+%si' %(self.real, self.imag)

    def __add__(self, other):
        real_result = self.real + other.real
        imaginary_result = self.imag + other.imag
        return complex_number(real_result, imaginary_result)

    def __sub__(self, other):
        real_result = self.real - other.real
        imaginary_result = self.imag - other.imag
        return complex_number(real_result, imaginary_result)

    def __mul__(self, other):
        r1 = self.real * other.real
        r2 = self.real * other.imag
        r3 = self.imag * other.real
        r4 = self.imag * other.imag 
        real = r1 + (r4*(-1))
        imaginary = r2 + r3
        return complex_number(real, imaginary)

    def __truediv__(self, other):
         #(a+bi)/(c+di)=(ac+bd)/c2+d2 + i(bcâad )/ c2+d2
        num1 = ((self.real*other.real)+(self.imag*other.imag))
        deno = (other.real**2) + (other.imag**2)
        num2 = ((self.imag*other.real)-(self.real*other.imag))
        return num1/deno,num2/deno
    
    def abs(self):
        return math.sqrt(self.real**2+self.imag**2)

    def conjugate(self):
        return self.real+ -self.imag

    def argument(self):
        result= math.degrees(math.atan(self.imag/self.real))
        return result
a = complex_number(4,4)
b = complex_number(4,-3)

c = complex_number(4,4)
d = complex_number(4,-3)



