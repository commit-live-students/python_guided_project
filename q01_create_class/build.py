# %load q01_create_class/build.py
import pandas as pd
import numpy as np
import math

'write your solution here'


import math

class complex_number:
    real = 0
    imag = 0
    complex_num = 0

    def __init__(self,real,imag):
        self.real =real
        self.imag = imag
    
    def getComplex(self):
        if self.imag>=0:
            self.complex_num = str(self.real)+'+'+str(self.imag)+'j'
        else:
            self.complex_num = str(self.real)+'-'+str(abs(self.imag))+'j'
        return self.complex_num
    
    def __add__(self,other):
        realsum  = self.real+other.real
        imgsum  = self.imag+other.imag
        #sum1 = str(realsum)+'+'+'i'+str(imgsum)
        return complex_number(realsum,imgsum)
    
    def __sub__(self,other):
        realsum  = self.real-other.real
        imgsum  = self.imag-other.imag
        ''' if(imgsum>=0):
            sum1 = str(realsum)+'+'+'i'+str(imgsum)
        else:
            sum1 = str(realsum)+'-'+'i'+str(abs(imgsum)) '''
        return complex_number(realsum,imgsum)

    def __mul__(self,other):
        realprod1 = (self.real*other.real) -  (self.imag*other.imag)
        imgprod1 = (self.real*other.imag) +  (self.imag*other.real)
        ''' if(imgprod1>=0):
            sum1 = str(realprod1)+'+'+'i'+str(imgprod1)
        else:
            sum1 = str(realprod1)+'-'+'i'+str(abs(imgprod1)) '''
        return complex_number(realprod1,imgprod1)

    def __truediv__(self,other):
        num1 = (self.real*other.real) +  (self.imag*other.imag)
        num2 = (self.imag*other.real) -  (self.real*other.imag)
        deno = other.real**2 + other.imag**2
        realdiv =  num1.__truediv__(deno)
        imgdiv = num2.__truediv__(deno)
        ''' if(imgdiv>=0):
            sum1 = str(realdiv)+'+'+'i'+str(imgdiv)
        else:
            sum1 = str(realdiv)+'-'+'i'+str(abs(imgdiv)) '''
        return realdiv, imgdiv
    
    
    def abs(self):
        return math.sqrt(self.real**2+self.imag**2)
    
    def argument(self):
        return math.degrees(math.atan(self.imag/self.real))
    
    def conjugate(self):
        self.imag = self.imag*-1
        return complex_number(self.real,self.imag)
    
    def __str__(self):
        if self.imag>=0:
            self.complex_num = str(self.real)+'+'+str(self.imag)+'j'
        else:
            self.complex_num = str(self.real)+'-'+str(abs(self.imag))+'j'
        return self.complex_num



