
import os
path = "file_path"
files = os.listdir(path)

li = [os.path.join(path,i) for i in os.listdir(path)]


def rename(files):
	i = 1
	for file in files:
	    # os.rename(os.path.join(path, file), os.path.join(path, str(i)+'.jpg'))
	    os.rename(os.path.join(path, file), os.path.join(path, str(i)))
	    i = i+1

for j in li:
	#i = 1 
	rename(j)