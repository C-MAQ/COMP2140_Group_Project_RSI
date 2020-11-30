import time


class InterpreterUI:
    def __init__(self, manager):
        self.manager = manager

    def go(self, name):
        self.dashboard(name)

    def dashboard(self, name):
        while True:
            print("******************************")
            print("INTERPRETER DASHBOARD")
            print("******************************")
            print(f'You are now {name.name} and Interpreting from {name.sourcelang} to {name.targetlang}')
            print(f'INCOMING CHANNEL: {name.sourcelang}')
            print(f'OUTGOING CHANNEL: {name.targetlang}')
            print("Interpreter Options:")
            print("1 - ADD OUTGOING CHANNEL")
            print("2 - REMOVE OUTGOING CHANNEL")
            print("3 - SELECT INCOMING CHANNEL")
            print("5 - REQUEST HANDOVER")
            print("6 - ACCEPT HANDOVER")
            print("7 - END INTERPRETATION")
            option = input("Choose and option: ")
            if option == '3':
                print("Available language channels:")
                self.manager.listChannels()
                lang = input("Select incoming language channel: ")
                if lang in self.manager.availableLanguages:
                    name.selectSourceLanguage(self.manager, lang)
                    print(f'{name.name} changed incoming channel to {name.sourcelang}')
                else:
                    print("Language channel selected is unavailable")
            if option == '5':
                print("HANDOVER REQUEST")
                print("Interpreters available for handover request:")
                available = [n for n in self.manager.interpretersList if n.name != name.name]
                for i in available:
                    print(i.name)
                choice = input("Who would you like to handover to?: ")
                for q in available:
                    if q.name == choice:
                        name.requestHandover(q)
                        time.sleep(5)
                        q.acceptHandover(name)
                        q.selectTargetLanguage(self.manager, name.targetlang)
                        q.selectSourceLanguage(self.manager, name.sourcelang)
                        self.dashboard(q)
                break
            if option == '7':
                break

