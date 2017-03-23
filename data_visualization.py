#Author: This file contains the necessary helper function for the image and its bounding box visualization. 



from augmentation import *

def get_image_and_BB(Dataframe , index , size = (640 , 300) , aug = False):

	file_path = Dataframe['fpath'][index] # This will give us the file path of the perticular image in the data set.

	# Lets open the image 
	img = cv2.imread(file_path)
	imgSize = np.shape(img)
	# Now, resizing the image
	#img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    #img = cv2.resize(img,size)
    bb_boxes = df[df['fpath'] == file_path].reset_index()
    if aug == True:
    	img,bb_boxes = translation_aug(img,bb_boxes,trans_range)
    	img = brightness_aug(img)



