"""
import json 
f = open('prelim_test/test.json')
data = json.load(f)
dict = {}
count=1
for i in data['master_deck']:
    if dict.get(i):
        dict[i] = dict[i]+1
    else:
        dict.update({i:1})
print(dict)
f.close()
"""

i = "STreamline+1"
i = i[:-2]
print(i)