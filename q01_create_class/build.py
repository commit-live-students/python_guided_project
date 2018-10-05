# %load q01_create_class/build.py
import pandas as pd
import numpy as np
import math

'write your solution here'


class complex_number:
    '''The complex number class.

    Attributes:
    attr1 (x): Real part of complex number.
    attr2 (y): Imaginary part of complex number.

    '''
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag
        
    def __add__(self, other):
        return complex_number(self.real + other.real, self.imag + other.imag)

    def __sub__(self, other):
        return complex_number(self.real - other.real, self.imag - other.imag)
    
    def __mul__(self, other):
        
        if(type(self) is type(other)):
            real_part = (self.real * other.real) - (self.imag * other.imag)
            imag_part = (self.imag * other.real) + (self.real * other.imag)
        else:
            real_part = self.real * other
            imag_part = self.imag * other
            
        return complex_number(real_part, imag_part)
    
    def __str__(self):
        #print('Test: ', self.imag)
        if(self.imag > 0):
            if(self.real == 0):
                return 'i{0}'.format(self.imag)
            else:
                return '{0} + i{1}'.format(self.real, self.imag)
        
        elif (self.imag == 0):
            if(self.real == 0):
                return ' '
            else:
                return '{0}'.format(self.real)
        
        else:
            if(self.real == 0):
                return '-i{0}'.format(abs(self.imag))
            else:
                return '{0} - i{1}'.format(self.real, abs(self.imag))
    
    def conjugate(self):
        if(self.imag > 0):
            return  complex_number(self.real, (self.imag * -1))
        else:
            return complex_number(self.real, abs(self.imag))
        
    def __truedivWithoutConjug__(self, other):
        numerator_real = (self.real * other.real) + (self.imag * other.imag)
        numerator_imag = (self.imag * other.real) - (self.real * other.imag)
        denominator = (other.real**2) + (other.imag**2)
        return (numerator_real/denominator, numerator_imag/denominator)

    def __truediv__(self, other):
        numerator = self * other.conjugate()
        denominator = (other.real ** 2) + (other.imag **2)
        #print('Denom is: ', denominator)
        return (numerator.real/denominator, numerator.imag/denominator)
        #return complex_number(numerator_real/denominator, numerator_imag/denominator)
    
    def abs(self):
        return math.sqrt((self.real ** 2) + (self.imag ** 2))
        
    def argument(self):
        tan_res = math.atan2(self.imag,self.real)
        return (tan_res * (180/math.pi))
    
a = complex_number(4,4)
print('First complex number is: ', str(a))
b = complex_number(4,-3)
print('Second complex number is: ', str(b))
add_res = a + b
print('Addition of complex numbers is: ', str(add_res))
sub_res = a - b
print('Subtraction of complex numbers is: ', str(sub_res))
mult_res = a * b
print('Multiplication of complex numbers is: ', str(mult_res))
conjug_res = b.conjugate()
print('Conjugation of complex number is: ', str(conjug_res))
div_res = a.__truediv__(b)
print('Division of complex numbers is: ', str(div_res))
abs_res = a.abs()
print('Absolute of complex number is: ', str(abs_res))
arg_res = a.argument()
print('Argument of complex number is: ', str(arg_res))
div_result = a.__truedivWithoutConjug__(b)
print('Division of complex numbers is: ', str(div_result))


