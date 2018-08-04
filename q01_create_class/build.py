import math

class complex_number:
    '''The complex number class.

    Attributes:
    attr1 (x): Real part of complex number.
    attr2 (y): Imaginary part of complex number.

    '''
#There are some functions you want to call as soon as you initialize my class- so as soon as I call the class, the thing with __init__ is called
class complex_number():
    def __init__(self, real, imag):
        self.real= real
        self.imag=imag
    
    def __str__(self):
        if self.imag<0:
            return '{0}-i{1}'.format(self.real,abs(self.imag))
        else:
            return '{0}+i{1}'.format(self.real,abs(self.imag))
    
    
    #Method overriding  
    
    def __add__(self,other):
        real_result= self.real+other.real
        imaginary_result= self.imag+other.imag
        result= complex_number(real_result,imaginary_result)
        return result
        
    def __sub__(self,other):
        real_result= self.real-other.real
        imaginary_result= self.imag- other.imag
        result = complex_number(real_result,imaginary_result)
        return result
    
    def abs(self):
            return math.sqrt(self.real**2+self.imag**2)
    
    def __mul__(self,other):
        real_result = self.real*other.real- self.imag*other.imag
        imaginary_result= self.imag*other.real+ self.real*other.imag
        result= complex_number(real_result, imaginary_result)
        return result
    
    def __truediv__(self,other):
        #(a+bi)/(c+di)=(ac+bd)/c2+d2 + i(bcâad )/ c2+d2
        num1 = ((self.real*other.real)+(self.imag*other.imag))
        deno = (other.real**2) + (other.imag**2)
        num2 = ((self.imag*other.real)-(self.real*other.imag))
        return num1/deno,num2/deno
    
    def conjugate(self):
        return self.real+ -self.imag

    def argument(self):
        result= math.degrees(math.atan(self.imag/self.real))
        return result




