import pandas as pd
import numpy as np
import math

class complex_numbers():

    def __init__(self,real,imag):
        self.real = real
        self.imag = imag

    def __add__(self,other):
        return complex_numbers(self.real + other.real, self.imag + other.imag)

    def __sub__(self,other):
        return complex_numbers(self.real - other.real, self.imag - other.imag)

    def __mul__(self,other):
        r = self.real * other.real - self.imag * other.imag
        i = self.imag * other.real + self.real * other.imag
        return complex_numbers(r,i)

    def __truediv__(self,other):
        denom =((other.real*other.real)+(other.imag*other.imag))
        conjugate = complex_numbers(other.real, -1*other.imag)
        num = self * conjugate
        return (num.real/denom,num.imag/denom)

    def abs(self):
        return math.sqrt(self.real ** 2 + self.imag ** 2)

    def argument(self):
        return math.degrees(np.arctan(self.imag/self.real))
