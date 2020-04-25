from tkinter import *
from modules.fullClases import *

#charged Work Space
WSPACE = 0

#method with the root window
def mainWindow():
    #main window
    root = Tk()
    root.config()
    root.title("CONTROL DE PROCESOS")
    root.resizable(False,False)

    #left Frame
    leftFrame = Frame(root)
    leftFrame.config(width="450px", height="500px")
    leftFrame.pack(side="left")
    Label(leftFrame, text="CONTROL DE OBRAS", font=("Courier", 25)).grid(row=0, column=0, sticky=N, padx=10, pady=10)

    #title left fram
    Label(leftFrame,text="OBRAS", font=("Courier", 20)).grid(row=1, column=0, sticky = N)
    Button(leftFrame,text="Agregar", command=formWorkSpace).grid(row=1, column=1 ,sticky = N, padx=10, pady=5)

    #function to charge and show a WS
    def chargeAndShow(name):
      WSPACE = WorkSpace(name)
      if(chargeWorkSpace(name) != 0):
        WSPACE.loadJson(chargeWorkSpace(name))
      root.destroy()
      showWorkspace(WSPACE)


    #list Work Spaces
    wks = listWorkSpaces()
    r = 2
    if(len(wks)):#minimal exist one work space
        for a,b in wks.items():
            Label(leftFrame,text=a, font=("Courier", 14)).grid(row=r, column=0, sticky = W, padx=20, pady=2)
            Button(leftFrame,text="Ver", command=lambda n=a: chargeAndShow(n)).grid(row=r, column=1 ,sticky = N, padx=10, pady=5)
            r+=1
    #pendiente hacer el save de las obras pero que genere el archivo json y guarde la obra


    root.mainloop()

#form to add house or houses to self apple
def formHouse(apple):
    #create a window
    wNHouse = Toplevel()
    wNHouse.resizable(False,False)
    wNHouse.title("NUEVA CASA")

    #frame to title
    titleFrame = Frame(wNHouse)
    titleFrame.config(width="300px", height="30px")
    titleFrame.pack()
    Label(titleFrame,text=apple.name, font=("Courier", 18)).grid(row=0, column=0 ,sticky = N, pady=5)

    #frame to form
    formFrame = Frame(wNHouse)
    formFrame.config(width="300px", height="500px")
    formFrame.pack()

    #frame to button
    btnFrame = Frame(wNHouse)
    btnFrame.config(width="300px", height="30px")
    btnFrame.pack()


    cant = StringVar()
    cost = StringVar()
    prototype = StringVar()
    prototype.set("Selecciona")
    types = listPrototypes()
    start = StringVar()
    final = StringVar()
    
    #number of houses
    Label(formFrame,text="Cantidad", font=("Courier", 14)).grid(row=1, column=0 ,sticky = W,padx=10, pady=5)
    Entry(formFrame, textvariable=cant).grid(row=1, column=1 ,sticky = N, padx=20,pady=5)

    #prototype of houses
    Label(formFrame,text="Tipo", font=("Courier", 14)).grid(row=2, column=0 ,sticky = W,padx=10, pady=5)
    OptionMenu(formFrame, prototype, *types).grid(row=2, column=1 ,sticky = N, padx=20,pady=5)

    #star of n houses
    Label(formFrame,text="Inicio", font=("Courier", 14)).grid(row=3, column=0 ,sticky = W,padx=10, pady=5)
    Entry(formFrame, textvariable=start).grid(row=3, column=1 ,sticky = N, padx=20,pady=5)

    #final of n houses
    Label(formFrame,text="Final", font=("Courier", 14)).grid(row=4, column=0 ,sticky = W,padx=10, pady=5)
    Entry(formFrame, textvariable=final).grid(row=4, column=1 ,sticky = N, padx=20,pady=5)

    #function add Houses
    def add():
        if(prototype.get() != "Selecciona" and cant.get() != ""):
            apple.addHouses(prototype.get(), int(start.get()), int(final.get()))
            wNHouse.destroy()

    #button
    Button(btnFrame, text="Agregar", command=add).grid(row=0, column=0 ,sticky = N, pady=5)
    Button(btnFrame, text="Cancelar", command=lambda : wNHouse.destroy()).grid(row=0, column=1 ,sticky = N, pady=5)

    wNHouse.mainloop()

