import glob

def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]




files_chunks = chunks(list(glob.glob('data/assets/user_content_animated/*.gif')),1000)

count = 1
for chunk in files_chunks:

	print(count)
	html = """
		
		<html>
			<head></head>
			<body style="background:black"></body>
	"""

	for file in chunk:
		file = file.split('/')[-1]
		html = html + f'<img loading="lazy" src="{file}">\n'

	

	count+=1

	html = html + f'<a href="{count + 1}.html">Page {count + 1}</a>'

	with open(f'data/assets/user_content_animated/{count}.html','w') as outfile:

		outfile.write(html)