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


def tv(image):

	print('reading image: ', image)
	filename = os.path.basename(image)
	name, ext = os.path.splitext(filename)

	coins = img_as_float(Image.open(image))
	tv_filter = restoration.denoise_tv_chambolle(coins, weight=0.1, n_iter_max=200, multichannel = True)

	return tv_filter