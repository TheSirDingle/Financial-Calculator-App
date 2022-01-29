from tkinter import *
import tkinter as tk
from main import *

# Tax Calculation for single filers
class taxesSingle():

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

# Class for the taxation calculation GUIs
class taxGui:

    def __init__(self, root, mainframe):
        self.single = "Nope Lol"
        self.root = root
        self.mainframe = mainframe

    # Main Window for federal income tax selection
    def OTG(self):

        mainReturn = traversalActions()

        otg = tk.Frame(self.root)
        otg.grid(row = 0, column=0, sticky='nsew')
        mainReturn.raiseFrame(otg)

        # Single Tax Filer GUI
        def singGui():

            window1 = tk.Frame(self.root)
            window1.grid(row = 0, column=0, sticky='nsew')
            mainReturn.raiseFrame(window1)

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

            singReturn = Button(window1, text="Return back to selection menu", command=lambda: singRet.raiseFrame(otg))
            singReturn.pack()

            lbl.pack()

        # Married Joint Tax Filer GUI
        def MJG():

            window1 = tk.Frame(self.root)
            window1.grid(row=0, column=0, sticky='nsew')
            mainReturn.raiseFrame(window1)

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

            mjgReturn = Button(window1, text="Return back to selection menu",command=lambda: mjgRet.raiseFrame(otg))
            mjgReturn.pack()

            lbl.pack()

        # Married Single Tax Filer GUI
        def MSG():

            window1 = tk.Frame(self.root)
            window1.grid(row=0, column=0, sticky='nsew')
            mainReturn.raiseFrame(window1)

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

            msgReturn = Button(window1, text="Return back to selection menu", command=lambda: msgRet.raiseFrame(otg))
            msgReturn.pack()

            lbl.pack()

        # Head of Household Tax Filer GUI
        def HOH():

            window1 = tk.Frame(self.root)
            window1.grid(row=0, column=0, sticky='nsew')
            mainReturn.raiseFrame(window1)

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

            hohReturn = Button(window1, text="Return back to selection menu", command=lambda: hohRet.raiseFrame(otg))
            hohReturn.pack()

            lbl.pack()

        stButton = Button(otg, text="Single File Taxer", command=singGui)
        mjgButton = Button(otg, text="Married Joint File Taxer", command=MJG)
        msgButton = Button(otg, text="Married Single File Taxer", command=MSG)
        hohButon = Button(otg, text="Head of Household File Taxer", command=HOH)
        mainMenuButton = Button(otg, text="Return to main menu", command= lambda : mainReturn.raiseFrame(self.mainframe))

        stButton.pack(pady = 4, padx = 4)
        mjgButton.pack(pady = 4, padx = 4)
        msgButton.pack(pady = 4, padx = 4)
        hohButon.pack(pady = 4, padx = 4)
        mainMenuButton.pack(pady = 4, padx = 4)

        return 0
