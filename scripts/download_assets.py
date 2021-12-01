import json
import requests
import shutil
import os.path
counter = 0
dupe_count = 0
digest={}

with open('data/gifs_allow_listed.ndjson') as infile:
	for line in infile:

		data = json.loads(line)


		

		# print(data['digest'],data['wayback_url'])
		if data['digest'] not in digest:
			digest[data['digest']] = True

		else:
			print('dupe')
			print(data['wayback_url'])
			dupe_count+=1

		if os.path.isfile('data/assets/gif/'+data['digest']+'.gif') == True:
			# print('skipp')
			counter+=1
			continue

		url = data['wayback_url']
		response = requests.get(url, stream=True)
		with open('data/assets/gif/'+data['digest']+'.gif', 'wb') as out_file:
			shutil.copyfileobj(response.raw, out_file)

		del response		

print(counter,dupe_count)
