
import math

class complex_number:
    def __init__(self, real, imag=0.0):
        self.real = real
        self.imag = imag
    
    def __str__(self):
        return str(self.real) + ' + i' + str(self.imag)

    ##This function adds two complex numbers. Returns result as another complex number##
    def __add__(self,other):
        return complex_number(self.real + other.real,
                       self.imag + other.imag)
    
    ##This function subtracts two complex numbers. Returns result as another complex number##
    def __sub__(self,other):
        return complex_number(self.real - other.real,
                       self.imag - other.imag)
    
    ##This function multiplies two complex numbers. Returns result as another complex number##
    def __mul__(self, other):
        return complex_number(self.real * other.real - self.imag * other.imag,
                       self.imag * other.real + self.real * other.imag)
    
    ##This function finds division of two complex numbers. Returns result as another complex number##
    def __truediv__(self, other):
        base = float(math.pow(other.real,2) + math.pow(other.imag,2))
        r = self.real * other.real + self.imag * other.imag
        i = self.imag * other.real - self.real * other.imag
        return (r/base, i/base)
    
    ##This function finds conjugate of complex number.##
    def conjugate(self):
        return complex_number(self.real, -self.imag)
    
    ##This function finds absolute of complex number.##
    def abs(self):
        return math.sqrt(math.pow(self.real,2) + math.pow(self.imag,2))
    
    ##This function finds argument of complex number in degrees.##
    def argument(self):
         return math.degrees(math.atan(self.imag / self.real))

