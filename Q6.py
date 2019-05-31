import math
import subprocess
import time
import matplotlib.pyplot as plt

class GaussianQuadrature:

    def __init__(self, n):
        self.N = n
        self.legendre_poly = calculate_legendre(self.N)
        self.d_legendre_poly = calculate_derivative(self.legendre_poly)
        self.legendre_zeros = [calculate_zeros(self.legendre_poly, math.cos(3.141592655 * (i - 0.25) / (self.N + 0.5))) for i in range(1, self.N + 1)]
        self.quadrature_weights = [2 / ((1 - i * i) * pow(calculate_poly(self.d_legendre_poly, i), 2)) for i in self.legendre_zeros]

    def reset(self, n):
        self.__init__(n)

    def function(self, x):
        return pow(x, 3) * math.cos(pow(x, 2)) / (x + 1)

    def integrate(self, a, b):
        return sum([self.quadrature_weights[i] * (b - a) * self.function((b - a) * self.legendre_zeros[i] / 2 + (b + a) / 2) / 2 for i in range(self.N)])

    

def calculate_poly(poly, x):
    return sum([poly[i] * pow(x, i) for i in range(len(poly))])

def calculate_legendre(n):
        if n == 1:
            return [0, 1]
        elif n == 0:
            return [1]

        coeff1 = [0] + calculate_legendre(n - 1)
        coeff2 = calculate_legendre(n - 2) + [0, 0]

        return [((2 * n - 1) * coeff1[i] - (n - 1) * coeff2[i]) / n for i in range(n + 1)]

 
def calculate_derivative(poly):
    return [i * poly[i] for i in range(1, len(poly))]

def calculate_zeros(poly, guess):
    d_poly = calculate_derivative(poly)

    x0 = -1
    x1 = guess
    while abs(x1 - x0) > 0.00001:
        x0 = x1
        x1 = x1 - calculate_poly(poly, x1) / calculate_poly(d_poly, x1)
    
    return x1
        
N = 20
pyTime = []
cTime = []

for i in range(N + 1):
    start = time.time_ns()
    myGauss = GaussianQuadrature(i)
    result = myGauss.integrate(0, 1)
    timeElapsed = float(time.time_ns() - start) / 1000000.0
    pyTime.append(timeElapsed)
    print("Result of Python code (n = " + str(N) +"):", )
    print(timeElapsed, "ms")

    start = time.time_ns()
    subprocess.call(["Gauss.exe", str(i)])
    timeElapsed = float(time.time_ns() - start) / 1000000.0
    cTime.append(timeElapsed)
    print(timeElapsed, "ms")


plt.plot(range(N + 1), pyTime)
plt.plot(range(N + 1), cTime)
plt.legend(["Python", "C++"])
plt.show()




