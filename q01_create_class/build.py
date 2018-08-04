import math


class complex_number:
    def __init__(self, real=0, imag=0):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        return complex_number(self.real + other.real,
                       self.imag + other.imag)

    def __sub__(self, other):
        return complex_number(self.real - other.real,
                       self.imag - other.imag)

    def __mul__(self, other):
        return complex_number(self.real*other.real - self.imag*other.imag,
                       self.imag*other.real + self.real*other.imag)
    
    def __truediv__(self, other):
        sr, si, o_r, oi = self.real, self.imag,other.real, other.imag # short forms
        r = float(o_r**2 + oi**2)
        return (sr*o_r+si*oi)/r, (si*o_r-sr*oi)/r

    def abs(self):
        return math.sqrt(self.real**2 + self.imag**2)
    
    def conjugate(self):   
        return complex_number(self.real, -self.imag)
    
        
    def argument(self):   
        return math.degrees((math.atan(self.imag/self.real)))
    
    def __str__(self):
        if self.imag > 0:
            return str(self.real)+'+'+'i'+str(self.imag) 
        else:
            return str(self.real)+'-'+'i'+str(abs(self.imag))
            

print('Select operation.')
print('1.Add')
print('2.Subtract')
print('3.Multiply')
print('4.Divide')
print('5.Absolute')
print('6.Conjugate')
print('7.Argument')


# Take input from the user 
choice = input('Enter choice(1/2/3/4/5/6/7):')

num1 = int(input('Enter First_Real number: '))
num2 = int(input('Enter First_imag number: '))
num3 = int(input('Enter Second_Real number: '))
num4 = int(input('Enter Second_imag number: '))
c1 = complex_number(num1,num2)
c2 = complex_number(num3,num4)
if choice == '1':
   print(c1,'+',c2,'=', (c1+c2))

elif choice == '2':
   print(c1,'-',c2,'=',(c1-c2))

elif choice == '3':
   print(c1,'*',c2,'=',(c1*c2))

elif choice == '4':
   print(c1,'/',c2,'=',(c1/c2))

elif choice == '5':
   print(c1,'=',c1.absu())

elif choice == '6':
   print(c1 ,'=',c1.cong())

elif choice == '7':
   print(c1 ,'=',c1.argu())


else:
   print('Invalid input')



