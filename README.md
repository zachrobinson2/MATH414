You need a few libraries installed to make this work:
install python
pip install numpy
pip install opencv-python
pip install PyWavelets

You can run the code on an image by doing the following in the command line:
> python wavelet.py <file_path> [decomp_depth]

file_path - The path to the image that we want to apply wavelets to
decomp_depth - The level to which we want to decompose the data (default value is 1)

output - a series of images including, the original, the decomposed function, and all the details collected