#form to extra concept in a specific hose
def formExtra(house):
    #create a window
    wExtra = Toplevel()
    wExtra.resizable(False,False)
    wExtra.title("EXTRA")

    #frame to title
    titleFrame = Frame(wExtra)
    titleFrame.config(width="300px", height="30px")
    titleFrame.pack()
    Label(titleFrame,text="CONCEPTO EXTRA", font=("Courier", 18)).grid(row=0, column=0 ,sticky = N, pady=5)

    #frame to form
    formFrame = Frame(wExtra)
    formFrame.config(width="300px", height="500px")
    formFrame.pack()

    #frame to button
    btnFrame = Frame(wExtra)
    btnFrame.config(width="300px", height="30px")
    btnFrame.pack()


    name = StringVar()
    cost = StringVar()
    state = StringVar()
    state.set("Selecciona")
    states = [True, False]
    
    #name fo concept
    Label(formFrame,text="Concepto", font=("Courier", 14)).grid(row=2, column=0 ,sticky = W,padx=10, pady=5)
    Entry(formFrame, textvariable=name).grid(row=2, column=1 ,sticky = N, padx=20,pady=5)

    #price of a concept
    Label(formFrame,text="Monto", font=("Courier", 14)).grid(row=3, column=0 ,sticky = W,padx=10, pady=5)
    Entry(formFrame, textvariable=cost).grid(row=3, column=1 ,sticky = N, padx=20,pady=5)

    #state of concept
    Label(formFrame,text="Estado", font=("Courier", 14)).grid(row=4, column=0 ,sticky = W,padx=10, pady=5)
    OptionMenu(formFrame, state, *states).grid(row=4, column=1 ,sticky = N, padx=20,pady=5)

    #function add new apple
    def addExtra():
        if(name.get() != "" and state != "Selecciona" and cost.get() != ""):
            house.dictionary[str(name.get())] = [int(cost.get()),bool(state.get())]
            wExtra.destroy()

    #button
    Button(btnFrame, text="Agregar", command=addExtra).grid(row=0, column=0 ,sticky = N, pady=5)
    Button(btnFrame, text="Cancelar", command=lambda : wExtra.destroy()).grid(row=0, column=1 ,sticky = N, pady=5)

    wExtra.mainloop()

#form to new Apple 
def formApple(WSpace):
    #create a window
    wapple = Toplevel()
    wapple.resizable(False,False)
    wapple.title(WSpace.name)

    #frame to title
    titleFrame = Frame(wapple)
    titleFrame.config(width="300px", height="30px")
    titleFrame.pack()

    #frame to form
    formFrame = Frame(wapple)
    formFrame.config(width="300px", height="500px")
    formFrame.pack()

    #frame to button
    btnFrame = Frame(wapple)
    btnFrame.config(width="300px", height="30px")
    btnFrame.pack()

    Label(titleFrame,text="NUEVA MANZANA", font=("Courier", 18)).grid(row=0, column=0 ,sticky = N, pady=5)

    name = StringVar()
    number = StringVar()
    typeH = StringVar()
    typeH.set("Selecciona")
    types = listPrototypes()
    start = StringVar()
    final = StringVar()
    
    #name
    Label(formFrame,text="Nombre", font=("Courier", 14)).grid(row=2, column=0 ,sticky = W,padx=10, pady=5)
    Entry(formFrame, textvariable=name).grid(row=2, column=1 ,sticky = N, padx=20,pady=5)

    #number of houses
    Label(formFrame,text="N.Casas", font=("Courier", 14)).grid(row=3, column=0 ,sticky = W,padx=10, pady=5)
    Entry(formFrame, textvariable=number).grid(row=3, column=1 ,sticky = N, padx=20,pady=5)

    #type house
    Label(formFrame,text="Tipo", font=("Courier", 14)).grid(row=4, column=0 ,sticky = W,padx=10, pady=5)
    OptionMenu(formFrame, typeH, *types).grid(row=4, column=1 ,sticky = N, padx=20,pady=5)

    #start
    Label(formFrame,text="Inicio", font=("Courier", 14)).grid(row=5, column=0 ,sticky = W, padx=10,pady=5)
    Entry(formFrame, textvariable=start).grid(row=5, column=1 ,sticky = N, padx=20,pady=5)

    #final
    Label(formFrame,text="Final", font=("Courier", 14)).grid(row=6, column=0 ,sticky = W,padx=10, pady=5)
    Entry(formFrame, textvariable=final).grid(row=6, column=1 ,sticky = N, padx=20,pady=5)

    #function add new apple
    def newApple():
        if(name.get() != ""):
            if(number.get() != "" and typeH != "Selecciona"):
                WSpace.listApples.append(Apple(name.get(), int(number.get()), int(start.get()), int(final.get())))
                WSpace.listApples[-1].fillApple(typeH.get())
            else:
                WSpace.listApples.append(Apple(name.get(),0,0,0))
            wapple.destroy()

    #button
    Button(btnFrame, text="Agregar", command=newApple).grid(row=0, column=0 ,sticky = N, pady=5)
    Button(btnFrame, text="Cancelar", command=lambda : wapple.destroy()).grid(row=0, column=1 ,sticky = N, pady=5)

    wapple.mainloop()

