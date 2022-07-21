import math

class Complex(object):
    def __init__(self, real, imaginary):
        self.real = real
        self.imag = imaginary
    def __add__(self, no):
        result = Complex(self.real, self.imag)
        result.real = self.real + no.real
        result.imaginary = self.imag + no.imag
        return result
    def __sub__(self, no):
        result = Complex(self.real, self.imag)
        result.real = self.real - no.real
        result.imaginary = self.imag - no.imag
        return result
    def __mul__(self, no):
        result = Complex(self.real, self.imag)
        result.real = self.real * no.real - self.imag * no.imag
        result.imaginary = self.real * no.imag + self.imag * no.real
        return result
    def __truediv__(self, no):
        result = Complex(self.real, self.imag)
        result.real = (self.real * no.real + self.imag * no.imag)/(no.real*no.real + no.imag * no.imag)
        result.imaginary = (self.imag * no.real - self.real * no.imag)/(no.real*no.real + no.imag * no.imag)
        return result
    def mod(self):
        result = Complex(self.real, self.imag)
        result.real = math.sqrt(self.real*self.real + self.imag * self.imag)
        result.imaginary = 0
        return result
    def __str__(self):
        if self.imaginary == 0:
            result = "%.2f+0.00i" % (self.real)
        elif self.real == 0:
            if self.imaginary >= 0:
                result = "0.00+%.2fi" % (self.imaginary)
            else:
                result = "0.00-%.2fi" % (abs(self.imaginary))
        elif self.imaginary > 0:
            result = "%.2f+%.2fi" % (self.real, self.imaginary)
        else:
            result = "%.2f-%.2fi" % (self.real, abs(self.imaginary))
        return result

if __name__ == '__main__':
    c = map(float, input().split())
    d = map(float, input().split())
    x = Complex(*c)
    y = Complex(*d)
    print(*map(str, [x+y, x-y, x*y, x/y, x.mod(), y.mod()]), sep='\n')