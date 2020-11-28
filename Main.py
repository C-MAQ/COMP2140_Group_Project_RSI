from Interpretation import manager
from Interpretation import participants
from UI import setup
from UI import interpreterui

if __name__ == '__main__':
    m = manager.InterpretationManager()

    '''m.addLanguage("SPANISH")
    m.addLanguage("FRENCH")
    m.addInterpreter("John","ENGLISH","SPANISH","john@tia.com")
    m.addInterpreter("Mary","ENGLISH","FRENCH","mary@tia.com")

    john = m.interpretersList[0]
    mary = m.interpretersList[1]

    john.printinfo()
    mary.printinfo()'''
    s = setup.setupUI(m).go()