#form WorkSpace
def formWorkSpace():
    #create a window
    wWs = Toplevel()
    wWs.resizable(False,False)
    wWs.title("OBRA")

    #frame to title
    titleFrame = Frame(wWs)
    titleFrame.config(width="300px", height="30px")
    titleFrame.pack()
    Label(titleFrame,text="NUEVA OBRA", font=("Courier", 18)).grid(row=0, column=0 ,sticky = N, pady=5)

    #frame to form
    formFrame = Frame(wWs)
    formFrame.config(width="300px", height="500px")
    formFrame.pack()

    #frame to button
    btnFrame = Frame(wWs)
    btnFrame.config(width="300px", height="30px")
    btnFrame.pack()

    name = StringVar()
    
    #name fo concept
    Label(formFrame,text="Nombre", font=("Courier", 14)).grid(row=2, column=0 ,sticky = W,padx=10, pady=5)
    Entry(formFrame, textvariable=name).grid(row=2, column=1 ,sticky = N, padx=20,pady=5)

    #function add new apple
    def add():
        if(name.get() != ""):
            writeWS(name.get())
            wWs.destroy()

    #button
    Button(btnFrame, text="Agregar", command=add).grid(row=0, column=0 ,sticky = N, pady=5)
    Button(btnFrame, text="Cancelar", command=lambda : wExtra.destroy()).grid(row=0, column=1 ,sticky = N, pady=5)

    wWs.mainloop()

#show concepts of a specific house --falta boton para editar
def showHouse(house):
    #create a window
    whouse = Tk()
    whouse.resizable(False,False)
    whouse.title("Casa "+str(house.dictionary['n'])+": "+house.dictionary['type'])

    #option frame to new concept
    optionFrame = Frame(whouse)
    optionFrame.pack()
    Button(optionFrame, text="Extra", command=lambda : formExtra(house)).grid(row=0, column=0 ,sticky = N, pady=10)
    Button(optionFrame, text="Cerrar", command=lambda : whouse.destroy()).grid(row=0, column=1 ,sticky = N, pady=10)


    #frame with the table
    tableFrame = Frame(whouse)
    tableFrame.config(width="300px", height="300px")
    tableFrame.pack()

    #function to change state of atribute
    def changeState(key):
        house.dictionary[key][1] = True

    z = 0
    r=3
    #labels for table
    Label(tableFrame,text="CONCEPTO", font=("Courier", 18)).grid(row=1, column=0 ,sticky = N, pady=2)
    Label(tableFrame,text="MONTO", font=("Courier", 18)).grid(row=1, column=1, sticky = N, pady=2)
    Label(tableFrame,text="AVANCE", font=("Courier", 18)).grid(row=1, column=2, sticky = N, padx=10, pady=2)
    
    total = 0
    avance = 0
    for x,y in house.dictionary.items():
        state = "black"
        if(z>1):
            if(y[1]):
                state = "green"
            Label(tableFrame,text=x, font=("Courier", 14)).grid(row=r, column=0 ,sticky = W, padx=7,pady=2)
            Label(tableFrame,text="$ "+str(y[0]), font=("Courier", 14), fg=state).grid(row=r, column=1, padx=20, pady=2)
            Label(tableFrame,text=str(y[1]), font=("Courier", 14), fg=state).grid(row=r, column=2, padx=20, pady=2)
            if(y[1] == 0):
                Button(tableFrame, text="Realizado", command=lambda s = x: changeState(s)).grid(row=r, column=3 ,sticky = N, padx=10, pady=3)

            total+=y[0]
            if(y[1]):
                avance+=y[0]

        z+=1
        r+=1
    
    Label(tableFrame,text="TOTAL", font=(12)).grid(row=r, column=0 ,sticky = W, padx=5,pady=10)
    Label(tableFrame,text="$"+str(total), font=(12), fg="red").grid(row=r, column=1, padx=20, pady=10)
    Label(tableFrame,text="$"+str(avance), font=(12), fg="green").grid(row=r, column=2, padx=30, pady=10)
    
    whouse.mainloop()

