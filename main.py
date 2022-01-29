# left off on getting multi-line queries to work on label
import tkinter as tk
from tkinter import *
import mysql.connector
from incomeTax import *


class traversalActions:
    def __init__(self):
        self.transversal = "class used for button traversal"

    def returnWindow(self, window, secWind):
        window.withdraw()
        secWind.deiconify()

    def raiseFrame(self, frame):
        frame.tkraise()

class queryStuff:
    def __init__(self):
        self.stuff = "more stuff"

    def qColumnS(self, Entry):

        entryQuery = Entry.get()
        if entryQuery == '':
            print("Please input something")
        else:
            str(entryQuery)

            query = (f'SELECT {entryQuery} from login')

            cur.execute(query)
            global i
            i = 0
            for stuff in cur:
                for j in range(len(stuff)):
                    labelcheck = print(stuff)
                    labelQuery = Label(root, pady = 3, padx = 3,text=stuff[j])
                    labelQuery.pack()

                i = i + 1

            print(labelcheck)

        return labelcheck

class buttonStuff:
    def __init__(self):
        self.but = "button stuff for buttons and stuff... stuff"

    # def myClick(self):
    #     myLabel = Label(root, pady = 3, padx = 3, text="Look! I clicked a Buttton!")
    #     myLabel.pack()

if __name__ == '__main__':

    root = tk.Tk()
    root.geometry('700x300')
    root.title("Main Menu")

    root.rowconfigure(0, weight=1)
    root.columnconfigure(0, weight=1)

    # [redacted]
    connection = mysql.connector.connect(
        host="[redacted]",
        port='[redacted]',
        user='[redacted]',
        password='[redacted]',
        database='[redacted]'
    )

    print(connection)

    mainFrame = tk.Frame(root)
    mainFrame.grid(row=0, column=0, stick='nsew')

    mainSec = Label(mainFrame, text='This section is the main part of the application')
    mainSec.pack()

    # click = buttonStuff()

    newGui = taxGui(root, mainFrame)

    # for tkinter don't put a () after the command in the command part
    # myButton = Button(root, text="Click Me!", command=click.myClick, fg="blue", bg="black")
    # myButton.pack(pady = 4, padx = 4)

    singleButton = Button(mainFrame, text="Income Tax Options", command=newGui.OTG, fg="red", bg="black")
    singleButton.pack(pady = 4, padx = 4)

    quitButton = Button(mainFrame, text="Quit", command=root.destroy)
    quitButton.pack(pady = 4, padx = 4)

    cur = connection.cursor()

    explainQ = Label(mainFrame, pady = 3, padx = 3, text="This section is used to query the docker mysql database")
    explainQ.pack()
    column = StringVar()
    sqlEntry = Entry(mainFrame, textvariable=column)
    sqlEntry.pack()

    sqlStuff = queryStuff()

    queryButton = Button(mainFrame, text='Query the database', command=lambda: sqlStuff.qColumnS(sqlEntry))
    queryButton.pack(pady = 10, padx = 10)

    root.mainloop()

    cur.close()