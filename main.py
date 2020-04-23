from modules.interface import *

#////////////////////////////////////////////////////////////
def menuObras():
    print(".:OBRAS:.\n")
    print("1) Agregar nueva obra")
    print("2) Acceder a una Obra")
    print("3) eliminar una obra")
    x = input("__")
    
#LOAD FILE WITH ALL THE OBRA'S NAME AND REGISTERED    
def loadObras():
    file = open("json/Obras.txt","r")
    print (file)

#IMPORT THE ASOICIATED FILE TO ANY OBRA
def importObra(ruta):
    with open(ruta) as cont:
        obra = json.load(cont)
        for apple in obra:
            print(apple.get('name'))


if __name__ == "__main__":
    #nota: ya funciona main, pero solo recupera el json de la obra, aun falta que lo cargue en su esctructura
    mainWindow()
    #formApple(obra1)
    #showWorkspace(obra1)

    #showHouse(obra1.listApples[0].listHouses[0])
    #showHouse(obra1.listApples[0].listHouses[1])
