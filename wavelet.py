import pywt
import matplotlib.pyplot as plt
import numpy as np

# Read in data from file
x1 = np.linspace(0, 2*np.pi, 100)
x2 = np.linspace(0, 2*np.pi, 50)
data = np.sin(x1)


# Perform transform
cA, cD = pywt.dwt(data, 'haar')

fig, axarr = plt.subplots(3)
plt.sca(axarr[0])
axarr[0].plot(x1, data)

plt.sca(axarr[1])
axarr[1].plot(x2, cA)

plt.sca(axarr[2])
axarr[2].plot(x2, cD)

plt.show()
