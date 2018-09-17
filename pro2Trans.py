import scipy.linalg as la
import numpy as np
import os
import sys




def maketransform(arr):

	rotat =  np.delete(arr,3, axis =0)
	trans =  arr[3,:]

	translation = np.transpose(np.array(trans))
	T = np.column_stack((rotat,trans))

	fake = np.array([0 ,0 ,0 ,1])

	T = np.row_stack((T,fake))

	print(T)
	return T

def getrtmat(arr):
	matrix = arr.reshape(3,4)
	R = la.pinv(matrix)

	return R
	
	
if __name__ == '__main__':




	for file in sys.argv[1:]:

		filename = os.path.basename(file)
		name, ext = os.path.splitext(filename)
		print("Reading file: %s"%name )
		with open(file, 'r') as fobj:
			num = []
			for line in fobj:

				numbers = [float(num) for num in line.split()]
				num = np.append(num, np.array(numbers))

		a = getrtmat(num)

		b = maketransform(a)

			#Flattening it just to make it easy to copy it to xml file, in future if you want to import it directly remove it.
		b = np.ndarray.flatten(b)

		with open("test.txt", "a") as myfile:
			myfile.write("\n")
			myfile.write("\n")
			myfile.write("Camera %s"%name)
			myfile.write("\n")			
			myfile.write(str(b))

	#print(a)