class InterpreterUI:
    def __init__(self, manager):
        self.manager = manager

    def go(self, name):
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
            input()

