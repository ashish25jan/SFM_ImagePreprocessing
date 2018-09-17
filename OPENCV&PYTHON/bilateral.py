import glob
import cv2
import numpy as np
import os

i = 0
#Change the img directory path as required
def bilateral(image):
	print('reading image: ', image)
	filename = os.path.basename(image)
	name, ext = os.path.splitext(filename)

	img = cv2.imread(image)

	kernel_length =10
	bilateral = cv2.bilateralFilter(img, kernel_length, kernel_length*2, kernel_length/2);
	return bilateral

	



























