import matlab.engine
eng = matlab.engine.start_matlab ()
import numpy as np
import os
import glob
from PIL import Image
import scipy.misc
import sys




if __name__ == '__main__':


	for image in sys.argv[1:]:
		print('reading image: ', image)
		filename = os.path.basename(image)
		name, ext = os.path.splitext(filename)


		print('Reading Image .......')
	
		image_mat=  eng.imread(image)
		print('Image passed to matlab engine')
		eng.dong(image_mat, str(name))
