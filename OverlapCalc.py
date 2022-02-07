import json
from re import template 

with open('data.json','r') as f:
    dict = json.load(f)
    print("JSON Read...")

overlap = {}
completedRuns = []
count = 1

for key in dict:
    dict[key]['runs'] = set(dict[key]['runs'])

for key in dict:
    tempList = {}

    print(str(count)+"/"+str(len(dict.keys())))

    for comparisonKey in dict:
        if(comparisonKey != key and comparisonKey not in completedRuns):
            overlapSize = len(dict[key]['runs'] & dict[comparisonKey]['runs'])
            tempList[comparisonKey] = overlapSize
    overlap[key] = tempList
    completedRuns.append(key)
    count+=1

print(overlap)
with open('overlap.json','w') as fp:
    json.dump(overlap,fp)