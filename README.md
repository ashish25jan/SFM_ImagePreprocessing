
The readme file is organised as follows:
1. Requirements
2. File structure
3. How to run the code
4. How to use Photoscan pro
5. How to run Evaluation

Requirements
1. Python 3(3.5 desired).
2. Python signal processing module scipy,scikit,skimage.
3. Python Image processing module.
4. Python wrapper for Matlab.
5. Python numpy module.
6. Matlab R2015 with Image processing toolbox.
7. OpenCV 3.0
8. GIMP(only if image editing is required).
9. Photoscan Pro(version is important, since script are version specific).
10. ImageMagick(only if noise is to be added)

File Structure

The main directory contains two sub folders:
• Python&Opencv
• Matlab&Python Wrapper

Opencv & Python :
The codes files inside this folder can be run through the main.py with following command:

python main.py <Type of Image Processing> <Type Of Filter> <Path To dataset/*.format> (1)

Type Of Image Processing = CE or denoise(case sensitive)
Type of Filters:

Filter Type			            Command line option

1. Bilateral Filter         =>       bilateral
2. Gaussian Filter 			    =>       gaussian
3. Non-Local Mean 				  =>       Nlm
4. Total Variation Filter 	=>		   Tv
5. Wavelet Denoising 			  =>       Wavelet
6. Wiener Filter 				    =>       Wiener
7. Sigmoid Gamma Correction =>		   sigmoid
8. CLAHE 				            =>    	 clahe
9. Logarithmic Gamma Correction  =>  log
10. Histogram Equalisation 			 =>  he

Once this command (1), is executed, a folder with the name of processing type (CE or
denoising) is created, which contains folder with the name of the type of filter used. This
folder contains the processed dataset.

These folders are created inside the directory where main.py exists. After running main.py for
one dataset, please move and save it in different location, otherwise, when you run process
for second time, all the images will get modified or lost.
Matlab&Python Wrapper:
The folder contains four sub-folders:
1. BPDHE
2. DHECI
3. DONG
4. TRISTATE

Running the code inside this is tricky since it’s a wrapper for matlab code. Hence, if you run
into problem, kindly let me know. Its not the problem with the code but with the complexity
of python wrapper for matlab.

BPDHE(CE)
Run the bpdhe.py file as below:
python bpdhe.py <path to dataset>
There is one problem with this implementation, it outputs a rotated image.
To get the correct orientation, please run the rotate.py as below:
python rotate.py <path to image processed by bpdhe/*.format >

DHECI(CE)
Run the dheci.py file as below:
python dheci.py <path to dataset/*.format >

DONG(CE)
Run the dong.py file as below:
python dong.py <path to dataset/*.format >

TRISTATE(denoising)
Run the tristate.py file as below:
python tristate.py <path to dataset/*.format >

The above matlab codes saves the processed image in the same folder in which they exist.
Running Photoscan:
• File -> new -> add all the images you require.
• Workflow -> Allign Photo
o Set tie points to 200,000.
• After the allignment is done. Get camera pose from Tools -> Export
Camera (XML format)
• Reprojection Error can be calculated by the code provided in the
submission_code folder(reprojectioner.py)
• Tool -> Run Script -> repro.py. This prints the reprojection error for whole
chunk.
• If you want to Build Dense Cloud. Workflow -> Build Dense Cloud

Running Evaluation:
The evaluation can be run by following command:
Python Evaluator.py <reference_camera.xml> <estimated_camera.xml>
This prints the result on terminal.
Notes:
o To obtain the camera pose from photoscan, you would have to obtain trial
licence. Its normally for 30 days.
o You can create your own reference camera.xml file, but I don’t have any
interface for it. You can obtain transformation matrix from projection
matrix by using pro2trans.py in submission folder. Commandpython
pro2trans.py <path to file/*.format>
It expects the projection matrix for individual cameras in separate files.
o The matlab codes takes a while to initiates and is very slow.


Datasets:
https://cvlab.epfl.ch/data/strechamvs/ - Semper, City Hall.
https://www.gcc.tu-darmstadt.de/home/proj/mve/ -MVE Kermit
https://github.com/rfabbri/pavilion-multiview-3d-dataset - Pavilion dataset
https://icwww.epfl.ch/~marquez/multiview/denseMVS.html - Fountain_dense, Herzues
