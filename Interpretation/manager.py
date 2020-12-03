from Interpretation import participants

""" System to manage Interpretations including Adding and Removing an Interpreter, Adding and Removing Languages,
List Interpreters and Channels, as well as, Making an Interpreter """
class InterpretationManager:
    def __init__(self):
        self.defaultLanguage = "ENGLISH"
        self.interpretersList = []
        self.availableLanguages = []
        self.availableLanguages += [self.defaultLanguage]

    def addInterpreter(self, name, sourcelang, targetlang, email):
        """Adds an interpreter to an existing list of interpreters"""
        interpreter = participants.Interpreter(name, sourcelang, targetlang, email)
        self.interpretersList += [interpreter]
        print(f'{interpreter.name} added as {interpreter.targetlang} interpreter')
        if not sourcelang in self.availableLanguages:
            self.availableLanguages += [sourcelang]
        if not targetlang in self.availableLanguages:
            self.availableLanguages += [targetlang]

    def removeInterpreter(self, name):
        """Removes a selected interpreter from the list of interpreters"""
        person = ""
        for i, j in enumerate(self.interpretersList):
            if j.name == name:
                person = i
                self.interpretersList.pop(i)
        if person != "":
            if self.interpretersList[person].name != name:
                print(f'{name} removed as interpreter')
        else:
            print(f'{name} not found in list of interpreters')

    def addLanguage(self, lang):
        """Adds a new language to a list of available languages for interpretation"""
        if lang in self.availableLanguages:
            print(f'{lang} is already an available language')
        else:
            self.availableLanguages += [lang]
            print(f'{lang} added to list of available languages')

    def removeLanguage(self, lang):
        """Removes a language from the list of available languages"""
        language = ""
        for i, j in enumerate(self.availableLanguages):
            if j == lang:
                language = i
                self.availableLanguages.pop(i)
                k = [x for x in self.interpretersList if x.targetlang == lang]
                for p, q in enumerate(self.interpretersList):
                    if q in k:
                        self.interpretersList.pop(p)
        if language != "":
            if self.availableLanguages[language] != lang:
                print(f'{lang} removed. {lang} no longer available')
        else:
            print(f'{lang} not found in list of available languages')

    def listInterpreters(self):
        """Displays a list of the available interpreters along with their source and target interpretation language"""
        print("\n")
        if len(self.interpretersList) == 0:
            print("No interpreters have been assigned as yet")
            return
        print("Available Interpreters:")
        for i in self.interpretersList:
            print(f'Interpreter {i.name} : {i.sourcelang} ===> {i.targetlang}')

    def listChannels(self):
        """Displays the list of available languages"""
        print("\nAvailable languages:")
        for i in self.availableLanguages:
            print(i)

    def makeInterpreter(self, attendee):
        """TODO Assign interpreter role to attendee"""
        pass

