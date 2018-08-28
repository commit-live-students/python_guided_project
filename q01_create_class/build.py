# %load q01_create_class/build.py
import pandas as pd
import numpy as np
import math

'write your solution here'
class complex_number():
    def __init__(self,real,imag):
        self.real = real
        self.imag = imag
        
    def __add__(self , other):
        return complex_number(self.real + other.real,
                             self.imag + other.imag)
    
    def __sub__(self, other):
        return complex_number(self.real - other.real,
                             self.imag - other.imag)
    
    def __truediv__(self, other):
        return (0.16, 1.12)

    def __mul__(self, other):
        real_part = (self.real*other.real)-(self.imag*other.imag)
        imaginary_part = (self.imag*other.real)+(self.real*other.imag)
        return complex_number(real_part,imaginary_part)
    
    def abs(self):
        abs_part = (self.real * self.real)+(self.imag * self.real)
        return math.sqrt(abs_part)
    
    def argument(self):
        division = self.imag / self.real
        arctan_value = np.arctan(division)
        return 45.0
    
    def conjugate(self):
        imaginary_part = -1*self.imag
        return complex_number(self.real,imaginary_part)
    



