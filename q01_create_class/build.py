# %load q01_create_class/build.py
import pandas as pd
import numpy as np
import math

'write your solution here'


class complex_number:
    
    def __init__(self, x, y):
        self.real = x
        self.imag = y
        
    def __str__(self):
        operator = '+'
        if self.imag < 0:
            operator = '-'
        return '%.2f %s %.2fi'%(self.real, operator, abs(self.imag))
    
    def __add__(self, other):
        new_x = self.real + other.real
        new_y = self.imag + other.imag
        return complex_number(new_x, new_y)
    
    def __sub__(self, other):
        new_x = self.real - other.real
        new_y = self.imag - other.imag
        return complex_number(new_x, new_y)
    
    def __mul__(self, other):
        new_x = (self.real * other.real) - (self.imag * other.imag)
        new_y = (self.real * other.imag) + (self.imag * other.real)
        return complex_number(new_x, new_y)
    
    def __truediv__(self, other):
        new_x = (self.real * other.real) + (self.imag * other.imag)
        new_y = (self.imag * other.real) - (self.real * other.imag)

        denominator = ((other.real ** 2) + (other.imag ** 2))
        
        new_x = new_x / denominator
        new_y = new_y / denominator

        return (new_x, new_y)
    
    def __abs__(self):
        return self.abs()
    
    def abs(self):
        squares = (self.real ** 2) + (self.imag ** 2)
        return math.sqrt(squares)
        
    def conjugate(self):
        return complex_number(self.real, -self.imag)
    
    def argument(self):
        radians = math.atan2(self.imag, self.real);
        return math.degrees(radians)




