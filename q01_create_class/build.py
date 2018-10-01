import math
import numpy as np

class complex_number():
    
    def __init__(self, real=0.0,imag=0.0):
        self.real=real #real part
        self.imag=imag #imaginary part

    def __repr__(self):
        if self.real == 0.0 and self.imag == 0.0:
            return '0.00'
        if self.real == 0:
            return '%.2fi' % self.imag
        if self.imag == 0:
            return '%.2f' % self.real
        return '%.2f %s %.2fi' % (self.real, '+' if self.imag >= 0 else '-', abs(self.imag))
         
    def abs(self):
        return (self.real**2+self.imag**2)**0.5
    
    def argument(self):
        return math.degrees(np.arctan(self.real/self.imag))
    
    def conjugate(self):
        return complex_number(self.real,-self.imag)
    
    def __add__(self,other):
        a1=self.real+other.real
        b1=self.imag+other.imag
        return complex_number(a1,b1)

    def __sub__(self,other):
        a1=self.real-other.real
        b1=self.imag-other.imag
        return complex_number(a1,b1)
    
    def __mul__(self,other):
        a1= (self.real*other.real)-(self.imag*other.imag)
        b1= (self.real*other.imag)+(other.real*self.imag)
        return complex_number(a1,b1)
    
    def __truediv__(self,other):
        c= ((self.real*other.real+self.imag*other.imag))/(other.real**2+other.imag**2)
        d= ((self.imag*other.real-self.real*other.imag))/(other.real**2+other.imag**2)
        return c,d



