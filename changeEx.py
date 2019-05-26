import glob, os

folder = "/home/ashok/Desktop/chekI"

for filename in glob.iglob(os.path.join(folder, '*.jpeg')):
    os.rename(filename, filename[:-4] + '.jpg')