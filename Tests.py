from Interpretation import manager
from Interpretation.participants import *


class TestBattery:
    def __init__(self):
        self.mgr = manager.InterpretationManager()

    def SelectIncomingChannel(self):
        print('********************************************')
        print('Test ID 6: Select Incoming Language Channel')
        print('********************************************')
        print('This test simulates an interpreter selecting an incoming language that is not available.')
        self.mgr.listChannels()
        interpreter1 = Interpreter('GABBY', 'ENGLISH', 'SPANISH', 'gabby@test.com')
        print("\nINPUT >>> 'SPANISH'")
        print("EXPECTED RESULT >>> Message indicating unavailability of selected language")
        print("ACTUAL RESULT:")
        interpreter1.selectSourceLanguage(self.mgr, 'SPANISH')
        print('\nThis test simulates an interpreter selecting an incoming language that is available.\n')
        self.mgr.addLanguage('FRENCH')
        self.mgr.addLanguage('HINDI')
        self.mgr.addLanguage('JAPANESE')
        print("\nINPUT >>> 'JAPANESE'")
        print("EXPECTED RESULT >>> 'You are now listening to JAPANESE'")
        print("ACTUAL RESULT:")
        interpreter1.selectSourceLanguage(self.mgr, 'JAPANESE')


if __name__ == '__main__':
    test = TestBattery()
    test.SelectIncomingChannel()
