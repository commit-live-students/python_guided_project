import pandas as pd
import numpy as np
import math



class complex_number:
    def __init__(self,real,imag):
        self.real=real
        self.imag=imag
    
    def __str__(self):
        return '{:d}{:+d}j'.format(self.real,self.imag)
    
    def __add__(self,other):
        return complex_number((self.real+other.real),(self.imag+other.imag))
    
    def __sub__(self,other):
        return complex_number((self.real-other.real),(self.imag-other.imag))
    
    def __mul__(self,other):
        real=((self.real*other.real)-(self.imag*other.imag))
        imag=((self.real*other.imag)+(self.imag*other.real))
        return complex_number(real,imag)
    
    def __truediv__(self,other):
        
        real=((self.real*other.real)+(self.imag*other.imag))/(other.real**2+other.imag**2)         
        imag=((self.imag*other.real)-(self.real*other.imag))/(other.real**2+other.imag**2)
        return (real,imag)
    
    def abs(self):
        return math.sqrt(self.real**2+self.imag**2)
    
    def conjugate(self):
        return complex_number(self.real,-(self.imag))
    
    def argument(self):
        return math.degrees(math.atan(self.imag/self.real))
        


