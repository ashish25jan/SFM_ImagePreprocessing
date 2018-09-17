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





def sigmoid(image):
	#print("Here") //for debugging
	
	print('reading image: ', image)
	
	image = img_as_float(Image.open(image))
	im = skimage.exposure.adjust_sigmoid(image, cutoff=0.5, gain=10, inv=False)
	return im
	
		