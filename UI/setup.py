from Interpretation import manager
from Interpretation import participants
from UI import interpreterui
import sys


class SetupUI:
    def __init__(self, manager):
        self.obj = manager

    def go(self):
        while True:
            print("\n******************************")
            print("INTERPRETATION SETTINGS")
            print("******************************")
            print("1 - ADD LANGUAGE")
            print("2 - ADD INTERPRETER")
            print("3 - REMOVE LANGUAGE")
            print("4 - REMOVE INTERPRETER")
            print("5 - LIST INTERPRETERS")
            print("6 - LIST AVAILABLE LANGUAGES")
            print("7 - START MEETING")
            print("8 - EXIT")
            option = input("\nSelect an option: ")
            if option == '1':
                self.addlang()
            if option == '3':
                self.removelang()
            if option == '4':
                self.removeint()
            if option == '8':
                print("\nCLOSING INTERPRETATION MODULE")
                sys.exit()
            if option == '2':
                self.addint()
            if option == '5':
                self.listint()
            if option == '6':
                self.obj.listChannels()
            if option == '7':
                if len(self.obj.interpretersList) < 2:
                    print("At least two interpreters have to be added first")
                    continue
                else:
                    self.selectui()

    def addint(self):
        name = input("Enter name of interpreter: ")
        slang = input("Enter source language of interpreter: ")
        tlang = input("Enter target language of interpreter: ")
        email = input("Enter email of interpreter: ")
        self.obj.addInterpreter(name, slang, tlang, email)

    def listint(self):
        self.obj.listInterpreters()

    def addlang(self):
        lang = input("Which language would like to add?: ")
        self.obj.addLanguage(lang)

    def removeint(self):
        self.obj.listInterpreters()
        name = input("Name of Interpreter to remove: ")
        self.obj.removeInterpreter(name)

    def removelang(self):
        self.obj.listChannels()
        lang = input("Which language do you want to remove?: ")
        self.obj.removeLanguage(lang)

    def selectui(self):
        choice = input("View as INTERPRETER (I) or ATTENDEE (A) ?: ")
        if choice == 'I':
            name = input("Name of Interpreter?: ")
            for i in self.obj.interpretersList:
                if i.name == name:
                    ui = interpreterui.InterpreterUI(self.obj)
                    ui.go(i)
                    break
        if choice == 'A':
            print("Attendee UI not yet implemented")
