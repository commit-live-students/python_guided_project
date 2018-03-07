import pandas as pd
import numpy as np
import math

"write your solution here"
class complex_numbers:
    def __init__(self,real=0.00,imag=0.00):
        self.real = real
        self.imag = imag

    def __str__(self):
        if self.imag < 0:
            return '{0}{1}i'.format(self.real,self.imag)
        else:
            return "{0}+{1}i".format(self.real,self.imag)

    def __add__(first,second):
        return complex_numbers(first.real + second.real, first.imag + second.imag)

    def __sub__(first ,second):
        return complex_numbers( first.real - second.real, first.imag - second.imag)

    def __mul__(first ,second):
        return complex_numbers( first.real * second.real - first.imag * second.imag ,first.real * second.imag + first.imag * second.real)

    def abs(first):
        return math.sqrt(first.real**2 + first.imag**2)

    def argument(first):
        if first.real==0 :
            return None
        return math.degrees( math.atan ( first.imag/first.real))

    def __truediv__(first ,second):
        if second.real*second.real + second.imag*second.imag != 0:
            return ((first.real*second.real + first.imag*second.imag) / (second.real*
                        second.real + second.imag*second.imag),
                    (first.imag*second.real - first.real*second.imag) / (second.real*
                        second.real + second.imag*second.imag))
