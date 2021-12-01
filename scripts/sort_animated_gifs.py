from PIL import Image, UnidentifiedImageError
import glob
from shutil import copyfile


from_dir = 'data/assets/gif/*.gif'
from_dir = 'data/assets/user_content/*.gif'



for file in glob.glob(from_dir):

	is_animated = False

	try:
		is_animated = Image.open(file).is_animated
	except AttributeError:
		print(file, " is not a gif")
	except UnidentifiedImageError:
		print(file, " is broken")
	except OSError:
		print(file, " is broken")


	if is_animated == True:
		# copyfile(file, file.replace('/gif','/gif_animated'))
		copyfile(file, file.replace('/user_content','/user_content_animated'))


