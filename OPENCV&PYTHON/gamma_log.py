from skimage import data
import glob
from skimage import filters
from skimage import restoration
import numpy as np
from PIL import Image
from skimage import data
from skimage import img_as_float
from skimage import img_as_float
import skimage
import scipy.misc
import os


def log(image):

	print('reading image: ', image)
	filename = os.path.basename(image)
	name, ext = os.path.splitext(filename)

	image = img_as_float(Image.open(image))

	im = skimage.exposure.adjust_log(image, gain=1, inv=False)
	return im





