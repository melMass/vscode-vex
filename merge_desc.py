import json
from pprint import pprint

def mergeDescriptions(descriptions,mainsnippets,outfile):

    with open(descriptions) as data_file:    
        d = json.load(data_file)

    with open(mainsnippets) as data_file2:    
        m = json.load(data_file2)

    for i in data.keys():
        m[i]["description"] = d[i]["description"]

    with open(outfile,"w") as out:
        json.dump(m,out,sort_keys=True,indent=4)


descriptions = "./descriptionsh16.json"
mainsnippets = "./functionsh16.json"
outfile = "./h16.json"


mergeDescriptions(descriptions,mainsnippets,outfile)
