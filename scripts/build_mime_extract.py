import glob


path_from = "/Volumes/BigGlum/lc_elections_webarchives_extracted/*.cdx"
path_to = 'data/extract_gif.cdx'
mime_type = " image/gif "



# path_to = 'data/extract_midi.cdx'
# mime_type = " audio/midi "
# mime_type2 = " audio/x-midi "


files = glob.glob(path_from)
counter = 1
errors = []


with open(path_to,'w') as outfile:

	for file in files:

		print(f"{counter}/{len(files)} - {file}")
		counter+=1
		try:
			with open(file) as infile:
				for line in infile:
					# if mime_type in line or mime_type2 in line:
					if mime_type in line:

						# add in the file name it came from as one of the data items
						outfile.write(file + ' ' + line)
		except UnicodeDecodeError as e:
			errors.append('unicode errror: ' + file)

print(errors)
