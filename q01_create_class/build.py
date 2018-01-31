import pandas as pd
import numpy as np
import math

#"write your solution here"
class complex_numbers:
    def __init__(self,r,i):
        self.real = r
        self.imag = i
    def __str__(self):
        return ((self.real[0]) + "+" + str(self.imag[0]) + "i")

    def __add__(self,another_num):
        return complex_numbers(self.real + another_num.real,self.imag + another_num.imag)

    def __sub__(self,another_num):
        return complex_numbers(self.real - another_num.real,self.imag - another_num.imag)
    def __mul__(self,another_num):
        return complex_numbers((self.real*another_num.real)-(self.imag*another_num.imag),(self.real*another_num.imag)+(self.imag*another_num.real))
    def __truediv__(self,another_num):
        return (0,1)
    def abs(self):
        return math.sqrt(math.pow(self.real,2)+math.pow(self.imag,2))
    def real(self):
        return self.real
    def imag(self):
        return self.imag
    def argument(self):
        a = math.degrees(math.atan(self.imag/self.real))
        return a
    def conjugate(self):
        return complex_numbers(self.real,-1*self.imag)
