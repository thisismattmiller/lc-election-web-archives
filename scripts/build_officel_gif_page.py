import json
import glob
from shutil import copyfile

alld = {}

with open('data/gifs_allow_listed.ndjson') as f:

	for line in f:


		d = json.loads(line)

		alld[d['digest']] = d



gifs = list(glob.glob('data/assets/gif_animated/*.gif'))

count = 1


print(count)
html = """
	
	<html>
		<head></head>
		<body style=""></body>
		<style>
			.img-div{
				display:inline-block;
				margin:1em;
				border: 1px solid gray;

			}
		</style>

"""

years = {} 

for file in gifs:

	digest = file.split('/')[-1].split('.')[0]



	if alld[digest]['timestamp'][0:4] not in years:
		years[alld[digest]['timestamp'][0:4]] = []

	years[alld[digest]['timestamp'][0:4]].append(alld[digest])


for year in sorted(years):

	html = html + f'<hr><div style="background-color:whitesmoke; color:black"><h1 style="font-size:4em;margin:0">{year}</h1></div><hr>'

	for data in years[year]:
		print(data)
		html = html + f'<div class="img-div"><img loading="lazy" src="img/{data["digest"]}.gif"><details><summary>Details</summary><pre><code>{json.dumps(data,indent=2)}</code></pre></details></div>\n'


		copyfile(f"data/assets/gif_animated/{data['digest']}.gif", f"offical/img/{data['digest']}.gif")

# print(sorted(years.keys()))
	# for file in chunk:
	# 	file = file.split('/')[-1]
	# 	html = html + f'<img loading="lazy" src="{file}">\n'

	

	# count+=1

	# html = html + f'<a href="{count + 1}.html">Page {count + 1}</a>'

with open(f'offical/index.html','w') as outfile:

	outfile.write(html)