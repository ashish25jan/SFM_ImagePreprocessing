from skimage import data
import glob
from skimage import filters
from skimage import restoration
import numpy as np
from PIL import Image
from skimage import data
from skimage import img_as_float
from skimage import img_as_float
import scipy.misc
import os


def wiener(image):

	print('reading image: ', image)
	filename = os.path.basename(image)
	name, ext = os.path.splitext(filename)

	im = img_as_float(Image.open(image))
	wiener = scipy.signal.wiener(im, mysize=None, noise=None)

	return wiener