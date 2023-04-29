import pywt
import numpy as np
import sys
import cv2

args = sys.argv

if len(args) < 2:
    print("Please enter a filename")
    sys.exit()

fileName = args[1]


print("Decomposing Data in", fileName)

# Read in data from file
image = cv2.imread(fileName)
image = np.float32(image)
image /= 255

# Perform transform
cA, (cDH, cDV, cDD) = pywt.dwt2(image, "db2")

# Reassemble image
image *= 255
image = np.uint8(image)
cA *= 255
cA = np.uint8(cA)
cDH *= 255
cDH = np.uint8(cDH)
cDV *= 255
cDV = np.uint8(cDV)
cDD *= 255
cDD = np.uint8(cDD)

cv2.imshow('Original', image)
cv2.imshow("Analysis", cA)
cv2.imshow("Horizontal Detail", cDH)
cv2.imshow("Veritical Detail", cDV)
cv2.imshow("Diagonal Detail", cDD)
cv2.waitKey(0)

