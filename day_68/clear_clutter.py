import os
files = os.listdir()
count =1
for file in files:
    if file == "clear_clutter.py":
        continue
    name , extension = os.path.splitext(file)
    new_name = str(count) + extension
    os.rename(file, new_name)
    count = count +1