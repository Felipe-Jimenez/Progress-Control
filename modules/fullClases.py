from modules.jsonFiles import *
#///////////////////////CLASS HOUSE///////////////////////////////
class House:#note: change the constructor to only one parameter with the json and move createJson to apple
    #general constructor
    def __init__(self,dictionary):
        self.dictionary = dictionary
        #self.dictionary = json.loads(json.dumps(self.__createJsonHouse()))#create a dicctionary from a json structure

    #return self dictionary converto to a json object
    def chargeJson(self):
        return json.loads(json.dumps(self.dictionary))

#///////////////////////CLASS APPLE///////////////////////////////
class Apple:
    #constructor with houses type
    def __init__(self,name,n_houses,typeh,start,final):
        self.name = name
        self.n_house = n_houses
        self.start = start
        self.final = final
        self.listHouses = []
        self.jsonA = {}#apple json(void structure)
        self.__createApple(typeh)

    #create a number of houses, but don't fill your own json
    def __createApple(self, typeh):
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

        return data[index]['data']

#///////////////////////CLASS WORKSPACE///////////////////////////////
class WorkSpace:
    def __init__(self, name):
        self.name = name
        self.listApples = []
