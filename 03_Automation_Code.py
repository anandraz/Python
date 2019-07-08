import shutil
import os

# Walking through a given path folder tree 

fetch_loc= '' #location where to search the file
req_ext='.pdf' #extension as per the requirement (.jpg,.pdf,.xlxs,.txt etc.)
store_loc=''

for folder,subfolder,filenames in os.walk(fetch_loc):
	for filename in filenames:
		if filename.endswith(req_ext):
			shutil.copy(filename, 'store_loc')	