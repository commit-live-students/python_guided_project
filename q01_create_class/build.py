# %load q01_create_class/build.py
import pandas as pd
import numpy as np
import math

'write your solution here'

class complex_number:
    real=0
    imag=0
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag
    def __add__(self, other):
        real_sum=self.real+other.real
        imag_sum=self.imag+other.imag
        #return str(real_sum)+'+'+'i'+str(imag_sum)
        return complex_number(real_sum,imag_sum)
    def __sub__(self, other):
        real_sub=self.real-other.real
        imag_sub=self.imag-other.imag
        if imag_sub<0:
            return complex_number(real_sub,abs(imag_sub))
        return complex_number(real_sub,imag_sub)
    def __mul__(self, other):
        real_mul=self.real*other.real
        imag_mul=self.imag*other.imag
        return complex_number(self.real*other.real-self.imag*other.imag,self.real*other.imag+self.imag*other.real)
    def __truediv__(self, other):
        num1=(self.real*other.real)+(self.imag*other.imag)
        num2=(self.imag*other.real)-(self.real*other.imag)
        sum_sqr=other.real**2+other.imag**2
        real=num1/sum_sqr
        imag=num2/sum_sqr
        return real,imag
    def abs(self):
        return math.sqrt(self.real**2+self.imag**2)
    def conjugate(self):
        return complex_number(self.real,-self.imag)
    def argument(self):
        return math.degrees(math.atan(self.imag/self.real))

    
    def __str__(self):
        if self.imag>0:
            return str(self.real)+'+'+'i'+str(self.imag)
        else:
            return str(self.real)+'-'+'i'+str(abs(self.imag))




