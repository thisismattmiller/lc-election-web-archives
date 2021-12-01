import gzip
import shutil
import glob
import os.path


path_from = "/Volumes/BigGlum/lc_elections_webarchives/*.gz"
path_to = "/Volumes/BigGlum/lc_elections_webarchives_extracted/"


files = glob.glob(path_from)

c=1
for file in files:

	filename = file.split('/')[-1][0:-3]

	print(f"{c}/{len(files)} - {filename}")

	if os.path.isfile(f"{path_to}{filename}") == False:

		try:
			with gzip.open(file, 'rb') as f_in:
				with open(f"{path_to}{filename}", 'wb') as f_out:
					shutil.copyfileobj(f_in, f_out)
		except:
			print('ERROR')
	else:
		print('skip')
	c+=1