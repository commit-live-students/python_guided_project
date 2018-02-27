import pandas as pd
import numpy as np
import math

from greyatomlib.python_guided_project.q01_create_class.build import complex_number

"write your solution here"
class complex_numbers:
    def __init__(self, real = 0.00 ,imag= 0.00):
        self.imag =  imag
        self.real =  real

    def __str__(self):
        if self.imag < 0:
            return "{0}  {1}i".format(self.real,self.imag)
        else:
            return "{0} + {1}i".format(self.real,self.imag)


    def __add__(self ,other):
        return complex_numbers( self.real + other.real, self.imag + other.imag)

    def __sub__(self ,other):
        return complex_numbers( self.real - other.real, self.imag - other.imag)

    def __mul__(self ,other):
        return complex_numbers( self.real * other.real - self.imag * other.imag ,
                                self.real * other.imag + self.imag * other.real
                            )

    def __truediv__(self ,other):
        if other.real*other.real + other.imag*other.imag != 0:
            return ((self.real*other.real + self.imag*other.imag) / (other.real*
                        other.real + other.imag*other.imag),
                    (self.imag*other.real - self.real*other.imag) / (other.real*
                        other.real + other.imag*other.imag))
        else:
            return null

    def abs(self ):
        return math.sqrt(self.real**2 + self.imag**2)

    def argument(self ):
        if self.real==0 :
            return None
        return math.degrees( math.atan ( self.imag/self.real))


#test cases
a = complex_numbers(1,2)
b = complex_numbers(4,-1)

print (a+b)
print (a*b)
print (a.__truediv__( b))
print (a.abs())
print (a.argument())


a = complex_numbers(4,4)
b = complex_numbers(4,-3)

c = complex_number(4,4)
d = complex_number(4,-3)

print 'Failed test cases'
x = a.__truediv__(b)
y = c.__truediv__(d)

print a
print b
print x


print y
