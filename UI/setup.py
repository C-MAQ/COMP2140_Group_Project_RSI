from Interpretation import manager
from Interpretation import participants
from UI import interpreterui
import sys

class setupUI:
    def __init__(self, manager):
        self.obj = manager

    def go(self):
        while True:
            print("******************************")
            print("INTERPRETATION SETTINGS")
            print("******************************")
            print("1 - ADD LANGUAGE")
            print("2 - ADD INTERPRETER")
            print("3 - REMOVE LANGUAGE")
            print("4 - REMOVE INTERPRETER")
            print("5 - LIST INTERPRETERS")
            print("6 - START MEETING")
            print("7 - EXIT")
            option = input("Select an option: ")
            if option == '7':
                sys.exit()
            if option == '2':
                self.addint()
            if option == '5':
                self.listint()
            if option == '6':
                if len(self.obj.interpretersList) < 2:
                    print("At least two interpreters have to be added first")
                    continue
                else:
                    self.selectui()

    def addint(self):
        name = input("Enter name of interpreter: ")
        slang = input("Enter source language of interpreter: ")
        tlang = input("Enter target language of interpreter: ")
        email = input("Enter email language of interpreter: ")
        self.obj.addInterpreter(name,slang,tlang,email)

    def listint(self):
        self.obj.listInterpreters()

    def selectui(self):
        choice = input("View as INTERPRETER or ATTENDEE?: ")
        if choice == 'INTERPRETER':
            name = input("Name of Interpreter?: ")
            for i in self.obj.interpretersList:
                if i.name == name:
                    ui = interpreterui.InterpreterUI(self.obj)
                    ui.go(i)
                    break