#show list of houses from a specific apple --
def showApple(apple):
    #create a window
    wApple = Toplevel()
    wApple.resizable(False,False)
    wApple.title("MANZANA")
    
    #title frame
    tAFrame = Frame(wApple)
    tAFrame.config(width="300px", height="50px")
    tAFrame.pack()
    Label(tAFrame,text=apple.name, font=("Courier", 20)).grid(row=0, column=0 ,sticky = N)

    #options frame
    optionFrame = Frame(wApple)
    optionFrame.config()
    optionFrame.pack()
    Button(tAFrame, text="Agregar Casas", command=lambda : formHouse(apple)).grid(row=1, column=0 ,sticky = N)
    Button(tAFrame, text="Cerrar", command=lambda : wApple.destroy()).grid(row=1, column=1 ,sticky = N)

    #table frame
    tAFrame = Frame(wApple)
    tAFrame.pack()

    #labels for table
    Label(tAFrame,text="N", font=("Courier", 16)).grid(row=2, column=0 ,sticky = N, padx=10,pady=2)
    Label(tAFrame,text="Tipo", font=("Courier", 16)).grid(row=2, column=1, sticky = N, padx=10, pady=2)
    Label(tAFrame,text="Avance", font=("Courier", 16)).grid(row=2, column=2, sticky = N, padx=10, pady=2)

    r = 3
    index = -2
    for i in apple.listHouses:
        index+=1
        Label(tAFrame,text=i.dictionary['n'], font=("Courier", 14)).grid(row=r, column=0 ,sticky = W, padx=7,pady=2)
        Label(tAFrame,text=i.dictionary['type'], font=("Courier", 14)).grid(row=r, column=1, padx=20, pady=2)
        
        t = 0
        advance = 0
        for a,b in i.dictionary.items():
            if(t>1):
                if(b[1]):
                    advance += b[0]
            t+=1


        Label(tAFrame,text=str(advance), font=("Courier", 14)).grid(row=r, column=2, padx=20, pady=2)
        Button(tAFrame, text="Ver", command=lambda j = index+1: showHouse(apple.listHouses[j])).grid(row=r, column=3 ,sticky = N, padx=10, pady=5)

        r+=1

    wApple.mainloop()

#show a list of apples from a specific workspace --IN PROGRESS
def showWorkspace(WSpace):
    #create a window
    wWspace = Tk()
    wWspace.resizable(False,False)
    wWspace.title("OBRA")

    #title frame
    titleFrame = Frame()
    titleFrame.config(width="300px", height="50px")
    Label(titleFrame,text=WSpace.name, font=("Courier", 20)).grid(row=0, column=0 ,sticky = N)
    titleFrame.pack()

    #return function
    def closeButton():
        WSpace.save()
        wWspace.destroy()
        mainWindow()

    #options frame
    optionFrame = Frame()
    optionFrame.config(width="300px", height="100px")
    Button(optionFrame, text="Agreagar Manzana", command=lambda : formApple(WSpace)).grid(row=1, column=1 ,sticky = N, pady=3)
    Button(optionFrame, text="Cerrar", command=closeButton).grid(row=1, column=2 ,sticky = N, pady=3)
    optionFrame.pack()

    #table frame
    tableFrame = Frame()
    tableFrame.pack()

    #table labels
    Label(tableFrame,text="MANZANA", font=("Courier", 16)).grid(row=2, column=0 ,sticky = N, padx=10,pady=2)
    Label(tableFrame,text="N.CASAS", font=("Courier", 16)).grid(row=2, column=1, sticky = N, padx=10, pady=2)
    Label(tableFrame,text="INI/FIN", font=("Courier", 16)).grid(row=2, column=2, sticky = N, padx=10, pady=2)
    
    r = 3
    index = 0
    for i in WSpace.listApples:
        Label(tableFrame,text=i.name, font=("Courier", 14)).grid(row=r, column=0 ,sticky = W, padx=7,pady=2)
        Label(tableFrame,text=str(i.n_house), font=("Courier", 14)).grid(row=r, column=1, padx=20, pady=2)
        Label(tableFrame,text=str(i.start)+"/"+str(i.final), font=("Courier", 14)).grid(row=r, column=2, padx=20, pady=2)
        Button(tableFrame, text="Ver", command=lambda j = index : showApple(WSpace.listApples[j])).grid(row=r, column=3 ,sticky = N, pady=3)

        r+=1
        index += 1
    
    wWspace.mainloop()