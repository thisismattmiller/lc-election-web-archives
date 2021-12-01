import json
import os.path
from shutil import copyfile



with open('data/glitter-graphics.ndjson') as inf: 


	for line in inf:

		data = json.loads(line)
		if os.path.isfile(f"data/assets/user_content/{data['digest']}.gif"):


			print(f"data/assets/user_content/{data['digest']}.gif")	

			copyfile(f"data/assets/user_content/{data['digest']}.gif", f"data/assets/glitter-graphics/{data['digest']}.gif")