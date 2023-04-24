import pywt
import matplotlib.pyplot as plt
import numpy as np
import sys
import math

args = sys.argv

if len(args) < 2:
    print("Please enter a filename")
    sys.exit()

dataFileName = args[1]
decompCount = int(args[2]) if len(args) == 3 else 1


print("Decomposing Data in", dataFileName, decompCount, "time(s).")

# TODO: Read in data from file
sampleCount = 1000
x = np.linspace(0, 2*np.pi, sampleCount)
cA = np.sin(x)


# Perform transform
rows = min(decompCount + 1, 3)
cols = math.ceil((decompCount + 2) / 3)
fig, axarr = plt.subplots(rows, cols)
plt.sca(axarr[0, 0])
plt.plot(x, cA)
plt.title("Original")

for i in range(1, decompCount + 1):
    cA, cD = pywt.dwt(cA, 'haar')
    cA = list(cA)
    cD = list(cD)
    x = np.linspace(0, 2*np.pi, len(cD))

    row = i % 3
    col = i // 3
    plt.sca(axarr[row, col])
    plt.plot(x, cD)
    plt.title("Details " + str(i))

row = (decompCount + 1) % 3
col = (decompCount + 1) // 3
plt.sca(axarr[row, col])
plt.plot(x, cA)
plt.title("Final Analysis")

plt.subplots_adjust(hspace=1)
plt.show()
