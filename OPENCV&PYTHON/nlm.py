import glob
import cv2
import numpy as np
import os

i = 0
#Change the img directory path as required
def nlm(image):
	print('reading image: ', image)
	filename = os.path.basename(image)
	name, ext = os.path.splitext(filename)

	img = cv2.imread(image)

	nlm = cv2.fastNlMeansDenoisingColored(img,None,10,10,7,21)
	return nlm
