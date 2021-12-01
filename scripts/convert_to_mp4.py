import glob
import subprocess

for file in glob.glob('data/assets/glitter-graphics/*.gif'):

	print(file)

	newfile = file.replace('glitter-graphics','glitter-graphics_mp4')
	newfile = newfile.replace('.gif','.mp4')
	print(newfile)

	return_code = subprocess.call(f"ffmpeg -i {file} {newfile}", shell=True)
	print(return_code)