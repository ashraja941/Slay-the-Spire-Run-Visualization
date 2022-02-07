from asyncore import write
from cProfile import label
import csv
from itertools import count
import json

def GenerateGephiData(dict):
    fileString = 'GephiData/DATA.csv'
    print("Generating weights...")
    with open(fileString,'w') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Source", "Target", "Weight"])
        for key in dict.keys():
            for node in dict[key].keys():
                writer.writerow([key,node,dict[key][node]])

def GenerateGehpiLabels(dict):
    fileString = 'GephiData/LABELS.csv'
    print("Generating Lables...")
    with open(fileString,'w') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["ID", "Label", "Count"])
        for key in dict.keys():
            writer.writerow([key,key,dict[key]['count']])
            #print(dict[key])

if __name__ == "__main__":
    with open('data.json','r') as f:
        labelDict = json.load(f)
    with open('overlap.json','r') as f:
        dataDict = json.load(f)

    GenerateGehpiLabels(labelDict)
    GenerateGephiData(dataDict)