import json

extract = "data/extract_gif.cdx"


domain_check = {}
dupe_check = {}
dupe_count = 0
counter = 1

final_list = open('data/user_content.ndjson','w')


with open(extract) as infile:

	for line in infile:

		# print(f"{counter}...dupes:{dupe_count}")
		counter+=1
		data = line.split(' ')	

		if data[9] == '-':
			data[9] = None
		else:
			try:
				data[9] = int(data[9])
			except ValueError:
				continue


		record = {

			'file': data[0],
			'urlkey': data[1],
			'timestamp': data[2],
			'original': data[3],
			'mimetype': data[4],
			'statuscode': data[5],
			'digest': data[6],
			'redirect': data[7],
			'metatags': data[8],
			'file_size': data[9],
			'offset': data[10],
			'WARC': data[11],
			'wayback_url': f"https://webarchive.loc.gov/all/{data[2]}/{data[3]}"



		}


		if record['file_size'] == None:
			continue


		if record['file_size'] > 15000:

			if record['original'] not in dupe_check:
				dupe_check[record['original']] = record['file_size']
			else:
				if dupe_check[record['original']] == record['file_size']:

					dupe_count+=1
					continue

			



			#'glitter-graphics.net' in record['original'] or 
			if 'glitter-graphics.net' in record['original'] or 'tumblr.com' in record['original']:
				for k in record:
					print(k," : ",record[k])

				print('----')
				final_list.write(json.dumps(record)+'\n')


final_list.close()
# domain_check = dict(sorted(domain_check.items(), reverse=True, key=lambda item: item[1]))
# json.dump(domain_check,open('data/domain_check.json','w'),indent=2)

