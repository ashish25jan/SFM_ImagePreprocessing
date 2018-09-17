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

		image = Image.open(image)
		print('Making Image Matlab readable .......')
	#image = eng.im2double(image)
		image_mat = matlab.uint8(list(image.getdata()))
		image_mat.reshape((image.size[0], image.size[1], 3))
		print('Image passed to matlab engine')
		k1 = eng.double(15)
		k2 = eng.double(80)
		k3 = eng.double(250)
		image_c = eng.bpdhe(image_mat)

		print('Reshaping image......')
		np.asarray(image_c)
		print('Saving Image ....')
		scipy.misc.imsave('%s.png' %name, image_c)
