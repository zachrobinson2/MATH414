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

def discrete_db2(x, y):
    array = pywt.wavedec(y, "db2", level=depth)
    cA = array[0]
    plt.figure()
    plt.title("Analysis")
    plt.plot(np.linspace(x[0], x[-1], len(cA)), cA)
    for i in range(1, len(array)):
        cD = array[-i]
        plt.figure()
        plt.title("Details " + str(i))
        plt.plot(np.linspace(x[0], x[-1], len(cD)), cD)
    plt.show()

def continuous_db2(y):
    global depth
    if depth == 1:
        depth += 1
    coeff, freq = pywt.cwt(y, np.arange(1, depth), "mexh")
    plt.figure()
    plt.imshow(coeff, extent=[-1, 1, 1, 31], cmap='PRGn', aspect='auto',
                vmax=abs(coeff).max(), vmin=-abs(coeff).max())  
    plt.title("CWT Result")
    plt.show()

args = sys.argv

if len(args) < 2:
    print("Please select an option")
    sys.exit()

option = args[1]
depth = int(args[2]) if (len(args) == 3) else 1

if option == "1":
    x = np.linspace(0,2,M)
    w = weierstrass(x,500)
    plt.figure()
    plt.title("Weierstrass")
    plt.plot(x, w)
    discrete_db2(x, w)
elif option == "2":
    x = np.linspace(0,1,M)
    b = blancmange_curve(500)(x)
    plt.figure()
    plt.title("Blancemange Curve")
    plt.plot(x, b)
    discrete_db2(x, b)
elif option == "3":
    x = np.linspace(0,1,M)
    y = wiener_process(1, M)
    plt.figure()
    plt.title("Wierner Process")
    plt.plot(x, y)
    discrete_db2(x, y)
if option == "4":
    x = np.linspace(0,2,M)
    w = weierstrass(x,500)
    plt.figure()
    plt.title("Weierstrass")
    plt.plot(x, w)
    continuous_db2(w)
elif option == "5":
    x = np.linspace(0,1,M)
    b = blancmange_curve(500)(x)
    plt.figure()
    plt.title("Blancemange Curve")
    plt.plot(x, b)
    continuous_db2(b)
elif option == "6":
    x = np.linspace(0,1,M)
    y = wiener_process(1, M)
    plt.figure()
    plt.title("Wierner Process")
    plt.plot(x, y)
    continuous_db2(y)
else:
    print("Invalid option selected. Please select one of the following options:\n" +
            "1 - Weierstrass function using Discrete Daubechie 2\n" +
            "2 - Blancmange Curve using Discrete Daubechie 2\n" +
            "3 - Wierner Process using Discrete Daubechie 2\n" +
            "4 - Weierstrass function using Continuous Wavelet Transform\n" +
            "5 - Blancmange Curve using Continuous Wavelet Transform\n" +
            "6 - Wierner Process using Continuous Wavelet Transform\n")