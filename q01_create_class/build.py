# %load q01_create_class/build.py
import pandas as pd
import numpy as np
import math

#'write your solution here'

#    '''The complex number class.

#    Attributes:
#    attr1 (x): Real part of complex number.
#    attr2 (y): Imaginary part of complex number.

#    '''

class complex_number:

    def __init__(self,real,imag):
        self.real=real
        self.imag=imag
        
    def __add__(self,num2):
        return complex_number(self.real+num2.real, self.imag+num2.imag)
 
    def __sub__(self,num2):
        return complex_number(self.real-num2.real, self.imag-num2.imag)
    
    def __mul__(self,num2): 
        return complex_number(self.real*num2.real - self.real*num2.imag, self.imag*num2.real + self.imag*num2.imag)
        
    def abs(self):
        return (math.sqrt(self.real**2 + self.imag**2))
    
    def conjugate(self):
        return complex_number(self.real,-self.imag)
    
    def argument(self):
        return math.degrees(math.atan(self.real/self.imag))
        
    def __str__(self):
        negative='+'
        if (self.imag<0):
            negative=''
        return '{}{}{}i'.format(self.real,negative,self.imag)    
    
    def __truediv__(self, num2):
        r=(self.real*num2.real + self.imag*num2.imag)/(num2.real**2 + num2.imag**2)
        i=(self.imag*num2.real - self.real*num2.imag)/(num2.real**2 + num2.imag**2)
        return r, i
    
n1=complex_number(-3,2)
n2=complex_number(-1,7)

n3=n1 + n2
n4=n1 - n2
print ('add', n3)
print ('subtract', n4)

n5=n1 * n2
print('multiply', n5)

n6=n1/n2
print('divide', n6)

n7=n1.abs()
print ('absolute', n7)

n8=n1.conjugate()
print('conjugate', n8)

n9=n1.argument()
print('arg', n9)




