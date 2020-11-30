class MeetingParticipant:
    """"Constructor: set participant's name and source language"""
    def __init__(self, name):
        self.name = name
        self.sourcelang = "ENGLISH"
        
    """Method allows for participant to select their source language"""
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
    
    """Getter: Prints the name of the specified participant"""
    def printinfo(self):
        print(self.name)


class Interpreter(MeetingParticipant):
    
    """Constructor: sets the name, source language,
        target language and email of the interpreter""""
        def __init__(self, name, sourcelang, targetlang, email):
            super().__init__(name)
            self.sourcelang = sourcelang
            self.targetlang = targetlang
            self.email = email

     """"Method to set the interpreter's target language"""
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
                
    """Method to send a handover request to a specified user"""
        def requestHandover(self, interpreter):
            print(f'{self.name} requesting handover to {interpreter.name}...')
            
    """Method to accept a handover request from a user"""
        def acceptHandover(self,manager, interpreter):
            self.selectTargetLanguage(manager, interpreter.targetlang)
            self.selectSourceLanguage(manager, interpreter.sourcelang)
            print(f'{self.name} accepted handover')
            print(f'{self.name} now interpreting into {self.targetlang}')


class Attendee(MeetingParticipant):
    """Constructor: sets the name of the attendees of the meeting"""
    def __init__(self, name):
        super().__init__(name)
    pass
