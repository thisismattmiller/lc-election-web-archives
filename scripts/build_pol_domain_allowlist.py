import requests
import json

sources = ['https://www.loc.gov/web-archives/?fa=partof:united+states+elections+2000&fo=json',
'https://www.loc.gov/web-archives/?fa=partof:united+states+elections+2002&fo=json',
'https://www.loc.gov/web-archives/?fa=partof:united+states+elections+2004&fo=json',
'https://www.loc.gov/web-archives/?fa=partof:united+states+elections+2006&fo=json',
'https://www.loc.gov/web-archives/?fa=partof:united+states+elections+2008&fo=json',
'https://www.loc.gov/web-archives/?fa=partof:united+states+elections+2010&fo=json',
'https://www.loc.gov/web-archives/?fa=partof:united+states+elections+2012&fo=json',
'https://www.loc.gov/web-archives/?fa=partof:united+states+elections+2013&fo=json',
'https://www.loc.gov/web-archives/?fa=partof:united+states+elections+2014&fo=json',
'https://www.loc.gov/web-archives/?fa=partof:united+states+elections+2015&fo=json',
'https://www.loc.gov/web-archives/?fa=partof:united+states+elections+2016&fo=json',
'https://www.loc.gov/web-archives/?fa=partof:united+states+elections+2017&fo=json',
'https://www.loc.gov/web-archives/?fa=partof:united+states+elections+web+archive&fo=json']


domains = []

for s in sources:
	print(s)
	response = requests.get(s)
	data = json.loads(response.text)

	for r in data['content']['results']:
		
		if 'scopes' in r['item']:
			domains = domains + r['item']['scopes']
		if 'source_url' in r['item']:
			domains = domains + r['item']['source_url']




domains_filtered = {}

for d in domains:

	d = d.replace('http://','')
	d = d.replace('https://','')
	d = d.replace(' (domain)','')
	d = d.strip()
	if d not in domains_filtered:
		domains_filtered[d] = 0

	domains_filtered[d]+=1


domains_filtered = dict(sorted(domains_filtered.items(), reverse=True, key=lambda item: item[1]))
json.dump(domains_filtered,open('data/domains_allowlist.json','w'),indent=2)

common_domains = {}

for d in domains_filtered:

	d = d.replace('www.','')
	d = d.split('/')
	if d[0] not in common_domains:
		common_domains[d[0]] = 0
	
	common_domains[d[0]]+=1

common_domains = dict(sorted(common_domains.items(), reverse=True, key=lambda item: item[1]))
json.dump(common_domains,open('data/domains_common.json','w'),indent=2)







