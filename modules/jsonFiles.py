import json
#read and return a list with the templates house dictionary
def chargeTemplates():
    with open("json/templates.json") as file:
        data = json.load(file)

    data = json.loads(json.dumps(data))
    return data

#read and return a json structure with the apples of a specific work Space
def chargeWorkSpace(name):
    root = "data/"+name+".json"
    with open(root) as file:
       data = json.load(file)

    data = json.loads(json.dumps(data))
    return data

#return the name of the prototypes of houses created
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
    with open("data/data.json") as file:
        data = json.load(file)
    data = json.loads(json.dumps(data))

    for wk in data:
        WSpaces[wk['name']] = wk['file']

    return WSpaces
