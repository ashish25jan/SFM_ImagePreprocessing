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
import cv2

def hist_eq(image):

	print('reading image: ', image)
	filename = os.path.basename(image)
	name, ext = os.path.splitext(filename)


	img = cv2.imread(image)

	img_lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)

	lab, a, b = cv2.split(img_lab)

	# equalize the histogram of the Y channel
	img_lab = cv2.equalizeHist(lab)

	imgm = cv2.merge((lab,a,b))


	# convert the YUV image back to RGB forma
	img_output = cv2.cvtColor(imgm, cv2.COLOR_LAB2BGR)

	return img_output