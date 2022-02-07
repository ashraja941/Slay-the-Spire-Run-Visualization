from itertools import count
import json 
import os


folder = r'THE_SILENT\\'
#os.chdir(folder)
dict = {}
mergeUpgrades = True

def Count(path,dict,name):
    f = open(path)
    data = json.load(f)
    for i in data['master_deck']:
        if i[-2:] == "+1" and mergeUpgrades:
            i = i[:-2]
        if dict.get(i):
            dict[i]['count'] = dict[i]['count'] + 1
            dict[i]['runs'].append(name)
        else:
            dict.update({i:{'count':1,'runs':[name]}})
    f.close()

for file in os.listdir(folder):
    if file.endswith(".json"):
        path = f"{folder}\{file}"
        Count(path,dict,file)

print(dict)
