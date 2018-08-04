# %load q01_create_class/build.py
import pandas as pd
import numpy as np
import math as mt


class complex_number():
    def __init__(self, realpart, imagpart):
        self.real = realpart
        self.imag = imagpart
        
    def __add__(self,rhgs):
        new_r = self.real + rhgs.real
        new_i = self.imag + rhgs.imag
        return complex_number(new_r,new_i)
    
    def __sub__(self,rhgs):
        new_r = self.real - rhgs.real
        new_i = self.imag - rhgs.imag
        return complex_number(new_r,new_i)
    
    def __mul__(self,rhgs):
        new_r = (self.real * rhgs.real) - (self.imag * rhgs.imag)
        new_i = (self.imag * rhgs.real) + (self.real * rhgs.imag)
        return complex_number(new_r,new_i)
    
    def __truediv__(self,rhgs):
        num1 = (self.real * rhgs.real) + (self.imag * rhgs.imag)
        num2 = (self.imag * rhgs.real) - (self.real * rhgs.imag)
        den  = rhgs.real**2 + rhgs.imag**2
        real = num1/den
        imag = num2/den
        return (real,imag)
    
    def abs(self):
        return mt.sqrt(self.real**2+self.imag**2)
    
    def conjugate(self):
        return complex_number(self.imag,self.real)
    
    def argument(self):
        return mt.degrees(mt.atan(self.real/self.imag))


