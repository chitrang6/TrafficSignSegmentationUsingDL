# Author: Chitrang Talaviya 



# Here We will use three techniques for the data augmentation one is brighness , translation and straching 



def brightness_aug(image , bright_param):
	image_temp = cv2.cvtColor(image,cv2.COLOR_RGB2HSV)
	brighness_control = bright_param + np.random.uniform()
	image_temp[:,:,2] = image_temp[:,:,2] * brighness_control
	final_image = cv2.cvtColor(image_temp,cv2.COLOR_HSV2RGB)
	return final_image




def translation_aug(image, BBoxe , translation_range):
	BBoxe = BBoxe.copy(deep = True)
	translation_x = translation_range*np.random.uniform() - translation_range/2
	translation_y = translation_range*np.random.uniform() - translation_range/2

	translation_matrix = np.float32([[1,0,translation_x],[0,1,translation_y]])
	row , col , channnels = image.shape

	translated_image = cv2.warpAffine(image , translation_matrix , (col, row))
	BBoxe['xmin'] = BBoxe['xmin'] + translation_x # As we are transalting the image we have to add this range in x and y direction
	BBoxe['xmax'] = BBoxe['xmax'] + translation_x
	BBoxe['ymin'] = BBoxe['ymin'] + translation_y
	BBoxe['ymax'] = BBoxe['ymax'] + translation_y
	return translated_image, BBoxe

