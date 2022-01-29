# left off on getting multi-line queries to work on label
import tkinter as tk
from tkinter import *
import mysql.connector
from xtra import *

# Tax Calculation for single filers
class taxesSingle:

    def __init__(self):
        self.tax = "single and ready to get taxed"

    def ten(self, income):
        stuff = income * .10
        print("This is what you're taxed: ${0}".format(stuff))
        return stuff

    def twelve(self, income):
        stuff = ((income - 9950) * 0.12) + 995
        print("This is what you're taxed: ${0}".format(stuff))
        return stuff

    def twentyTwo(self, income):
        stuff = ((income - 40525) * 0.22) + 4664
        print("This is what you're taxed: ${0}".format(stuff))
        return stuff

    def twentyFour(self, income):
        stuff = ((income - 86375) * 0.24) + 14751
        print("This is what you're taxed: ${0}".format(stuff))
        return stuff

    def thirtyTwo(self, income):
        stuff = ((income - 164925) * 0.32) + 33603
        print("This is what you're taxed: ${0}".format(stuff))
        return stuff

    def thirtyFive(self, income):
        stuff = ((income - 209425) * 0.35) + 47483
        print("This is what you're taxed: ${0}".format(stuff))
        return stuff

    def thirtySeven(self, income):
        stuff = ((income - 523600) * 0.37) + 157804.25
        print("This is what you're taxed: ${0}".format(stuff))
        return stuff

# Tax calculation for joint married filers
class taxesMarriedJoin:

    def __init__(self):
        self.tax = "married... that's tough"

    def tenJ(self, income):
        stuff = income * .10
        print("This is what you're taxed: ${0}".format(stuff))
        return stuff

    def twelveJ(self, income):
        stuff = ((income - 19900) * 0.12) + 1990
        print("This is what you're taxed: ${0}".format(stuff))
        return stuff

    def twentytwoJ(self, income):
        stuff = ((income - 81050) * 0.22) + 9328
        print("This is what you're taxed: ${0}".format(stuff))
        return stuff

    def twentyfourj(self, income):
        stuff = ((income - 172750) * 0.24) + 29502
        print("This is what you're taxed: ${0}".format(stuff))
        return stuff

    def thirtytwoj(self, income):
        stuff = ((income - 329850) * 0.32) + 67206
        print("This is what you're taxed: ${0}".format(stuff))
        return stuff

    def thirtyfivej(self, income):
        stuff = ((income - 418850) * 0.35) + 95686
        print("This is what you're taxed: ${0}".format(stuff))
        return stuff

    def thirtysevenj(self, income):
        stuff = ((income - 628300) * 0.37) + 168993.5
        print("This is what you're taxed: ${0}".format(stuff))
        return stuff

# Tax calculation for married separate filers
class taxesMarriedSeparate:

    def __init__(self):
        self.tax = "separate for 0 reason"

    def tenS(self, income):
        stuff = income * .10
        print("This is what you're taxed: ${0}".format(stuff))
        return stuff

    def twelveS(self, income):
        stuff = ((income - 9950) * 0.12) + 995
        print("This is what you're taxed: ${0}".format(stuff))
        return stuff

    def twentytwoS(self, income):
        stuff = ((income - 40525) * 0.22) + 4464
        print("This is what you're taxed: ${0}".format(stuff))
        return stuff

    def twentyfourS(self, income):
        stuff = ((income - 86375) * 0.24) + 14751
        print("This is what you're taxed: ${0}".format(stuff))
        return stuff

    def thirtytwoS(self, income):
        stuff = ((income - 164925) * 0.32) + 33603
        print("This is what you're taxed: ${0}".format(stuff))
        return stuff

    def thirtyfiveS(self, income):
        stuff = ((income - 209425) * 0.35) + 47843
        print("This is what you're taxed: ${0}".format(stuff))
        return stuff

    def thirtysevenS(self, income):
        stuff = ((income - 314150) * 0.37) + 84496.75
        print("This is what you're taxed: ${0}".format(stuff))
        return stuff

# Tax calculation for Head of Household
class taxesHOH:

    def __init__(self):
        self.tax = "the big boss"

    def tenH(self, income):
        stuff = income * .10
        print("This is what you're taxed: ${0}".format(stuff))
        return stuff

    def twelveH(self, income):
        stuff = ((income - 14200) * 0.12) + 1420
        print("This is what you're taxed: ${0}".format(stuff))
        return stuff

    def twentytwoH(self, income):
        stuff = ((income - 54200) * 0.22) + 6220
        print("This is what you're taxed: ${0}".format(stuff))
        return stuff

    def twentyfourH(self, income):
        stuff = ((income - 86350) * 0.24) + 13293
        print("This is what you're taxed: ${0}".format(stuff))
        return stuff

    def thirtytwoH(self, income):
        stuff = ((income - 164900) * 0.32) + 32145
        print("This is what you're taxed: ${0}".format(stuff))
        return stuff


    def thirtyfiveH(self, income):
        stuff = ((income - 209400) * 0.35) + 46385
        print("This is what you're taxed: ${0}".format(stuff))
        return stuff

    def thirtysevenH(self, income):
        stuff = ((income - 523600) * 0.37) + 156355
        print("This is what you're taxed: ${0}".format(stuff))
        return stuff

