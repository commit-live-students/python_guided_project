# %load q01_create_class/build.py
import pandas as pd
import numpy as np
import math

#'write your solution here'


class complex_number:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag
    def __add__(self, other):
        return complex(self.real+other.real, self.imag+other.imag)
    def __sub__(self, other):
        return complex(self.real-other.real, self.imag-other.imag)
    def __mul__(self, other):
        return complex(self.real*other.real-self.imag*other.imag, self.real*other.imag+self.imag*other.real)
    def __truediv__(self, no):
        conj = complex(no.real, no.imag*(-1))
        num = self*conj
        denom = no*conj
        realQuo = num.real/denom.real
        imaginaryQuo = num.imag/denom.real
        return (realQuo, imaginaryQuo)

    def abs(self):
        return math.sqrt(self.real**2 + self.imag**2)
    
    def conjugate(self):
        return complex(self.real, -self.imag)
    def argument(self):
        return math.degrees(math.atan(self.imag/self.real))
    



