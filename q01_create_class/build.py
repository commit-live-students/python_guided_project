# %load q01_create_class/build.py
import pandas as pd
import numpy as np
import math

'write your solution here'


class complex_number:
    
    def __init__(self,real=0,imag=0):
        self.real=real
        self.imag=imag
        
    def __str__(self):
        if '-' in str(self.imag):
            return '{0} - {1}i'.format(self.real,self.imag)
        else:
            return '{0} + {1}i'.format(self.real,self.imag)
   
    def __add__(self,other):
        x= self.real + other.real
        y= self.imag + other.imag
        return complex_number(x,y)
        
    def __sub__(self,other):
        x= self.real - other.real
        y= self.imag - other.imag
        return complex_number(x,y)

    def __mul__(self,other):
        x= self.real*other.real - self.imag*other.imag
        y = self.real*other.imag + self.imag*other.real
        return complex_number(x,y)
    
    def __truediv__(self,other):
        x= (self.real*other.real + self.imag*other.imag) / (other.real ** 2 + other.imag **2)
        y = (other.real*self.imag - self.imag*other.imag)/(other.real ** 2 + other.imag **2)
        return (x,y)
     
    def test_conjugate(self):
        return complex_number(self.real ,self.imag)
   
    def abs(self):
        return (math.sqrt(self.real ** 2 + self.imag ** 2))
   
    def argument(self):
        return ((180/math.pi) * (math.atan(self.imag / self.real)))
        
    




