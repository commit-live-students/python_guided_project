# %load q01_create_class/build.py
import pandas as pd
import numpy as np
import math

'write your solution here'

class complex_number(object):
    def __init__ (self, real, imag):
        self.real= real
        self.imag= imag
        
    def __add__(self, num):
        return(complex_number(self.real + num.real, self.imag + num.imag))
    
    def __sub__(self, num):
        return(complex_number(self.real - num.real, self.imag - num.imag))
    
    def __mul__(self, num):
        if num.imag !=0:
            real = self.real * num.real - self.imag * num.imag
            imag = self.real * num.imag + self.imag * num.real
        else:
            real = (self.real * num.real) + (self.imag * num.real)
            imag = 0
        return (complex_number(real,imag))
    
    def conjugate(self):
        real = self.real
        imag = self.imag*(-1)
        return (complex_number(real,imag))
            
    def abs(self):
        real=self.real
        imag= self.imag
        sq=self.real * self.real + self.imag * self.imag
        sqrt1=math.sqrt(sq)
        return(sqrt1)
    
    def __truediv__(self, num):
        real= (self.real * num.real + self.imag * num.imag) / ((num.real **2) + (num.imag **2))
        imag= (self.imag * num.real - self.real * num.imag) / ((num.real **2) + (num.imag **2))
               
        return (real, imag)
    
    def argument(self):
        ar=math.degrees(math.atan2(self.real,self.imag))
        return ar
            
        
    
c1= complex(4,4)
c2= complex(4,-3)
o1= complex_number(c1.real,c1.imag)
o2= complex_number(c2.real,c2.imag)
output_add=o1.__add__(o2)
print('Addition of Complex numbers ' + str(c1.real) + ' + ' + str(c1.imag) + ' is:\nReal numbers:' + str(output_add.real) + '\nImaginary numbers:'+ str(output_add.imag)+'\n')
output_sub=o1.__sub__(o2)
print('Subtraction of Complex numbers is:\nReal numbers:' + str(output_sub.real) + '\nImaginary numbers:'+ str(output_sub.imag)+'\n')
output_mul=o1.__mul__(o2)

print('Multiplication of Complex numbers is:\nReal numbers:' + str(output_mul.real) + '\nImaginary numbers:'+ str(output_mul.imag)+'\n')
output_conj=o1.conjugate()
print('Conjugate of Complex numbers is ' +(str(output_conj.real) +' '+ str(output_conj.imag)))
absolute=o1.abs()
print('Absolute of Complex numbers is ' + str(absolute))
output_div_real, output_div_imag= o1.__truediv__(o2)

print('Division of Complex numbers is:\nReal numbers:' + str(output_div_real) + '\nImaginary numbers:'+ str(output_div_imag)+'\n')
argu=o1.argument()
print('Argument of Complex numbers is ' + str(argu))


