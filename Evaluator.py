# This file script can parse Photoscan xml file to find pose of the camera, still need to add argument feature.
#UPDATE ======>>>> ADDED THE FEATURES.


from xml.dom import pulldom
import numpy as np
import sys
import os
from scipy.spatial import distance
from numpy import *
from math import sqrt
import sympy as sy
import scipy as scipy
a =[]
b=[]
c=[]
B = np.empty((0,4), float)
A = np.empty((0,4), float)
app = np.array([1,1,1])

m=4
n=4



def getInnerText(oNode):
    rc = ""
    nodelist = oNode.childNodes
    for node in nodelist:
        if node.nodeType == node.TEXT_NODE:
            rc = rc + node.data
        elif node.nodeType==node.ELEMENT_NODE:
            rc = rc + getInnerText(node)   # recursive !!!
        elif node.nodeType==node.CDATA_SECTION_NODE:
            rc = rc + node.data
        else:
            # node.nodeType: PROCESSING_INSTRUCTION_NODE, COMMENT_NODE, DOCUMENT_NODE, NOTATION_NODE and so on
           pass
    return rc





def create_transf_matrix(filename, camid):


	stream = pulldom.parse(filename) 
	for event, node in stream:


		if event == "START_ELEMENT" and node.nodeName == "camera":
			
			#this is the node attribute to check.
			file = str(camid)

			if node.getAttribute("id") == file:
				stream.expandNode(node) # node now contains a mini-dom tree
				type_nodes = node.getElementsByTagName('transform')
				for type_node in type_nodes:
					# type_text will have the value of what's inside the type text
					type_text = getInnerText(type_node)
					nums = [float(n) for n in type_text.split()]

					#GUARD TO RECOVER FROM EXCEPTION WHEN CAMERA IS NOT REGISTERED AND THE XML NODE IS EMPTY
					if not nums:
						return 0
					else :

						matrix = np.array(nums).reshape(m,n)
                    	
                    	#delete last column, last row from transformation matrix to obtain Rotation matrix

						temp = np.delete(matrix, 3, axis=0)

						Rotation = np.delete(temp, 3, axis=1)

                    	#obtain translation vector

						last_column = np.array(matrix[:, 3])

                    	#delete last row from translation vector

						T = np.delete(last_column ,3 , axis=0)
						Trans_row =  np.array([T])

						translation = np.transpose(Trans_row)
						R = np.transpose(Rotation)
                    	#setup for numpy multiplication

						mx= np.matrix(R)
						my= np.matrix(translation)
						r = (-1)*mx*my
						R = np.transpose(r)
						R = np.around(R,3)
						Trans_row = np.append(Trans_row, app[0])
						return Trans_row



def change_basis(A, B):

	assert len(A) == len(B)

	A = np.matrix(A)
	B = np.matrix(B)

	scale = A*np.linalg.pinv(B, rcond=1e-5)


	R, S = scipy.linalg.rq(scale)


	return scale  
	




#WE ARE NOT USING THIS FUNCTION ANYMORE, BUT KEEP IT.

def rigid_transform_3D(A, B):
    assert len(A) == len(B)

    A = np.matrix(A)
    B = np.matrix(B)

    N = A.shape[0]; # total points

    centroid_A = mean(A, axis=0)
    centroid_B = mean(B, axis=0)
    
    # centre the points
    AA = A - tile(centroid_A, (N, 1))
    BB = B - tile(centroid_B, (N, 1))

    # dot is matrix multiplication for array
    H = transpose(AA) * BB

    U, S, Vt = linalg.svd(H)

    R = Vt * U.T

    # special reflection case
    if linalg.det(R) < 0:
       print ("Reflection detected")
       Vt[2,:] *= -1
       R = Vt.T * U.T

    t = -R*centroid_A.T + centroid_B.T

  

    return R, t


if __name__ == '__main__':

	if(len(sys.argv)<4 or len(sys.argv)>4):

		print("Too many or too less arguments, We need two arguments, Camera reference and Camera estimated.")
		sys.exit(0);

	num =  int(sys.argv[3])
	for i in range(num):

		filename = os.path.basename(sys.argv[1])
		name, ext = os.path.splitext(filename)

		if (ext == '.xml'):

			x = np.array(create_transf_matrix(sys.argv[1],i))

		else:
			print("FILE is in text format")
		
		y = np.array(create_transf_matrix(sys.argv[2],i))


		if not y.any():
			print("")
		else:
			
			A = np.append(A, np.array([x]),axis =0)#ref coord
			B = np.append(B, np.array([y]),axis =0)

			

		
	A= np.transpose(A)
	B= np.transpose(B)

	S = change_basis(A, B)

	translation = np.array(S[:, 3])
	translation = np.delete(translation, 3, axis=0)

	#SCALE IS THE VECTOR LENGTH OF THE TRANFORMATION MATRIX

	sx = np.linalg.norm(np.array(S[:,0]))
	sy = np.linalg.norm(np.array(S[:,1]))
	sz = np.linalg.norm(np.array(S[:,2]))

	#ARRANGING SCALE FACTOR INTO 3X3 MATRIX
	scale = np.array([[sx, 0, 0],[0, sy, 0],[0, 0, sz]])

	#ROTATION VECTOR IN X, Y, Z DIRECTION IS OBTAINED BY DIVIDING EACH COLUMN VECTOR OF TRANSFORMATION MATRIX
	#WITH SCALE FACTOR IN THAT AXIS

	rx = np.divide(np.array(S[:,0]), sx)
	ry = np.divide(np.array(S[:,1]), sy)
	rz = np.divide(np.array(S[:,2]), sz)
	
	#APPEND THE THREE COMPONENETS OF ROTAION TO FORM A 3X3 MATRIX	
	rx = np.append(rx,ry, axis = 1)
	rx = np.append(rx,rz, axis = 1)
	
	rotation = np.delete(rx ,3, axis =0)


	#CONVERT THE THREE NUMPY ARRAY FOR MATRIX OPERATION
	rotation = np.matrix(rotation)
	scale = np.matrix(scale)
	translation = np.matrix(translation)




	for i in range(num):
		
		x = create_transf_matrix(sys.argv[1],i)
		y = create_transf_matrix(sys.argv[2],i)
		
		y= np.matrix(y)
		y = transpose(y)

		
		if not y.any():

			print("Camera number: %d not registered" %i)

		else:

			x =np.matrix(x)
			x = transpose(x)
			y = np.delete(y,3,axis=0)
			x = np.delete(x,3,axis=0)

			y_new = rotation*y 
			y_new = scale * y_new +translation

			err = np.linalg.norm(x - y_new)

			err = multiply(err, err)

			error_sum = 0
			error_sum = error_sum + err

	rmse = sqrt(error_sum/num);

	print("The root mean square error between reference camera pose and recovered camera pose is %5f" %( error_sum))
		
		









		



		

	



