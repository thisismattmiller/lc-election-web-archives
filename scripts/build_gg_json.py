import json

allgg=[]

# with open('data/glitter-graphics.ndjson') as f:

# 	for line in f:


# 		d = json.loads(line)

# 		allgg.append(d['digest'])


# json.dump(allgg,open('data/gg.json','w'))

data = json.load(open('data/gg.json'))

data = list(set(data))

json.dump(data,open('data/gg.json','w'))

