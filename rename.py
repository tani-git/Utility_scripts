import os
pp = "filepath"
count = 0

l = os.listdir(pp)
# l = [i for i in l if i[0] not in "U."]

def rename(fol):
    global count
    files = os.listdir(fol)
    for i in files:
        path = os.path.join(fol, i)
        new_path = os.path.join(fol, str(count) + ".jpg")
        os.rename(path, new_path)
        count += 1



for i in l:
    rename(os.path.join(pp, i))