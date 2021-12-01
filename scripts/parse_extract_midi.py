import json

extract = "data/extract_gif.cdx"


domain_check = {}
dupe_check = {}
dupe_count = 0
counter = 1
with open(extract) as infile:

	for line in infile:

		if 'audio/midi' in line:

			# print(f"{counter}...dupes:{dupe_count}")
			counter+=1
			data = line.split(' ')	
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
				'file_size': int(data[9]),
				'offset': data[10],
				'WARC': data[11],
				'wayback_url': f"https://webarchive.loc.gov/all/{data[2]}/{data[3]}"



			}
			for k in record:
				print(k," : ",record[k])

			print('----')



			
			# if record['file_size'] > 15000:

			# 	if record['original'] not in dupe_check:
			# 		dupe_check[record['original']] = record['file_size']
			# 	else:
			# 		if dupe_check[record['original']] == record['file_size']:

			# 			dupe_count+=1
			# 			continue

			# 	tld = record['urlkey'].split(')')[0].split(',')[0:2]
			# 	tld = ".".join([tld[1],tld[0]])
			# 	if tld not in domain_check:
			# 		domain_check[tld] = 0

			# 	domain_check[tld]+=1



			# 	#'glitter-graphics.net' in record['original'] or 
			# 	if 'blingee.com' in record['original']:
			# 		for k in record:
			# 			print(k," : ",record[k])

			# 		print('----')



# domain_check = dict(sorted(domain_check.items(), reverse=True, key=lambda item: item[1]))
# json.dump(domain_check,open('data/domain_check.json','w'),indent=2)

