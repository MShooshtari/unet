from glob import glob
import random
from PIL import Image
import os 

def divide_train_test(img_folder, lbl_folder, ratio=0.2):
	img_folder_list = glob(img_folder+'/*.jpg')
	random.shuffle(img_folder_list)
	sample_size = int(len(img_folder_list)*ratio)

	img_train_list = img_folder_list[sample_size:]
	img_test_list = img_folder_list[:sample_size]

	lbl_train_list = [x.replace(img_folder, lbl_folder).replace('.jpg', '.png') for x in img_train_list]
	lbl_test_list = [x.replace(img_folder, lbl_folder).replace('.jpg', '.png') for x in img_test_list]

	return [img_train_list, img_test_list, lbl_train_list, lbl_test_list]


# Convert JPG to PNG
def convert_img_and_save(img_list, output_folder):
	for img_address in img_list:
		im = Image.open(img_address)
		output_address = output_folder + '/' + os.path.basename(img_address).replace('.jpg', '.png')
		im.save(output_address)

# Convert [0, 1] to [0, 255]
def convert_lbl_and_save(img_list, output_folder):
	for img_address in img_list:
		img = Image.open(img_address)
		pixels = img.load()
		for i in range(img.size[0]): # for every pixel:
			for j in range(img.size[1]):
				if pixels[i,j] > 0:
					pixels[i,j] = 255

		output_address = output_folder + '/' + os.path.basename(img_address)
		img.save(output_address)

img_folder = 'Original_Data/Planet_Tiffs_RGB_Corrected_Cropped_512'
lbl_folder = 'Original_Data/Mask_Tiffs_RGB_Corrected_Cropped_512'

img_train_folder = 'data_mahdi/satellite_roads/train/image'
img_test_folder = 'data_mahdi/satellite_roads/test/image'

lbl_train_folder = 'data_mahdi/satellite_roads/train/label'
lbl_train_folder = 'data_mahdi/satellite_roads/test/label'



[img_train_list, img_test_list, lbl_train_list, lbl_test_list]  = divide_train_test(img_folder, lbl_folder)

img_train_png_list = convert_img_and_save(img_train_list, img_train_folder) # Convert JPG to PNG
img_test_png_list = convert_img_and_save(img_test_list, img_test_png_list) # Convert JPG to PNG

lbl_train_png_list = convert_lbl_and_save(lbl_train_list, lbl_train_folder) # Convert [0, 1] to [0, 255]
lbl_test_png_list = convert_lbl_and_save(lbl_test_list, lbl_train_folder) # Convert [0, 1] to [0, 255]

