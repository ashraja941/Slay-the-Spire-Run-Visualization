import os

folder = r'THE_SILENT\\'
count = 1

for file_name in os.listdir(folder):
    source = folder + file_name
    destination = folder + "RUN_" + str(count) + ".json"
    os.rename(source,destination)
    count+=1

print('All files have been renamed')