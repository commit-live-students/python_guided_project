# %load q01_create_class/build.py
import pandas as pd
import numpy as np
import math
from greyatomlib.python_guided_project.q01_create_class.build import complex_number
from unittest import TestCase
from inspect import getargspec

'write your solution here'

class complex_numbers:

    #Initialize the input values
    def __init__(self, real=0.0, imag=0.0):
        self.real = real
        self.imag = imag
        
    #To finalize the return value for below defined functions.
    def __str__(self):
        if self.imag < 0:
            return '{0} {1}i'.format(self.real,self.imag)
        else:
            return '{0} + {1}i'.format(self.real,self.imag)
        
    
    #To perform addition {the sum of 5 + 3i and 4 + 2i is 9 + 5i}          
    def __add__(self, new):
        return complex_numbers(self.real+new.real, self.imag+new.imag)
    
    #To perform substraction {the sub of 5 + 3i and 4 + 2i is 1 + 1i}
    def __sub__(self, new):
        return complex_numbers(self.real-new.real, self.imag-new.imag)
    
    #To perform Multiplication  { (3 + 2i)(1 + 4i) = 3 + 12i + 2i + 8i2. (i2 = -1)}
    def __mul__(self, new):
        return complex_numbers(((self.real*new.real)-(self.imag*new.imag)),((self.real*new.imag)+(self.imag*new.real)))
    
    #To perform Division
    '''
    Step 1:	To divide complex numbers, you must multiply by the conjugate. To find the conjugate of a complex number all you have to do is change the sign between the two terms in the denominator.
    Step 2:	Distribute (or FOIL) in both the numerator and denominator to remove the parenthesis.
    Step 3:	Simplify the powers of i, specifically remember that i*i = -1
    Step 4:	Combine like terms in both the numerator and denominator, that is, combine real numbers with real numbers and imaginary numbers with imaginary numbers.
    Step 5:	Write you answer in the form a + bi.
    '''
    
    def __truediv__(self, new):
        deno = new.real*new.real + new.imag*new.imag
        if deno != 0:
            #    print temp_y.real, temp_y.imag
            #   cal_real, cal_imag = __mul__(self, temp_y)
            #    print cal.real, cal.imag
            #    print cal_demo
            return ((self.real*new.real + self.imag*new.imag) / (deno),
                    (self.imag*new.real - self.real*new.imag) / (deno))
            
        else:
            return null
     
    # To get absolute value of complex number is basically the square root of sum of square of  real and imag. 
    def abs(self ):
        return math.sqrt(self.real**2 + self.imag**2)
    
    # To get argument is tan^-1(y/x) in degrees
    def argument(self):
        return math.degrees( math.atan ( self.imag/self.real))




