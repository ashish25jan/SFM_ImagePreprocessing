import glob
import cv2
import numpy as np
import os

i = 0
#Change the img directory path as required
def gaussian(image):
	print('reading image: ', image)
	filename = os.path.basename(image)
	name, ext = os.path.splitext(filename)

	img = cv2.imread(image)

	gauss_blur = cv2.GaussianBlur(img,(9,9),0)
	return gauss_blur

	



























