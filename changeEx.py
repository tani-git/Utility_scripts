import glob, os

folder = "filepath"

for filename in glob.iglob(os.path.join(folder, '*.jpeg')):
    os.rename(filename, filename[:-4] + '.jpg')