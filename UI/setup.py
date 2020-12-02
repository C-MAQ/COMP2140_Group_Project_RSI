import sys
import time
from UI import interpreterui


class SetupUI:
    def __init__(self, manager):
        self.obj = manager

    """Menu Interface for the host of the meeting"""
    def mainmenu(self):
        while True:
            print("\n******************************")
            print("INTERPRETATION MODULE SETTINGS")
            print("******************************\n")
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
                    time.sleep(2)
                    continue
                else:
                    self.selectui()

    """Input method to read data from the user about
        the interpreter being added"""
    def addint(self):
        name = input("\nEnter name of interpreter: ")
        slang = input("Enter source language of interpreter: ")
        tlang = input("Enter target language of interpreter: ")
        email = input("Enter email of interpreter: ")
        self.obj.addInterpreter(name, slang, tlang, email)

    """Method to print a list of all the availiable interpreters"""
    def listint(self):
        print("\nAvailable interpreters:")
        self.obj.listInterpreters()

    """Input method to read the language being added to the list"""
    def addlang(self):
        lang = input("Which language would you like to add? : ")
        self.obj.addLanguage(lang)

    """Method that removes a selected interpreter from the list"""
    def removeint(self):
        self.obj.listInterpreters()
        name = input("Name of interpreter to remove: ")
        self.obj.removeInterpreter(name)

    """Method that removes a selected language from the list"""
    def removelang(self):
        self.obj.listChannels()
        lang = input("Which language do you want to remove? : ")
        self.obj.removeLanguage(lang)

    """Method to access specific interface based on which
        the type of user is using the system"""
    def selectui(self):
        choice = input("\nView as INTERPRETER (I) or ATTENDEE (A) : ")
        if choice == 'I' or choice == 'i':
            self.obj.listInterpreters()
            name = input("Select name of Interpreter: ")
            for i in self.obj.interpretersList:
                if i.name == name:
                    ui = interpreterui.InterpreterUI(self.obj)
                    ui.go(i)
                    break
        if choice == 'A':
            print("\nAttendee UI not yet implemented")
