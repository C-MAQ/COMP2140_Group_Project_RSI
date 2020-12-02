class MeetingParticipant:
    def __init__(self, name):
        self.name = name
        self.sourcelang = "ENGLISH"

    def selectSourceLanguage(self, manager, lang): 
        """Method that allows the participant to select a source language for interpretation"""
        templang = ""
        for i, j in enumerate(manager.availableLanguages):
            if j == lang:
                templang = j
        if templang == lang:
            self.sourcelang = templang
            print(f'You are now listening to {lang}')
        else:
            print(f'{lang} is not available as a source language')

    def printinfo(self):
        print(self.name)


class Interpreter(MeetingParticipant):
        def __init__(self, name, sourcelang, targetlang, email):
            super().__init__(name)
            self.sourcelang = sourcelang
            self.targetlang = targetlang
            self.email = email

        def selectTargetLanguage(self, manager, lang):
            """Allows user to set the language they will be interpreting to"""
            templang = ""
            for i, j in enumerate(manager.availableLanguages):
                if j == lang:
                    templang = j
            if templang == lang:
                self.targetlang = templang
                print(f'You are now interpreting to {lang}')
            else:
                print(f'{lang} is not available as a target language')

        def requestHandover(self, interpreter):
            """Method to allow an interpreter to request handover to another interpreter"""
            print(f'{self.name} requesting handover to {interpreter.name}...')

        def acceptHandover(self,manager, interpreter):
            """Method that updates the source and target language of the interpreter that accepted the handover request"""
            self.selectTargetLanguage(manager, interpreter.targetlang)
            self.selectSourceLanguage(manager, interpreter.sourcelang)
            print(f'{self.name} accepted handover')
            print(f'{self.name} is now interpreting into {self.targetlang}')


class Attendee(MeetingParticipant):
    """TODO"""
    def __init__(self, name):
        super().__init__(name)
    pass
