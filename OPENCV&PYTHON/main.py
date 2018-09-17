import numpy as np
from gama_sigmoid import sigmoid
from clahe import clahe
from gamma_log import log
from hist_eq import hist_eq
from bilateral import bilateral
from Gaussian_blur import gaussian
from nlm import nlm
from tv import tv
from wavelet import wavelet
from wiener import wiener
import sys
import glob
import scipy.misc
import os
import pathlib
from scipy.misc import imsave
import cv2


# This document contains all the functions which run on python and opencv Library.
# USAGE : python main.py <CE/denoise> <type of filter>
# OUTPUT: processed image is saved in same folder as the main.py, under foldername ===>> <type of image processing>/<type of filter>
# BEST USAGE : RUN it in python virtual environment with opencv also installed in same virtual environment.


if __name__ == '__main__':


	if(sys.argv[1] == 'CE'):

		if(sys.argv[2] == 'sigmoid'):

			for image in sys.argv[3:]:

				filename = os.path.basename(image)
				name, ext = os.path.splitext(filename)

				img = sigmoid(image)

				os.makedirs('CE/Sigmoid', exist_ok=True)

				imsave('CE/Sigmoid/%s.png' %name, img)

			
		if(sys.argv[2] == 'clahe'):

			for image in sys.argv[3:]:

				filename = os.path.basename(image)
				name, ext = os.path.splitext(filename)

				img = clahe(image)
				os.makedirs('CE/clahe', exist_ok=True)

				cv2.imwrite('CE/clahe/%s.png'%name, img)


		if(sys.argv[2] == 'log'):
			for image in sys.argv[3:]:

				filename = os.path.basename(image)
				name, ext = os.path.splitext(filename)

				img = log(image)

				os.makedirs('CE/gamma_log', exist_ok=True)

				imsave('CE/gamma_log/%s.png' %name, img)

				


		if(sys.argv[2] == 'he'):
			for image in sys.argv[3:]:
				filename = os.path.basename(image)
				name, ext = os.path.splitext(filename)

				img = hist_eq(image)
				os.makedirs('CE/HE', exist_ok=True)

				cv2.imwrite('CE/HE/%s.png'%name, img)


	elif(sys.argv[1] == 'denoise'):
		if(sys.argv[2] == 'bilateral'):

			for image in sys.argv[3:]:

				filename = os.path.basename(image)
				name, ext = os.path.splitext(filename)

				img = bilateral(image)

				os.makedirs('denoise/bilateral', exist_ok=True)

				cv2.imwrite('denoise/bilateral/%s.png' %name, img)

			
		if(sys.argv[2] == 'gaussian'):

			for image in sys.argv[3:]:

				filename = os.path.basename(image)
				name, ext = os.path.splitext(filename)

				img = gaussian(image)
				os.makedirs('denoise/gaussian', exist_ok=True)

				cv2.imwrite('denoise/gaussian/%s.png'%name, img)


		if(sys.argv[2] == 'nlm'):
			for image in sys.argv[3:]:

				filename = os.path.basename(image)
				name, ext = os.path.splitext(filename)

				img = nlm(image)

				os.makedirs('denoise/nlm', exist_ok=True)

				imsave('denoise/nlm/%s.png' %name, img)

		if(sys.argv[2] == 'tv'):

			for image in sys.argv[3:]:

				filename = os.path.basename(image)
				name, ext = os.path.splitext(filename)

				img = tv(image)

				os.makedirs('denoise/tv', exist_ok=True)

				imsave('denoise/tv/%s.png' %name, img)

			
		if(sys.argv[2] == 'wavelet'):

			for image in sys.argv[3:]:

				filename = os.path.basename(image)
				name, ext = os.path.splitext(filename)

				img = wavelet(image)
				os.makedirs('denoise/wavelet', exist_ok=True)

				imsave('denoise/wavelet/%s.png'%name, img)


		if(sys.argv[2] == 'wiener'):
			for image in sys.argv[3:]:

				filename = os.path.basename(image)
				name, ext = os.path.splitext(filename)

				img = wiener(image)

				os.makedirs('denoise/wiener', exist_ok=True)

				imsave('denoise/wiener/%s.png' %name, img)

	else:

		print("NO ARGUMENT PROVIDED")





	
