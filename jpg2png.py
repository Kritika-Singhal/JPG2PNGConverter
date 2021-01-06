from PIL import Image
import sys
import os
​
# grab the first and second argument
image_folder = sys.argv[1]
output_folder = sys.argv[2]
​
​
# check if folder exits, if not create it 
if not os.path.exists(output_folder):
	os.makedirs(output_folder)
​
​
# loop through pokedex, convert images to png, save it to new folder
for filename in os.listdir(image_folder):
	img = Image.open(f'{image_folder}{filename}')
​
	# to remove file extension from filename
	filename = os.path.splitext(filename)[0]
​
	img.save(f'{output_folder}{filename}.png','png')