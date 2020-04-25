import json
import os

#read and return a list with the templates house dictionary
def chargeTemplates():
    with open("json/templates.json") as file:
        data = json.load(file)

    data = json.loads(json.dumps(data))
    return data

#read and return a json structure with the apples of a specific work Space
def chargeWorkSpace(name):
    root = "data/"+name+".json"
    if(os.stat(root).st_size == 0):
        return 0

    with open(root) as file:
        data = json.load(file)
   

    data = json.loads(json.dumps(data))
    return data

#return the name of the prototypes of created houses
def listPrototypes():
    types = []
    with open("json/templates.json") as file:
        data = json.load(file)

    data = json.loads(json.dumps(data))
    for key in data:
        types.append(key['proto'])

    return types

#read an return a dictionary with the names and file names of all the Work spaces
def listWorkSpaces():
    WSpaces = {}

    if(os.stat("data/data.json").st_size == 0):
        return 0

    with open("data/data.json") as file:
        data = json.load(file)
    data = json.loads(json.dumps(data))

    for wk in data:
        WSpaces[wk['name']] = wk['file']

    return WSpaces

#open data.json and write a new work space
def writeWS(name):
    data = {
        'name':name,
        'file':name+".json"
    }

    dictionary = []

    if(os.stat("data/data.json").st_size != 0):
        with open("data/data.json") as file:
            dictionary = json.load(file)
        dictionary = json.loads(json.dumps(dictionary))
    
    dictionary.append(data)
    
    with open("data/data.json", 'w') as file:
        json.dump(dictionary, file, indent=4)

    file = open("data/"+data['file'], "w")
    file.close()

