from modules.jsonFiles import *
#///////////////////////CLASS HOUSE///////////////////////////////
class House:
    #constructor with dictionary paramether
    def __init__(self,dictionary):
        self.dictionary = dictionary
        #self.dictionary = json.loads(json.dumps(self.__createJsonHouse()))#create a dicctionary from a json structure

    #return self dictionary 
    def chargeDict(self):
        return self.dictionary

#///////////////////////CLASS APPLE///////////////////////////////
class Apple:
    #constructor to void apples
    def __init__(self,name, n_house, start, final):
        self.name = name
        self.n_house = n_house
        self.start = start
        self.final = final
        self.listHouses = []

    #create a number of houses with a prototype
    def fillApple(self, typeh):
        if(typeh != "null"):
            for x in range(self.start,self.final+1):
                self.listHouses.append(House(self.__createDictHouse(typeh)))
                self.listHouses[-1].dictionary['n'] = x
                self.listHouses[-1].dictionary['type'] = typeh

    #import a templates of house and return a dictionary with a correct prototype
    def __createDictHouse(self, typeh):
        data = chargeTemplates()
        index = 0
        for a in data:
            if(a['proto'] == typeh):
                break
            index+=1

        if(index == len(data)):
            index = 0

        return data[index]['data']

    #create a dictionary structure with own information
    def chargeDict(self):
        jsonA = {}
        jsonA['name'] = self.name
        jsonA['n_house'] = self.n_house
        jsonA['start'] = self.start
        jsonA['final'] = self.final
        jsonA['houses'] = []
        for i in self.listHouses:
            jsonA['houses'].append(i.chargeDict())

        return jsonA

#///////////////////////CLASS WORKSPACE///////////////////////////////
class WorkSpace:
    def __init__(self, name):
        self.name = name
        self.listApples = []

    #take a json file and load that in a instace of Workspace object
    def loadJson(self, data):
        if(data != ""):
            for i in data:#divide pher apples
                self.listApples.append(Apple(i['name'], i['n_house'], i['start'], i['final']))
                for h in i['houses']:
                    self.listApples[-1].listHouses.append(House(h))

    #save the workspace data in json file     
    def save(self):
        data = []
        for i in self.listApples:
            data.append(i.chargeDict())

        archive = "data/"+self.name+".json"
        with open(archive, 'w') as file:
            json.dump(data, file, indent=4)