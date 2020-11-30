from Interpretation import manager
from Interpretation import participants
from UI import setup
from UI import interpreterui

if __name__ == '__main__':
    m = manager.InterpretationManager()
    s = setup.SetupUI(m).go()