class traversalActions:
    def __init__(self):
        self.transversal = "class used for button traversal"

    def returnWindow(self, window, secWind):
        window.withdraw()
        secWind.deiconify()


# Class for the taxation calculation GUIs
class taxGui:
    def __init__(self):
        self.single = "Damn SON YOUR ABOUT TO GET SCREWED"

    # Main Window for federal income tax selection
    def OTG(self):

        root.withdraw()
        mainReturn = traversalActions()

        otg = Toplevel(root)
        otg.geometry('700x300')
        otg.title("Taxing Type")

        # Single Tax Filer GUI
        def singGui():

            otg.withdraw()

            window1 = Toplevel(root)
            window1.geometry('700x300')
            window1.title('Single Tax Filer')

            taxable = IntVar()
            lbl = Label(window1, text="Your total tax will be: ")

            singEntry = Entry(window1, textvariable=taxable)
            singEntry.pack()

            # Single filer tax calculation comparison and call
            def singTax():

                taxed = IntVar()
                taxable = int(singEntry.get())
                taxInc = taxesSingle()

                match taxable:
                    case taxable if taxable <= 9950:
                        taxed = taxInc.ten(taxable)
                    case taxable if taxable >= 9951 & taxable <= 40525:
                        taxed = taxInc.twelve(taxable)
                    case taxable if taxable >= 40526 & taxable <= 86375:
                        taxed = taxInc.twentyTwo(taxable)
                    case taxable if taxable >= 86376 & taxable <= 164925:
                        taxed = taxInc.twentyFour(taxable)
                    case taxable if taxable >= 164926 & taxable <= 209425:
                        taxed = taxInc.thirtyTwo(taxable)
                    case taxable if taxable >= 209426 & taxable <= 523600:
                        taxed = taxInc.thirtyFive(taxable)
                    case taxable if taxable >= 523601:
                        taxed = taxInc.thirtySeven(taxable)
                    case taxable if taxable == None:
                        print("No Tax Included BB")

                print(taxed)
                lbl.config(text="Your total tax will be: ${0}".format(taxed))
                return taxed

            singRet = traversalActions()

            singleButton = Button(window1, text="Calculate Tax", command=singTax)
            singleButton.pack()

            singReturn = Button(window1, text="Return back to selection menu", command=lambda: singRet.returnWindow(window1, otg))
            singReturn.pack()

            lbl.pack()

        # Married Joint Tax Filer GUI
        def MJG():

            otg.withdraw()

            window1 = Toplevel(root)
            window1.geometry('700x300')
            window1.title('Married Joint Tax Filer')

            taxable = IntVar()
            lbl = Label(window1, text="Your total tax will be: ")

            singEntry = Entry(window1, textvariable=taxable)
            singEntry.pack()

            # Married Joint filer tax calculation comparison and call
            def MarriedJointTax():

                taxed = IntVar()
                taxable = int(singEntry.get())
                taxInc = taxesMarriedJoin()

                match taxable:
                    case taxable if taxable <= 19900:
                        taxed = taxInc.tenJ(taxable)
                    case taxable if taxable >= 19901 & taxable <= 81050:
                        taxed = taxInc.twelveJ(taxable)
                    case taxable if taxable >= 81051 & taxable <= 172750:
                        taxed = taxInc.twentytwoJ(taxable)
                    case taxable if taxable >= 172751 & taxable <= 329850:
                        taxed = taxInc.twentyfourj(taxable)
                    case taxable if taxable >= 329851 & taxable <= 418850:
                        taxed = taxInc.thirtytwoj(taxable)
                    case taxable if taxable >= 418851 & taxable <= 628300:
                        taxed = taxInc.thirtyfivej(taxable)
                    case taxable if taxable >= 628301:
                        taxed = taxInc.thirtysevenj(taxable)
                    case taxable if taxable == None:
                        print("No Tax Included BB")

                print(taxed)
                lbl.config(text="Your total tax will be: ${0}".format(taxed))
                return taxed

            singleButton = Button(window1, text="Calculate Tax", command=MarriedJointTax)
            singleButton.pack()

            mjgRet = traversalActions()

            mjgReturn = Button(window1, text="Return back to selection menu",command=lambda: mjgRet.returnWindow(window1, otg))
            mjgReturn.pack()

            lbl.pack()

        # Married Single Tax Filer GUI
        def MSG():

            otg.withdraw()

            window1 = Toplevel(root)
            window1.geometry('700x300')
            window1.title('Married Single Tax Filer')

            taxable = IntVar()
            lbl = Label(window1, text="Your total tax will be: ")

            singEntry = Entry(window1, textvariable=taxable)
            singEntry.pack()

            # Married Single filer tax calculation comparison and call
            def marriedSingleTax():

                taxed = IntVar()
                taxable = int(singEntry.get())
                taxInc = taxesMarriedSeparate()

                match taxable:
                    case taxable if taxable <= 9950:
                        taxed = taxInc.tenS(taxable)
                    case taxable if taxable >= 9951 & taxable <= 40525:
                        taxed = taxInc.twelveS(taxable)
                    case taxable if taxable >= 40526 & taxable <= 86375:
                        taxed = taxInc.twentytwoS(taxable)
                    case taxable if taxable >= 86376 & taxable <= 164925:
                        taxed = taxInc.twentyfourS(taxable)
                    case taxable if taxable >= 164926 & taxable <= 209425:
                        taxed = taxInc.thirtytwoS(taxable)
                    case taxable if taxable >= 209426 & taxable <= 314150:
                        taxed = taxInc.thirtyfiveS(taxable)
                    case taxable if taxable >= 314151:
                        taxed = taxInc.thirtysevenS(taxable)
                    case taxable if taxable == None:
                        print("No Tax Included BB")

                print(taxed)
                lbl.config(text="Your total tax will be: ${0}".format(taxed))
                return taxed

            singleButton = Button(window1, text="Calculate Tax", command=marriedSingleTax)
            singleButton.pack()

            msgRet = traversalActions()

            msgReturn = Button(window1, text="Return back to selection menu", command=lambda: msgRet.returnWindow(window1, otg))
            msgReturn.pack()

            lbl.pack()

        # Head of Household Tax Filer GUI
        def HOH():

            otg.withdraw()

            window1 = Toplevel(root)
            window1.geometry('700x300')
            window1.title('Head of Household Tax Filer')

            taxable = IntVar()
            lbl = Label(window1, text="Your total tax will be: ")

            singEntry = Entry(window1, textvariable=taxable)
            singEntry.pack()

            # Head of Household filer tax calculation comparison and call
            def HOHTax():

                taxed = IntVar()
                taxable = int(singEntry.get())
                taxInc = taxesHOH()

                match taxable:
                    case taxable if taxable <= 14200:
                        taxed = taxInc.tenH(taxable)
                    case taxable if taxable >= 14201 & taxable <= 54200:
                        taxed = taxInc.twelveH(taxable)
                    case taxable if taxable >= 54201 & taxable <= 86350:
                        taxed = taxInc.twentytwoH(taxable)
                    case taxable if taxable >= 86351 & taxable <= 164900:
                        taxed = taxInc.twentyfourH(taxable)
                    case taxable if taxable >= 164901 & taxable <= 209400:
                        taxed = taxInc.thirtytwoH(taxable)
                    case taxable if taxable >= 209401 & taxable <= 523600:
                        taxed = taxInc.thirtyfiveH(taxable)
                    case taxable if taxable >= 523601:
                        taxed = taxInc.thirtysevenH(taxable)
                    case taxable if taxable == None:
                        print("No Tax Included BB")

                print(taxed)
                lbl.config(text="Your total tax will be: ${0}".format(taxed))
                return taxed

            singleButton = Button(window1, text="Calculate Tax", command=HOHTax)
            singleButton.pack()

            hohRet = traversalActions()

            hohReturn = Button(window1, text="Return back to selection menu", command=lambda: hohRet.returnWindow(window1, otg))
            hohReturn.pack()

            lbl.pack()

        stButton = Button(otg, text="Single File Taxer", command=singGui)
        mjgButton = Button(otg, text="Married Joint File Taxer", command=MJG)
        msgButton = Button(otg, text="Married Single File Taxer", command=MSG)
        hohButon = Button(otg, text="Head of Household File Taxer", command=HOH)
        mainMenuButton = Button(otg, text="Return to main menu", command= lambda : mainReturn.returnWindow(otg, root))

        stButton.pack(pady = 4, padx = 4)
        mjgButton.pack(pady = 4, padx = 4)
        msgButton.pack(pady = 4, padx = 4)
        hohButon.pack(pady = 4, padx = 4)
        mainMenuButton.pack(pady = 4, padx = 4)

        return 0


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

    connection = mysql.connector.connect(
        host="localhost",
        port=3306,
        user='root',
        password='friday01',
        database='FincCalc'
    )

    print(connection)

    mainSec = Label(root, text='This section is the main part of the application')
    mainSec.pack()
    click = buttonStuff()
    newGui = taxGui()

    # for tkinter don't put a () after the command in the command part
    # myButton = Button(root, text="Click Me!", command=click.myClick, fg="blue", bg="black")
    # myButton.pack(pady = 4, padx = 4)

    singleButton = Button(root, text="Income Tax Options", command=newGui.OTG, fg="red", bg="black")
    singleButton.pack(pady = 4, padx = 4)

    quitButton = Button(root, text="Quit", command=root.destroy)
    quitButton.pack(pady = 4, padx = 4)

    cur = connection.cursor()

    explainQ = Label(root, pady = 3, padx = 3, text="This section is used to query the docker mysql database")
    explainQ.pack()
    column = StringVar()
    sqlEntry = Entry(root, textvariable=column)
    sqlEntry.pack()

    sqlStuff = queryStuff()

    queryButton = Button(root, text='Query the database', command=lambda: sqlStuff.qColumnS(sqlEntry))
    queryButton.pack(pady = 10, padx = 10)

    root.mainloop()
    cur.close()