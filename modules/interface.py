from tkinter import *
from modules.fullClases import *

#method with the root window
def mainWindow():
    #main window
    root = Tk()
    root.resizable(False,False)

    #main Frame
    rootFrame = Frame()
    rootFrame.config(width="900px", height="500px", bg="gray")
    rootFrame.pack()

    #title
    Label(rootFrame,text="Control de Obras", font=(18)).place(x=545,y=10)

    root.mainloop()

#form to new Apple 
def formApple(WSpace):
    #create a window
    wapple = Tk()
    wapple.resizable(False,False)
    wapple.title(WSpace.name)

    #frame to title
    titleFrame = Frame()
    titleFrame.config(width="300px", height="30px")
    titleFrame.pack()

    #frame to form
    formFrame = Frame()
    formFrame.config(width="300px", height="500px")
    formFrame.pack()

    #frame to button
    btnFrame = Frame()
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
        if(int(number.get()) or typeH != "Selecciona"):
            WSpace.listApples.append(Apple(name.get(), int(number.get()),typeH.get(), int(start.get()), int(final.get())))
        else:
            WSpace.listApples.append(Apple(name.get(),0,"null",0,0))
        wapple.destroy()

    #button
    btnAcept = Button(btnFrame, text="Agregar", command=newApple).grid(row=0, column=0 ,sticky = N, pady=5)

    wapple.mainloop()

#show concepts of a specific house --FINISHED
def showHouse(house):
    #create a window
    whouse = Tk()
    whouse.resizable(False,False)
    whouse.title("Casa "+str(house.dictionary['n'])+": "+house.dictionary['type'])

    #frame with the table
    tableFrame = Frame(whouse)
    tableFrame.config(width="300px", height="300px")
    tableFrame.pack()

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

            total+=y[0]
            if(y[1]):
                avance+=y[0]

        z+=1
        r+=1
    
    Label(tableFrame,text="TOTAL", font=(12)).grid(row=r, column=0 ,sticky = W, padx=5,pady=10)
    Label(tableFrame,text="$"+str(total), font=(12), fg="red").grid(row=r, column=1, padx=20, pady=10)
    Label(tableFrame,text="$"+str(avance), font=(12), fg="green").grid(row=r, column=2, padx=30, pady=10)
    
    whouse.mainloop()

#show list of houses from a specific apple --START
def showApple(apple):
    #create a window
    wApple = Tk()
    wApple.resizable(False,False)
    wApple.title(apple.name)
    
    #title frame
    tAFrame = Frame()
    tAFrame.config(width="300px", height="50px")
    tAFrame.pack()
    Label(tAFrame,text=apple.name, font=("Courier", 20)).grid(row=0, column=0 ,sticky = N)

    #table frame
    tAFrame = Frame()
    tAFrame.pack()

    #labels for table
    Label(tAFrame,text="N", font=("Courier", 16)).grid(row=1, column=0 ,sticky = N, padx=10,pady=2)
    Label(tAFrame,text="Tipo", font=("Courier", 16)).grid(row=1, column=1, sticky = N, padx=10, pady=2)
    Label(tAFrame,text="Avance", font=("Courier", 16)).grid(row=1, column=2, sticky = N, padx=10, pady=2)
    btns = []

    def indexHouse(ind):
        showHouse(apple.listHouses[ind])

    r = 2
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
                    avance += b[0]
            t+=1


        Label(tAFrame,text=str(advance), font=("Courier", 14)).grid(row=r, column=2, padx=20, pady=2)
        btns.append(Button(tAFrame, text="Ver", command=lambda j = index+1: indexHouse(j)).grid(row=r, column=3 ,sticky = N, padx=10, pady=5))

        r+=1

    wApple.mainloop()



#show a list of apples from a specific workspace --IN PROGRESS
def showWorkspace(WSpace):
    #create a window
    wWspace = Tk()
    wWspace.resizable(False,False)
    wWspace.title("Obra")

    #title frame
    titleFrame = Frame()
    titleFrame.config(width="300px", height="50px")
    Label(titleFrame,text=WSpace.name, font=("Courier", 20)).grid(row=0, column=0 ,sticky = N)
    titleFrame.pack()

    #table frame
    tableFrame = Frame()
    tableFrame.pack()

    #table labels
    Label(tableFrame,text="MANZANA", font=("Courier", 16)).grid(row=1, column=0 ,sticky = N, padx=10,pady=2)
    Label(tableFrame,text="N.CASAS", font=("Courier", 16)).grid(row=1, column=1, sticky = N, padx=10, pady=2)
    Label(tableFrame,text="INI/FIN", font=("Courier", 16)).grid(row=1, column=2, sticky = N, padx=10, pady=2)
    
    r = 2
    for i in WSpace.listApples:
        Label(tableFrame,text=i.name, font=("Courier", 14)).grid(row=r, column=0 ,sticky = W, padx=7,pady=2)
        Label(tableFrame,text=str(i.n_house), font=("Courier", 14)).grid(row=r, column=1, padx=20, pady=2)
        Label(tableFrame,text=str(i.start)+"/"+str(i.final), font=("Courier", 14)).grid(row=r, column=2, padx=20, pady=2)
        btnAcept = Button(tableFrame, text="Ver").grid(row=r, column=3 ,sticky = N, pady=3)

        r+=1
    
    wWspace.mainloop()