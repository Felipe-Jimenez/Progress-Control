import json
#read and return a list with the templates house dictionary
def chargeTemplates():
    with open("json/templates.json") as file:
        data = json.load(file)

    data = json.loads(json.dumps(data))
    return data

def listPrototypes():
    types = []
    with open("json/templates.json") as file:
        data = json.load(file)
    data = json.loads(json.dumps(data))
    for key in data:
        types.append(key['proto'])

    return types
