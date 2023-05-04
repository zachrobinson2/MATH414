You need a few libraries installed to make this work:
install python
pip install numpy
pip install PyWavelets
pip install matplotlib

You can run the code on an image by doing the following in the command line:
> python wavelet.py <option> [depth]

option - One of the options below
    1 - Weierstrass function using Discrete Daubechie 2
    2 - Blancmange Curve using Discrete Daubechie 2
    3 - Wierner Process using Discrete Daubechie 2
    4 - Weierstrass function using Continuous Wavelet Transform
    5 - Blancmange Curve using Continuous Wavelet Transform
    6 - Wierner Process using Continuous Wavelet Transform

depth - The level to which we want to decompose the data (default value is 1)


output - a series of graphs including, the original, the decomposed function, and all the details collected

Example:
> python wavelet.py 1 10

This will decompose the Weierstrass frunction using Dicrete Daubechie 2 to the tenth level.
