from Interpretation import participants


class InterpretationManager:
    def __init__(self):
        self.defaultLanguage = "ENGLISH"
        self.interpretersList = []
        self.availableLanguages = []
        self.availableLanguages += [self.defaultLanguage]

    def addInterpreter(self, name, sourcelang, targetlang, email):
        interpreter = participants.Interpreter(name, sourcelang, targetlang, email)
        self.interpretersList += [interpreter]
        print(f'{interpreter.name} added as {interpreter.targetlang} interpreter')
        if not sourcelang in self.availableLanguages:
            self.availableLanguages += [sourcelang]
        if not targetlang in self.availableLanguages:
            self.availableLanguages += [targetlang]

    def removeInterpreter(self, name):
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
        self.availableLanguages += [lang]
        print(f'{lang} added to list of available languages')

    def removeLanguage(self, lang):
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
                print(f'{lang} removed. {lang} not available')
        else:
            print(f'{lang} not found in list of available languages')

    def listInterpreters(self):
        if len(self.interpretersList) == 0:
            print("No interpreters have been assigned as yet")
            return
        for i in self.interpretersList:
            print(f'Interpreter {i} : {self.interpretersList[i].name}')