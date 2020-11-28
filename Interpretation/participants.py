class MeetingParticipant:
    def __init__(self, name):
        self.name = name
        self.sourcelang = "ENGLISH"

    def selectSourceLanguage(self, manager, lang):
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
            print(f'{self.name} requesting handover to {interpreter.name}')

        def acceptHandover(self, interpreter):
            print(f'{self.name} accepted handover')
            print(f'{self.name} now interpreting into {interpreter.targetlang}')


class Attendee(MeetingParticipant):
    pass
