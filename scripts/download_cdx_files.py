import requests
import glob
import shutil
import os.path

save_to_dir = "/Volumes/BigGlum/lc_elections_webarchives/"

base = 'https://d2rxokvmqqcpq7.cloudfront.net/'


def download_file(url):
    local_filename = f"{save_to_dir}{url.split('/')[-1]}"

    with requests.get(url, stream=True) as r:
        with open(local_filename, 'wb') as f:
            shutil.copyfileobj(r.raw, f)


    return local_filename




cdxs = []
for file in glob.glob('manifest/*.txt'):

	with open(file) as manifest:
		for line in manifest:
			
			cdx = line.strip().split('\t')[1]
			cdxs.append(cdx)

counter = 0


already_downloaded = {}
print('building already downloaded lookup')
for file in glob.glob(f"{save_to_dir}*.gz"):

	file = file.split('/')[-1]

	already_downloaded[file] = True







for c in cdxs:

	counter+=1

	print(f"{counter}/{len(cdxs)} - {c}")

	if c.split('/')[-1] in already_downloaded:
		print('Skipping, already exists...')
		continue

	print(f"{save_to_dir}{c.split('/')[-1]}")
	# if os.path.isfile(f"{save_to_dir}{c.split('/')[-1]}") == False:
	download_file(f"{base}{c}")
	# else:
	# 	print('Skipping, already exists...')






