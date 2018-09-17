import numpy as np
import os
import cv2
import glob
from PIL import Image
import scipy.misc



def clahe(image):

	img = cv2.imread(image, 1)


	#-----Converting image to LAB Color model----------------------------------- 
	lab= cv2.cvtColor(img, cv2.COLOR_BGR2LAB)

	#-----Splitting the LAB image to different channels-------------------------
	l, a, b = cv2.split(lab)
	#cv2.imshow('l_channel', l)
	#cv2.imshow('a_channel', a)
	#cv2.imshow('b_channel', b)


	#-----Applying CLAHE to L-channel-------------------------------------------
	clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
	cl = clahe.apply(l)

	#-----Merge the CLAHE enhanced L-channel with the a and b channel-----------

	limg = cv2.merge((cl,a,b))

	#-----Converting image from LAB Color model to RGB model-------------------

	final = cv2.cvtColor(limg, cv2.COLOR_LAB2BGR)

	return final



























