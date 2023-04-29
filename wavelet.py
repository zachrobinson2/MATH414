import pywt
import numpy as np
import sys
import cv2

args = sys.argv

if len(args) < 2:
    print("Please enter a filename")
    sys.exit()

fileName = args[1]
depth = args[2] if (len(args) == 3) else 1


print("Decomposing Data in", fileName)

# Read in data from file
image = cv2.imread(fileName, cv2.IMREAD_GRAYSCALE)
image = np.float32(image)
image /= 255


# Perform transform
array = pywt.wavedec2(image, "db2", level=int(depth))

# Reassemble image
image *= 255
image = np.uint8(image)
cA = array[0] * 255
cA = np.uint8(cA)
cv2.imshow('Original', image)
cv2.imshow("Analysis", cA)
for i in range(1, len(array)):
    cH = array[-i][0]
    cV = array[-i][1]
    cD = array[-i][2]
    cv2.imshow("Horizontal" + str(i), cH)
    cv2.imshow("Veritical" + str(i), cV)
    cv2.imshow("Diagonal" + str(i), cD)

cv2.waitKey(0)

