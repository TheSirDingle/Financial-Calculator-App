# left off on getting multi-line queries to work on label
import tkinter as tk
from tkinter import *
from tkinter import messagebox
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

    def login(self, window1, window2, email, password):

        inEmail = email.get()
        inPassword = password.get()

        acEmail = str(inEmail)
        actPass = str(inPassword)


        query = f'SELECT email, password FROM login WHERE email= "{acEmail}" && password= "{actPass}"'
        cur.execute(query)
        cur.fetchall()

        rowCount = cur.rowcount

        print(rowCount)

        if rowCount == 0 or rowCount > 1:
            messagebox.showerror("Miss Input", "You either inputted the wrong password or email, or you need to register an account")
        elif rowCount == 1:
            print("hell yeah bro")
            window1.withdraw()
            window2.deiconify()

    def Register(self, frame):

        registerFrame = Toplevel(frame)
        registerFrame.title('Register')
        registerFrame.geometry('300x300')

        registerFrame.columnconfigure(0, weight=0)
        registerFrame.columnconfigure(1, weight=1)
        registerFrame.columnconfigure(2, weight=1)

        cantStop = traversalActions

        frame.withdraw()

        email= StringVar()
        name= StringVar()
        password= StringVar()

        Label(registerFrame, text="This is the register page").grid(column=1, row=0, pady=4)

        Label(registerFrame, text="Email: ").grid(column=0, row=1)
        regEmail = Entry(registerFrame, textvariable=email)
        regEmail.grid(column=1, row=1, pady=4)

        Label(registerFrame, text="Name: ").grid(column=0, row=2)
        regName = Entry(registerFrame, textvariable=name)
        regName.grid(column=1, row=2, pady=4)

        Label(registerFrame, text="Password: ").grid(column=0, row=3)
        regPassword = Entry(registerFrame, textvariable=password)
        regPassword.grid(column=1, row=3)

        def regUser():

            inpEmail = str(regEmail.get())
            inpName = str(regName.get())
            inpPassword = str(regPassword.get())

            print("{}, {}, {}".format(inpEmail, inpName, inpPassword))

            # States the query in text
            query = f'SELECT email FROM login WHERE email = "{inpEmail}"'

            # executes the query
            cur.execute(query)
            # gets the query result
            cur.fetchall()

            row_count = cur.rowcount
            print(row_count)
            if row_count > 0:
                print()
                messagebox.showerror('Unsuccessful', 'User already registered')
            else:
                if inpEmail == '' or inpName == '' or inpPassword == '':
                    messagebox.showerror('Empty Entry', 'Please fill in the entry boxes')
                else:
                    messagebox.showinfo('Successful', 'You have successfully registered a user')
                    sucQuery = f'INSERT INTO login(email, name, password) VALUES ("{inpEmail}", "{inpName}","{inpPassword}")'
                    cur.execute(sucQuery)
                    connection.commit()
                    cur.execute("SELECT * FROM login")
                    print(cur.fetchall())

        Button(registerFrame, text="Register", command=regUser).grid(column=1, row=4)

        Button(registerFrame, text="Return To Login", command=lambda :cantStop.returnWindow(0, registerFrame, frame)).grid(column=1, row=5, pady=5)

        quitBtn = Button(registerFrame, text="Quit", command=exit)
        quitBtn.grid(column=1, row=6, pady=4)


class queryStuff:
    def __init__(self):
        self.stuff = "more stuff"

    def qColumnS(self, Entry):

        entryQuery = Entry.get()
        if entryQuery == '':
            print("Please input something")
            messagebox.showerror("Error", "Please Input A Column Name")
        else:
            str(entryQuery)

            query = f'SELECT {entryQuery} from login'

            cur.execute(query)
            global i
            i = 0
            for stuff in cur:
                for j in range(len(stuff)):
                    labelcheck = print(stuff)
                    labelQuery = Label(mainFrame, pady = 3, padx = 3,text=stuff[j])
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
    root.title("Finance Application")

    root.rowconfigure(0, weight=1)
    root.columnconfigure(0, weight=1)

    root.withdraw()

    travAct = traversalActions

    # ----------------------Login Window-----------------------------

    logWindow = tk.Tk()
    logWindow.title('Login')
    logWindow.geometry('300x200')

    logWindow.columnconfigure(0, weight=1)
    logWindow.columnconfigure(1, weight=1)

    emailE = StringVar()
    passwordE = StringVar()

    Label(logWindow, text="email: ").grid(column=0, row=0, pady=5)
    emailEntry = Entry(logWindow, textvariable=emailE)
    emailEntry.grid(column=1, row=0, pady=5)

    Label(logWindow, text='Password: ').grid(column=0, row=1, pady=5)
    passEntry = Entry(logWindow, textvariable=passwordE)
    passEntry.grid(column=1, row=1, pady=5)

    Button(logWindow, text="Login", command= lambda : travAct.login(logWindow, logWindow, root, emailEntry, passEntry)).grid(column=1, padx=5, pady=5)
    Button(logWindow, text='Register', command= lambda : travAct.Register(logWindow, logWindow)).grid(column=1, padx=5, pady=5)
    Button(logWindow, text='Quit', command=exit).grid(column=1, pady=5)

    # ----------------------End Login Window-----------------------------

    # [redacted]
    connection = mysql.connector.connect(
        host="localhost",
        port=3306,
        user='root',
        password='friday01',
        database='FincCalc'
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

    returnLogin = Button(mainFrame, text="Return To Login Page", command=lambda :travAct.returnWindow(0, root, logWindow))
    returnLogin.pack(pady = 4, padx = 4)

    quitButton = Button(mainFrame, text="Quit", command=exit)
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