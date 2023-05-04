import pywt
import numpy as np
import sys
import matplotlib.pyplot as plt

M = 10000

def weierstrass(x, N):
    y = np.zeros((1,M))
    for n in range(N+1):
        y = y + np.cos(3**n*np.pi*x)/2**n
    return np.reshape(y, (M,))

def s(x):
    d = x - np.floor(x)
    return np.minimum(d, 1 - d)

def blancmange_curve(N):
    def f(x):
        return sum(s(x * 2 ** n) / 2 ** n for n in range(N))
    return f

def wiener_process(t, n):
    dt = t / n
    dW = np.random.normal(0, np.sqrt(dt), n)
    W = np.cumsum(dW)
    return W

args = sys.argv

if len(args) < 2:
    print("Please select an option")
    sys.exit()

option = args[1]
depth = args[2] if (len(args) == 3) else 1

if option == "1":
    x = np.linspace(0,2,M)
    w = weierstrass(x,500)
    plt.plot(x, w, 'r-')
    plt.show()
elif option == "2":
    x = np.linspace(0,1,M)
    b = blancmange_curve(500)(x)
    plt.plot(x, b, 'r-')
    plt.show()
elif option == "3":
    x = np.linspace(0,1,M)
    y = wiener_process(1, M)
    plt.plot(x, y, 'r-')
    plt.show()


